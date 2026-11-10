import tkinter as tk
from tkinter import messagebox

class AplikasiBioskopIta:
    def __init__(self, root):
        self.root = root
        self.root.title("Bioskop Yuk")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffe4e1") # Tema soft pink sesuai preferensi

        # Variabel dan Tipe Data (Tugas Ita: Kerangka Utama & Variabel Dasar)
        self.nama_aplikasi = "BIOSKOP YUK"
        self.versi = 1.0

        # Header / Judul Utama
        self.label_judul = tk.Label(
            root, 
            text=f"🎟️ {self.nama_aplikasi} 🎟️", 
            font=("Arial", 18, "bold"), 
            bg="#ffe4e1", 
            fg="#d1477a"
        )
        self.label_judul.pack(pady=20)

        # Informasi Pemilik / Pembuat (Ita)
        self.label_info = tk.Label(
            root, 
            text="Modul Utama GUI & Kerangka Program oleh: Ita", 
            font=("Arial", 10, "italic"), 
            bg="#ffe4e1", 
            fg="#555555"
        )
        self.label_info.pack(pady=5)

        # Frame Utama untuk Konten GUI
        self.frame_utama = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
        self.frame_utama.pack(pady=15, fill="both", expand=True, padx=25)

        self.label_konten = tk.Label(
            self.frame_utama, 
            text="Area Tampilan Utama Aplikasi Bioskop\n(Kerangka GUI Tugas Ita)", 
            font=("Arial", 11), 
            bg="#ffffff", 
            fg="#333333"
        )
        self.label_konten.pack(expand=True)

        # Tombol Aksi / Interaksi GUI
        self.btn_info = tk.Button(
            root, 
            text="Tentang Aplikasi", 
            command=self.tampilkan_pesan, 
            bg="#ff69b4", 
            fg="white", 
            font=("Arial", 10, "bold"),
            width=15
        )
        self.btn_info.pack(pady=5)

        self.btn_keluar = tk.Button(
            root, 
            text="Keluar", 
            command=root.quit, 
            bg="#d1477a", 
            fg="white", 
            font=("Arial", 10, "bold"),
            width=15
        )
        self.btn_keluar.pack(pady=10)

    def tampilkan_pesan(self):
        messagebox.showinfo("Informasi", f"Selamat datang di {self.nama_aplikasi} v{self.versi}!\nKerangka GUI dirancang oleh Ita.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiBioskopIta(root)
    root.mainloop()
