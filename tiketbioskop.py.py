import tkinter as tk
from tkinter import messagebox

# Harga tiket bioskop
harga_tiket = 75000

# Pajak hiburan 10%
pajak = 0.10

# Biaya layanan per transaksi
biaya_layanan = 5000

def hitung_total():
    try:
        # Mengambil jumlah tiket
        jumlah = int(entry_jumlah.get())

        # Validasi jumlah tiket
        if jumlah <= 0:
            messagebox.showwarning(
                "Peringatan",
                "Jumlah tiket harus lebih dari 0!"
            )
            return

        # Menghitung biaya
        subtotal = harga_tiket * jumlah
        total_pajak = subtotal * pajak
        total_bayar = subtotal + total_pajak + biaya_layanan

        # Menampilkan hasil perhitungan
        hasil = (
            f"Harga Tiket: Rp{harga_tiket:,}\n"
            f"Jumlah Tiket: {jumlah}\n"
            f"Subtotal: Rp{subtotal:,.0f}\n"
            f"Pajak 10%: Rp{total_pajak:,.0f}\n"
            f"Biaya Layanan: Rp{biaya_layanan:,.0f}\n"
            f"--------------------------\n"
            f"Total Bayar: Rp{total_bayar:,.0f}"
        )

        messagebox.showinfo("Rincian Pembayaran", hasil)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Masukkan jumlah tiket dengan angka!"
        )
# Membuat jendela aplikasi
root = tk.Tk()
root.title("Tiket Bioskop")
root.geometry("350x250")

# Judul
tk.Label(
    root,
    text="PEMBELIAN TIKET BIOSKOP"
).pack(pady=10)

# Kotak jumlah tiket
tk.Label(
    root,
    text="Masukkan Jumlah Tiket:"
).pack()

entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol hitung
tk.Button(
    root,
    text="Hitung Total",
    command=hitung_total
).pack(pady=10)

root.mainloop()