# Product Requirements Document (PRD) - Bioskop Yuk! (m.tix Cinema 21)

## 1. Ringkasan Eksekutif & Tujuan Proyek
"Bioskop Yuk!" adalah aplikasi web pemesanan tiket bioskop interaktif berbasis Python dan Streamlit. Aplikasi ini mensimulasikan platform m.tix Cinema 21 secara mobile-friendly dengan tema pastel soft pink dan soft blue. Dokumen PRD ini dirancang secara rinci agar setiap anggota kelompok maupun AI pendamping dapat memahami spesifikasi fungsional dan teknis secara mendalam.

---

## 2. Rincian Pembagian Tugas & Tanggung Jawab Anggota Kelompok (Jobdesk)

### A. Ita — Desain UI/UX & Kerangka Web Interaktif
- **Fokus Utama:** Arsitektur halaman web, navigasi alur sistem, dan estetika visual.
- **Detail Teknis & Implementasi:**
  - Menggunakan modul streamlit (st.set_page_config, st.tabs, st.columns, st.button).
  - Mengelola status navigasi multi-langkah menggunakan st.session_state (page, step, selected_movie, selected_cinema, selected_date, selected_time, selected_seats, selected_fb).
  - Menyusun styling CSS kustom (st.markdown dengan unsafe_allow_html=True) untuk tema pastel (Soft Pink dan Soft Blue) ala m.tix mobile.

### B. Repa — Manajemen Katalog Film & Database Jadwal Studio
- **Fokus Utama:** Pengelolaan data film yang sedang tayang, advance ticket, dan database bioskop.
- **Detail Teknis & Implementasi:**
  - Menggunakan struktur data List of Dictionaries (MOVIES dan CINEMAS) serta Tuples untuk data statis.
  - Menerapkan format string untuk menampilkan harga, durasi, usia penonton (D17+, R13+, SU 13+), serta genre film.
  - Perulangan data (for loop) untuk menampilkan daftar film secara dinamis ke dalam kartu poster portrait di halaman utama maupun halaman pemesanan.

### C. Viron — Sistem Interaktif Denah Kursi Studio
- **Fokus Utama:** Pemilihan kursi bioskop secara visual dan interaktif.
- **Detail Teknis & Implementasi:**
  - Menggunakan struktur data List Comprehension untuk menghasilkan daftar kursi secara otomatis dari baris A sampai D dan kolom 1 sampai 6 (A1-D6).
  - Menerapkan percabangan (if-else) dan perulangan (for) untuk validasi ketersediaan kursi serta batas minimal booking (minimal 1 kursi harus dipilih).
  - Integrasi dengan st.multiselect untuk menangkap daftar kursi pilihan penonton secara real-time.

### D. Apriyanti — Logika Perhitungan Biaya, Camilan Café XXI, Pajak & Total
- **Fokus Utama:** Kalkulasi finansial, transaksi F&B, dan pajak hiburan.
- **Detail Teknis & Implementasi:**
  - Mengelola menu camilan (FB_MENU) dengan tipe data bilangan (Integer untuk harga dan Float/Integer untuk kuantitas porsi).
  - Menerapkan operator aritmatika dasar untuk menghitung:
    - Subtotal Tiket = Jumlah Kursi * Harga Film
    - Subtotal F&B = Jumlah (Harga Makanan * Kuantitas)
    - Pajak Hiburan 10% = 10% * (Subtotal Tiket + Subtotal F&B)
    - Biaya Layanan m.tix = Rp 3.000 (tetap)
    - Total Pembayaran Keseluruhan = Subtotal Tiket + Subtotal F&B + Pajak + Biaya Layanan.

### E. Shireen — Checkout Pembayaran, Validasi Eksepsi & Penerbitan E-Ticket Digital
- **Fokus Utama:** Keamanan transaksi, metode pembayaran, validasi eksepsi, dan e-ticket.
- **Detail Teknis & Implementasi:**
  - Menerapkan seleksi kondisi (if-elif-else) untuk berbagai metode pembayaran (QRIS, Virtual Account BCA/Mandiri, Kartu Kredit/Debit, Tunai di Kasir).
  - Menerapkan penanganan error & validasi input (Error Handling / try-except) pada fitur "Cek Tiket" menggunakan kode booking unik (contoh: BYK-123456).
  - Merancang tampilan E-Ticket digital lengkap dengan nomor kode booking acak (random.randint), rincian pesanan, dan simulasi barcode.
