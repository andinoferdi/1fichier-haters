<!-- BEGIN:project-context -->
# 1fichier-haters

Stack: `Python 3.11 (core/download - download engine, worker threads, proxy & reCAPTCHA bypass)` + `PyQt5 (core/gui - desktop GUI)` + `tidak ada database (state/config di app/settings dan file proxy list lokal)`. Baca file tree dulu, struktur nyata repo adalah sumber kebenaran. Jangan tambah framework/library baru jika stack atau helper project sudah cukup. Abaikan `__pycache__`, `graphify-out`, `dist`, `build`, log dan asset besar.
<!-- END:project-context -->

<!-- BEGIN:coding-rules -->
# Coding rules

Perubahan minimal dan spesifik pada task. Pahami file terdekat, route/endpoint terkait, dan pola modul sebelum mengubah kode. Jangan rombak arsitektur atau redesign UI tanpa instruksi eksplisit.

- Jaga route, method, middleware, permission, dan kontrak request/response yang sudah berjalan.
- Validasi input di server. Jangan percaya role, harga, stok, status, atau ownership dari client.
- Logic berat ikut pola layer yang ada, bukan menumpuk di controller/handler.
- Hindari N+1 pada listing, tabel, export, dan dashboard.
- Jangan hardcode secret, credential, URL production, token, atau API key.
<!-- END:coding-rules -->

<!-- BEGIN:commands -->
# Commands

Jika RTK tersedia, awali shell command dengan `rtk`.

```powershell
rtk python 1fichier-dl.py
rtk python -m unittest discover -s tests
rtk pyinstaller --windowed --noconsole --onefile --noconfirm --clean --hiddenimport=_cffi_backend --additional-hooks-dir=. --icon=core/gui/res/ico.ico --add-data "core/gui/res/*.*;res/" .\1fichier-dl.py
```

Jalankan hanya command yang relevan dengan task. Verifikasi sesuai area perubahan: unittest untuk logic di `core/download`, cek manual GUI untuk perubahan di `core/gui`, build PyInstaller hanya kalau task menyentuh proses build/release. Jika verifikasi tidak bisa jalan karena environment, catat alasannya di final response. Jangan jalankan command berat (full build, full test suite, deploy) tanpa kebutuhan task.
<!-- END:commands -->

<!-- BEGIN:safety -->
# Safety

- Jangan commit, push, atau membuat build release (PyInstaller) tanpa instruksi eksplisit.
- Jangan mengubah `https_proxy_list.txt`/`socks5_proxy_list.txt` default atau file di `app/settings` tanpa alasan jelas dari task.
- Jangan menghapus validasi input link, filter duplicate, atau error handling proxy/reCAPTCHA demi menyederhanakan kode.
- Jangan mengubah file environment/hook (`hook-curl_cffi.py`, `.vscode/settings.json`) kecuali diminta.
- Ada perubahan user di worktree yang bukan buatan Anda: jangan revert, bekerja berdampingan.
<!-- END:safety -->

<!-- BEGIN:related-docs -->
# Related docs

Ikuti bersama `chat-rules.md`, `code-rules.md`, dan `token.md`. Detail teknis: `be-rules.md`, `fe-rules.md`. Git: `git-workflow.md`, `git-naming.md`, `git-branch-tips.md`. Konflik aturan: instruksi sistem/platform > instruksi user terbaru > dokumen ini.
<!-- END:related-docs -->

<!-- Block di bawah ini milik tool/framework (auto-generated). Jangan edit manual, biarkan tool yang update. Contoh: -->

<!-- BEGIN:nextjs-agent-rules -->
<!-- Terisi otomatis oleh Next.js bila project memakainya. Hapus placeholder ini jika tidak relevan. -->
<!-- END:nextjs-agent-rules -->
