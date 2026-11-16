import tkinter as tk
from tkinter import messagebox

class PemilihanFilmFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#282727")

        self.film = [
            {
                "judul": "Avengers: Endgame",
                "genre": " Action / Adventure",
                "durasi": "181 Menit",
                "sinopsis": "para Avengers berjuang menyelamatkan alam semesta.",
                "jadwal": "10:00 | 13:00 | 16:00",
                "studio": "Studio 1"
            },
            {
                "judul": "3726 mdpl",
                "genre": "Romance / drama",
                "durasi": "200 Menit",
                "sinopsis": "kisah cinta Rangga Raja(Abun Sungkar), mahasiswa kehutanan yang hobi mendaki gunung dengan adik tingkatnya yang berprestasi Andini Hangura(Callista Arum).",
                "jadwal": "11:00 | 14:00 | 19:00",
                "studio": "Studio 2"
            },
            {
                "judul": "The Conjuring",
                "genre": "Horor / mystery",
                "durasi": "112 menit",
                "sinopsis": "Kisah penyelidikan kejadian misterius.",
                "jadwal": "12:00 | 15:00 | 20:00",
                "studio": "Studio 3"
            },
            {
                "judul": "Coco",
                "genre": "Animation / Family",
                "durasi": "105 menit",
                "sinopsis": "pertualangan seorang anak dalam dunia musik.",
                "jadwal": "09:00 | 12:00 | 17:00",
                "studio": "Studio 4"
            }
        ]

        self.film_terpilih = None

        self.buat_tampilan()

    def buat_tampilan(self):

        header = tk.Frame(self, bg="#1E1D1D")
        header.pack(fill="x")

        tk.Label(
            header,
            text="BIOSKOP YUK",
            font=("Segoe UI", 23, "bold"),
            bg="#1E1D1D",
            fg="white"
        ).pack(pady=(15, 3))

        tk.Label(
            header,
            text="PEMILIHAN FILM & VALIDASI PILIHAN",
            font=("Segoe UI", 11),
            bg="#1E1D1D",
            fg="#F5B942"
        ).pack(pady=(0, 15))

        tk.Label(
            self,
            text="Silakan Pilih Film",
            font=("Segoe UI", 17, "bold"),
            bg="#282727",
            fg="white"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        tk.Label(
            self,
            text="Klik salah satu film pada daftar, lalu tekan tombol Pilih Film.",
            font=("Segoe UI", 10),
            bg="#282727",
            fg="#B8C7DC"
        ).pack(anchor="w", padx=20, pady=(0, 10))

        area = tk.Frame(self, bg="#282727")
        area.pack(fill="both", expand=True, padx=15)

        kiri = tk.Frame(area, bg="#B1B2B5", padx=12, pady=10)
        kiri.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(
            kiri,
            text="Daftar Film",
            font=("Segoe UI", 12, "bold"),
            bg="#B1B2B5",
            fg="#17243A"
        ).pack(anchor="w", pady=(0, 6))

        self.listbox = tk.Listbox(
            kiri,
            font=("Segoe UI", 11),
            width=24,
            height=8,
            bg="#303031",
            fg="white",
            selectbackground="#F5B942",
            selectforeground="#17243A",
            selectmode=tk.SINGLE,
            exportselection=False,
            activestyle="none",
            relief="flat"
        )
        self.listbox.pack()

        for f in self.film:
            self.listbox.insert(tk.END, f["judul"])

        self.listbox.bind("<<ListboxSelect>>", self.tampilkan_detail)

        kanan = tk.Frame(area, bg="#243249", padx=12, pady=10)
        kanan.pack(side="left", fill="both", expand=True)

        tk.Label(
            kanan,
            text="Detail Film",
            font=("Segoe UI", 12, "bold"),
            bg="#243249",
            fg="#F5B942"
        ).pack(anchor="w", pady=(0, 6))

        self.lbl_detail = tk.Label(
            kanan,
            text="Belum ada film yang dipilih.",
            font=("Segoe UI", 10),
            bg="#243249",
            fg="#B8C7DC",
            justify="left",
            anchor="nw",
            wraplength=380
        )
        self.lbl_detail.pack(fill="both", expand=True)

        tombol = tk.Frame(self, bg="#282727")
        tombol.pack(pady=15)

        tk.Button(
            tombol,
            text="Pilih Film",
            bg="#F5B942",
            fg="#17243A",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            command=self.pilih_film
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            tombol,
            text="Reset",
            bg="#B1B2B5",
            fg="#17243A",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            command=self.reset_pilihan
        ).grid(row=0, column=1, padx=8)

        self.lbl_status = tk.Label(
            self,
            text="Status: belum ada film yang dipilih",
            font=("Segoe UI", 10, "bold"),
            bg="#282727",
            fg="#F5B942"
        )
        self.lbl_status.pack()

        tk.Label(
            self,
            text="© 2026 BIOSKOP YUK | Pemilihan Film",
            font=("Segoe UI", 9),
            bg="#282727",
            fg="#8795A8"
        ).pack(pady=12)

    def ambil_indeks(self):

        pilihan = self.listbox.curselection()

        if len(pilihan) == 0:
            return None
        else:
            return pilihan[0]

    def tampilkan_detail(self, event=None):

        indeks = self.ambil_indeks()

        if indeks is None:
            self.lbl_detail.config(text="Belum ada film yang dipilih.")
        else:
            film = self.film[indeks]
            self.lbl_detail.config(
                text=f'Judul: {film["judul"]}\n'
                     f'Genre: {film["genre"]}\n'
                     f'Durasi: {film["durasi"]}\n'
                     f'Jadwal: {film["jadwal"]}\n'
                     f'Studio: {film["studio"]}\n\n'
                     f'Sinopsis:\n{film["sinopsis"]}'
            )

    def pilih_film(self):

        indeks = self.ambil_indeks()

        if indeks is None:
            messagebox.showwarning(
                "Peringatan",
                "Anda belum memilih film!\nSilakan pilih minimal 1 film."
            )
        else:
            film = self.film[indeks]

            lanjut = messagebox.askyesno(
                "Konfirmasi Pilihan",
                f'Anda memilih film:\n\n'
                f'Judul: {film["judul"]}\n'
                f'Jadwal: {film["jadwal"]}\n'
                f'Studio: {film["studio"]}\n\n'
                f'Lanjutkan?'
            )

            if lanjut:
                self.film_terpilih = film
                self.lbl_status.config(
                    text=f'Status: film terpilih - {film["judul"]}'
                )
                messagebox.showinfo(
                    "Berhasil",
                    f'Film "{film["judul"]}" berhasil dipilih!'
                )
            else:
                self.lbl_status.config(text="Status: pemilihan dibatalkan")

    def reset_pilihan(self):

        self.listbox.selection_clear(0, tk.END)
        self.film_terpilih = None
        self.lbl_detail.config(text="Belum ada film yang dipilih.")
        self.lbl_status.config(text="Status: belum ada film yang dipilih")


if __name__ == "__main__":

    root = tk.Tk()
    root.title("BIOSKOP YUK - Pemilihan Film")
    root.geometry("800x650")

    aplikasi = PemilihanFilmFrame(root)
    aplikasi.pack(fill="both", expand=True)

    root.mainloop()
