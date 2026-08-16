---
type: "query"
date: "2026-08-15T23:53:51.216886+00:00"
question: "Mengapa GuiBehavior menghubungkan Download Behavior Controls dengan Main GUI Workflow dan GUI Loading Signals?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["GuiBehavior", ".add_links()", ".download_receive_signal()", ".show_loading_overlay()", ".hide_loading_overlay()", "FilterWorker", "DownloadWorker"]
---

# Q: Mengapa GuiBehavior menghubungkan Download Behavior Controls dengan Main GUI Workflow dan GUI Loading Signals?

## Answer

Expanded from original query via graph vocab: [gui, behavior, download, controls, main, loading, signals, worker]. GuiBehavior is the orchestration hub: its pause/resume/stop methods own user controls; add_links creates FilterWorker; download_receive_signal creates DownloadWorker; show/hide loading wrappers delegate visual state to Gui. This crosses communities 1, 3, 12, and 0.

## Outcome

- Signal: useful

## Source Nodes

- GuiBehavior
- .add_links()
- .download_receive_signal()
- .show_loading_overlay()
- .hide_loading_overlay()
- FilterWorker
- DownloadWorker