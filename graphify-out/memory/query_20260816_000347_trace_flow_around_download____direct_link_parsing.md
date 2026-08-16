---
type: "query"
date: "2026-08-16T00:03:47.129066+00:00"
question: "Trace flow around download(), direct link parsing, DownloadWorker status, and /register.pl false bypass"
contributor: "graphify"
outcome: "useful"
source_nodes: ["download()", "DownloadWorker", ".run()"]
---

# Q: Trace flow around download(), direct link parsing, DownloadWorker status, and /register.pl false bypass

## Answer

Expanded from original query via graph vocab: [download, direct, link, bypass, proxy, retry, request, status, worker, url]. DFS depth 2 returned 67 nodes. Extracted evidence: DownloadWorker method .run() calls download() at core/download/workers.py:L213; download() is defined at core/download/download.py:L31 and calls wait_for_password(), convert_size(), and download_speed(). Explain reports degree 6. No graph path exists from DownloadWorker to the screenshot-derived Proxy Bypass Status node, so status behavior must be verified in source and tests.

## Outcome

- Signal: useful

## Source Nodes

- download()
- DownloadWorker
- .run()