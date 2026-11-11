import html
import json
from pathlib import Path
from urllib.parse import quote

import streamlit as st

BASE_DIR = Path(__file__).parent

# ---------------------------------------------------------------- konfigurasi
WA_NUMBER = "6281234567890"  # GANTI dengan nomor WhatsApp kamu (format 62xxxxxxxxxx)
WA_MESSAGE = "Halo, saya ingin konsultasi gratis tentang tugas / project IT."

DEVICON = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{n}/{n}-original.svg"
SIMPLE = "https://cdn.simpleicons.org/{n}"
LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static/icons/{n}.svg"

# nama icon di JSON -> (sumber, slug)
ICON_MAP = {
    "Word": ("lucide", "file-text"),
    "PDF": ("simple", "adobeacrobatreader"),
    "LaTeX": ("dev", "latex"),
    "Docs": ("simple", "googledocs"),
    "Buku": ("lucide", "book-open"),
    "Topi Wisuda": ("lucide", "graduation-cap"),
    "Catatan": ("lucide", "notebook-pen"),
    "Kuis": ("lucide", "clipboard-check"),
    "HTML5": ("dev", "html5"),
    "CSS": ("dev", "css3"),
    "Vue": ("dev", "vuejs"),
    "React": ("dev", "react"),
    "Laravel": ("dev", "laravel"),
    "Flutter": ("dev", "flutter"),
    "Kotlin": ("dev", "kotlin"),
    "Android": ("dev", "android"),
    "Swift": ("dev", "swift"),
    "Python": ("dev", "python"),
    "TensorFlow": ("dev", "tensorflow"),
    "PyTorch": ("dev", "pytorch"),
    "Scikit-learn": ("dev", "scikitlearn"),
    "Jupyter": ("dev", "jupyter"),
    "R": ("dev", "r"),
    "Pandas": ("dev", "pandas"),
    "Grafik": ("lucide", "chart-column"),
    "ERD": ("lucide", "network"),
    "Draw.io": ("simple", "diagramsdotnet"),
    "MySQL": ("dev", "mysql"),
    "PostgreSQL": ("dev", "postgresql"),
    "Figma": ("dev", "figma"),
    "Adobe XD": ("dev", "xd"),
    "Illustrator": ("dev", "illustrator"),
    "Sketch": ("dev", "sketch"),
    "Arduino": ("dev", "arduino"),
    "Raspberry Pi": ("dev", "raspberrypi"),
    "ESP32": ("simple", "espressif"),
    "Node": ("dev", "nodejs"),
    "Unity": ("dev", "unity"),
    "Unreal": ("dev", "unrealengine"),
    "Godot": ("dev", "godot"),
    "Gamepad": ("lucide", "gamepad-2"),
    "C#": ("dev", "csharp"),
    "Java": ("dev", "java"),
    "C++": ("dev", "cplusplus"),
    "Wrench": ("lucide", "wrench"),
    "Bug": ("lucide", "bug"),
    "Code": ("lucide", "code"),
    "Refresh": ("lucide", "refresh-cw"),
    "Cloud": ("lucide", "cloud"),
    "Database": ("lucide", "database"),
    "NGINX": ("dev", "nginx"),
    "Docker": ("dev", "docker"),
    "Layers": ("lucide", "layers"),
    "Settings": ("lucide", "settings"),
    "Puzzle": ("lucide", "puzzle"),
    "More": ("lucide", "ellipsis"),
}


def icon_url(name: str) -> tuple[str, bool]:
    """Kembalikan (url, is_generic). Icon generik (Lucide) diberi warna biru lewat CSS."""
    kind, slug = ICON_MAP.get(name, ("lucide", "box"))
    if kind == "dev":
        return DEVICON.format(n=slug), False
    if kind == "simple":
        return SIMPLE.format(n=slug), False
    return LUCIDE.format(n=slug), True


# ------------------------------------------------------------------ halaman
st.set_page_config(
    page_title="Solusi Tugas & Project IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

data = json.loads((BASE_DIR / "data.json").read_text(encoding="utf-8"))
css = (BASE_DIR / "style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def render_icons(icons: list[str]) -> str:
    parts = []
    for name in icons:
        url, generic = icon_url(name)
        cls = "icon generic" if generic else "icon"
        parts.append(
            f'<div class="{cls}" title="{esc(name)}">'
            f'<img src="{url}" alt="{esc(name)}" loading="lazy">'
            f"<span>{esc(name)}</span></div>"
        )
    parts.append('<div class="dll">dll.</div>')
    return "".join(parts)


def render_card(service: dict, index: int) -> str:
    return (
        f'<article class="card" style="--i:{index}">'
        f'<div class="card-head"><span class="num">{esc(service["id"])}</span>'
        f'<h3>{esc(service["name"])}</h3></div>'
        f'<div class="card-body">{render_icons(service["icons"])}</div>'
        f"</article>"
    )


badges = "".join(f'<span class="pill">{esc(b)}</span>' for b in data["badges"])
cards = "".join(render_card(s, i) for i, s in enumerate(data["services"]))
wa_link = f"https://wa.me/{WA_NUMBER}?text={quote(WA_MESSAGE)}"

# HTML sengaja dirangkai tanpa indentasi / baris kosong agar tidak dibaca sebagai code block.
page = (
    '<div class="page">'
    '<header class="hero">'
    f'<h1 class="hero-title">{esc(data["title"])}</h1>'
    "</header>"
    '<section class="panel">'
    f'<h2 class="subtitle">{esc(data["subtitle"])}</h2>'
    f'<div class="badges">{badges}</div>'
    f'<div class="grid">{cards}</div>'
    "</section>"
    '<section class="cta">'
    '<h2 class="cta-title">Konsultasi Gratis Sekarang</h2>'
    '<p class="cta-text">Ceritakan kebutuhan tugas atau project IT kamu, kami bantu carikan solusinya.</p>'
    f'<a class="wa-btn" href="{wa_link}" target="_blank" rel="noopener">'
    '<img class="wa-ico" src="https://cdn.simpleicons.org/whatsapp/ffffff" alt="WhatsApp" width="26" height="26">'
    "<span>Chat via WhatsApp</span></a>"
    "</section>"
    '<footer class="foot">Aman &bull; Profesional &bull; Tepat Waktu</footer>'
    "</div>"
)

st.markdown(page, unsafe_allow_html=True)
