import streamlit as st

st.set_page_config(
    page_title="Selamat Wisuda!",
    page_icon="🎓",
    layout="centered",
)

NAMA_PACAR = "Dita"
JUDUL_SURAT = f"Happy Graduation, {NAMA_PACAR}! 🎓"

PARAGRAF_SURAT = [
    "Congraduation lah ya kalo kata orang-orang. Setelah menempuh huru-hara, suka, duka, duka, dan duka (hehe..), akhirnya dia LULUS GUYS!",
    "Terima kasih sudah bertahan dan berjuang menempuh pendidikan di dalam tirani REZIM WOWOK. Ya.. setidaknya proses selama 7 tahun itu membuahkan IJAZAH ASLI!",
    "Semoga bisa cepat mendapatkan 1 dari 19jt lapangan pekerjaan yang dijanjikan. Semoga selalu dijauhkan dari WAPRES (Waduh & Depressed). Selamat menempuh hidup BADDIE!",
]

PENUTUP_SURAT = "Sending lots of cheers & info loker!"
NAMA_PENGIRIM = "From Your Beloved Adek & Nam Joo-hyuk"

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

css_lines = [
    "<style>",
    "@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');",
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
    "  z-index: 3;",
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
    "  margin-top: 0.4rem;",
    "  box-shadow: 0 14px 32px rgba(202, 138, 4, 0.14), inset 0 2px 0 rgba(255, 255, 255, 0.9);",
    "  animation: letterSlideUp 0.55s ease 0.15s both;",
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
    ".replay-wrap {",
    "  margin-top: 1.4rem;",
    "  text-align: center;",
    "}",
    ".replay-link {",
    "  display: inline-block;",
    "  text-decoration: none !important;",
    "  background: #FEF08A;",
    "  color: #5A3B0C !important;",
    "  border: 1.5px solid #FACC15;",
    "  border-radius: 999px;",
    "  padding: 0.45rem 1.1rem;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 0.85rem;",
    "  box-shadow: 0 3px 0 #FDE047;",
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
        <div class="y2k-pill">Hello Dita!</div>
        <div class="header-title">Special Mail For You</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not st.session_state.amplop_terbuka:
    st.markdown(
        f"""
        <a class="envelope-link" href="?buka=1" target="_self">
            <div class="envelope">
                <div class="envelope-sparkle-tl">*</div>
                <div class="envelope-sparkle-tr">+</div>
                <div class="envelope-flap"></div>
                <div class="envelope-card-preview">For {NAMA_PACAR} 🎓</div>
                <div class="envelope-pocket"></div>
                <div class="envelope-seal">*</div>
            </div>
        </a>
        <div class="envelope-hint">Tap this out!</div>
        """,
        unsafe_allow_html=True,
    )
else:
    paragraf_html = "\n".join(
        f'<p class="letter-body">{paragraf}</p>' for paragraf in PARAGRAF_SURAT
    )

    st.markdown(
        f"""
        <div class="letter-container">
            <div class="letter-title">{JUDUL_SURAT}</div>
            {paragraf_html}
            <div class="letter-footer">
                <div>{PENUTUP_SURAT}</div>
                <strong>{NAMA_PENGIRIM}</strong>
            </div>
            <div class="replay-wrap">
                <a class="replay-link" href="?buka=0" target="_self">Putar ulang dari amplop</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )