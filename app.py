import streamlit as st
import json
import urllib.parse

# ===== CONFIG =====
st.set_page_config(page_title="Solusi Tugas & Project IT Kamu!", page_icon="💻", layout="wide")
WA_NUMBER = "6289501857938"  # <-- GANTI NOMOR LU DISINI KING

# ===== DATA (dari JSON) =====
DATA = {
  "services": [
    {"id": "01", "name": "Laporan & Skripsi", "price": 150000, "durasi": "3-7 Hari", "desc": "Bab 1-5, Revisi sampai ACC, Cek Turnitin", "icons": [("Word", "microsoftword"), ("PDF", "adobeacrobatreader"), ("LaTeX", "latex"), ("Docs", "googledocs")]},
    {"id": "02", "name": "Tugas Kuliah & UTS/UAS", "price": 50000, "durasi": "1-3 Hari", "desc": "Semua matkul IT & Non-IT, Dijamin tepat waktu", "icons": [("Buku", "bookstack"), ("Wisuda", "graduationcap"), ("Catatan", "notion"), ("Kuis", "quizlet")]},
    {"id": "03", "name": "Website", "price": 250000, "durasi": "3-7 Hari", "desc": "Company Profile, Toko Online, Sistem Informasi", "icons": [("HTML5", "html5"), ("CSS", "css"), ("React", "react"), ("Laravel", "laravel")]},
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
}

def rupiah(n):
    return f"Rp {n:,}".replace(",", ".")

def wa_link(pesan):
    return f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(pesan)}"

# ===== CSS MEWAH =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
.stApp { background: linear-gradient(180deg, #0B2CFF 0%, #001A8A 100%); font-family: 'Poppins', sans-serif; }
header, footer { visibility: hidden; }
.block-container { max-width: 1100px; padding-top: 10px; }
.hero-title { text-align: center; color: white; font-size: 38px; font-weight: 800; line-height: 1.1; text-shadow: 0 4px 20px rgba(0,0,0,0.3); }
.hero-sub { text-align: center; color: #FFE27A; font-size: 28px; font-weight: 800; margin-top: 5px; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }
.pill { display: inline-block; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.4); color: white; padding: 8px 20px; border-radius: 50px; font-weight: 600; margin: 5px; backdrop-filter: blur(10px); }
.card { background: white; border-radius: 22px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-bottom: 18px; transition: 0.3s; }
.card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
.card-head { background: #2563EB; color: white; padding: 14px 16px; display: flex; align-items: center; gap: 12px; }
.card-num { background: #FFE27A; color: #001A8A; font-weight: 800; width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; }
.card-name { font-weight: 700; font-size: 19px; line-height: 1.2; }
.card-body { padding: 14px; display: flex; justify-content: space-between; align-items: flex-end; gap: 8px; }
.icon-box { text-align: center; width: 58px; }
.icon-box img { width: 44px; height: 44px; background: #FCE7F3; border-radius: 14px; padding: 7px; object-fit: contain; }
.icon-box span { font-size: 11px; color: #333; font-weight: 500; display: block; margin-top: 3px; }
.calc-box { background: rgba(255,255,255,0.95); border-radius: 22px; padding: 22px; margin: 18px 0; box-shadow: 0 15px 35px rgba(0,0,0,0.25); }
.price-big { font-size: 32px; font-weight: 800; color: #0B2CFF; }
.stat-box { background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 18px; padding: 16px; text-align: center; color: white; }
.stat-num { font-size: 26px; font-weight: 800; color: #FFE27A; }
.floating-wa { position: fixed; bottom: 20px; right: 20px; z-index: 9999; background: #25D366; color: white !important; padding: 14px 20px; border-radius: 50px; font-weight: 700; text-decoration: none; box-shadow: 0 10px 25px rgba(0,0,0,0.4); font-family: 'Poppins', sans-serif; }
.floating-wa:hover { background: #1EBE5A; }
div[data-testid="stExpander"] { background: #F8FAFF; border-radius: 12px; border: none; }
</style>
""", unsafe_allow_html=True)

# ===== FLOATING WA =====
st.markdown(f'<a class="floating-wa" href="{wa_link("Halo kak, mau konsultasi tugas IT")} " target="_blank">💬 Chat WA</a>', unsafe_allow_html=True)

# ===== HERO =====
st.markdown('<div class="hero-title">Solusi Tugas & Project IT Kamu!</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Layanan Untuk Mahasiswa</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin:12px 0;"><span class="pill">✨ Beban Tugas Jadi Lebih Ringan</span><span class="pill">🛡️ Aman & Profesional</span></div>', unsafe_allow_html=True)

# ===== STATS =====
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="stat-box"><div class="stat-num">100+</div>Project Selesai</div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-box"><div class="stat-num">Garansi</div>Revisi Sampai ACC</div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-box"><div class="stat-num">DP 50%</div>Bisa Dicicil / DP Dulu</div>', unsafe_allow_html=True)

# ===== KALKULATOR HARGA - IDE JENIUS =====
st.markdown('<div class="calc-box"><h3 style="margin:0; color:#001A8A;">🧮 Kalkulator Harga Otomatis</h3><p style="color:#666; margin:5px 0 15px;">Cek estimasi harga & durasi, langsung order ke WA.</p></div>', unsafe_allow_html=True)
# Pakai container biar rapi di dalam calc
colA, colB = st.columns(2)
with colA:
    pilih = st.selectbox("Mau bikin apa?", [s["name"] for s in DATA["services"]])
with colB:
    deadline = st.selectbox("Deadline kamu?", ["Normal (Sesuai Estimasi)", "Buruan / Urgent (+50%)", "Santai / 2 Minggu (-20%)"])
svc = next(s for s in DATA["services"] if s["name"] == pilih)
base = svc["price"]
if "Urgent" in deadline: total = int(base * 1.5)
elif "Santai" in deadline: total = int(base * 0.8)
else: total = base
st.markdown(f'<div style="text-align:center; background:#EFF6FF; padding:16px; border-radius:16px; margin:10px 0;"><span style="color:#666;">Estimasi untuk <b>{pilih}</b> • Durasi: {svc["durasi"]}</span><div class="price-big">{rupiah(total)}</div><span style="color:#666; font-size:13px;">Harga mulai dari • Bisa nego sesuai kesulitan</span></div>', unsafe_allow_html=True)
st.link_button(f"✅ Order {pilih} - {rupiah(total)} via WA", wa_link(f"Halo kak, saya mau order {pilih}. Deadline: {deadline}. Estimasi harga: {rupiah(total)}. Boleh info detailnya?"), use_container_width=True)

# ===== SEARCH =====
st.markdown('<h3 style="color:white; text-align:center; margin-top:20px;">Semua Layanan</h3>', unsafe_allow_html=True)
cari = st.text_input("🔍 Cari layanan...", placeholder="Contoh: website, skripsi, game...", label_visibility="collapsed")
filtered = [s for s in DATA["services"] if cari.lower() in s["name"].lower()] if cari else DATA["services"]
if not filtered:
    st.warning("Gak ketemu, coba kata lain atau chat WA aja langsung.")
else:
    # Grid 2 kolom
    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i+j < len(filtered):
                s = filtered[i+j]
                icons_html = "".join([f'<div class="icon-box"><img src="https://cdn.simpleicons.org/{icon}"><span>{label}</span></div>' for label, icon in s["icons"]])
                with col:
                    st.markdown(f"""
                    <div class="card">
                      <div class="card-head"><div class="card-num">{s["id"]}</div><div class="card-name">{s["name"]}</div></div>
                      <div class="card-body"><div style="display:flex; gap:6px;">{icons_html}</div><div style="color:#2563EB; font-weight:800; font-style:italic;">dll.</div></div>
                      <div style="padding:0 14px 14px; display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:13px; color:#666;">Mulai <b style="color:#0B2CFF; font-size:15px;">{rupiah(s["price"])}</b> • {s["durasi"]}</span>
                        <a href="{wa_link(f'Halo kak, mau tanya {s["name"]}, harga {rupiah(s["price"])}')}" target="_blank" style="background:#0B2CFF; color:white; padding:7px 14px; border-radius:20px; text-decoration:none; font-size:13px; font-weight:600;">Chat WA →</a>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander(f"Lihat Harga & Detail {s['name']}"):
                        st.write(f"**Harga mulai:** {rupiah(s['price'])}")
                        st.write(f"**Durasi:** {s['durasi']}")
                        st.write(f"**Termasuk:** {s['desc']}")
                        st.write("**Garansi:** Revisi 2x gratis, Full source code, Bimbingan sampai paham")
                        st.link_button("Order Sekarang", wa_link(f"Halo kak, mau order {s['name']}"))

# ===== TESTIMONI =====
st.markdown('<h3 style="color:white; text-align:center; margin-top:10px;">Kata Mereka Yang Udah Order ⭐</h3>', unsafe_allow_html=True)
t1, t2, t3 = st.columns(3)
with t1: st.markdown('<div style="background:white; padding:16px; border-radius:18px;">⭐⭐⭐⭐⭐<br><b>"Websiteku ACC langsung!"</b><br><span style="color:#666; font-size:13px;">- Rina, Mhs. Sistem Informasi</span></div>', unsafe_allow_html=True)
with t2: st.markdown('<div style="background:white; padding:16px; border-radius:18px;">⭐⭐⭐⭐⭐<br><b>"Skripsi dibantu sampai bab 5, aman."</b><br><span style="color:#666; font-size:13px;">- Dimas, Mhs. Teknik Informatika</span></div>', unsafe_allow_html=True)
with t3: st.markdown('<div style="background:white; padding:16px; border-radius:18px;">⭐⭐⭐⭐⭐<br><b>"Bug-nya dibenerin cepet banget."</b><br><span style="color:#666; font-size:13px;">- Sari, Mhs. Ilmu Komputer</span></div>', unsafe_allow_html=True)

# ===== FAQ =====
st.markdown('<h3 style="color:white; text-align:center; margin-top:20px;">Tanya Jawab</h3>', unsafe_allow_html=True)
with st.expander("Apakah aman? Data saya bocor gak?"): st.write("Aman 100%. Data tugas & identitas kamu tidak kami sebar. Project hanya untuk referensi belajar kamu.")
with st.expander("Bisa DP dulu?"): st.write("Bisa banget. DP 50%, pelunasan setelah project selesai & kamu cek hasilnya.")
with st.expander("Kalau revisi, bayar lagi?"): st.write("Enggak. Revisi 2x gratis sampai ACC dosen, selama masih sesuai brief awal.")
with st.expander("Berapa lama pengerjaannya?"): st.write("Tergantung kesulitan. Tugas kuliah 1-3 hari, Website 3-7 hari, Mobile / AI 7-14 hari. Kalau urgent bisa dipercepat.")

# ===== CTA AKHIR =====
st.markdown(f"""
<div style="background: rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.3); border-radius:24px; padding:28px; text-align:center; margin-top:20px; backdrop-filter: blur(10px);">
  <div style="color:#FFE27A; font-size:32px; font-weight:800; line-height:1.2;">Konsultasi Gratis<br>Sekarang</div>
  <p style="color:white; margin:12px 0;">Ceritakan kebutuhan tugas atau project IT kamu, kami bantu carikan solusinya.</p>
  <a href="{wa_link('Halo kak, mau konsultasi gratis tugas IT')}" target="_blank" style="display:inline-block; background:#25D366; color:white; padding:14px 28px; border-radius:50px; font-weight:700; text-decoration:none; font-size:16px; box-shadow:0 10px 20px rgba(0,0,0,0.3);">💬 Chat via WhatsApp</a>
  <p style="color:rgba(255,255,255,0.8); font-size:12px; margin-top:12px;">Fast respon • Online setiap hari • Privasi terjaga</p>
</div>
""", unsafe_allow_html=True)
