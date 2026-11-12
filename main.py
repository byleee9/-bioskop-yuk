import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# PROGRAM BIOSKOP YUK! - TEMA ELEGAN & SINEMATIK
# ==========================================

daftar_film = [
    {"judul": "Avatar 3: Fire & Ash", "genre": "Sci-Fi / IMAX", "harga": 50000},
    {"judul": "Siksa Kubur: Reborn", "genre": "Horror / Premiere", "harga": 45000},
    {"judul": "Agak Laen 2: Menyala", "genre": "Comedy / Deluxe", "harga": 40000}
]

def jalankan_pemesanan():
    pilihan_index = list_box.curselection()
    if not pilihan_index:
        messagebox.showerror("Peringatan", "Silakan pilih salah satu film terlebih dahulu!")
        return
    
    index = pilihan_index[0]
    film_terpilih = daftar_film[index]
    
    try:
        jumlah_tiket = int(entry_jumlah.get())
        if jumlah_tiket <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Jumlah tiket harus berupa angka bulat positif!")
        return

    subtotal = jumlah_tiket * film_terpilih["harga"]
    pajak = int(0.10 * subtotal)  # Pajak hiburan 10%
    biaya_admin = 3000            # Biaya layanan
    total_bayar = subtotal + pajak + biaya_admin

    kode_booking = f"BYK-{random.randint(100000, 999999)}"
    metode = pilihan_bayar.get()

    struk = f"""
====================================
      🎬 E-TICKET VIP CINEMA 🎬       
====================================
Kode Booking : {kode_booking}
Judul Film   : {film_terpilih['judul']}
Genre/Studio : {film_terpilih['genre']}
Jumlah Tiket : {jumlah_tiket} Kursi
------------------------------------
Rincian Biaya:
- Subtotal   : Rp {subtotal:,}
- Pajak (10%): Rp {pajak:,}
- Layanan    : Rp {biaya_admin:,}
====================================
TOTAL BAYAR  : Rp {total_bayar:,}
Metode Bayar : {metode}
Status       : LUNAS ✅
====================================
Nikmati pengalaman menonton terbaik!
"""
    messagebox.showinfo("Tiket Berhasil Dipesan!", struk)

# ==========================================
# PEMBUATAN JENDELA UTAMA GUI (ELEGAN THEME)
# ==========================================
root = tk.Tk()
root.title("Bioskop Yuk! - VIP Cinema Edition")
root.geometry("520x620")
root.configure(bg="#121212") # Dark Cinematic Background

# Judul Header (Gold & Dark)
lbl_judul = tk.Label(root, text="🎬 BIOSKOP YUK! - VIP CINEMA 🎬", font=("Arial", 16, "bold"), bg="#1A1A24", fg="#D4AF37", pady=12)
lbl_judul.pack(fill="x")

# Label Petunjuk
lbl_info = tk.Label(root, text="Pilih Film Tayang:", font=("Arial", 10, "bold"), bg="#121212", fg="#E0E0E0")
lbl_info.pack(anchor="w", padx=25, pady=(15, 5))

# Listbox untuk Daftar Film
list_box = tk.Listbox(root, font=("Arial", 10), height=4, bg="#1E1E2D", fg="#FFFFFF", selectbackground="#D4AF37", selectforeground="#121212", bd=0, highlightthickness=1, highlightcolor="#D4AF37")
list_box.pack(fill="x", padx=25, pady=5)

for film in daftar_film:
    list_box.insert(tk.END, f"  {film['judul']} | {film['genre']} | Rp {film['harga']:,}")

# Input Jumlah Tiket
lbl_jml = tk.Label(root, text="Jumlah Tiket:", font=("Arial", 10, "bold"), bg="#121212", fg="#E0E0E0")
lbl_jml.pack(anchor="w", padx=25, pady=(15, 5))

entry_jumlah = tk.Entry(root, font=("Arial", 11), width=10, bg="#1E1E2D", fg="#FFFFFF", insertbackground="white", bd=0, relief="solid")
entry_jumlah.pack(anchor="w", padx=25, pady=5)
entry_jumlah.insert(0, "1")

# Pilihan Metode Pembayaran
lbl_bayar = tk.Label(root, text="Metode Pembayaran:", font=("Arial", 10, "bold"), bg="#121212", fg="#E0E0E0")
lbl_bayar.pack(anchor="w", padx=25, pady=(15, 5))

pilihan_bayar = tk.StringVar(value="QRIS VIP")
tk.Radiobutton(root, text="QRIS (Instant Payment)", variable=pilihan_bayar, value="QRIS VIP", bg="#121212", fg="#CCCCCC", selectcolor="#1E1E2D", activebackground="#121212", activeforeground="#FFFFFF", font=("Arial", 9)).pack(anchor="w", padx=35)
tk.Radiobutton(root, text="Transfer Bank (BCA / Mandiri / BNI)", variable=pilihan_bayar, value="Transfer Bank", bg="#121212", fg="#CCCCCC", selectcolor="#1E1E2D", activebackground="#121212", activeforeground="#FFFFFF", font=("Arial", 9)).pack(anchor="w", padx=35)
tk.Radiobutton(root, text="Cash / Tunai di Ticket Box", variable=pilihan_bayar, value="Tunai", bg="#121212", fg="#CCCCCC", selectcolor="#1E1E2D", activebackground="#121212", activeforeground="#FFFFFF", font=("Arial", 9)).pack(anchor="w", padx=35)

# Tombol Eksekusi (Gold Button)
btn_pesan = tk.Button(root, text="🎟️ Cetak E-Ticket VIP Sekarang", font=("Arial", 11, "bold"), bg="#D4AF37", fg="#121212", activebackground="#C59B27", activeforeground="#121212", command=jalankan_pemesanan, padx=15, pady=10, bd=0, cursor="hand2")
btn_pesan.pack(pady=25)

root.mainloop()
