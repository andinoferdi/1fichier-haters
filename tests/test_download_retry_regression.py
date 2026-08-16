import queue
import requests
import sys
import tempfile
import unittest
from contextlib import chdir
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import ANY, call, patch

from PyQt5.QtGui import QStandardItem

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.download.download import download


class Response:
    def __init__(self, content=b'', headers=None, chunks=()):
        self.content = content
        self.text = content.decode()
        self.headers = headers or {}
        self._chunks = chunks

    def iter_content(self, _chunk_size):
        return iter(self._chunks)


class DownloadRetryRegressionTest(unittest.TestCase):
    def test_invalid_href_retries_before_marking_bypassed(self):
        file_data = b'x' * (128 * 1024)
        invalid = Response(b'<html><body><div></div><div></div><div></div><div><div></div><div><a href="/register.pl">Register</a></div></div></body></html>')
        missing_host = Response(b'<html><body><div></div><div></div><div></div><div><div></div><div><a href="https://">Broken</a></div></div></body></html>')
        malformed_host = Response(b'<html><body><div></div><div></div><div></div><div><div></div><div><a href="https://:443/file">Broken</a></div></div></body></html>')
        valid = Response(b'<html><body><div></div><div></div><div></div><div><div></div><div><a href="https://cdn.example/file.bin">Download</a></div></div></body></html>')
        stream = Response(
            headers={
                'Content-Disposition': 'attachment; filename="file.bin"',
                'Content-Length': str(len(file_data)),
            },
            chunks=(file_data,),
        )

        with tempfile.TemporaryDirectory() as directory, chdir(directory):
            updates = []
            worker = type('Worker', (), {})()
            worker.link = 'https://1fichier.com/?example'
            worker.dl_name = ''
            worker.dl_directory = directory
            worker.stopped = worker.paused = False
            worker.timeout = 5
            worker.data = [None, None, None, None, None, None, QStandardItem('No password')]
            worker.signals = SimpleNamespace(
                update_signal=SimpleNamespace(emit=lambda _data, update: updates.append(update)))
            worker.proxies = queue.Queue()
            worker.proxies.put({'https': 'http://first.proxy:80'})
            worker.proxies.put({'https': 'http://second.proxy:80'})
            worker.proxies.put({'https': 'http://third.proxy:80'})
            worker.proxies.put({'https': 'http://fourth.proxy:80'})

            with patch('core.download.download.requests.post', side_effect=(invalid, missing_host, malformed_host, valid)), \
                    patch('core.download.download.requests.get', return_value=stream) as get:
                download(worker)

            downloaded_file = Path(directory) / 'file.bin'
            self.assertTrue(downloaded_file.exists())
            self.assertEqual(downloaded_file.read_bytes(), file_data)
            self.assertEqual([update[2] for update in updates if len(update) > 2 and update[2] == 'Bypassed'], ['Bypassed'])
            get.assert_called_once_with(
                'https://cdn.example/file.bin', stream=True, headers=ANY,
                proxies={'https': 'http://fourth.proxy:80'}, timeout=5, verify=False)

    def test_stream_request_failure_retries_with_next_proxy(self):
        file_data = b'x' * (128 * 1024)
        direct_link = Response(b'<html><body><div></div><div></div><div></div><div><div></div><div><a href="https://cdn.example/file.bin">Download</a></div></div></body></html>')
        stream = Response(
            headers={
                'Content-Disposition': 'attachment; filename="file.bin"',
                'Content-Length': str(len(file_data)),
            },
            chunks=(file_data,),
        )

        with tempfile.TemporaryDirectory() as directory, chdir(directory):
            worker = type('Worker', (), {})()
            worker.link = 'https://1fichier.com/?example'
            worker.dl_name = ''
            worker.dl_directory = directory
            worker.stopped = worker.paused = False
            worker.timeout = 5
            worker.data = (None, None, None, None, None, None, QStandardItem('No password'))
            worker.proxies = queue.Queue()
            worker.proxies.put({'https': 'http://first.proxy:80'})
            worker.proxies.put({'https': 'http://second.proxy:80'})

            with patch('core.download.download.requests.post', side_effect=(direct_link, direct_link)), \
                    patch('core.download.download.requests.get', side_effect=(requests.Timeout(), stream)) as get:
                download(worker)

            downloaded_file = Path(directory) / 'file.bin'
            self.assertTrue(downloaded_file.exists())
            self.assertEqual(downloaded_file.read_bytes(), file_data)
            self.assertEqual(get.call_args_list, [
                call('https://cdn.example/file.bin', stream=True, headers=ANY,
                     proxies={'https': 'http://first.proxy:80'}, timeout=5, verify=False),
                call('https://cdn.example/file.bin', stream=True, headers=ANY,
                     proxies={'https': 'http://second.proxy:80'}, timeout=5, verify=False),
            ])


if __name__ == '__main__':
    unittest.main()
