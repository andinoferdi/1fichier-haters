import io
import pickle
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from core.download.workers import FilterWorker
from core.gui.gui import GuiBehavior


URL = 'https://1fichier.com/?duplicate'


class DownloadThread:
    def setMaxThreadCount(self, count):
        self.count = count


class DuplicateDownloadRegressionTest(unittest.TestCase):
    def test_duplicate_cached_link_is_restored_once(self):
        cached_download = [URL, None, None, -1]
        files = {
            'cache': pickle.dumps([cached_download, cached_download.copy()]),
            'settings': pickle.dumps([None, 0, 30, '', 1]),
        }
        actions = GuiBehavior.__new__(GuiBehavior)
        actions.gui = SimpleNamespace(links='')
        actions.download_thread = DownloadThread()

        def open_file(path, _mode):
            return io.BytesIO(files['cache' if str(path).endswith('cache') else 'settings'])

        restored = []
        with patch('builtins.open', side_effect=open_file), \
                patch.object(actions, 'add_links', side_effect=lambda state, download: restored.append(download)):
            actions.handle_init()

        self.assertEqual(restored, [cached_download])
        self.assertEqual(actions.cached_downloads, [cached_download])

    def test_repeated_link_in_one_submission_is_emitted_once(self):
        actions = self._actions(f'{URL}\n{URL}')
        emitted = self._run_filter(actions)

        self.assertEqual(len(emitted), 1)

    def test_link_already_downloading_is_not_emitted_again(self):
        actions = self._actions(URL)
        actions.download_workers = [SimpleNamespace(link=URL)]
        emitted = self._run_filter(actions)

        self.assertEqual(emitted, [])
        self.assertEqual(actions.events, ['hidden', 'complete'])

    @staticmethod
    def _actions(links):
        events = []
        return SimpleNamespace(
            cached_downloads=[],
            download_workers=[],
            events=events,
            gui=SimpleNamespace(
                links=links,
                hide_loading_overlay=lambda: events.append('hidden'),
                add_links_complete=lambda: events.append('complete'),
            ),
        )

    @staticmethod
    def _run_filter(actions):
        emitted = []
        worker = FilterWorker(actions)
        worker.signals.download_signal.connect(lambda *args: emitted.append(args))
        with patch('core.download.workers.get_link_info', return_value=['file.bin', '1 MB']):
            worker.run()
        return emitted


if __name__ == '__main__':
    unittest.main()
