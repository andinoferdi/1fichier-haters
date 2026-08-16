# Graph Report - .  (2026-08-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 240 nodes · 270 edges · 27 communities
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 24 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `070e9b91`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GuiBehavior
- DownloadWorker
- Python Dependency Set
- 1Fichier-dl Project
- download.py
- Download Manager Shell
- Connection Tab
- Download Manager Shell
- Download Manager Shell
- Proxy Bypass Status
- 1fichier File Page
- Browser Address Bar
- Clipboard Icon
- Zap Icon
- Application Icon
- 1Fichier Downloader Application Icon
- Vector Application Icon
- Download Icon
- GitHub Mark
- Three-segment Loading Spinner
- Pause Action
- Resume Action
- Configuration Action
- Red Cross Stop Icon

## God Nodes (most connected - your core abstractions)
1. `GuiBehavior` - 20 edges
2. `DownloadWorker` - 11 edges
3. `Gui` - 11 edges
4. `Python Dependency Set` - 9 edges
5. `1Fichier-dl Project` - 7 edges
6. `HTTPS Proxy Source List` - 7 edges
7. `FilterWorker` - 6 edges
8. `check_selection()` - 6 edges
9. `1Fichier Download Manager` - 6 edges
10. `absp()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `PyInstaller One-file Build Command` --references--> `PyInstaller 5.13.2`  [INFERRED]
  build command.txt → requirements.txt
- `requests[socks]` --conceptually_related_to--> `SOCKS5 Proxy Source List`  [INFERRED]
  requirements.txt → socks5_proxy_list.txt
- `HTTPS Proxy Source List` --conceptually_related_to--> `SOCKS5 Proxy Source List`  [INFERRED]
  https_proxy_list.txt → socks5_proxy_list.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Supported Link Bypass Inputs** — readme_1fichier_download_manager, readme_proxy_wait_bypass, readme_ouo_recaptcha_bypass, readme_clipboard_download [EXTRACTED 1.00]
- **Windows One-file Build Bundle** — build_command_pyinstaller_onefile_command, build_command_application_entrypoint, build_command_gui_resources, build_command_cffi_hidden_import [EXTRACTED 1.00]
- **Remote Proxy Source Aggregation** — https_proxy_list_https_proxy_sources, socks5_proxy_list_socks5_proxy_sources, readme_proxy_wait_bypass [INFERRED 0.85]
- **Primary Download Workflow** — screenshots_screenshot_dark_top_action_toolbar, screenshots_screenshot_dark_downloads_table, screenshots_screenshot_dark_bottom_download_controls [INFERRED 0.95]
- **Primary Download Workflow** — screenshots_screenshot_light_top_action_toolbar, screenshots_screenshot_light_downloads_table, screenshots_screenshot_light_bottom_download_controls [INFERRED 0.95]
- **Download Lifecycle Controls** — screenshots_preview0_resume_control, screenshots_preview0_pause_control, screenshots_preview0_remove_control [EXTRACTED 1.00]
- **Link Acquisition Actions** — screenshots_preview0_clipboard_link_input, screenshots_preview0_manual_link_input, screenshots_preview0_settings_access [INFERRED 0.75]
- **Proxy Bypass Observability** — screenshots_preview_settings0_proxy_bypass_status, screenshots_preview_settings0_bypass_attempt_counter, screenshots_preview_settings0_proxy_server_column, screenshots_preview_settings0_zero_transfer_speed [INFERRED 0.95]
- **Connection Tuning Controls** — screenshots_preview_settings1_request_timeout_setting, screenshots_preview_settings1_direct_proxy_list_setting, screenshots_preview_settings1_simultaneous_proxy_downloads_setting [EXTRACTED 1.00]

## Communities (27 total, 0 thin omitted)

### Community 0 - "GuiBehavior"
Cohesion: 0.06
Nodes (22): abs_config(), absp(), alert(), check_selection(), create_file(), getClipboardText(), Gui, GuiBehavior (+14 more)

### Community 1 - "DownloadWorker"
Cohesion: 0.10
Nodes (20): convert_size(), download_speed(), get_all_proxies(), get_link_info(), get_proxies(), get_proxies_from_api(), is_valid_link(), process_proxy_list() (+12 more)

### Community 2 - "Python Dependency Set"
Cohesion: 0.08
Nodes (24): 1fichier-dl.py Entry Point, _cffi_backend Hidden Import, GUI Resource Bundle, PyInstaller One-file Build Command, claude89757 free_https_proxies, databay-labs free-proxy-list, gfpcom free-proxy-list, HTTPS Proxy Source List (+16 more)

### Community 3 - "1Fichier-dl Project"
Cohesion: 0.12
Nodes (17): 1Fichier-dl Project, 1Fichier Download Manager, Proposed Asyncio Downloads, Add from Clipboard, User-provided Proxy List, Feather Icons, FREE_PROXIES_LIST, loading.io (+9 more)

### Community 4 - "download.py"
Cohesion: 0.18
Nodes (5): download(), Name is self-explanatory.     1 - Get direct 1Fichier link using proxies., wait_for_password(), DownloadRetryRegressionTest, Response

### Community 5 - "Download Manager Shell"
Cohesion: 0.22
Nodes (9): Clipboard Link Input, Download Manager Shell, Downloads Table, Downloader Main Window Screenshot, Manual Link Input, Pause Control, Remove Control, Resume Control (+1 more)

### Community 6 - "Connection Tab"
Cohesion: 0.22
Nodes (9): Connection Configuration, Connection Settings Screenshot, Connection Tab, Dark Download Manager, Direct Proxy List Setting, Request Timeout Setting, Restart Required Constraint, Settings Dialog (+1 more)

### Community 7 - "Download Manager Shell"
Cohesion: 0.22
Nodes (9): Bottom Download Controls, Dark Theme, Dark Theme Downloader Screenshot, Download Directory Control, Download Manager Shell, Downloads Table, Settings Dialog, Theme Selector (+1 more)

### Community 8 - "Download Manager Shell"
Cohesion: 0.22
Nodes (9): Bottom Download Controls, Download Directory Control, Download Manager Shell, Downloads Table, Light Theme, Light Theme Downloader Screenshot, Settings Dialog, Theme Selector (+1 more)

### Community 9 - "Proxy Bypass Status"
Cohesion: 0.25
Nodes (8): Active Bypass Screenshot, Bypass Attempt Counter, Dark Download Manager, Parallel Download Rows, No Password State, Proxy Bypass Status, Proxy Server Column, Zero Transfer Speed

### Community 10 - "1fichier File Page"
Cohesion: 0.33
Nodes (7): Browser Address Bar, 1fichier Browser Screenshot, 1fichier File Page, File Metadata Panel, Highlighted 1fichier File URL, Premium Subscription Modal, Waiting and Speed Limitations

### Community 11 - "Browser Address Bar"
Cohesion: 0.33
Nodes (7): Browser Address Bar, OUO Shortlink Browser Screenshot, Destination Gate Card, Destination Redirect Flow, Highlighted OUO Short URL, Human Verification Button, ouo.io Shortlink Page

### Community 12 - "Clipboard Icon"
Cohesion: 0.40
Nodes (5): Clipboard Icon, Clipboard Input Action, Clipboard Visual Metaphor, Feather Outline Style, Indigo Action Accent

### Community 13 - "Zap Icon"
Cohesion: 0.40
Nodes (5): Feather Zap Outline, Indigo Action Accent, Lightning Bolt Metaphor, Speed Action Cue, Zap Icon

### Community 14 - "Application Icon"
Cohesion: 0.40
Nodes (5): Application Icon, Download Application Identity, Download Arrow Symbol, Indigo Brand Tile, Rounded Square Tile

### Community 15 - "1Fichier Downloader Application Icon"
Cohesion: 0.50
Nodes (4): 1Fichier Downloader Application Icon, Application Identity, Download Action, Rounded-square Application Branding

### Community 16 - "Vector Application Icon"
Cohesion: 0.50
Nodes (4): Vector Application Icon, Vector Application Identity, Download Action, Scalable Brand Asset

### Community 17 - "Download Icon"
Cohesion: 0.67
Nodes (3): Download Action, Download Icon, Downward Transfer Metaphor

### Community 18 - "GitHub Mark"
Cohesion: 0.67
Nodes (3): GitHub Mark, GitHub Platform, Source Repository Navigation

### Community 19 - "Three-segment Loading Spinner"
Cohesion: 0.67
Nodes (3): Cyclic Waiting Metaphor, Indeterminate Progress, Three-segment Loading Spinner

### Community 20 - "Pause Action"
Cohesion: 0.67
Nodes (3): Download Control, Pause Action, Pause Icon

### Community 21 - "Resume Action"
Cohesion: 0.67
Nodes (3): Download Control, Resume Action, Resume Icon

### Community 22 - "Configuration Action"
Cohesion: 0.67
Nodes (3): Application Preferences, Configuration Action, Settings Gear Icon

### Community 23 - "Red Cross Stop Icon"
Cohesion: 0.67
Nodes (3): Destructive Control, Red Cross Stop Icon, Stop or Remove Action

## Knowledge Gaps
- **81 isolated node(s):** `User-provided Proxy List`, `ouo.io reCAPTCHA Bypass`, `Add from Clipboard`, `Python 3.11`, `Feather Icons` (+76 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DownloadWorker` connect `DownloadWorker` to `GuiBehavior`, `download.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `FilterWorker` connect `DownloadWorker` to `GuiBehavior`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **What connects `User-provided Proxy List`, `ouo.io reCAPTCHA Bypass`, `Add from Clipboard` to the rest of the system?**
  _81 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `GuiBehavior` be split into smaller, more focused modules?**
  _Cohesion score 0.06431372549019608 - nodes in this community are weakly interconnected._
- **Should `DownloadWorker` be split into smaller, more focused modules?**
  _Cohesion score 0.0967741935483871 - nodes in this community are weakly interconnected._
- **Should `Python Dependency Set` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `1Fichier-dl Project` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._