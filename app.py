import streamlit as st
import urllib.parse

# ================= CONFIG =================
st.set_page_config(page_title="Solusi Tugas & Project IT Kamu!", page_icon="💻", layout="wide")
WA_NUMBER = "6289501857938"  # <-- GANTI NOMOR WA LU DISINI

# ================= DATA =================
SERVICES = [
    {"id": "01", "name": "Laporan & Skripsi", "price": 150000, "durasi": "3-7 Hari", "desc": "Bab 1-5, Revisi sampai ACC, Cek Turnitin, Bimbingan", "icons": [("Word", "microsoftword"), ("PDF", "adobeacrobatreader"), ("LaTeX", "latex"), ("Docs", "googledocs")]},
    {"id": "02", "name": "Tugas Kuliah & UTS/UAS", "price": 50000, "durasi": "1-3 Hari", "desc": "Semua matkul IT & Non-IT, Dijamin tepat waktu", "icons": [("Buku", "bookstack"), ("Wisuda", "graduationcap"), ("Catatan", "notion"), ("Kuis", "quizlet")]},
    {"id": "03", "name": "Website", "price": 250000, "durasi": "3-7 Hari", "desc": "Company Profile, Toko Online, Sistem Informasi", "icons": [("HTML5", "html5"), ("CSS", "css3"), ("React", "react"), ("Laravel", "laravel")]},
    {"id": "04", "name": "Aplikasi Mobile", "price": 500000, "durasi": "7-14 Hari", "desc": "Android & iOS, Flutter / Kotlin, Full Source Code", "icons": [("Flutter", "flutter"), ("Kotlin", "kotlin"), ("Android", "android"), ("Swift", "swift")]},
    {"id": "05", "name": "AI / Machine Learning", "price": 400000, "durasi": "5-10 Hari", "desc": "Klasifikasi, Prediksi, Chatbot, Computer Vision", "icons": [("Python", "python"), ("TensorFlow", "tensorflow"), ("PyTorch", "pytorch"), ("Scikit", "scikitlearn")]},
    {"id": "06", "name": "Data Science", "price": 300000, "durasi": "3-7 Hari", "desc": "Analisis Data, Visualisasi, Dashboard, Jupyter", "icons": [("Jupyter", "jupyter"), ("R", "r"), ("Pandas", "pandas"), ("Plotly", "plotly")]},
    {"id": "07", "name": "Diagram & Database", "price": 75000, "durasi": "1-2 Hari", "desc": "ERD, DFD, UML, Use Case, Flowchart + Database", "icons": [("ERD", "diagramsdotnet"), ("Draw.io", "diagramsdotnet"), ("MySQL", "mysql"), ("PostgreSQL", "postgresql")]},
    {"id": "08", "name": "UI/UX Design", "price": 200000, "durasi": "2-5 Hari", "desc": "Design Figma, Prototype Interaktif, Siap Handoff", "icons": [("Figma", "figma"), ("Adobe XD", "adobexd"), ("Illustrator", "adobeillustrator"), ("Sketch", "sketch")]},
    {"id": "09", "name": "Internet of Things (IoT)", "price": 450000, "durasi": "7-14 Hari", "desc": "Arduino, ESP32, Raspberry Pi, Monitoring Sensor", "icons": [("Arduino", "arduino"), ("Raspberry", "raspberrypi"), ("ESP32", "espressif"), ("Node", "nodered")]},
    {"id": "10", "name": "Game Development", "price": 500000, "durasi": "7-21 Hari", "desc": "Game 2D/3D, Unity, Godot, Siap Build APK", "icons": [("Unity", "unity"), ("Unreal", "unrealengine"), ("Godot", "godotengine"), ("Gamepad", "itchdotio")]},
    {"id": "11", "name": "Aplikasi Desktop", "price": 350000, "durasi": "5-10 Hari", "desc": "Kasir, Inventori, Absensi, Java / C# / Python", "icons": [("C#", "csharp"), ("Java", "openjdk"), ("Python", "python"), ("C++", "cplusplus")]},
    {"id": "12", "name": "Perbaikan & Take Over Project", "price": 100000, "durasi": "1-5 Hari", "desc": "Fix Bug, Lanjutin Project Orang, Tambah Fitur", "icons": [("Fix", "wrench"), ("Bug", "bugzilla"), ("Code", "visualstudiocode"), ("Refresh", "refresh")]},
    {"id": "13", "name": "Hosting & Deployment", "price": 100000, "durasi": "1 Hari", "desc": "Deploy ke Vercel, Streamlit, VPS, Setting Domain", "icons": [("Cloud", "cloudflare"), ("Database", "supabase"), ("NGINX", "nginx"), ("Docker", "docker")]},
    {"id": "14", "name": "Layanan Lainnya", "price": 50000, "durasi": "Chat aja", "desc": "Chat aja dulu, semua tugas IT bisa kami bantu", "icons": [("Layers", "layers"), ("Settings", "settings"), ("Puzzle", "puzzle"), ("More", "more")]},
]

def rupiah(n):
    return f"Rp {n:,}".replace(",", ".")

def wa_link(pesan):
    return f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(pesan)}"

# ================= CSS MEWAH - GOLD + ROYAL BLUE + GLASS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700&display=swap');

/* Background utama - Biru dongker mewah dengan cahaya */
.stApp {
    background: radial-gradient(ellipse at top, #1E40FF 0%, #0B2CFF 30%, #020A4A 100%);
    background-attachment: fixed;
    font-family: 'Poppins', sans-serif;
}
header, footer { visibility: hidden; }
.block-container { max-width: 1120px; padding-top: 8px; padding-bottom: 40px; }

/* HERO */
.hero-badge { text-align:center; margin-bottom:10px; }
.hero-badge span { background: linear-gradient(135deg, #FFD700, #FFAA00); color:#1A1000; font-size:12px; font-weight:800; letter-spacing:2px; padding:6px 18px; border-radius:50px; box-shadow:0 5px 20px rgba(255,215,0,0.5); }
.hero-title { text-align:center; color:white; font-size:40px; font-weight:900; line-height:1.05; text-shadow:0 5px 25px rgba(0,0,0,0.5); }
.hero-title em { font-family:'Playfair Display', serif; font-style:italic; background: linear-gradient(135deg, #FFE27A, #FFD700, #FFAA00); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero-sub { text-align:center; color:#FFE27A; font-size:30px; font-weight:800; letter-spacing:1px; margin-top:4px; text-shadow:0 3px 15px rgba(255,215,0,0.4); }
.pill { display:inline-block; background: rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.35); backdrop-filter:blur(12px); color:white; padding:9px 20px; border-radius:50px; font-weight:600; font-size:13px; margin:4px; box-shadow:0 4px 15px rgba(0,0,0,0.2); }

/* STATS - Kaca */
.stat-box { background: linear-gradient(135deg, rgba(255,255,255,0.22), rgba(255,255,255,0.08)); border:1px solid rgba(255,255,255,0.35); border-radius:20px; padding:18px 10px; text-align:center; color:white; backdrop-filter:blur(15px); box-shadow:0 10px 25px rgba(0,0,0,0.2); }
.stat-num { font-size:26px; font-weight:900; background: linear-gradient(135deg, #FFE27A, #FFD700); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.stat-label { font-size:12px; opacity:0.9; font-weight:500; }

/* KALKULATOR - Putih mewah + border emas */
.calc-box { background: linear-gradient(180deg, #FFFFFF 0%, #FFF8E1 100%); border:2px solid #FFD700; border-radius:24px; padding:22px; margin:18px 0; box-shadow:0 20px 40px rgba(0,0,0,0.35), 0 0 0 5px rgba(255,215,0,0.15); position:relative; overflow:hidden; }
.calc-box::before { content:''; position:absolute; top:0; left:0; right:0; height:5px; background: linear-gradient(90deg, #FFD700, #FFAA00, #FFD700); }
.price-big { font-size:36px; font-weight:900; color:#0B2CFF; line-height:1; }

/* KARTU - Putih premium */
.card { background: #FFFFFF; border-radius:22px; overflow:hidden; box-shadow:0 12px 30px rgba(0,0,0,0.25); margin-bottom:6px; border:1px solid rgba(255,215,0,0.0); transition: all 0.3s ease; }
.card:hover { transform: translateY(-4px); box-shadow:0 20px 40px rgba(0,0,0,0.35); border:1px solid #FFD700; }
.card-head { background: linear-gradient(135deg, #2B4BFF 0%, #0B2CFF 60%, #001A8A 100%); color:white; padding:15px 16px; display:flex; align-items:center; gap:12px; }
.card-num { background: linear-gradient(135deg, #FFE27A, #FFD700); color:#1A1000; font-weight:900; width:48px; height:48px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:19px; flex-shrink:0; box-shadow:0 4px 12px rgba(0,0,0,0.3); }
.card-name { font-weight:700; font-size:18px; line-height:1.2; }
.card-body { padding:16px 14px 6px; display:flex; justify-content:space-between; align-items:flex-end; }
.icon-box { text-align:center; width:58px; }
.icon-box img { width:46px; height:46px; background: linear-gradient(135deg, #FFF5F5, #FFE8E8); border-radius:15px; padding:8px; object-fit:contain; border:1px solid #FFE0E0; }
.icon-box span { font-size:11px; color:#444; font-weight:600; display:block; margin-top:4px; }
.card-price { padding:0 14px 4px; font-size:13px; color:#666; }

/* TOMBOL Streamlit - Dibikin mewah semua */
div[data-testid="stLinkButton"] > a, div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #0B2CFF, #1E40FF) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 20px rgba(11,44,255,0.4) !important;
    padding: 10px 20px !important;
}
div[data-testid="stLinkButton"] > a:hover { background: linear-gradient(135deg, #FFD700, #FFAA00) !important; color: #1A1000 !important; transform: translateY(-2px); }

/* Expander */
div[data-testid="stExpander"] { background: #F8FAFF; border-radius:14px; border:1px solid #E0E7FF; }
div[data-testid="stExpander"] summary { font-weight:600; color:#0B2CFF; }

/* Input */
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius:14px !important; font-family:'Poppins',sans-serif; }

/* Testimoni */
.testi { background: white; padding:18px; border-radius:20px; box-shadow:0 10px 25px rgba(0,0,0,0.2); border-top:4px solid #FFD700; height:100%; }
.cta-box { background: linear-gradient(135deg, rgba(255,255,255,0.20), rgba(255,255,255,0.05)); border:1px solid rgba(255,215,0,0.5); border-radius:26px; padding:30px 20px; text-align:center; backdrop-filter:blur(15px); box-shadow:0 20px 40px rgba(0,0,0,0.3); }
</style>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown('<div class="hero-badge"><span>✦ PREMIUM SERVICE ✦</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Solusi Tugas &<br><em>Project IT Kamu!</em></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Layanan Untuk Mahasiswa</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin:14px 0 6px;"><span class="pill">✨ Beban Tugas Jadi Lebih Ringan</span><span class="pill">🛡️ Aman & Profesional</span></div>', unsafe_allow_html=True)

# ================= STATS =================
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="stat-box"><div class="stat-num">100+</div><div class="stat-label">Project Selesai</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-box"><div class="stat-num">Garansi</div><div class="stat-label">Revisi Sampai ACC</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-box"><div class="stat-num">DP 50%</div><div class="stat-label">Bisa DP Dulu</div></div>', unsafe_allow_html=True)

# ================= KALKULATOR =================
st.markdown('<div class="calc-box"><h3 style="margin:0; color:#001A8A; font-size:20px;">🧮 Kalkulator Harga Otomatis</h3><p style="color:#666; margin:6px 0 0; font-size:13px;">Cek estimasi harga & durasi, langsung order ke WA.</p></div>', unsafe_allow_html=True)
colA, colB = st.columns(2)
with colA:
    pilih = st.selectbox("Mau bikin apa?", [s["name"] for s in SERVICES])
with colB:
    deadline = st.selectbox("Deadline kamu?", ["Normal (Sesuai Estimasi)", "Buruan / Urgent (+50%)", "Santai / 2 Minggu (-20%)"])
svc = next(s for s in SERVICES if s["name"] == pilih)
base = svc["price"]
if "Urgent" in deadline: total = int(base * 1.5)
elif "Santai" in deadline: total = int(base * 0.8)
else: total = base
st.markdown(f'<div style="text-align:center; background:#EFF6FF; border:1px dashed #0B2CFF; padding:18px; border-radius:18px; margin:10px 0;"><span style="color:#666; font-size:13px;">Estimasi untuk <b>{pilih}</b> • Durasi: {svc["durasi"]}</span><div class="price-big">{rupiah(total)}</div><span style="color:#666; font-size:12px;">Harga mulai dari • Bisa nego sesuai kesulitan</span></div>', unsafe_allow_html=True)
st.link_button(f"✅ Order {pilih} - {rupiah(total)} via WA", wa_link(f"Halo kak, saya mau order {pilih}. Deadline: {deadline}. Estimasi harga: {rupiah(total)}. Boleh info detailnya?"), use_container_width=True)

# ================= SEARCH + GRID =================
st.markdown('<h3 style="color:white; text-align:center; margin-top:22px; font-size:24px;">✦ Semua Layanan ✦</h3>', unsafe_allow_html=True)
cari = st.text_input("Cari layanan...", placeholder="🔍 Contoh: website, skripsi, game...", label_visibility="collapsed")
filtered = [s for s in SERVICES if cari.lower() in s["name"].lower()] if cari else SERVICES
if not filtered:
    st.warning("Gak ketemu, coba kata lain atau chat WA aja langsung.")
else:
    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i+j < len(filtered):
                s = filtered[i+j]
                icons_html = "".join([f'<div class="icon-box"><img src="https://cdn.simpleicons.org/{icon}/0B2CFF"><span>{label}</span></div>' for label, icon in s["icons"]])
                with col:
                    st.markdown(f"""
                    <div class="card">
                      <div class="card-head"><div class="card-num">{s["id"]}</div><div class="card-name">{s["name"]}</div></div>
                      <div class="card-body"><div style="display:flex; gap:6px;">{icons_html}</div><div style="color:#2563EB; font-weight:800; font-style:italic;">dll.</div></div>
                      <div class="card-price">Mulai <b style="color:#0B2CFF; font-size:15px;">{rupiah(s["price"])}</b> • {s["durasi"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.link_button(f"💬 Chat WA - {s['name']}", wa_link(f"Halo kak, mau tanya {s['name']}, harga {rupiah(s['price'])}"), use_container_width=True)
                    with st.expander(f"Lihat Harga & Detail"):
                        st.write(f"**Harga mulai:** {rupiah(s['price'])}")
                        st.write(f"**Durasi:** {s['durasi']}")
                        st.write(f"**Termasuk:** {s['desc']}")
                        st.write("**Garansi:** Revisi 2x gratis, Full source code, Bimbingan sampai paham")
                        st.link_button("Order Sekarang →", wa_link(f"Halo kak, mau order {s['name']}"), use_container_width=True)

# ================= TESTIMONI =================
st.markdown('<h3 style="color:white; text-align:center; margin-top:22px;">⭐ Kata Mereka Yang Udah Order</h3>', unsafe_allow_html=True)
t1, t2, t3 = st.columns(3)
with t1: st.markdown('<div class="testi">⭐⭐⭐⭐⭐<br><b>"Websiteku ACC langsung!"</b><br><span style="color:#666; font-size:13px;">- Rina, Mhs. Sistem Informasi</span></div>', unsafe_allow_html=True)
with t2: st.markdown('<div class="testi">⭐⭐⭐⭐⭐<br><b>"Skripsi dibantu sampai bab 5, aman."</b><br><span style="color:#666; font-size:13px;">- Dimas, Mhs. Teknik Informatika</span></div>', unsafe_allow_html=True)
with t3: st.markdown('<div class="testi">⭐⭐⭐⭐⭐<br><b>"Bug-nya dibenerin cepet banget."</b><br><span style="color:#666; font-size:13px;">- Sari, Mhs. Ilmu Komputer</span></div>', unsafe_allow_html=True)

# ================= FAQ =================
st.markdown('<h3 style="color:white; text-align:center; margin-top:22px;">❓ Tanya Jawab</h3>', unsafe_allow_html=True)
with st.expander("Apakah aman? Data saya bocor gak?"): st.write("Aman 100%. Data tugas & identitas kamu tidak kami sebar.")
with st.expander("Bisa DP dulu?"): st.write("Bisa banget. DP 50%, pelunasan setelah project selesai & kamu cek hasilnya.")
with st.expander("Kalau revisi, bayar lagi?"): st.write("Enggak. Revisi 2x gratis sampai ACC dosen, selama masih sesuai brief awal.")
with st.expander("Berapa lama pengerjaannya?"): st.write("Tugas kuliah 1-3 hari, Website 3-7 hari, Mobile / AI 7-14 hari. Kalau urgent bisa dipercepat.")

# ================= CTA AKHIR =================
st.markdown(f"""
<div class="cta-box">
  <div style="color:#FFE27A; font-size:32px; font-weight:900; line-height:1.2;">Konsultasi Gratis<br>Sekarang</div>
  <p style="color:white; margin:12px 0; font-size:14px;">Ceritakan kebutuhan tugas atau project IT kamu, kami bantu carikan solusinya.</p>
</div>
""", unsafe_allow_html=True)
st.link_button("💬 Chat via WhatsApp - GRATIS Konsultasi", wa_link("Halo kak, mau konsultasi gratis tugas IT"), use_container_width=True)
st.markdown('<p style="text-align:center; color:rgba(255,255,255,0.8); font-size:12px; margin-top:10px;">Fast respon • Online setiap hari • Privasi terjaga</p>', unsafe_allow_html=True)
