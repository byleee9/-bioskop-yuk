# ==========================================
# Kode oleh Apriyanti - Perhitungan Biaya, Pajak & Total
# Kode oleh Shireen - Metode Pembayaran & E-Ticket
# ==========================================
import tkinter as tk
from tkinter import messagebox


HARGA_TIKET = 75000        # Harga tiket bioskop
PAJAK = 0.10               # Pajak hiburan 10%
BIAYA_LAYANAN = 5000       # Biaya layanan per transaksi


def hitung_total(jumlah_tiket):
    """Fungsi logika perhitungan harga milik Apriyanti.
    Menerima jumlah tiket, mengembalikan rincian pembayaran (dict)."""
    subtotal = HARGA_TIKET * jumlah_tiket
    total_pajak = subtotal * PAJAK
    total_bayar = subtotal + total_pajak + BIAYA_LAYANAN

    return {
        "harga_satuan": HARGA_TIKET,
        "jumlah": jumlah_tiket,
        "subtotal": subtotal,
        "pajak": total_pajak,
        "biaya_layanan": BIAYA_LAYANAN,
        "total_bayar": total_bayar,
    }


class PemesananTiketFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#1E1E24")

        tk.Label(
            self,
            text="Form Pemesanan",
            font=("Segoe UI", 11, "bold"),
            bg="#1E1E24",
            fg="#F5C518"
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            self,
            text="Jumlah Tiket:",
            font=("Segoe UI", 10, "bold"),
            bg="#1E1E24",
            fg="#FFFFFF"
        ).pack(anchor="w")

        self.entry_jumlah = tk.Entry(self, width=20, font=("Segoe UI", 11))
        self.entry_jumlah.pack(anchor="w", pady=(3, 15))

        tk.Label(
            self,
            text="Metode Pembayaran:",
            font=("Segoe UI", 10, "bold"),
            bg="#1E1E24",
            fg="#FFFFFF"
        ).pack(anchor="w")

        self.var_metode = tk.StringVar(value="QRIS")
        self.opsi_pembayaran = [
            "QRIS",
            "Transfer Bank (Virtual Account)",
            "E-Wallet (GoPay / OVO / DANA)"
        ]

        for opsi in self.opsi_pembayaran:
            tk.Radiobutton(
                self,
                text=opsi,
                variable=self.var_metode,
                value=opsi,
                font=("Segoe UI", 9),
                bg="#1E1E24",
                fg="#A0A0A0",
                selectcolor="#1E1E24",
                activebackground="#1E1E24"
            ).pack(anchor="w", pady=1)

        tk.Button(
            self,
            text="ðŸ’³ Bayar & Terbitkan E-Ticket",
            command=self.proses_pembayaran,
            bg="#28a745",
            fg="#FFFFFF",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            pady=6
        ).pack(fill="x", pady=(20, 0))

    def proses_pembayaran(self):
        try:
            jumlah_tiket = int(self.entry_jumlah.get())

            if jumlah_tiket <= 0:
                messagebox.showwarning(
                    "Peringatan Input",
                    "Jumlah tiket minimal harus 1!"
                )
                return

        except ValueError:
            messagebox.showerror(
                "Error Input",
                "Masukkan jumlah tiket menggunakan angka yang valid!"
            )
            return

        metode = self.var_metode.get()
        if not metode:
            messagebox.showwarning(
                "Peringatan",
                "Silakan pilih metode pembayaran terlebih dahulu!"
            )
            return

        rincian = hitung_total(jumlah_tiket)

        struk_eticket = (
            "====================================\n"
            "           E-TICKET DIGITAL         \n"
            "====================================\n"
            f"Harga Tiket       : Rp {rincian['harga_satuan']:,}\n"
            f"Jumlah Tiket      : {rincian['jumlah']} Tiket\n"
            f"Subtotal          : Rp {rincian['subtotal']:,}\n"
            f"Pajak 10%         : Rp {rincian['pajak']:,.0f}\n"
            f"Biaya Layanan     : Rp {rincian['biaya_layanan']:,}\n"
            f"------------------------------------\n"
            f"Metode Pembayaran : {metode}\n"
            f"TOTAL PEMBAYARAN  : Rp {rincian['total_bayar']:,.0f}\n"
            f"Status            : LUNAS\n"
            "====================================\n"
            "Terima kasih! Tunjukkan E-Ticket ini\n"
            "saat memasuki bioskop."
        )

        messagebox.showinfo("Penerbitan E-Ticket Berhasil", struk_eticket)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bioskop Yuk - Pemesanan Tiket")
    root.geometry("360x420")
    root.configure(bg="#121212")

    aplikasi = PemesananTiketFrame(root)
    aplikasi.pack(fill="both", expand=True, padx=15, pady=15)

    root.mainloop()
