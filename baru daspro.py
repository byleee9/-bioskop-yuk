import random
import tkinter as tk
from tkinter import messagebox


def proses_pembayaran():
  try:
    jumlah_tiket = int(entry_jumlah.get())

    if jumlah_tiket <= 0:
      messagebox.showwarning(
          "Peringatan Input", "Jumlah tiket minimal harus 1!"
      )
      return

  except ValueError:
    messagebox.showerror(
        "Error Input", "Masukkan jumlah tiket menggunakan angka yang valid!"
      )
    return

  metode = var_metode.get()
  if not metode:
    messagebox.showwarning(
        "Peringatan", "Silakan pilih metode pembayaran terlebih dahulu!"
    )
    return

  harga_satuan = 50000
  subtotal = harga_satuan * jumlah_tiket
  pajak = subtotal * 0.10
  biaya_layanan = 2500
  total_bayar = subtotal + pajak + biaya_layanan

  kode_booking = "BK-" + str(random.randint(10000, 99999))

  struk_eticket = (
      "------------------------------------\n"
      "           E-TICKET DIGITAL         \n"
      "------------------------------------\n"
      f"Kode Booking      : {kode_booking}\n"
      f"Jumlah Tiket      : {jumlah_tiket} Tiket\n"
      f"Metode Pembayaran : {metode}\n"
      f"Total Pembayaran  : Rp {total_bayar:,.0f}\n"
      "Status            : LUNAS\n"
      "------------------------------------\n"
      "Terima kasih! Tunjukkan E-Ticket ini\n"
      "saat memasuki area acara."
  )

  messagebox.showinfo("Penerbitan E-Ticket Berhasil", struk_eticket)


root = tk.Tk()
root.title("Aplikasi Pemesanan Tiket")
root.geometry("380x350")
root.configure(padx=20, pady=20)

tk.Label(root, text="Jumlah Tiket:", font=("Arial", 10, "bold")).pack(anchor="w")
entry_jumlah = tk.Entry(root, width=30)
entry_jumlah.pack(anchor="w", pady=(2, 15))

tk.Label(
    root, text="Pilih Metode Pembayaran:", font=("Arial", 10, "bold")
).pack(anchor="w")

var_metode = tk.StringVar(value="QRIS")

opsi_pembayaran = [
    "QRIS",
    "Transfer Bank (Virtual Account)",
    "E-Wallet (GoPay / OVO / DANA)",
]

for opsi in opsi_pembayaran:
  rb = tk.Radiobutton(
      root, text=opsi, variable=var_metode, value=opsi, font=("Arial", 10)
  )
  rb.pack(anchor="w", pady=2)

btn_bayar = tk.Button(
    root,
    text="Bayar & Terbitkan E-Ticket",
    command=proses_pembayaran,
    bg="#28a745",
    fg="white",
    font=("Arial", 10, "bold"),
    pady=6,
)
btn_bayar.pack(fill="x", pady=20)

root.mainloop()