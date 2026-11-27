import streamlit as st

st.set_page_config(
    page_title="Congraduation Guys!",
    page_icon="🎓",
    layout="centered",
)

NAMA_PACAR = "Dita"
JUDUL_SURAT = f"Met wisuda, {NAMA_PACAR}! 🎓"

PARAGRAF_SURAT = [
    "Congraduation lah ya kalo kata orang-orang. Setelah menempuh huru-hara, suka, duka, duka, dan duka (hehe..), akhirnya dia LULUS GUYS!",
    "Terima kasih sudah bertahan dan berjuang menempuh pendidikan di dalam tirani REZIM WOWOK. Ya.. setidaknya proses selama 7 tahun itu menjadi IJAZAH ASLI!",
    "Semoga bisa cepat mendapatkan 1 dari 19JT LAPANGAN PEKERJAAN yang dijanjikan. Semoga selalu dijauhkan dari WAPRES (Waduh & Depressed).",
    "Selamat menempuh hidup BADDIE!",
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
    "  background: linear-gradient(125deg, #FFFDF0, #FEF9C3, #FEF08A, #FFF8DB);",
    "  background-size: 320% 320%;",
    "  animation: softYellowGradient 14s ease infinite;",
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
    "  animation: envelopeFadeIn 0.4s ease both;",
    "}",
    ".envelope {",
    "  position: relative;",
    "  width: 286px;",
    "  height: 180px;",
    "  background: linear-gradient(160deg, #FDFBF5 0%, #F4EFE3 100%);",
    "  border-radius: 18px;",
    "  box-shadow: 0 12px 26px rgba(145, 114, 38, 0.16), inset 0 2px 3px rgba(255, 255, 255, 0.95);",
    "  overflow: hidden;",
    "  border: 2px solid #E5DABF;",
    "  cursor: pointer;",
    "  transition: transform 0.25s ease, box-shadow 0.25s ease;",
    "}",
    ".envelope-link:hover .envelope {",
    "  transform: translateY(-15px) rotate(-10deg);",
    "  box-shadow: 0 16px 32px rgba(145, 114, 38, 0.22);",
    "}",
    ".envelope-sparkle-tl {",
    "  position: absolute;",
    "  top: 10px;",
    "  left: 14px;",
    "  font-size: 0.9rem;",
    "  color: #8A6522;",
    "  z-index: 6;",
    "}",
    ".envelope-sparkle-tr {",
    "  position: absolute;",
    "  top: 12px;",
    "  right: 14px;",
    "  font-size: 0.85rem;",
    "  color: #A17628;",
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
    "  border-top: 98px solid #F7F3E8;",
    "  transform-origin: top;",
    "  z-index: 3;",
    "}",
    ".envelope-card-preview {",
    "  position: absolute;",
    "  left: 20px;",
    "  right: 20px;",
    "  bottom: 14px;",
    "  height: 138px;",
    "  background: #FFFDF7;",
    "  border-radius: 12px;",
    "  border: 1.5px dashed #E5DABF;",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-weight: 600;",
    "  font-size: 0.96rem;",
    "  color: #5A3B0C;",
    "  z-index: 2;",
    "}",
    ".envelope-pocket {",
    "  position: absolute;",
    "  bottom: 0;",
    "  left: 0;",
    "  width: 0;",
    "  height: 0;",
    "  border-left: 141px solid #FAF7EE;",
    "  border-right: 141px solid #F3ECE0;",
    "  border-bottom: 94px solid #ECE4D3;",
    "  border-top: 86px solid transparent;",
    "  z-index: 4;",
    "}",
    ".envelope-seal {",
    "  position: absolute;",
    "  top: 72px;",
    "  left: 50%;",
    "  transform: translateX(-50%);",
    "  width: 46px;",
    "  height: 46px;",
    "  background: radial-gradient(circle at 32% 30%, #E5484D 0%, #B91C1C 68%, #7F1D1D 100%);",
    "  border: 2px solid #991B1B;",
    "  border-radius: 50%;",
    "  box-shadow: 0 5px 12px rgba(127, 29, 29, 0.35), inset 0 0 0 2px rgba(254, 202, 202, 0.45), inset 0 2px 3px rgba(255, 255, 255, 0.35);",
    "  display: flex;",
    "  align-items: center;",
    "  justify-content: center;",
    "  font-family: 'Fredoka', sans-serif;",
    "  font-size: 1.05rem;",
    "  color: #FEF2F2;",
    "  z-index: 5;",
    "}",
    ".envelope-hint {",
    "  text-align: center;",
    "  font-size: 0.86rem;",
    "  font-weight: 500;",
    "  color: #8A6522;",
    "  margin-bottom: 1.2rem;",
    "}",
    ".modal-backdrop {",
    "  position: fixed;",
    "  inset: 0;",
    "  background: rgba(84, 59, 20, 0.24);",
    "  backdrop-filter: blur(8px);",
    "  -webkit-backdrop-filter: blur(8px);",
    "  z-index: 998;",
    "  animation: backdropFadeIn 0.75s ease both;",
    "}",
    ".letter-container {",
    "  position: fixed;",
    "  top: 50%;",
    "  left: 50%;",
    "  transform: translate(-50%, -50%);",
    "  width: min(92vw, 560px);",
    "  max-height: 84vh;",
    "  overflow-y: auto;",
    "  background: linear-gradient(180deg, #FFFDF7 0%, #FEFCE8 100%);",
    "  border: 2px solid #FDE047;",
    "  border-radius: 24px;",
    "  padding: 1.8rem 1.4rem;",
    "  margin-top: 0;",
    "  z-index: 999;",
    "  box-shadow: 0 22px 48px rgba(84, 59, 20, 0.28), inset 0 2px 0 rgba(255, 255, 255, 0.95);",
    "  animation: modalPopIn 1.05s cubic-bezier(0.22, 1, 0.36, 1) 0.45s both;",
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
    "  text-align: justify;",
    "}",
    ".letter-footer {",
    "  margin-top: 1.5rem;",
    "  padding-top: 1rem;",
    "  border-top: 2px dotted #FACC15;",
    "  font-size: 0.96rem;",
    "  color: #7A581B;",
    "  text-align: center;",
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
    "@keyframes softYellowGradient {",
    "  0% { background-position: 0% 50%; }",
    "  50% { background-position: 100% 50%; }",
    "  100% { background-position: 0% 50%; }",
    "}",
    "@keyframes envelopeFadeIn {",
    "  from { opacity: 0; transform: scale(0.96) translateY(8px); }",
    "  to { opacity: 1; transform: scale(1) translateY(0); }",
    "}",
    "@keyframes letterSlideUp {",
    "  from { opacity: 0; transform: translateY(18px); }",
    "  to { opacity: 1; transform: translateY(0); }",
    "}",
    "@keyframes backdropFadeIn {",
    "  from { opacity: 0; }",
    "  to { opacity: 1; }",
    "}",
    "@keyframes modalPopIn {",
    "  0% { opacity: 0; transform: translate(-50%, -42%) scale(0.92); }",
    "  100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }",
    "}",
    "</style>",
]

st.markdown("\n".join(css_lines), unsafe_allow_html=True)

st.markdown(
    """
    <div class="header-box">
        <div class="y2k-pill">Dari HR PT Larping Sejahtera Abadi Nan Jaya</div>
        <div class="header-title">Offering Letter (Tapi Boong)</div>
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
        <div class="modal-backdrop"></div>
        <div class="letter-container">
            <div class="letter-title">{JUDUL_SURAT}</div>
            {paragraf_html}
            <div class="letter-footer">
                <div>{PENUTUP_SURAT}</div>
                <strong>{NAMA_PENGIRIM}</strong>
            </div>
            <div class="replay-wrap">
                <a class="replay-link" href="?buka=0" target="_self">Close</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )