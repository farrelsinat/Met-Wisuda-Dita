import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Selamat Wisuda! Y2K Edition",
    page_icon="🎓",
    layout="centered",
)

NAMA_PACAR = "Dita"
JUDUL_SURAT = f"Happy Graduation, {NAMA_PACAR}! 🎓"

DAFTAR_FOTO = [
    ("foto_1.jpg", "pre-grad glow up & good vibes"),
    ("foto_2.jpg", "late nights, big dreams & lots of laughs"),
    ("foto_3.jpg", "officially graduated! so proud of you"),
]

JEDA_ANTAR_FOTO = 0.85

PARAGRAF_SURAT = [
    "Selamat atas kelulusanmu hari ini! Rasanya baru kemarin melihatmu sibuk menyusun jadwal, begadang menyelesaikan revisi, dan melewati hari-hari yang melelahkan demi sampai di titik ini.",
    "Terima kasih sudah bertahan dan berjuang sejauh ini. Setiap proses yang kamu lewati bukan hal yang mudah, dan aku bangga banget melihat semua usaha kerasmu akhirnya terbayar.",
    "Semoga gelar baru ini menjadi awal dari banyak langkah baik, peluang seru, dan hari-hari yang makin bersinar ke depannya. Selamat merayakan pencapaianmu!",
]

PENUTUP_SURAT = "Sending lots of cheers & proud energy"
NAMA_PENGIRIM = "From your #1 supporter"


def encode_foto_base64(path_str: str) -> str | None:
    """Membaca file foto lokal dan mengubahnya menjadi data URI."""
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

jumlah_foto = max(len(DAFTAR_FOTO), 1)
delay_awal_foto = 0.20
delay_surat = round(delay_awal_foto + (jumlah_foto * JEDA_ANTAR_FOTO) + 0.15, 2)

css_lines = [
    "<style>",
    "@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');",
    ".stApp {",
    "  background-color: #FFFDF0;",
    "  background-image: radial-gradient(#FDE047 1.35px, transparent 1.35px), radial-gradient(#FACC15 1.1px, #FFFDF0 1.1px);",
    "  background-size: 28px 28px;",
    "  background-position: 0 0, 14px 14px;",
    "  color: #543B14;",
    "  font-family: 'Plus Jakarta Sans', sans-serif;",
    "}",
    ".block-container {",
    "  padding-top: 2rem;",
    "  padding-bottom: 3.2rem;",
    "  max-width: 640px;",
    "}",
    ".header-box {",
    "  text-align: center;",
    "  background: linear-gradient(145deg, rgba(255, 254, 242, 0.96), rgba(254, 249, 195, 0.92));",
    "  border: 2px solid #FDE047;",
    "  border-radius: 24px;",
    "  padding: 1.35rem 1.2rem;",
    "  margin-bottom: 1.5rem;",
    "  box-shadow: 0 10px 24px rgba(234, 179, 8, 0.16), inset 0 2px 0 rgba(255, 255, 255, 0.9);",
    "}",
    ".y2k-pill {",
    "  display: inline-block;",
    "  background: #FEF08A;",
    "  color: #6B440A;",
    "  border: 1.5px solid #FACC15;",
    "  border-radius: 999px;",
    "  padding: 0.2rem 0.8rem;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 0.75rem;",
    "  letter-spacing: 0.06em;",
    "  margin-bottom: 0.55rem;",
    "  box-shadow: 0 3px 0 #FDE047;",
    "}",
    ".header-title {",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 1.85rem;",
    "  font-weight: 700;",
    "  color: #5A3B0C;",
    "  margin-bottom: 0.25rem;",
    "  line-height: 1.2;",
    "}",
    ".header-sub {",
    "  font-size: 0.93rem;",
    "  color: #8A6522;",
    "}",
    ".envelope-link {",
    "  text-decoration: none !important;",
    "  display: flex;",
    "  justify-content: center;",
    "  margin: 1rem 0 0.55rem 0;",
    "  -webkit-tap-highlight-color: transparent;",
    "}",
    ".envelope {",
    "  position: relative;",
    "  width: 286px;",
    "  height: 180px;",
    "  background: linear-gradient(160deg, #FEF08A 0%, #FDE047 100%);",
    "  border-radius: 18px;",
    "  box-shadow: 0 12px 26px rgba(202, 138, 4, 0.20), inset 0 2px 3px rgba(255, 255, 255, 0.85);",
    "  overflow: hidden;",
    "  border: 2px solid #FACC15;",
    "  cursor: pointer;",
    "  transition: transform 0.25s ease, box-shadow 0.25s ease;",
    "}",
    ".envelope-link:hover .envelope {",
    "  transform: translateY(-5px) rotate(-1deg);",
    "  box-shadow: 0 16px 32px rgba(202, 138, 4, 0.26);",
    "}",
    ".envelope-sparkle-tl {",
    "  position: absolute;",
    "  top: 10px;",
    "  left: 14px;",
    "  font-size: 0.9rem;",
    "  color: #A16207;",
    "  z-index: 6;",
    "}",
    ".envelope-sparkle-tr {",
    "  position: absolute;",
    "  top: 12px;",
    "  right: 14px;",
    "  font-size: 0.85rem;",
    "  color: #CA8A04;",
    "  z-index: 6;",
    "}",
    ".envelope-flap {",
    "  position: absolute;",
    "  top: 0;",
    "  left: 0;",
    "  width: 0;",
    "  height: 0;",
    "  border-left: 141px solid transparent;",
    "  border-right: 141px solid transparent;",
    "  border-top: 98px solid #FDE047;",
    "  transform-origin: top;",
    "  transition: transform 0.6s ease;",
    "  z-index: 3;",
    "}",
    ".envelope.open .envelope-flap {",
    "  transform: rotateX(180deg);",
    "  z-index: 1;",
    "}",
    ".envelope-card-preview {",
    "  position: absolute;",
    "  left: 20px;",
    "  right: 20px;",
    "  bottom: 14px;",
    "  height: 138px;",
    "  background: #FFFDF5;",
    "  border-radius: 12px;",
    "  border: 1.5px dashed #FACC15;",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-weight: 600;",
    "  font-size: 0.96rem;",
    "  color: #6B440A;",
    "  z-index: 2;",
    "  transition: transform 0.5s ease;",
    "}",
    ".envelope.open .envelope-card-preview {",
    "  transform: translateY(-28px);",
    "}",
    ".envelope-pocket {",
    "  position: absolute;",
    "  bottom: 0;",
    "  left: 0;",
    "  width: 0;",
    "  height: 0;",
    "  border-left: 141px solid #FDE68A;",
    "  border-right: 141px solid #FCD34D;",
    "  border-bottom: 94px solid #FACC15;",
    "  border-top: 86px solid transparent;",
    "  z-index: 4;",
    "}",
    ".envelope-seal {",
    "  position: absolute;",
    "  top: 75px;",
    "  left: 50%;",
    "  transform: translateX(-50%);",
    "  width: 42px;",
    "  height: 42px;",
    "  background: linear-gradient(145deg, #FFFDF5, #FEF08A);",
    "  border: 2px solid #EAB308;",
    "  border-radius: 50%;",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 1.1rem;",
    "  color: #713F12;",
    "  z-index: 5;",
    "  box-shadow: 0 4px 10px rgba(202, 138, 4, 0.22);",
    "  transition: opacity 0.3s ease;",
    "}",
    ".envelope.open .envelope-seal {",
    "  opacity: 0;",
    "}",
    ".envelope-hint {",
    "  text-align: center;",
    "  font-size: 0.86rem;",
    "  font-weight: 500;",
    "  color: #8A6522;",
    "  margin-bottom: 1.2rem;",
    "}",
    ".letter-container {",
    "  background: linear-gradient(180deg, #FFFDF7 0%, #FEFCE8 100%);",
    "  border: 2px solid #FDE047;",
    "  border-radius: 24px;",
    "  padding: 1.8rem 1.4rem;",
    "  margin-top: 1.2rem;",
    "  box-shadow: 0 14px 32px rgba(202, 138, 4, 0.14), inset 0 2px 0 rgba(255, 255, 255, 0.9);",
    "  animation: shellAppear 0.35s ease both;",
    "}",
    ".polaroid-stack {",
    "  display: flex;",
    "  flex-direction: column;",
    "  align-items: center;",
    "  margin: 0.4rem auto 2rem auto;",
    "  padding: 0.4rem 0;",
    "}",
    ".polaroid-card {",
    "  width: 100%;",
    "  max-width: 288px;",
    "  background: #FFFDF9;",
    "  padding: 11px 11px 16px 11px;",
    "  border-radius: 12px;",
    "  border: 1.5px solid #FDE047;",
    "  box-shadow: 0 10px 22px rgba(202, 138, 4, 0.16), 0 3px 0 #FEF08A;",
    "  margin-bottom: -10px;",
    "  opacity: 0;",
    "  transform: rotate(var(--tilt-angle, 0deg));",
    "  transition: transform 0.3s ease, box-shadow 0.3s ease;",
    "  animation: polaroidSlideOut 0.75s cubic-bezier(0.22, 1, 0.36, 1) var(--photo-delay, 0.2s) forwards;",
    "  position: relative;",
    "  z-index: var(--card-z, 1);",
    "}",
    ".polaroid-card:last-child {",
    "  margin-bottom: 0;",
    "}",
    ".polaroid-card:hover {",
    "  transform: rotate(0deg) scale(1.03) !important;",
    "  box-shadow: 0 16px 30px rgba(202, 138, 4, 0.24);",
    "  z-index: 20;",
    "}",
    ".polaroid-photo-box {",
    "  background: #FEF9C3;",
    "  border-radius: 8px;",
    "  overflow: hidden;",
    "  border: 1px solid #FDE047;",
    "}",
    ".polaroid-photo-box img {",
    "  width: 100%;",
    "  height: auto;",
    "  display: block;",
    "}",
    ".polaroid-caption {",
    "  margin-top: 0.65rem;",
    "  text-align: center;",
    "  font-family: 'Caveat', cursive, sans-serif;",
    "  font-size: 1.28rem;",
    "  font-weight: 700;",
    "  line-height: 1.25;",
    "  color: #5A3B0C;",
    "}",
    ".polaroid-placeholder {",
    "  padding: 1.4rem 0.8rem;",
    "  text-align: center;",
    "  font-size: 0.85rem;",
    "  color: #7A581B;",
    "}",
    ".letter-stage {",
    "  opacity: 0;",
    f"  animation: letterSlideUp 0.75s ease {delay_surat}s forwards;",
    "}",
    ".letter-title {",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 1.48rem;",
    "  font-weight: 700;",
    "  color: #5A3B0C;",
    "  margin-bottom: 1.1rem;",
    "  text-align: center;",
    "}",
    ".letter-body {",
    "  font-size: 1.02rem;",
    "  line-height: 1.78;",
    "  color: #543B14;",
    "  margin-bottom: 1rem;",
    "  text-align: left;",
    "}",
    ".letter-footer {",
    "  margin-top: 1.5rem;",
    "  padding-top: 1rem;",
    "  border-top: 2px dotted #FACC15;",
    "  font-size: 0.96rem;",
    "  color: #7A581B;",
    "}",
    "@keyframes shellAppear {",
    "  from { opacity: 0; transform: translateY(10px); }",
    "  to { opacity: 1; transform: translateY(0); }",
    "}",
    "@keyframes polaroidSlideOut {",
    "  0% { opacity: 0; transform: translateY(55px) scale(0.9) rotate(0deg); }",
    "  65% { opacity: 1; transform: translateY(-8px) scale(1.01) rotate(calc(var(--tilt-angle, 0deg) * 1.15)); }",
    "  100% { opacity: 1; transform: translateY(0) scale(1) rotate(var(--tilt-angle, 0deg)); }",
    "}",
    "@keyframes letterSlideUp {",
    "  from { opacity: 0; transform: translateY(18px); }",
    "  to { opacity: 1; transform: translateY(0); }",
    "}",
    "</style>",
]

st.markdown("\n".join(css_lines), unsafe_allow_html=True)

st.markdown(
    """
    <div class="header-box">
        <div class="y2k-pill">Y2K POP EDITION</div>
        <div class="header-title">Special Mail For You</div>
        <div class="header-sub">Tap langsung amplop kuningnya buat ngintip kejutan wisuda</div>
    </div>
    """,
    unsafe_allow_html=True,
)

status_amplop = "open" if st.session_state.amplop_terbuka else ""
target_param = "?buka=0" if st.session_state.amplop_terbuka else "?buka=1"
teks_petunjuk = (
    "Tap amplop lagi buat nutup surat"
    if st.session_state.amplop_terbuka
    else "Tap amplop buat buka surat"
)

st.markdown(
    f"""
    <a class="envelope-link" href="{target_param}" target="_self">
        <div class="envelope {status_amplop}">
            <div class="envelope-sparkle-tl">*</div>
            <div class="envelope-sparkle-tr">+</div>
            <div class="envelope-flap"></div>
            <div class="envelope-card-preview">For {NAMA_PACAR} 🎓</div>
            <div class="envelope-pocket"></div>
            <div class="envelope-seal">*</div>
        </div>
    </a>
    <div class="envelope-hint">{teks_petunjuk}</div>
    """,
    unsafe_allow_html=True,
)

if st.session_state.amplop_terbuka:
    sudut_miring = [-3.5, 3.0, -2.5, 3.6, -2.8]
    foto_items_html = []

    for idx, (path_foto, caption_foto) in enumerate(DAFTAR_FOTO):
        delay_foto = round(delay_awal_foto + (idx * JEDA_ANTAR_FOTO), 2)
        tilt = sudut_miring[idx % len(sudut_miring)]
        foto_uri = encode_foto_base64(path_foto)

        if foto_uri:
            isi_media = f'<img src="{foto_uri}" alt="{caption_foto}" />'
        else:
            isi_media = (
                f'<div class="polaroid-placeholder">'
                f"Letakkan file <strong>{path_foto}</strong> di folder yang sama dengan <code>app.py</code>"
                f"</div>"
            )

        foto_items_html.append(
            f"""
            <div class="polaroid-card" style="--photo-delay: {delay_foto}s; --tilt-angle: {tilt}deg; --card-z: {idx + 1};">
                <div class="polaroid-photo-box">
                    {isi_media}
                </div>
                <div class="polaroid-caption">{caption_foto}</div>
            </div>
            """
        )

    polaroid_stack_html = "\n".join(foto_items_html)
    paragraf_html = "\n".join(
        f'<p class="letter-body">{paragraf}</p>' for paragraf in PARAGRAF_SURAT
    )

    st.markdown(
        f"""
        <div class="letter-container">
            <div class="polaroid-stack">
                {polaroid_stack_html}
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