import base64
from pathlib import Path
import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Selamat Wisuda! ✦ Y2K Edition",
    page_icon="🎓",
    layout="centered",
)

# 2. Pengaturan Konten (Silakan edit bagian ini)
NAMA_PACAR = "Dita"  # Ganti dengan nama panggilan
JUDUL_SURAT = f"Happy Graduation, {NAMA_PACAR}! 🎓✦"

# Daftar foto yang akan keluar bergantian (path_file, caption_polaroid)
DAFTAR_FOTO = [
    ("foto_1.jpg", "✦ pre-grad glow up & good vibes"),
    ("foto_2.jpg", "♡ late nights, big dreams & lots of laughs"),
    ("foto_3.jpg", "✿ officially graduated! so proud of you"),
]

# Durasi jeda antar foto keluar (detik)
JEDA_ANTAR_FOTO = 0.85

PARAGRAF_SURAT = [
    "Selamat atas kelulusanmu hari ini! Rasanya baru kemarin melihatmu sibuk menyusun jadwal, begadang menyelesaikan revisi, dan melewati hari-hari yang melelahkan demi sampai di titik ini.",
    "Terima kasih sudah bertahan dan berjuang sejauh ini. Setiap proses yang kamu lewati bukan hal yang mudah, dan aku bangga banget melihat semua usaha kerasmu akhirnya terbayar.",
    "Semoga gelar baru ini menjadi awal dari banyak langkah baik, peluang seru, dan hari-hari yang makin bersinar ke depannya. Selamat merayakan pencapaianmu!",
]

PENUTUP_SURAT = "Sending lots of cheers & proud energy ✦"
NAMA_PENGIRIM = "From your #1 supporter"


def encode_foto_base64(path_str: str) -> str | None:
    """Membaca file foto lokal dan mengubahnya menjadi data URI untuk animasi CSS."""
    file_path = Path(path_str)
    if not file_path.exists():
        return None

    ext = file_path.suffix.lower().lstrip(".")
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
        "gif": "image/gif",
    }
    mime_type = mime_map.get(ext, "image/jpeg")
    encoded = base64.b64encode(file_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


# 3. State & Penanganan Klik Langsung pada Amplop via Query Params
if "amplop_terbuka" not in st.session_state:
    st.session_state.amplop_terbuka = False

aksi = st.query_params.get("buka")
if aksi == "1":
    if not st.session_state.amplop_terbuka:
        st.session_state.amplop_terbuka = True
        st.session_state.trigger_balloons = True
    st.query_params.clear()
    st.rerun()
elif aksi == "0":
    st.session_state.amplop_terbuka = False
    st.query_params.clear()
    st.rerun()

if st.session_state.get("trigger_balloons"):
    st.balloons()
    st.session_state.trigger_balloons = False

# Hitung jeda surat agar baru muncul setelah seluruh foto selesai keluar
jumlah_foto = max(len(DAFTAR_FOTO), 1)
delay_awal_foto = 0.20
delay_surat = round(delay_awal_foto + (jumlah_foto * JEDA_ANTAR_FOTO) + 0.15, 2)

# 4. CSS Kustom: Girly Pop Y2K Kuning Soft
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Latar belakang kuning soft + pola polka lembut ala Y2K */
    .stApp {{
        background-color: #FFFDF0;
        background-image:
            radial-gradient(#FDE047 1.35px, transparent 1.35px),
            radial-gradient(#FACC15 1.1px, #FFFDF0 1.1px);
        background-size: 28px 28px;
        background-position: 0 0, 14px 14px;
        color: #543B14;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3.2rem;
        max-width: 640px;
    }}

    /* Header girly pop Y2K */
    .header-box {{
        text-align: center;
        background: linear-gradient(145deg, rgba(255, 254, 242, 0.96), rgba(254, 249, 195, 0.92));
        border: 2px solid #FDE047;
        border-radius: 24px;
        padding: 1.35rem 1.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 24px rgba(234, 179, 8, 0.16), inset 0 2px 0 rgba(255, 255, 255, 0.9);
    }}
    .y2k-pill {{
        display: inline-block;
        background: #FEF08A;
        color: #6B440A;
        border: 1.5px solid #FACC15;
        border-radius: 999px;
        padding: 0.2rem 0.8rem;
        font-family: 'Fredoka', sans-serif;
        font-size: 0.75rem;
        letter-spacing: 0.06em;
        margin-bottom: 0.55rem;
        box-shadow: 0 3px 0 #FDE047;
    }}
    .header-title {{
        font-family: 'Fredoka', sans-serif;
        font-size: 1.85rem;
        font-weight: 700;
        color: #5A3B0C;
        margin-bottom: 0.25rem;
        line-height: 1.2;
    }}
    .header-sub {{
        font-size: 0.93rem;
        color: #8A6522;
    }}

    /* Amplop interaktif bernuansa kuning glossy */
    .envelope-link {{
        text-decoration: none !important;
        display: flex;
        justify-content: center;
        margin: 1rem 0 0.55rem 0;
        -webkit-tap-highlight-color: transparent;
    }}
    .envelope {{
        position: relative;
        width: 286px;
        height: 180px;
        background: linear-gradient(160deg, #FEF08A 0%, #FDE047 100%);
        border-radius: 18px;
        box-shadow:
            0 12px 26px rgba(202, 138, 4, 0.20),
            inset 0 2px 3px rgba(255, 255, 255, 0.85);
        overflow: hidden;
        border: 2px solid #FACC15;
        cursor: pointer;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .envelope-link:hover .envelope {{
        transform: translateY(-5px) rotate(-1deg);
        box-shadow: 0 16px 32px rgba(202, 138, 4, 0.26);
    }}

    /* Kilau sudut Y2K pada amplop */
    .envelope-sparkle-tl {{
        position: absolute;
        top: 10px;
        left: 14px;
        font-size: 0.9rem;
        color: #A16207;
        z-index: 6;
    }}
    .envelope-sparkle-tr {{
        position: absolute;
        top: 12px;
        right: 14px;
        font-size: 0.85rem;
        color: #CA8A04;
        z-index: 6;
    }}

    /* Tutup segitiga amplop */
    .envelope-flap {{
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 141px solid transparent;
        border-right: 141px solid transparent;
        border-top: 98px solid #FDE047;
        transform-origin: top;
        transition: transform 0.6s ease;
        z-index: 3;
    }}
    .envelope.open .envelope-flap {{
        transform: rotateX(180deg);
        z-index: 1;
    }}

    /* Kartu mengintip di dalam amplop */
    .envelope-card-preview {{
        position: absolute;
        left: 20px;
        right: 20px;
        bottom: 14px;
        height: 138px;
        background: #FFFDF5;
        border-radius: 12px;
        border: 1.5px dashed #FACC15;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
        font-size: 0.96rem;
        color: #6B440A;
        z-index: 2;
        transition: transform 0.5s ease;
    }}
    .envelope.open .envelope-card-preview {{
        transform: translateY(-28px);
    }}

    /* Lipatan bawah amplop */
    .envelope-pocket {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 141px solid #FDE68A;
        border-right: 141px solid #FCD34D;
        border-bottom: 94px solid #FACC15;
        border-top: 86px solid transparent;
        z-index: 4;
    }}

    /* Segel star-charm di tengah amplop */
    .envelope-seal {{
        position: absolute;
        top: 75px;
        left: 50%;
        transform: translateX(-50%);
        width: 42px;
        height: 42px;
        background: linear-gradient(145deg, #FFFDF5, #FEF08A);
        border: 2px solid #EAB308;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Fredoka', sans-serif;
        font-size: 1.1rem;
        color: #713F12;
        z-index: 5;
        box-shadow: 0 4px 10px rgba(202, 138, 4, 0.22);
        transition: opacity 0.3s ease;
    }}
    .envelope.open .envelope-seal {{
        opacity: 0;
    }}

    /* Label petunjuk bawah amplop */
    .envelope-hint {{
        text-align: center;
        font-size: 0.86rem;
        font-weight: 500;
        color: #8A6522;
        margin-bottom: 1.2rem;
    }}

    /* Wadah utama surat & polaroid */
    .letter-container {{
        background: linear-gradient(180deg, #FFFDF7 0%, #FEFCE8 100%);
        border: 2px solid #FDE047;
        border-radius: 24px;
        padding: 1.8rem 1.4rem;
        margin-top: 1.2rem;
        box-shadow:
            0 14px 32px rgba(202, 138, 4, 0.14),
            inset 0 2px 0 rgba(255, 255, 255, 0.9);
        animation: shellAppear 0.35s ease both;
    }}

    /* Tumpukan Polaroid miring lucu */
    .polaroid-stack {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0.4rem auto 2rem auto;
        padding: 0.4rem 0;
    }}
    .polaroid-card {{
        width: 100%;
        max-width: 288px;
        background: #FFFDF9;
        padding: 11px 11px 16px 11px;
        border-radius: 12px;
        border: 1.5px solid #FDE047;
        box-shadow: 0 10px 22px rgba(202, 138, 4, 0.16), 0 3px 0 #FEF08A;
        margin-bottom: -10px;
        opacity: 0;
        transform: rotate(var(--tilt-angle, 0deg));
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: polaroidSlideOut 0.75s cubic-bezier(0.22, 1, 0.36, 1) var