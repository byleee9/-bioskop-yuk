# UI/UX Design & Architecture Specification (design.md) — "Bioskop Yuk!"

## 1. Konsep & Arsitektur Desain
Aplikasi web ini dirancang menggunakan paradigma Mobile-First Design agar menyerupai aplikasi seluler resmi m.tix Cinema 21. Seluruh elemen antarmuka dibungkus dalam kontainer berukuran seluler dengan orientasi vertikal yang bersih.

## 2. Panduan Warna & Tipografi (Pastel Theme)
- Background Utama (#111 & #161616): Memberikan kesan bioskop gelap yang elegan dan sinematik.
- Warna Aksen Utama (#FFB6C1 - Soft Pink): Digunakan untuk judul logo, sorotan harga, tombol interaktif utama, badge rating usia, dan garis pembatas penting.
- Warna Aksen Sekunder (#BEE3F8 - Soft Blue): Digunakan untuk informasi lokasi, tag format studio (IMAX, Dolby Atmos), dan teks bantuan.
- Tipografi: Menggunakan font modern sans-serif (Inter / Quicksand / Poppins) untuk keterbacaan yang optimal pada layar kecil.

## 3. Spesifikasi Komponen & Halaman (Berdasarkan Jobdesk)
1. Halaman Beranda & Katalog (Ita & Repa):
   - Menampilkan banner selamat datang, daftar film sedang tayang dalam bentuk scroll horizontal/vertikal dengan poster format portrait (object-fit: cover).
   - Tab informasi tipe studio (IMAX, Premiere, Deluxe, Dolby Atmos).
2. Halaman Pemilihan Jadwal & Kursi (Ita, Repa, & Viron):
   - Pemilihan bioskop, tanggal, dan jam tayang.
   - Denah kursi interaktif dengan legenda warna (Tersedia, Dipilih, Terisi).
3. Halaman Café & F&B (Apriyanti):
   - Daftar camilan dengan kartu menu rapi dan pengatur jumlah porsi.
4. Halaman Checkout & Pembayaran (Shireen):
   - Ringkasan total biaya transparan (Tiket + F&B + Pajak 10% + Layanan).
   - Pilihan metode pembayaran dan tombol eksekusi pembayaran.
5. Halaman E-Ticket Digital (Shireen):
   - Desain e-voucher tiket dengan kotak kode booking beraksen putus-putus dan simulasi barcode garis.
