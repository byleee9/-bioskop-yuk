import tkinter as tk
from tkinter import messagebox

class KatalogFilmFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#FEF9FA")

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
                "studio": "Studio 4",
            }
        ]

        self.buat_tampilan()

    def buat_tampilan(self):


        tk.Label(
            self,
            text="Film Yang Sedang Tayang",
            font=("Segoe UI", 17, "bold"),
            bg="#323334",
            fg="white"
        ).pack(anchor="w", padx=20, pady=15)

        wrapper = tk.Frame(self, bg="#282727")
        wrapper.pack(fill="both", expand=True, padx=15)

        canvas = tk.Canvas(wrapper, bg="#282727", highlightthickness=0)
        scrollbar = tk.Scrollbar(wrapper, orient="vertical", command=canvas.yview)
        daftar = tk.Frame(canvas, bg="#282727")

        daftar.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        jendela_daftar = canvas.create_window((0, 0), window=daftar, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(jendela_daftar, width=e.width))

        def scroll_roda(event):
            canvas.yview_scroll(1 if event.delta < 0 else -1, "units")

        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", scroll_roda))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for film in self.film:

            card = tk.Frame(
                daftar,
                bg="#B1B2B5",
                padx=12,
                pady=10
            )
            card.pack(fill="x", pady=6)

            tk.Label(
                card,
                text="ðŸŽ¬",
                font=("Segoe UI", 25),
                bg="#2B2C2D",
                fg="white"
            ).pack(side="left", padx=12)

            info = tk.Frame(card, bg="#243249")
            info.pack(side="left", fill="x", expand=True)

            tk.Label(
                info,
                text=film["judul"],
                font=("Segoe UI", 12, "bold"),
                bg="#3B3C3C",
                fg="white"
            ).pack(anchor="w")

            tk.Label(
                info,
                text=f'{film["genre"]} | {film["durasi"]}',
                font=("Segoe UI", 9),
                bg="#303031",
                fg="#B8C7DC"
            ).pack(anchor="w")

            tk.Label(
                info,
                text=f'Jadwal: {film["jadwal"]}',
                font=("Segoe UI", 9),
                bg="#243249",
                fg="#F5B942"
            ).pack(anchor="w")

            tk.Button(
                card,
                text="Detail",
                bg="#F5B942",
                fg="#17243A",
                font=("Segoe UI", 9, "bold"),
                relief="flat",
                cursor="hand2",
                command=lambda f=film: self.detail_film(f)
            ).pack(side="right", padx=8)

        tk.Label(
            self,
            text="Â© 2026 BIOSKOP YUK | Katalog Film",
            font=("Segoe UI", 9),
            bg="#101827",
            fg="#8795A8"
        ).pack(pady=12)

    def detail_film(self, film):

        messagebox.showinfo(
            film["judul"],
            f'Judul: {film["judul"]}\n'
            f'Genre: {film["genre"]}\n'
            f'Durasi: {film["durasi"]}\n\n'
            f'Sinopsis:\n{film["sinopsis"]}\n\n'
            f'Jadwal: {film["jadwal"]}\n'
            f'Studio: {film["studio"]}'
        )


if __name__ == "__main__":

    root = tk.Tk()
    root.title("BIOSKOP YUK - Katalog Film")
    root.geometry("800x650")

    aplikasi = KatalogFilmFrame(root)
    aplikasi.pack(fill="both", expand=True)

    root.mainloop()
