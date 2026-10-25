# Ranking Position Ladies — Festival Citylink (Paket Final)

Paket ini menggunakan template PowerPoint terbaru yang dikirim pada percakapan ini.

## Isi paket
- `app.py` — aplikasi Streamlit untuk memasukkan foto ranking dan menghasilkan PowerPoint.
- `template_ranking.pptx` — template terbaru 26 slide.
- `requirements.txt` — pustaka yang diperlukan.

## Menjalankan di komputer
1. Ekstrak ZIP ke folder baru.
2. Buka Command Prompt di folder hasil ekstrak.
3. Jalankan `python -m pip install -r requirements.txt`.
4. Jalankan `python -m streamlit run app.py`.
5. Buka alamat lokal yang ditampilkan di terminal.

## Deploy ke GitHub / Streamlit Community Cloud
Unggah `app.py`, `requirements.txt`, dan `template_ranking.pptx` ke folder utama repository. Pastikan nama template tepat `template_ranking.pptx`, lalu tunggu deployment selesai.

## Cara kerja
- Setiap laporan dibuat dari template asli yang bersih; hasil sebelumnya tidak digunakan sebagai template.
- Setelah PowerPoint berhasil dibuat, daftar foto input dikosongkan otomatis.
- File hasil diperiksa sebagai arsip PPTX dan dicoba dibuka kembali oleh `python-pptx` sebelum disediakan untuk diunduh.
- Data tidak disimpan ke database.
