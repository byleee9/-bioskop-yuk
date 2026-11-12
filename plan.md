# Project Plan (plan.md) — Rencana Kerja & Eksekusi "Bioskop Yuk!"

## 1. Milestone & Tahapan Pengembangan
Proyek ini dikerjakan secara terstruktur dan kolaboratif oleh 5 anggota tim dengan tahapan sebagai berikut:

### Tahap 1: Inisialisasi & Kerangka Dasar (Oleh Ita)
- Membuat berkas utama app_web_xxi.py dan konfigurasi dasar Streamlit.
- Menyiapkan arsitektur st.session_state agar perpindahan halaman/langkah (steps) berjalan mulus tanpa kehilangan data.
- Menulis kode CSS global untuk tema pastel soft pink dan soft blue dengan tampilan mobile container (lebar max 480px).

### Tahap 2: Database Film & Bioskop (Oleh Repa)
- Menyusun struktur data MOVIES (List of Dictionaries) berisi ID, judul, format, rating usia, durasi, genre, harga, tautan poster portrait, dan sinopsis.
- Menyusun data CINEMAS berisi daftar bioskop di Pontianak dan sekitarnya lengkap dengan informasi studio dan nomor kontak.

### Tahap 3: Denah & Pemilihan Kursi (Oleh Viron)
- Mengimplementasikan list comprehension untuk menghasilkan array kursi (A1-D6).
- Membuat komponen interaktif pemilihan kursi dan validasi agar tombol lanjut tidak aktif jika belum memilih kursi.

### Tahap 4: F&B Café & Kalkulasi Finansial (Oleh Apriyanti)
- Menambahkan daftar menu camilan XXI (FB_MENU).
- Menghubungkan input jumlah porsi (st.number_input) dengan perhitungan aritmatika otomatis untuk tiket, F&B, pajak hiburan 10%, dan biaya layanan.

### Tahap 5: Checkout, Validasi & E-Ticket Digital (Oleh Shireen)
- Membuat dropdown pilihan metode pembayaran dan tombol konfirmasi bayar.
- Menambahkan logika penerbitan kode booking unik serta fitur pencarian tiket melalui tab "Cek Tiket" dengan validasi try-except.
- Menguji seluruh alur aplikasi dari awal hingga akhir untuk memastikan tidak ada bug atau error sintaks.

## 2. Cara Menjalankan Proyek
pip install streamlit
py -m streamlit run app_web_xxi.py
