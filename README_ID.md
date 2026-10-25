# Ranking Position Ladies — Festival Citylink (FINAL Office 2013)

## Isi paket
- `app.py`: aplikasi Streamlit yang membuat PowerPoint dari template bersih.
- `template_ranking.pptx`: template terbaru yang dikirimkan, berisi 26 slide.
- `requirements.txt`: dependensi aplikasi.

## Pasang / perbarui di GitHub
1. Ekstrak ZIP di komputer.
2. Buka repository GitHub dan ganti file `app.py` dengan `app.py` dari paket ini.
3. Ganti file `template_ranking.pptx` dengan file dari paket ini. Nama harus persis sama.
4. Ganti `requirements.txt` dengan versi dalam paket.
5. Klik **Commit changes** dan tunggu deployment Streamlit selesai.

## Cara penggunaan
1. Pilih tanggal mulai dan akhir laporan.
2. Pilih kategori dan ranking, lalu ambil foto melalui kamera atau unggah dari perangkat.
3. Klik **Simpan foto ke daftar ranking**. Ulangi untuk setiap slot.
4. Klik **BUAT POWERPOINT & KOSONGKAN DAFTAR**.
5. Unduh hasil dari tombol **Download PowerPoint (.pptx)**.

## Perilaku aplikasi
- Foto masuk ke slide kategori dan ranking yang dipilih.
- Slide utama **POSITION RANKING** (slide 2) menampilkan foto GLOBAL rank 1. Jika slot itu belum diisi, aplikasi memakai foto pertama yang dimasukkan.
- Setiap file baru dibuat dari template asli yang bersih; foto laporan sebelumnya tidak dimasukkan ke template.
- Setelah pembuatan berhasil, daftar foto serta input kamera/upload direset untuk laporan berikutnya.
- Tidak memakai database.

## Kompatibilitas
File keluaran disimpan sebagai `.pptx` standar dan diperiksa dengan validasi ZIP serta dibuka ulang menggunakan `python-pptx`. Ini bukan pengujian langsung di Microsoft PowerPoint 2013; setelah deploy, buat satu laporan percobaan dan buka hasilnya di PowerPoint desktop.
