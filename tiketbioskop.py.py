import tkinter as tk
from tkinter import messagebox

harga_tiket = 75000

pajak = 0.10

biaya_layanan = 5000

def hitung_total():
    try:
        jumlah = int(entry_jumlah.get())

        if jumlah <= 0:
            messagebox.showwarning(
                "Peringatan",
                "Jumlah tiket harus lebih dari 0!"
            )
            return

        subtotal = harga_tiket * jumlah
        total_pajak = subtotal * pajak
        total_bayar = subtotal + total_pajak + biaya_layanan

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
root = tk.Tk()
root.title("Tiket Bioskop")
root.geometry("350x250")

tk.Label(
    root,
    text="PEMBELIAN TIKET BIOSKOP"
).pack(pady=10)

tk.Label(
    root,
    text="Masukkan Jumlah Tiket:"
).pack()

entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

tk.Button(
    root,
    text="Hitung Total",
    command=hitung_total
).pack(pady=10)

root.mainloop()
