import tkinter as tk
from tkinter import messagebox

from data_film import data_film

BG_UTAMA = "#121212"
BG_KARTU = "#1E1E2D"
WARNA_AKSEN = "#D4AF37"
WARNA_MERAH = "#540D10"
TEKS_UTAMA = "#FFFFFF"
TEKS_REDUP = "#A0A0A0"

KURSI_KOSONG = "#2F6B3F"
KURSI_DIPILIH = WARNA_AKSEN
KURSI_TERISI = "#3A3A42"


def buat_denah(terisi=()):
    """Buat denah 4x6 (list 2 dimensi / matriks), kursi di 'terisi' ditandai "X".
    Contoh: buat_denah(["A2", "B3"])"""
    baris = ["A", "B", "C", "D"]
    denah = []
    for i in range(4):
        isi_baris = []
        for j in range(6):
            kode = f"{baris[i]}{j + 1}"
            isi_baris.append("X" if kode in terisi else "O")
        denah.append(isi_baris)
    return denah

def buat_daftar_film():
    """Membangun daftar film dari data_film.py dan menambahkan denah kursi."""
    denah_terisi = {
        "Avengers: Endgame": ["A2", "B3", "C4"],
        "3726 mdpl": ["A1", "A2", "D5", "D6"],
        "The Conjuring": ["B2", "B3", "C3", "C4"],
        "Coco": ["A3", "B4"],
    }
    daftar = []
    for film in data_film:
        item = dict(film)
        item["jadwal"] = " | ".join(film["jadwal"])
        item["denah"] = buat_denah(denah_terisi.get(film["judul"], []))
        daftar.append(item)
    return daftar


class PemilihanFrame(tk.Frame):
    """Pemilihan film + denah kursi A1-D6.

    Isi matriks denah:  "O" = kosong,  "X" = sudah dibeli
    Setiap film punya denah sendiri di film["denah"].
    """

    BARIS = ["A", "B", "C", "D"]
    KOLOM = 6

    def __init__(self, parent, daftar_film, film_awal=None, on_konfirmasi=None):
        super().__init__(parent, bg=BG_UTAMA)

        self.daftar_film = daftar_film
        for f in self.daftar_film:
            f.setdefault("denah", buat_denah())

        self.on_konfirmasi = on_konfirmasi

        self.film = film_awal if film_awal is not None else daftar_film[0]
        self.var_film = tk.IntVar(value=self.daftar_film.index(self.film))

        self.terpilih = []     
        self.tombol = {}      

        self.buat_tampilan()

    def buat_tampilan(self):
        tk.Label(
            self, text="PILIH FILM & KURSI", font=("Helvetica", 15, "bold"),
            bg=BG_UTAMA, fg=WARNA_AKSEN
        ).pack(pady=(12, 4))

        tk.Label(
            self, text="1. Pilih Film", font=("Helvetica", 9, "bold"),
            bg=BG_UTAMA, fg=TEKS_REDUP
        ).pack(anchor="w", padx=20)

        frame_film = tk.Frame(self, bg=BG_UTAMA)
        frame_film.pack(padx=20, pady=4, anchor="w")

        for idx in range(len(self.daftar_film)):
            tk.Radiobutton(
                frame_film,
                text=self.daftar_film[idx]["judul"],
                variable=self.var_film, value=idx,
                command=self.ganti_film,
                indicatoron=0,                     
                font=("Helvetica", 9, "bold"),
                bg=BG_KARTU, fg=TEKS_UTAMA,
                selectcolor=WARNA_AKSEN,
                activebackground=WARNA_AKSEN, activeforeground=TEKS_UTAMA,
                relief="flat", padx=10, pady=5, cursor="hand2"
            ).grid(row=idx // 4, column=idx % 4, padx=3, pady=3)

        kartu = tk.Frame(self, bg=BG_KARTU, padx=12, pady=8)
        kartu.pack(fill="x", padx=20, pady=(4, 0))

        self.lbl_judul = tk.Label(
            kartu, font=("Helvetica", 11, "bold"), bg=BG_KARTU, fg=TEKS_UTAMA,
            anchor="w", justify="left"
        )
        self.lbl_judul.pack(fill="x")

        self.lbl_meta = tk.Label(
            kartu, font=("Helvetica", 9), bg=BG_KARTU, fg=TEKS_REDUP,
            anchor="w", justify="left"
        )
        self.lbl_meta.pack(fill="x")

        self.lbl_jadwal = tk.Label(
            kartu, font=("Helvetica", 9, "bold"), bg=BG_KARTU, fg=WARNA_AKSEN,
            anchor="w", justify="left"
        )
        self.lbl_jadwal.pack(fill="x", pady=(2, 0))

        self.lbl_sinopsis = tk.Label(
            kartu, font=("Helvetica", 9), bg=BG_KARTU, fg=TEKS_UTAMA,
            anchor="w", justify="left", wraplength=540
        )
        self.lbl_sinopsis.pack(fill="x", pady=(2, 0))

        tk.Label(
            self, text="2. Pilih Kursi", font=("Helvetica", 9, "bold"),
            bg=BG_UTAMA, fg=TEKS_REDUP
        ).pack(anchor="w", padx=20, pady=(10, 0))

        tk.Label(
            self, text="LAYAR", font=("Helvetica", 9, "bold"),
            bg=BG_KARTU, fg=TEKS_REDUP, width=44
        ).pack(pady=8)

        grid = tk.Frame(self, bg=BG_UTAMA)
        grid.pack(pady=4)

        for i in range(len(self.BARIS)):
            tk.Label(
                grid, text=self.BARIS[i], font=("Helvetica", 10, "bold"),
                bg=BG_UTAMA, fg=TEKS_UTAMA
            ).grid(row=i, column=0, padx=8)

            for j in range(self.KOLOM):
                kode = f"{self.BARIS[i]}{j + 1}"      
                btn = tk.Button(
                    grid, width=5, height=1,
                    font=("Helvetica", 9, "bold"), relief="flat", cursor="hand2",
                    command=lambda k=kode, r=i, c=j: self.klik_kursi(k, r, c)
                )
                btn.grid(row=i, column=j + 1, padx=4, pady=3)
                self.tombol[kode] = btn

        legenda = tk.Frame(self, bg=BG_UTAMA)
        legenda.pack(pady=6)
        for teks, warna in [("Kosong", KURSI_KOSONG), ("Dipilih", KURSI_DIPILIH),
                            ("Terisi (X)", KURSI_TERISI)]:
            tk.Label(legenda, text="   ", bg=warna).pack(side="left", padx=(10, 3))
            tk.Label(legenda, text=teks, bg=BG_UTAMA, fg=TEKS_REDUP,
                     font=("Helvetica", 9)).pack(side="left")

        self.lbl_info = tk.Label(
            self, text="Kursi dipilih: -", font=("Helvetica", 10),
            bg=BG_UTAMA, fg=TEKS_UTAMA
        )
        self.lbl_info.pack(pady=4)

        aksi = tk.Frame(self, bg=BG_UTAMA)
        aksi.pack(pady=6)

        tk.Button(
            aksi, text="Reset Pilihan", command=self.reset_pilihan,
            bg=WARNA_MERAH, fg=TEKS_UTAMA, font=("Helvetica", 10, "bold"),
            relief="flat", padx=12, pady=6, cursor="hand2"
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            aksi, text="Konfirmasi Kursi", command=self.konfirmasi,
            bg=WARNA_AKSEN, fg=TEKS_UTAMA, font=("Helvetica", 10, "bold"),
            relief="flat", padx=12, pady=6, cursor="hand2"
        ).grid(row=0, column=1, padx=8)

        self.update_info_film()
        self.refresh_tampilan()

    def ganti_film(self):
        """Dipanggil saat radio film diklik: pindah ke denah milik film itu."""
        self.film = self.daftar_film[self.var_film.get()]
        self.terpilih = []              
        self.update_info_film()
        self.refresh_tampilan()
        self.update_info()

    def update_info_film(self):
        f = self.film
        self.lbl_judul.config(text=f["judul"])
        self.lbl_meta.config(
            text=f"{f['genre'].strip()}  |  {f['durasi']}  |  {f['studio']}"
        )
        self.lbl_jadwal.config(text=f"Jadwal: {f['jadwal']}")
        self.lbl_sinopsis.config(text=f"Sinopsis: {f['sinopsis']}")

    def refresh_tampilan(self):
        """Gambar ulang semua kursi sesuai denah film terpilih (perulangan bersarang)."""
        denah = self.film["denah"]
        for i in range(len(denah)):
            for j in range(len(denah[i])):
                kode = f"{self.BARIS[i]}{j + 1}"
                btn = self.tombol[kode]

                if denah[i][j] == "X":
                    btn.config(text="X", bg=KURSI_TERISI, fg=TEKS_REDUP,
                               activebackground=KURSI_TERISI)
                elif kode in self.terpilih:
                    btn.config(text=kode, bg=KURSI_DIPILIH, fg=TEKS_UTAMA,
                               activebackground=KURSI_DIPILIH)
                else:
                    btn.config(text=kode, bg=KURSI_KOSONG, fg=TEKS_UTAMA,
                               activebackground=KURSI_KOSONG)

    def klik_kursi(self, kode, baris, kolom):
        if self.film["denah"][baris][kolom] == "X":
            messagebox.showwarning(
                "Kursi Tidak Tersedia",
                f"Kursi {kode} sudah dibeli.\nSilakan pilih kursi lain."
            )
            return

        if kode in self.terpilih:
            self.terpilih.remove(kode)      
        else:
            self.terpilih.append(kode)

        self.terpilih.sort()
        self.refresh_tampilan()
        self.update_info()

    def update_info(self):
        if self.terpilih:
            self.lbl_info.config(text="Kursi dipilih: " + ", ".join(self.terpilih))
        else:
            self.lbl_info.config(text="Kursi dipilih: -")

    def reset_pilihan(self):
        self.terpilih = []
        self.refresh_tampilan()
        self.update_info()

    def konfirmasi(self):
        if len(self.terpilih) == 0:
            messagebox.showwarning("Peringatan", "Pilih minimal 1 kursi dulu ya!")
            return

        for kode in self.terpilih:
            i = self.BARIS.index(kode[0])
            j = int(kode[1:]) - 1
            self.film["denah"][i][j] = "X"

        hasil = list(self.terpilih)
        film = self.film
        self.terpilih = []
        self.refresh_tampilan()
        self.update_info()

        if self.on_konfirmasi:
            self.on_konfirmasi(film, hasil)    
        else:
            messagebox.showinfo(
                "Pilihan Anda",
                f"Film: {film['judul']}\nKursi: {', '.join(hasil)}"
            )

    def get_pilihan(self):
        return self.film, list(self.terpilih)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("BIOSKOP YUK - Pemilihan Film & Kursi")
    root.geometry("620x680")
    root.configure(bg=BG_UTAMA)

    PemilihanFrame(root, buat_daftar_film()).pack(fill="both", expand=True)

    root.mainloop()
