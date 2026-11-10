import tkinter as tk
from tkinter import messagebox

class AplikasiBioskopIta:
    def __init__(self, root):
        self.root = root
        self.root.title("Bioskop Yuk - Sistem Pemesanan Tiket")
        self.root.geometry("700x550")
        self.root.configure(bg="#FFF0F5") # LavenderBlush / Soft Pastel Pink

        # Variabel dan Tipe Data
        self.nama_aplikasi = "BIOSKOP YUK"
        self.versi = "1.0"
        self.pembuat = "Ita"

        # Header Banner Frame
        header_frame = tk.Frame(root, bg="#FFB6C1", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)

        lbl_judul = tk.Label(
            header_frame, 
            text=f"🎬  {self.nama_aplikasi}  🎬", 
            font=("Segoe UI", 20, "bold"), 
            bg="#FFB6C1", 
            fg="#FFFFFF"
        )
        lbl_judul.pack(expand=True)

        # Sub-header / Info Pembuat
        sub_frame = tk.Frame(root, bg="#FFF0F5")
        sub_frame.pack(fill="x", padx=20, pady=10)

        lbl_info = tk.Label(
            sub_frame, 
            text=f"Modul Utama GUI & Kerangka Program | Dibuat oleh: {self.pembuat}", 
            font=("Segoe UI", 10, "italic"), 
            bg="#FFF0F5", 
            fg="#8B4513"
        )
        lbl_info.pack(anchor="w")

        # Container Card Utama (White Card with Rounded effect simulation)
        card_frame = tk.Frame(root, bg="#FFFFFF", bd=1, relief="solid")
        card_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Konten di dalam Card
        lbl_card_title = tk.Label(
            card_frame, 
            text="✨ Selamat Datang di Panel Utama Bioskop Yuk ✨", 
            font=("Segoe UI", 14, "bold"), 
            bg="#FFFFFF", 
            fg="#C71585"
        )
        lbl_card_title.pack(pady=20)

        lbl_deskripsi = tk.Label(
            card_frame, 
            text="Ini adalah kerangka utama tampilan grafis (GUI) aplikasi.\nDirancang bersih, elegan, dan siap dikembangkan lebih lanjut.", 
            font=("Segoe UI", 11), 
            bg="#FFFFFF", 
            fg="#555555",
            justify="center"
        )
        lbl_deskripsi.pack(pady=10)

        # Frame Tombol Aksi
        btn_frame = tk.Frame(card_frame, bg="#FFFFFF")
        btn_frame.pack(pady=25)

        btn_info = tk.Button(
            btn_frame, 
            text="ℹ️ Info Aplikasi", 
            command=self.tampilkan_pesan, 
            bg="#FF69B4", 
            fg="#FFFFFF", 
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_info.grid(row=0, column=0, padx=10)

        btn_keluar = tk.Button(
            btn_frame, 
            text="❌ Keluar", 
            command=root.quit, 
            bg="#DB7093", 
            fg="#FFFFFF", 
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_keluar.grid(row=0, column=1, padx=10)

        # Footer
        footer_frame = tk.Frame(root, bg="#FFC0CB", height=30)
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)

        lbl_footer = tk.Label(
            footer_frame, 
            text=f"© 2026 - {self.nama_aplikasi} v{self.versi}", 
            font=("Segoe UI", 8), 
            bg="#FFC0CB", 
            fg="#FFFFFF"
        )
        lbl_footer.pack(expand=True)

    def tampilkan_pesan(self):
        messagebox.showinfo("Informasi Aplikasi", f"Aplikasi {self.nama_aplikasi} v{self.versi}\nModul Kerangka GUI Utama oleh {self.pembuat}.\nSemua komponen siap digunakan!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiBioskopIta(root)
    root.mainloop()
