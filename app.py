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
    "  perspective: 800px;",
    "  transition: transform 0.25s ease, box-shadow 0.25s ease;",
    "}",
    ".envelope-link:hover .envelope {",
    "  transform: translateY(-5px) rotate(-1deg);",
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
    "  position: absolute