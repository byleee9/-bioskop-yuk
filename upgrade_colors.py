path = "C:/Users/user/bioskop-yuk/app_web_xxi.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace CSS styling to gorgeous pastel: soft blue (#ADD8E6, #1A2436), soft pink (#FFB6C1, #FF69B4, #FFF0F5), clean white & rose gold
old_css = """<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background: #0B0E14;
        color: #F0F2F5;
    }
    .mobile-header {
        background: linear-gradient(180deg, #1A1F2C 0%, #10141E 100%);
        border-bottom: 2px solid #D4AF37;
        padding: 12px 16px;
        position: sticky;
        top: 0;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 10px 10px 0 0;
    }
    .xxi-logo {
        font-size: 22px;
        font-weight: 800;
        letter-spacing: 2px;
        color: #D4AF37;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.4);
    }
    .xxi-badge {
        background: #FF69B4;
        color: #FFFFFF;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 600;
    }
    .movie-box {
        background: #151A26;
        border: 1px solid #283044;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    .tag-age {
        background: #2D3748;
        color: #E2E8F0;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
    }
    .tag-format {
        background: #4A154B;
        color: #FFB6C1;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
    }
    .screen-cinema {
        background: linear-gradient(180deg, #D4AF37 0%, rgba(212,175,55,0.05) 100%);
        height: 18px;
        border-radius: 50% / 100% 100% 0 0;
        text-align: center;
        font-size: 9px;
        color: #000;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 18px;
    }
    .ticket-paper {
        background: #FFFFFF;
        color: #111111;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        border-top: 6px solid #D4AF37;
    }
    .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%);
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(212,175,55,0.3) !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #FF69B4 0%, #D4AF37 100%) !important;
        color: #FFFFFF !important;
    }
</style>"""

new_css = """<style>
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
    /* Native container borders in pastel style */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #FFB6C1 !important;
        border-radius: 14px !important;
        background: #181E34 !important;
        box-shadow: 0 4px 20px rgba(255, 182, 193, 0.15) !important;
    }
</style>"""

text = text.replace(old_css, new_css)

# Update price color in now-playing to pretty pastel pink
text = text.replace("color:#D4AF37", "color:#FFB6C1")
text = text.replace("CINEMA 21", "CINEMA 21 𐙚")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("PALETTE_UPGRADED_TO_PASTEL")
