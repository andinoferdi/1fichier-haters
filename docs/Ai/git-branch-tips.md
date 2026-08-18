# Git Branch Tips

Tips praktis menjaga branch dan Pull Request tetap bersih di `1fichier-haters`. Repo ini solo dev, hanya punya branch `main` (tidak ada staging terpisah). Panduan utama tetap `git-workflow.md` dan `git-naming.md`.

## 1. Mulai branch dari branch utama
Pakai `origin/main` sebagai titik mulai agar branch benar-benar dari remote terbaru.

```bash
git fetch origin --prune
git checkout -b andinoferdi/feat/nama-fitur origin/main
```

Local `main` boleh dipakai bila sudah dipastikan sama dengan remote:

```bash
git checkout main
git pull --ff-only origin main
git checkout -b andinoferdi/feat/nama-fitur
```

Alasan mulai dari branch utama: branch lebih bersih, PR hanya berisi task sendiri, tidak membawa commit lain.

## 2. Meniru branch lain: jangan langsung merge
Untuk sekadar meniru behavior dari branch eksperimen, lihat bedanya dulu, jangan merge branch itu ke branch kerja.

```bash
git diff main..origin/nama-branch-lain -- path/relevan
git show origin/nama-branch-lain:path/ke/file      # lihat file tanpa pindah branch
```

Cherry-pick hanya untuk mem-port commit tertentu secara terkontrol. Setelah tahu behavior yang dibutuhkan, implementasikan di branch sendiri sesuai scope task.

## 3. Commit kecil, satu concern
Jangan tunggu semua selesai baru commit sekali. Commit kecil lebih mudah dicek, di-cherry-pick, dan resolve conflict.

```bash
git add core/download/workers.py
git commit -m "feat(download): tambah flow utama"
git add tests/test_duplicate_download_regression.py
git commit -m "test(download): tambah test flow utama"
```

## 4. Pola rebuild dari branch utama
Kalau branch kerja sudah lama tertinggal dari `main` dan merge langsung membuat diff membengkak (ikut membawa banyak commit lain), rebuild branch dari `main` lalu cherry-pick commit sendiri.

Diagnosis dulu sebelum mengubah history:

```bash
git fetch origin --prune
git rev-list --count origin/main..HEAD
git diff --stat origin/main...HEAD
git log --oneline origin/main..HEAD
```

Jika diff terhadap `main` besar dan banyak file non-task, rebuild:

```bash
git checkout -b andinoferdi/feat/nama-fitur-clean origin/main
git cherry-pick <commit_task_1>
git cherry-pick <commit_task_2>
```

Kalau conflict muncul, resolve hanya di file area fitur. Pertahankan `origin/main` sebagai baseline, tambahkan perubahan fitur di titik yang diperlukan. Jangan membawa perubahan milik task lain hanya karena ikut muncul. Jangan commit folder tool/cache untracked (contoh: `graphify-out/`, `__pycache__/`).

## 5. Verifikasi diff tetap fokus
Sebelum update branch PR:

```bash
git diff --stat origin/main...HEAD
git diff --name-only origin/main...HEAD
git diff --check
git log --oneline origin/main..HEAD
```

Ekspektasi: file changed hanya area fitur, commit hanya commit sendiri, tidak ada whitespace error. Jalankan syntax check/targeted test sesuai area (`python -m py_compile`, atau jalankan `python 1fichier-dl.py` untuk cek manual GUI). Kalau diff membengkak, stop, biasanya ada commit asing atau base branch salah.

## 6. Update branch PR dengan aman
Gunakan `--force-with-lease`, bukan `--force` (Git menolak bila remote berubah tanpa sepengetahuan lokal).

```bash
git push --force-with-lease origin HEAD:andinoferdi/feat/nama-fitur
```

Setelah push: refresh PR, pastikan conflict hilang, `Files changed` fokus, commit hanya milik sendiri. Update remote PR hanya setelah yakin bersih.

## 7. Sinkronkan local branch
```bash
git checkout andinoferdi/feat/nama-fitur
git fetch origin --prune
git pull --ff-only origin andinoferdi/feat/nama-fitur
```

Jika history berbeda karena remote sudah di-force-with-lease, samakan local ke remote hanya setelah working tree bersih:

```bash
git branch -f andinoferdi/feat/nama-fitur origin/andinoferdi/feat/nama-fitur
```

## 8. Warning
- Jangan `git push --force`. Pakai `--force-with-lease` dan hanya di branch sendiri.
- Jangan commit file environment, credential, API key, log, cache (`graphify-out/`, `__pycache__/`, `app/settings`), atau perubahan debug.
- Jangan branch dari branch orang jika tidak ingin commit mereka ikut PR.
- Jangan merge `origin/main` langsung ke branch PR bila tujuannya hanya menjaga diff PR tetap fokus saat `main` banyak berubah dari kontributor lain.

## Referensi
- git cherry-pick: https://git-scm.com/docs/git-cherry-pick
- git push & --force-with-lease: https://git-scm.com/docs/git-push
- Resolve conflict via CLI: https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line
