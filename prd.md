# Product Requirements Document (PRD) - Bioskop Yuk! (Python GUI Tkinter)

## 1. Ringkasan Eksekutif & Tujuan Proyek
"Bioskop Yuk!" adalah aplikasi desktop GUI pemesanan tiket bioskop interaktif yang dikembangkan menggunakan bahasa pemrograman **Python** dan pustaka **Tkinter**. Aplikasi ini dirancang untuk memenuhi tugas proyek akhir Pemrograman Dasar dengan antarmuka grafis yang elegan, sinematik, dan mudah dioperasikan.

## 2. Rincian Pembagian Tugas Anggota Kelompok (Jobdesk)
1. **Ita — Desain Antarmuka Utama (UI/UX) & Kerangka GUI**
   - Mengatur struktur jendela utama Tkinter (`tk.Tk`, ukuran, geometri, dan tema warna sinematik elegan).
   - Menata tata letak header, label, listbox, dan tombol aksi.
2. **Repa — Manajemen Katalog Film & Database Jadwal**
   - Menyusun struktur data `List of Dictionaries` (`daftar_film`) berisi judul, genre, dan harga tiket.
   - Mengisi komponen `Listbox` agar menampilkan daftar film secara rapi dan dinamis.
3. **Viron — Sistem Interaktif Pemilihan Film & Validasi**
   - Menangani fungsi klik pada `Listbox` (`curselection()`) untuk mendeteksi film yang dipilih pengguna.
   - Menerapkan percabangan (`if-else`) untuk memastikan pengguna sudah memilih film sebelum melanjutkan transaksi.
4. **Apriyanti — Logika Perhitungan Biaya, Pajak & Total**
   - Mengelola input jumlah tiket dengan tipe data Integer.
   - Menerapkan operator aritmatika dasar untuk menghitung subtotal, **Pajak Hiburan 10%**, biaya layanan, dan total pembayaran keseluruhan.
5. **Shireen — Metode Pembayaran & Penerbitan E-Ticket Digital**
   - Menyediakan pilihan metode pembayaran menggunakan `Radiobutton` (QRIS, Transfer Bank, Tunai).
   - Menangani validasi error (`try-except`) serta menerbitkan kotak dialog **E-Ticket Digital** lengkap dengan kode booking acak (`random.randint`).

## 3. Cara Menjalankan Aplikasi
```bash
python main.py
```
