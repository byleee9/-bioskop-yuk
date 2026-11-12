import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Cinema 21 - m.tix XXI Mobile",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling persis m.21cineplex.com dengan Tema Pastel Soft Pink & Blue
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Poppins:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Quicksand', 'Poppins', sans-serif;
    }
    .main {
        background: radial-gradient(circle at top, #1A1F36 0%, #0F1221 100%);
        color: #F8FAFC;
    }
    .mobile-header {
        background: linear-gradient(135deg, #242B48 0%, #1C223B 100%);
        border-bottom: 2px solid #FFB6C1;
        padding: 14px 18px;
        position: sticky;
        top: 0;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 14px;
        box-shadow: 0 6px 20px rgba(255, 182, 193, 0.2);
        margin-bottom: 15px;
    }
    .xxi-logo {
        font-size: 22px;
        font-weight: 800;
        letter-spacing: 2px;
        background: linear-gradient(135deg, #FFB6C1 0%, #BEE3F8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .xxi-badge {
        background: linear-gradient(135deg, #FF80BF 0%, #BEE3F8 100%);
        color: #1A202C;
        padding: 4px 10px;
        border-radius: 14px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .movie-box {
        background: #181E34;
        border: 1.5px solid #FFB6C1;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    }
    .tag-age {
        background: #2D3748;
        color: #BEE3F8;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: bold;
        border: 1px solid #4A5568;
    }
    .tag-format {
        background: #4A1D36;
        color: #FFB6C1;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: bold;
        border: 1px solid #FF80BF;
    }
    .screen-cinema {
        background: linear-gradient(180deg, #FFB6C1 0%, rgba(190, 227, 248, 0.1) 100%);
        height: 20px;
        border-radius: 50% / 100% 100% 0 0;
        text-align: center;
        font-size: 10px;
        color: #1A202C;
        font-weight: 800;
        letter-spacing: 5px;
        margin-bottom: 22px;
        box-shadow: 0 0 15px rgba(255, 182, 193, 0.5);
    }
    .stButton>button {
        background: linear-gradient(135deg, #FF99C8 0%, #BEE3F8 100%) !important;
        color: #1A202C !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: 1px solid #FFB6C1 !important;
        box-shadow: 0 4px 14px rgba(255, 153, 200, 0.35) !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #FF80BF 0%, #90CDF4 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(255, 128, 191, 0.5) !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #FFB6C1 !important;
        border-radius: 14px !important;
        background: #181E34 !important;
        box-shadow: 0 4px 20px rgba(255, 182, 193, 0.15) !important;
    }
</style>
""", unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = "pilih_film"
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
if "selected_cinema" not in st.session_state:
    st.session_state.selected_cinema = "Ayani XXI Pontianak"
if "selected_date" not in st.session_state:
    st.session_state.selected_date = "Hari ini, 10 Nov 2026"
if "selected_time" not in st.session_state:
    st.session_state.selected_time = "14:15"
if "selected_seats" not in st.session_state:
    st.session_state.selected_seats = []
if "selected_fb" not in st.session_state:
    st.session_state.selected_fb = {}
if "last_booking" not in st.session_state:
    st.session_state.last_booking = None

MOVIES = [
    {
        "id": "PS3",
        "title": "PENGABDI SETAN 3",
        "format": "2D & IMAX",
        "age": "D17+",
        "duration": "118 Menit",
        "genre": "Horror, Mystery",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=400&q=80",
        "synopsis": "Keluarga Rini menemukan rahasia kelam di balik sekte misterius yang kembali bangkit menuntut tumbal."
    },
    {
        "id": "AV3",
        "title": "AVATAR 3: FIRE AND ASH",
        "format": "3D & DOLBY ATMOS",
        "age": "R13+",
        "duration": "192 Menit",
        "genre": "Action, Sci-Fi, Adventure",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=400&q=80",
        "synopsis": "Perjalanan keluarga Jake Sully menghadapi bangsa api Na'vi yang bringas di wilayah terlarang Pandora."
    },
    {
        "id": "AL2",
        "title": "AGAK LAEN 2",
        "format": "2D REGULAR",
        "age": "SU 13+",
        "duration": "115 Menit",
        "genre": "Comedy, Drama",
        "price": 40000,
        "image": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=400&q=80",
        "synopsis": "Empat sekawan penjaga pasar malam terseret dalam investigasi komedi kocak penuh tawa."
    },
    {
        "id": "AVS",
        "title": "AVENGERS: SECRET WARS",
        "format": "IMAX WITH LASER",
        "age": "R13+",
        "duration": "180 Menit",
        "genre": "Action, Superhero, Sci-Fi",
        "price": 55000,
        "image": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=400&q=80",
        "synopsis": "Pertempuran penutup multiverse MCU dengan kolaborasi superhero lintas dimensi paling akbar."
    }
]

FB_MENU = [
    {"name": "Popcorn Caramel XXI (M)", "price": 35000, "desc": "Jagung renyah karamel khas Cinema 21"},
    {"name": "Coca-Cola Cup Dingin (M)", "price": 20000, "desc": "Minuman soda dingin segar"},
    {"name": "Combo Hemat XXI", "price": 50000, "desc": "1 Popcorn Caramel + 2 Minuman Soda"},
    {"name": "French Fries Bolognese", "price": 38000, "desc": "Kentang goreng renyah saus bolognese premium"}
]

st.markdown("""
<div class="mobile-header">
    <div class="xxi-logo">CINEMA 21 𐙚 𐙚 𐙚 𐙚 𐙚 𐙚 𐙚</div>
    <div><span class="xxi-badge">m.tix Official</span></div>
</div>
""", unsafe_allow_html=True)

if st.session_state.step == "pilih_film":
    st.markdown("<p style='color:#A0AEC0; font-size:12px; margin-top:10px;'>📍 Bioskop: <b>Ayani XXI Pontianak</b></p>", unsafe_allow_html=True)
    tab_now, tab_soon, tab_check = st.tabs(["🎬 Sedang Tayang", "⏳ Segera Hadir", "🔍 Cek Tiket"])
    
    with tab_now:
        for m in MOVIES:
            col_img, col_txt = st.columns([1, 2])
            with col_img:
                st.image(m["image"], use_container_width=True)
            with col_txt:
                st.markdown(f"### {m['title']}")
                st.markdown(f"<span class='tag-age'>{m['age']}</span> <span class='tag-format'>{m['format']}</span> • {m['duration']}", unsafe_allow_html=True)
                st.caption(m["genre"])
                st.write(m["synopsis"])
                st.markdown(f"<b style='color:#FFB6C1; font-size:16px;'>Rp {m['price']:,}</b>", unsafe_allow_html=True)
                
                if st.button(f"🎟️ Beli Tiket • {m['title']}", key=f"btn_buy_{m['id']}"):
                    st.session_state.selected_movie = m
                    st.session_state.step = "pilih_jadwal"
                    st.rerun()
            st.markdown("<hr style='border-color:#202533; margin:15px 0;'>", unsafe_allow_html=True)
            
    with tab_soon:
        st.info("🔜 **Spider-Man: Beyond the Spider-Verse** • Rilis Akhir Tahun")
        st.info("🔜 **The Conjuring: Last Rites** • Segera di Layar Lebar XXI")
        
    with tab_check:
        st.markdown("#### Masukkan Kode Booking:")
        code_input = st.text_input("Kode Booking (contoh: MTX-XXXXXX):")
        if st.button("Cari Tiket"):
            if st.session_state.last_booking and st.session_state.last_booking["code"] == code_input.strip():
                st.session_state.step = "tiket_selesai"
                st.rerun()
            else:
                st.error("Tiket tidak ditemukan.")

elif st.session_state.step == "pilih_jadwal":
    m = st.session_state.selected_movie
    st.markdown(f"### 🎬 {m['title']}")
    st.caption(f"{m['age']} • {m['genre']} • {m['duration']}")
    st.markdown("---")
    st.markdown("#### 1. Pilih Bioskop & Hari")
    st.session_state.selected_cinema = st.selectbox("Lokasi XXI:", ["Ayani XXI Pontianak", "Mega Mall XXI", "Kubu Raya Premiere XXI"])
    st.session_state.selected_date = st.radio("Pilih Tanggal:", ["Hari Ini, 10 Nov", "Besok, 11 Nov", "Lusa, 12 Nov"], horizontal=True)
    
    st.markdown("#### 2. Jam Tayang Studio")
    times = ["12:15", "14:45", "17:15", "19:45", "21:30"]
    st.session_state.selected_time = st.radio("Waktu Tayang Reguler:", times, horizontal=True)
    
    st.markdown("---")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("⬅️ Kembali ke Film"):
            st.session_state.step = "pilih_film"
            st.rerun()
    with col_b2:
        if st.button("Pilih Kursi Studio ➡️"):
            st.session_state.step = "pilih_kursi"
            st.rerun()

elif st.session_state.step == "pilih_kursi":
    m = st.session_state.selected_movie
    st.markdown(f"### 🪑 Pilih Kursi • {m['title']}")
    st.caption(f"{st.session_state.selected_cinema} • {st.session_state.selected_time} WIB")
    st.markdown("<div class='screen-cinema'>LAYAR BIOSKOP</div>", unsafe_allow_html=True)
    
    rows = ["A", "B", "C", "D"]
    all_seats = [f"{r}{c}" for r in rows for c in range(1, 7)]
    
    picked = st.multiselect("Pilih Nomor Kursi:", all_seats, default=st.session_state.selected_seats)
    st.session_state.selected_seats = picked
    
    num_seats = len(picked)
    ticket_cost = num_seats * m["price"]
    
    st.markdown(f"""
    <div class='movie-box'>
        <b>Kursi Terpilih:</b> {', '.join(picked) if picked else 'Belum ada'}<br>
        <b>Jumlah Tiket:</b> {num_seats} Orang<br>
        <b>Subtotal:</b> <span style='color:#00FF7F; font-weight:bold;'>Rp {ticket_cost:,}</span>
    </div>
    """, unsafe_allow_html=True)
    
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        if st.button("⬅️ Ganti Jadwal"):
            st.session_state.step = "pilih_jadwal"
            st.rerun()
    with col_k2:
        if st.button("Lanjut ke Camilan Café ➡️"):
            if not picked:
                st.error("Silakan pilih minimal 1 kursi!")
            else:
                st.session_state.step = "pilih_fb"
                st.rerun()

elif st.session_state.step == "pilih_fb":
    st.markdown("### 🍿 XXI Café & Camilan")
    st.caption("Pesan makanan dan minuman sebelum masuk studio.")
    
    fb_choices = {}
    for idx, item in enumerate(FB_MENU):
        col_m1, col_m2 = st.columns([3, 1])
        with col_m1:
            st.markdown(f"**{item['name']}**")
            st.caption(f"{item['desc']} • Rp {item['price']:,}")
        with col_m2:
            current_qty = int(st.session_state.selected_fb.get(item['name'], {}).get("qty", 0)) if isinstance(st.session_state.selected_fb.get(item['name']), dict) else 0
            qty = st.number_input("Porsi", min_value=0, max_value=5, value=current_qty, key=f"fb_qty_{idx}")
            if qty > 0:
                fb_choices[item['name']] = {"price": item['price'], "qty": qty}
        st.markdown("<hr style='border-color:#1E2638; margin:8px 0;'>", unsafe_allow_html=True)
        
    st.session_state.selected_fb = fb_choices
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("⬅️ Kembali ke Kursi"):
            st.session_state.step = "pilih_kursi"
            st.rerun()
    with col_f2:
        if st.button("Lanjut Pembayaran ➡️"):
            st.session_state.step = "checkout"
            st.rerun()

elif st.session_state.step == "checkout":
    m = st.session_state.selected_movie
    num_seats = len(st.session_state.selected_seats)
    ticket_total = num_seats * m["price"]
    fb_total = sum(v["price"] * v["qty"] for v in st.session_state.selected_fb.values())
    pajak = int((ticket_total + fb_total) * 0.10)
    biaya_layanan = 3000
    grand_total = ticket_total + fb_total + pajak + biaya_layanan
    
    st.markdown("### 💳 Checkout Pembayaran")
    st.markdown(f"""
    <div class='movie-box' style='border-color:#FFB6C1;'>
        <h4 style='color:#FFB6C1; margin:0;'>{m['title']}</h4>
        <p style='color:#A0AEC0; font-size:12px; margin:0;'>{st.session_state.selected_cinema} • {st.session_state.selected_time} WIB</p>
        <hr style='border-color:#283044;'>
        <p><b>Kursi Studio:</b> {', '.join(st.session_state.selected_seats)} ({num_seats} tiket) = <b>Rp {ticket_total:,}</b></p>
        <p><b>Café XXI:</b> {', '.join([f"{k} ({v['qty']}x)" for k,v in st.session_state.selected_fb.items()]) if st.session_state.selected_fb else 'Tidak ada'} = <b>Rp {fb_total:,}</b></p>
        <p><b>Pajak Hiburan (10%):</b> Rp {pajak:,}</p>
        <p><b>Biaya Layanan m.tix:</b> Rp {biaya_layanan:,}</p>
        <hr style='border-color:#283044;'>
        <h3 style='color:#00FF7F; margin:0;'>Total Bayar: Rp {grand_total:,}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    pay_method = st.selectbox(
        "Metode Pembayaran:",
        [
            "📱 QRIS (GoPay, OVO, ShopeePay, BCA Mobile)",
            "🏦 Virtual Account BCA (Otomatis)",
            "🏦 Virtual Account Mandiri / Livin",
            "💳 Kartu Kredit / Debit (Visa / Mastercard)",
            "💵 Tunai di Kasir Bioskop"
        ]
    )
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        if st.button("⬅️ Ganti Camilan"):
            st.session_state.step = "pilih_fb"
            st.rerun()
    with col_c2:
        if st.button("✅ BAYAR SEKARANG"):
            booking_code = f"MTX-{random.randint(100000, 999999)}"
            now_str = datetime.now().strftime("%d %b %Y, %H:%M:%S")
            
            st.session_state.last_booking = {
                "code": booking_code,
                "movie": m["title"],
                "cinema": st.session_state.selected_cinema,
                "date": st.session_state.selected_date,
                "time": st.session_state.selected_time,
                "seats": ", ".join(st.session_state.selected_seats),
                "num_seats": num_seats,
                "fb": ", ".join([f"{k} (x{v['qty']})" for k,v in st.session_state.selected_fb.items()]) if st.session_state.selected_fb else "-",
                "total": grand_total,
                "pay_method": pay_method,
                "time_stamp": now_str
            }
            st.session_state.step = "tiket_selesai"
            st.rerun()

elif st.session_state.step == "tiket_selesai":
    t = st.session_state.last_booking
    st.balloons()
    st.success("Pembayaran Berhasil! E-Ticket m.tix Anda telah terbit.")
    
    clean_payment = t['pay_method']
    for icon in ['📱', '🏦', '💳', '💵']:
        clean_payment = clean_payment.replace(icon, '').strip()

    with st.container(border=True):
        st.subheader("CINEMA 21 𐙚 𐙚 𐙚 𐙚 𐙚 𐙚 𐙚")
        st.caption("m.tix Official Electronic Ticket")
        
        col_c1, col_c2 = st.columns([1, 1])
        with col_c1:
            st.write("**KODE BOOKING:**")
        with col_c2:
            st.info(f"**{t['code']}**")
            
        st.divider()
        st.write(f"### {t['movie']}")
        
        c_a, c_b = st.columns([1, 2])
        with c_a:
            st.write("Bioskop")
            st.write("Jadwal Tayang")
            st.write("Nomor Kursi")
            st.write("Pesanan Café")
            st.write("Pembayaran")
        with c_b:
            st.write(f": **{t['cinema']}**")
            st.write(f": **{t['date']} • {t['time']} WIB**")
            st.write(f": **{t['seats']}** ({t['num_seats']} Orang)")
            st.write(f": **{t['fb']}**")
            st.write(f": **{clean_payment}**")
            
        st.divider()
        c_t1, c_t2 = st.columns([1, 1])
        with c_t1:
            st.write("#### TOTAL BAYAR:")
        with c_t2:
            st.write(f"#### Rp {t['total']:,}")
            
        st.code("||| | |||| || ||| | |||| ||\\n(Barcode Tiket Masuk Studio)", language=None)
        st.caption("Tunjukkan barcode digital ini ke petugas pintu masuk bioskop XXI.")

    st.write("")
    if st.button("Pesan Tiket Baru / Kembali ke Beranda"):
        st.session_state.step = "pilih_film"
        st.session_state.selected_seats = []
        st.session_state.selected_fb = {}
        st.rerun()
