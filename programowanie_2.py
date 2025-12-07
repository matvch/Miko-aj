import streamlit as st
import base64

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="Kreator Mikołaja", page_icon="🎅")

st.title("🎅 Twój Personalizowany Mikołaj")
st.write("Dostosuj kolory w panelu bocznym i stwórz własną wersję Świętego!")

# --- 2. Definicja kształtu Mikołaja (SVG) ---
# To ten sam szablon co wcześniej, z poprawioną brodą i uśmiechem
SANTA_SVG_FINAL = """
<svg width="400" height="500" viewBox="0 0 200 250" xmlns="http://www.w3.org/2000/svg">
    
    <rect x="60" y="200" width="30" height="20" fill="#333333"/>
    <rect x="110" y="200" width="30" height="20" fill="#333333"/>

    <rect x="50" y="100" width="100" height="100" rx="10" fill="{CLOTHING_COLOR}"/>
    
    <rect x="25" y="110" width="30" height="20" rx="5" fill="{CLOTHING_COLOR}" transform="rotate(-15 40 120)"/>
    <rect x="145" y="110" width="30" height="20" rx="5" fill="{CLOTHING_COLOR}" transform="rotate(15 160 120)"/>

    <rect x="95" y="100" width="10" height="100" fill="{FUR_COLOR}"/> 

    <rect x="50" y="140" width="100" height="15" fill="black"/>
    <rect x="90" y="142" width="20" height="11" fill="gold"/>
    
    <circle cx="28" cy="130" r="10" fill="{GLOVE_COLOR}"/>
    <circle cx="172" cy="130" r="10" fill="{GLOVE_COLOR}"/>

    <circle cx="100" cy="85" r="30" fill="{SKIN_COLOR}"/>

    <path d="M 55 90 C 50 120, 150 120, 145 90 L 100 130 Z" fill="{BEARD_COLOR}"/>
    <circle cx="100" cy="85" r="45" fill="{BEARD_COLOR}"/> 
    
    <circle cx="85" cy="80" r="3" fill="black"/>
    <circle cx="115" cy="80" r="3" fill="black"/>

    <circle cx="100" cy="92" r="7" fill="{NOSE_COLOR}"/>

    <path d="M 85 108 Q 100 125 115 108" stroke="black" stroke-width="3" fill="none" stroke-linecap="round"/>

    <path d="M 60 40 L 140 40 L 100 0 Z" fill="{CLOTHING_COLOR}"/>
    <rect x="50" y="30" width="100" height="10" fill="{FUR_COLOR}"/> 
    <circle cx="100" cy="0" r="10" fill="{FUR_COLOR}"/> 
</svg>
"""

# --- 3. Panel boczny (Sidebar) z kontrolkami ---
with st.sidebar:
    st.header("🎨 Edycja Wyglądu")
    
    st.subheader("Ciało")
    skin_color = st.color_picker("Kolor Skóry", "#F0C9B1")
    nose_color = st.color_picker("Kolor Nosa", "#FF9999")
    beard_color = st.color_picker("Kolor Brody", "#EEEEEE")
    
    st.subheader("Ubranie")
    clothing_color = st.color_picker("Kolor Stroju", "#CC0000")
    fur_color = st.color_picker("Kolor Futra/Wykończeń", "#FFFFFF")
    glove_color = st.color_picker("Rękawiczki", "#333333")

# --- 4. Generowanie SVG ---
# Podmieniamy placeholdery na kolory wybrane w sidebarze
svg_code = SANTA_SVG_FINAL.format(
    SKIN_COLOR=skin_color,
    NOSE_COLOR=nose_color,
    CLOTHING_COLOR=clothing_color,
    FUR_COLOR=fur_color,
    GLOVE_COLOR=glove_color,
    BEARD_COLOR=beard_color
)

# --- 5. Wyświetlanie ---
# Wyświetlamy obrazek na środku kolumny
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Renderujemy SVG jako HTML, bo st.image czasami ma problem z raw stringami SVG
    st.markdown(f'<div style="text-align: center">{svg_code}</div>', unsafe_allow_html=True)

# --- 6. Przycisk pobierania (Bonus) ---
# Konwersja SVG do base64, aby można było go pobrać
b64 = base64.b64encode(svg_code.encode('utf-8')).decode("utf-8")
href = f'<a href="data:image/svg+xml;base64,{b64}" download="moj_mikolaj.svg">📥 Pobierz Mikołaja (SVG)</a>'

st.markdown("---")
st.markdown(href, unsafe_allow_html=True)
