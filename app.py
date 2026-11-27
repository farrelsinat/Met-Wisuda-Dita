import base64
from pathlib import Path
import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Selamat Wisuda!",
    page_icon="🎓",
    layout="centered",
)

# 2. Pengaturan Konten (Silakan edit bagian ini)
NAMA_PACAR = "Dita"  # Ganti dengan nama panggilan
JUDUL_SURAT = f"Selamat Wisuda, {NAMA_PACAR} 🎓"

# Daftar foto yang akan keluar bergantian (path_file, caption)
DAFTAR_FOTO = [
    ("foto_1.jpg", "Momen persiapan sebelum hari wisuda"),
    ("foto_2.jpg", "Proses panjang penuh cerita dan perjuangan"),
    ("foto_3.jpg", "Akhirnya resmi menyandang gelar baru!"),
]

# Durasi jeda antar foto keluar (detik)
JEDA_ANTAR_FOTO = 0.85

PARAGRAF_SURAT = [
    "Selamat atas kelulusanmu hari ini. Rasanya baru kemarin melihatmu sibuk menyusun jadwal, begadang menyelesaikan revisi, dan melewati hari-hari yang melelahkan demi sampai di titik ini.",
    "Terima kasih sudah bertahan dan berjuang sejauh ini. Setiap proses yang kamu lewati bukan hal yang mudah, dan aku sangat bangga melihat semua usaha kerasmu akhirnya terbayar.",
    "Semoga gelar baru ini menjadi awal dari banyak langkah baik, pintu kesempatan yang luas, dan hari-hari yang jauh lebih tenang ke depannya. Selamat merayakan pencapaianmu!",
]

PENUTUP_SURAT = "Dengan penuh rasa bangga,"
NAMA_PENGIRIM = "Dari seseorang yang selalu mendukungmu"


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

# 4. CSS Kustom: Palet Kuning Soft, Amplop Klik Langsung & Foto Bergantian
st.markdown(
    f"""
    <style>
    /* Latar belakang utama: Soft Cream & Butter Yellow */
    .stApp {{
        background: linear-gradient(180deg, #FFFDF5 0%, #FFF8DC 100%);
        color: #4A3F28;
    }}

    /* Merapikan padding atas */
    .block-container {{
        padding-top: 2.2rem;
        padding-bottom: 3rem;
        max-width: 640px;
    }}

    /* Judul atas */
    .header-box {{
        text-align: center;
        margin-bottom: 1.4rem;
    }}
    .header-title {{
        font-size: 1.75rem;
        font-weight: 700;
        color: #5C4B24;
        margin-bottom: 0.25rem;
    }}
    .header-sub {{
        font-size: 0.95rem;
        color: #8C7849;
    }}

    /* Tautan pembungkus amplop agar bisa diklik langsung */
    .envelope-link {{
        text-decoration: none !important;
        display: flex;
        justify-content: center;
        margin: 1rem 0 0.6rem 0;
        -webkit-tap-highlight-color: transparent;
    }}

    /* Visual Amplop */
    .envelope {{
        position: relative;
        width: 280px;
        height: 175px;
        background: #FDE68A;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(180, 145, 50, 0.16);
        overflow: hidden;
        border: 2px solid #F5D061;
        cursor: pointer;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .envelope-link:hover .envelope {{
        transform: translateY(-4px);
        box-shadow: 0 14px 28px rgba(180, 145, 50, 0.22);
    }}

    /* Tutup segitiga amplop */
    .envelope-flap {{
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 138px solid transparent;
        border-right: 138px solid transparent;
        border-top: 95px solid #FCD34D;
        transform-origin: top;
        transition: transform 0.6s ease;
        z-index: 3;
    }}
    .envelope.open .envelope-flap {{
        transform: rotateX(180deg);
        z-index: 1;
    }}

    /* Kertas mengintip di dalam amplop */
    .envelope-card-preview {{
        position: absolute;
        left: 20px;
        right: 20px;
        bottom: 14px;
        height: 135px;
        background: #FFFBEB;
        border-radius: 8px;
        border: 1px solid #FDE68A;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.92rem;
        color: #785E22;
        z-index: 2;
        transition: transform 0.5s ease;
    }}
    .envelope.open .envelope-card-preview {{
        transform: translateY(-28px);
    }}

    /* Bagian lipatan bawah amplop */
    .envelope-pocket {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 138px solid #FBE178;
        border-right: 138px solid #F9D857;
        border-bottom: 92px solid #F7CE46;
        border-top: 85px solid transparent;
        z-index: 4;
    }}

    /* Segel stiker di tengah amplop */
    .envelope-seal {{
        position: absolute;
        top: 74px;
        left: 50%;
        transform: translateX(-50%);
        width: 38px;
        height: 38px;
        background: #FFFBEB;
        border: 2px solid #F59E0B;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.05rem;
        z-index: 5;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        transition: opacity 0.3s ease;
    }}
    .envelope.open .envelope-seal {{
        opacity: 0;
    }}

    /* Petunjuk kecil di bawah amplop */
    .envelope-hint {{
        text-align: center;
        font-size: 0.85rem;
        color: #8C7849;
        margin-bottom: 1.2rem;
    }}

    /* Wadah Utama Isi Amplop */
    .letter-container {{
        background-color: #FFFDF7;
        border: 1.5px solid #FDE68A;
        border-radius: 16px;
        padding: 1.8rem 1.6rem;
        margin-top: 1.2rem;
        box-shadow: 0 12px 30px rgba(180, 145, 50, 0.10);
        animation: shellAppear 0.35s ease both;
    }}

    /* Kumpulan foto yang keluar bergantian */
    .photo-gallery-sequence {{
        display: flex;
        flex-direction: column;
        gap: 1.15rem;
        margin: 0.4rem auto 1.6rem auto;
        max-width: 340px;
    }}
    .photo-stage {{
        text-align: center;
        opacity: 0;
        animation: photoSlideOut 0.7s cubic-bezier(0.22, 1, 0.36, 1) var(--photo-delay, 0.2s) forwards;
    }}
    .photo-frame {{
        background: #FFFBEB;
        padding: 10px 10px 12px 10px;
        border-radius: 14px;
        border: 1.5px solid #FDE68A;
        box-shadow: 0 10px 22px rgba(180, 145, 50, 0.14);
        overflow: hidden;
    }}
    .photo-frame img {{
        width: 100%;
        height: auto;
        border-radius: 10px;
        display: block;
    }}
    .photo-caption {{
        margin-top: 0.55rem;
        font-size: 0.88rem;
        color: #7A632B;
        font-style: italic;
    }}

    /* Tahap Surat: Muncul setelah seluruh foto keluar */
    .letter-stage {{
        opacity: 0;
        animation: letterSlideUp 0.75s ease {delay_surat}s forwards;
    }}
    .letter-title {{
        font-size: 1.4rem;
        font-weight: 700;
        color: #5C481C;
        margin-bottom: 1rem;
        text-align: center;
    }}
    .letter-body {{
        font-size: 1.02rem;
        line-height: 1.75;
        color: #4A3F28;
        margin-bottom: 1rem;
        text-align: left;
    }}
    .letter-footer {{
        margin-top: 1.5rem;
        padding-top: 1rem;
        border-top: 1px dashed #FCD34D;
        font-size: 0.96rem;
        color: #6E5826;
    }}

    @keyframes shellAppear {{
        from {{
            opacity: 0;
            transform: translateY(10px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes photoSlideOut {{
        0% {{
            opacity: 0;
            transform: translateY(50px) scale(0.92);
        }}
        65% {{
            opacity: 1;
            transform: translateY(-8px) scale(1.01);
        }}
        100% {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}
    }}

    @keyframes letterSlideUp {{
        from {{
            opacity: 0;
            transform: translateY(18px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 5. Bagian Header
st.markdown(
    """
    <div class="header-box">
        <div class="header-title">Ada Pesan Kecil Untukmu ✉️</div>
        <div class="header-sub">Ketuk atau klik langsung amplopnya untuk membuka surat</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 6. Render Amplop Interaktif yang Bisa Diklik Langsung
status_amplop = "open" if st.session_state.amplop_terbuka else ""
target_param = "?buka=0" if st.session_state.amplop_terbuka else "?buka=1"
teks_petunjuk = (
    "Klik amplop lagi untuk menutup"
    if st.session_state.amplop_terbuka
    else "Klik amplop untuk membuka"
)

st.markdown(
    f"""
    <a class="envelope-link" href="{target_param}" target="_self">
        <div class="envelope {status_amplop}">
            <div class="envelope-flap"></div>
            <div class="envelope-card-preview">Untuk {NAMA_PACAR} 🎓</div>
            <div class="envelope-pocket"></div>
            <div class="envelope-seal">💛</div>
        </div>
    </a>
    <div class="envelope-hint">{teks_petunjuk}</div>
    """,
    unsafe_allow_html=True,
)

# 7. Isi Amplop: Foto Keluar Bergantian Dulu, Lalu Surat Menyusul
if st.session_state.amplop_terbuka:
    foto_items_html = []
    for idx, (path_foto, caption_foto) in enumerate(DAFTAR_FOTO):
        delay_foto = round(delay_awal_foto + (idx * JEDA_ANTAR_FOTO), 2)
        foto_uri = encode_foto_base64(path_foto)

        if foto_uri:
            konten_foto = f"""
            <div class="photo-frame">
                <img src="{foto_uri}" alt="{caption_foto}" />
            </div>
            <div class="photo-caption">{caption_foto}</div>
            """
        else:
            konten_foto = f"""
            <div class="photo-frame">
                <div class="photo-caption">
                    Letakkan file foto <strong>{path_foto}</strong> di folder yang sama dengan <code>app.py</code>.
                </div>
            </div>
            <div class="photo-caption">{caption_foto}</div>
            """

        foto_items_html.append(
            f'<div class="photo-stage" style="--photo-delay: {delay_foto}s;">{konten_foto}</div>'
        )

    foto_sequence_html = "\n".join(foto_items_html)
    paragraf_html = "\n".join(
        f'<p class="letter-body">{paragraf}</p>' for paragraf in PARAGRAF_SURAT
    )

    st.markdown(
        f"""
        <div class="letter-container">
            <div class="photo-gallery-sequence">
                {foto_sequence_html}
            </div>
            <div class="letter-stage">
                <div class="letter-title">{JUDUL_SURAT}</div>
                {paragraf_html}
                <div class="letter-footer">
                    <div>{PENUTUP_SURAT}</div>
                    <strong>{NAMA_PENGIRIM}</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )