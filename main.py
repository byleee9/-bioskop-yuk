import tkinter as tk
from katalog_film import KatalogFilmFrame
from pemesanan_tiket import PemesananTiketFrame

BG_UTAMA = "#121212"
BG_KARTU = "#1E1E2D"
WARNA_AKSEN = "#D4AF37"
WARNA_HEADER = "#1E1D1D"
TEKS_UTAMA = "#FFFFFF"
TEKS_REDUP = "#A0A0A0"

root = tk.Tk()
root.title("Bioskop Yuk! - Sistem Pemesanan Tiket Bioskop")
root.geometry("900x620")
root.configure(bg=BG_UTAMA)

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

frame_konten = tk.Frame(root, bg=BG_UTAMA, padx=15, pady=15)
frame_konten.pack(fill="both", expand=True)

frame_kiri = tk.Frame(frame_konten, bg=BG_KARTU, padx=5, pady=5, bd=1, relief="ridge")
frame_kiri.pack(side="left", fill="both", expand=True, padx=(0, 5))

label_section_film = tk.Label(
    frame_kiri,
    text="DAFTAR FILM & JADWAL",
    font=("Segoe UI", 11, "bold"),
    bg=BG_KARTU,
    fg=WARNA_AKSEN
)
label_section_film.pack(anchor="w", pady=(0, 5))

katalog_film = KatalogFilmFrame(frame_kiri)
katalog_film.pack(fill="both", expand=True)

frame_kanan = tk.Frame(frame_konten, bg=BG_KARTU, padx=10, pady=10, bd=1, relief="ridge")
frame_kanan.pack(side="right", fill="both", expand=True, padx=(5, 0))

label_section_pesan = tk.Label(
    frame_kanan,
    text="PEMESANAN TIKET",
    font=("Segoe UI", 11, "bold"),
    bg=BG_KARTU,
    fg=WARNA_AKSEN
)
label_section_pesan.pack(anchor="w", pady=(0, 5))

pemesanan_tiket = PemesananTiketFrame(frame_kanan)
pemesanan_tiket.pack(fill="both", expand=True)

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
