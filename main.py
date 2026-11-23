import tkinter as tk
from tkinter import ttk, messagebox

from katalog_film import KatalogFilmFrame
from pemilihan import PemilihanFrame, buat_daftar_film
from pemesanan_tiket import PemesananTiketFrame

BG_UTAMA = "#121212"
BG_KARTU = "#1E1E2D"
WARNA_AKSEN = "#D4AF37"
WARNA_HEADER = "#1E1D1D"
TEKS_UTAMA = "#FFFFFF"
TEKS_REDUP = "#A0A0A0"

root = tk.Tk()
root.title("Bioskop Yuk! - Sistem Pemesanan Tiket Bioskop")
root.geometry("980x720")
root.configure(bg=BG_UTAMA)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "TNotebook",
    background=BG_UTAMA,
    borderwidth=0
)
style.configure(
    "TNotebook.Tab",
    background=BG_KARTU,
    foreground=TEKS_REDUP,
    padding=(16, 8),
    font=("Segoe UI", 10, "bold")
)
style.map(
    "TNotebook.Tab",
    background=[("selected", WARNA_AKSEN)],
    foreground=[("selected", "#17243A")]
)

frame_header = tk.Frame(root, bg=WARNA_HEADER, pady=15)
frame_header.pack(fill="x")

label_judul = tk.Label(
    frame_header,
    text="🎬 BIOSKOP YUK!",
    font=("Segoe UI", 20, "bold"),
    bg=WARNA_HEADER,
    fg=WARNA_AKSEN
)
label_judul.pack()

label_subjudul = tk.Label(
    frame_header,
    text="Nikmati Pengalaman Menonton Terbaik",
    font=("Segoe UI", 10, "italic"),
    bg=WARNA_HEADER,
    fg=TEKS_REDUP
)
label_subjudul.pack()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=15)

tab_katalog = tk.Frame(notebook, bg=BG_UTAMA)
tab_pemilihan = tk.Frame(notebook, bg=BG_UTAMA)
tab_pemesanan = tk.Frame(notebook, bg=BG_UTAMA)

notebook.add(tab_katalog, text="1. Katalog Film")
notebook.add(tab_pemilihan, text="2. Pilih Film & Kursi")
notebook.add(tab_pemesanan, text="3. Pemesanan Tiket")

katalog_film = KatalogFilmFrame(tab_katalog)
katalog_film.pack(fill="both", expand=True)

pemesanan_tiket = PemesananTiketFrame(tab_pemesanan)
pemesanan_tiket.pack(fill="both", expand=True, padx=15, pady=15)


def saat_kursi_dikonfirmasi(film, kursi):
    pemesanan_tiket.set_pilihan(film, kursi)
    notebook.select(tab_pemesanan)
    messagebox.showinfo(
        "Pilihan Disimpan",
        f'Film: {film["judul"]}\n'
        f'Kursi: {", ".join(kursi)}\n\n'
        "Silakan lanjutkan ke halaman Pemesanan Tiket."
    )


pemilihan_film = PemilihanFrame(
    tab_pemilihan,
    buat_daftar_film(),
    on_konfirmasi=saat_kursi_dikonfirmasi
)
pemilihan_film.pack(fill="both", expand=True)

frame_footer = tk.Frame(root, bg=BG_KARTU, pady=8)
frame_footer.pack(fill="x", side="bottom")

label_footer = tk.Label(
    frame_footer,
    text="© 2026 Bioskop Yuk!",
    font=("Segoe UI", 9),
    bg=BG_KARTU,
    fg=TEKS_REDUP
)
label_footer.pack()

root.mainloop()
