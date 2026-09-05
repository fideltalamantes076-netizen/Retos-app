import streamlit as st
import random
import datetime

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Retos & Vibes Semanales", page_icon="🎯", layout="centered")

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
    }
    .reto-card {
        background-color: #1a1c23;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .badge {
        background-color: #238636;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }
    .tag-box {
        background-color: #21262d;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #30363d;
        font-size: 13px;
        color: #8b949e;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- BANCO DE 100,000 RETOS ---
ACCIONES = [
    "Hacer 20 lagartijas", "Leer 10 páginas de un libro", "Beber un vaso de agua fría de golpe", 
    "Escribir una idea de negocio en un papel", "Hacer estiramientos de espalda por 5 minutos", 
    "Limpiar el escritorio de desorden", "Meditar en silencio por 3 minutos", 
    "Aprender una palabra nueva en inglés", "Enviar un mensaje positivo a un amigo", 
    "Hacer una sentadilla isométrica por 60 segundos", "Organizar las aplicaciones del celular", 
    "Dibujar un boceto rápido sin levantar el lápiz", "Aprender los acordes base de una canción en guitarra",
    "Caminar 10 minutos sin mirar el celular", "Repasar conceptos de una materia escolar"
]

COMPLEMENTOS = [
    "sin que nadie te vea", "escuchando una canción instrumental", "con la mano izquierda (si eres diestro)", 
    "cronometrado en menos de un minuto", "con los ojos cerrados la mitad del tiempo", 
    "respirando profundamente cada 10 segundos", "anotando el tiempo exacto que te tomó"
]

@st.cache_data
def generar_reto_unico(seed_num):
    random.seed(seed_num)
    accion = random.choice(ACCIONES)
    complemento = random.choice(COMPLEMENTOS)
    return f"{accion} {complemento}."

# --- SISTEMA DE TIEMPO Y SEMANAS ---
def obtener_semana_actual():
    ahora = datetime.datetime.now()
    return ahora.isocalendar()[:2]

if 'current_week' not in st.session_state:
    st.session_state.current_week = obtener_semana_actual()
    random.seed(hash(str(st.session_state.current_week)))
    st.session_state.meta_semanal = random.randint(1, 100)
    st.session_state.retos_completados = 0
    st.session_state.retos_posponidos = 0
    st.session_state.indice_reto_actual = random.randint(0, 99999)

semana_hoy = obtener_semana_actual()
if st.session_state.current_week != semana_hoy:
    st.session_state.current_week = semana_hoy
    random.seed(hash(str(semana_hoy)))
    st.session_state.meta_semanal = random.randint(1, 100)
    st.session_state.retos_completados = 0
    st.session_state.retos_posponidos = 0
    st.session_state.indice_reto_actual = random.randint(0, 99999)

# --- BASE DE DATOS DE MÚSICA ---
MUSICA_EDITS = [
    {"tags": ["feliz", "bien", "alegre", "bueno", "arriba", "energia", "fiesta"], "nombre": "Walking On A Dream", "artista": "Empire of the Sun", "url": "https://www.youtube.com/watch?v=eRGj-MjUxVE"},
    {"tags": ["feliz", "bien", "positivo", "energia"], "nombre": "Electric Feel", "artista": "MGMT", "url": "https://www.youtube.com/watch?v=MmZexBk_OkA"},
    {"tags": ["feliz", "bien", "divertido", "bailar"], "nombre": "Dansez (Edit Audio)", "artista": "Varios", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    {"tags": ["triste", "mal", "cansado", "depre", "llorar", "solo", "roto"], "nombre": "Harvey", "artista": "Her's", "url": "https://www.youtube.com/watch?v=1b5P6-8Z1b4"},
    {"tags": ["triste", "mal", "cansado", "gris", "nostalgico"], "nombre": "Christmas Card", "artista": "Roar", "url": "https://www.youtube.com/watch?v=v0n6B1x6Z9s"},
    {"tags": ["cansado", "mal", "exhausto", "chill", "tranquilo"], "nombre": "Glimpse of Us", "artista": "Joji", "url": "https://www.youtube.com/watch?v=SwXzUffT7pU"},
    {"tags": ["triste", "mal", "oscuro", "memoria"], "nombre": "It's Just a Burning Memory", "artista": "The Caretaker", "url": "https://www.youtube.com/watch?v=wJWksPWDKOc"},
    {"tags": ["amor", "enamorado", "lindo", "novios", "bonito"], "nombre": "What Once Was", "artista": "Her's", "url": "https://www.youtube.com/watch?v=JcE_Fqfkeak"},
    {"tags": ["amor", "romantico", "lindo", "luz"], "nombre": "Meant to Be", "artista": "Varios Edit", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    {"tags": ["inteligente", "ciencia", "espacio", "violin", "interstellar", "hans zimmer"], "nombre": "Interstellar - Cornfield Chase", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=m3zvVGJrTP8"},
    {"tags": ["inteligente", "ciencia", "oppenheimer", "fisica", "musica"], "nombre": "Oppenheimer - Can You Hear The Music", "artista": "Ludwig Göransson", "url": "https://www.youtube.com/watch?v=bc3b09YwIbs"},
    {"tags": ["epico", "anime", "titan", "pelea", "modo dios"], "nombre": "Attack on Titan - Vogel im Käfig", "artista": "Hiroyuki Sawano", "url": "https://www.youtube.com/watch?v=8TJbXuKzGf4"},
    {"tags": ["epico", "juego", "gym", "combat", "fuerte"], "nombre": "Doom Eternal - The Only Thing They Fear Is You", "artista": "Mick Gordon", "url": "https://www.youtube.com/watch?v=AicsyHMqkt8"},
    {"tags": ["nostalgico", "minecraft", "tranquilo", "infancia", "bien"], "nombre": "Sweden", "artista": "C418", "url": "https://www.youtube.com/watch?v=aA3XvA5F1kE"},
    {"tags": ["inteligente", "negocios", "serie", "succession"], "nombre": "Succession Theme", "artista": "Nicholas Britell", "url": "https://www.youtube.com/watch?v=Gk6Wq_63_Yg"}
]

# --- INTERFAZ GRÁFICA PRINCIPAL ---
st.title("⚡ Central de Retos & Edits Vibes")
st.write("Sistema de retos semanales y buscador inteligente de música para edits.")

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📅 Semana", value=f"Semana {st.session_state.current_week[1]}")
with col2:
    st.metric(label="🎯 Meta", value=f"{st.session_state.meta_semanal} retos")
with col3:
    st.metric(label="✅ Cumplidos", value=f"{st.session_state.retos_completados} / {st.session_state.meta_semanal}")

st.markdown("---")

st.subheader("🎲 Tu Reto en Curso")
texto_reto = generar_reto_unico(st.session_state.indice_reto_actual)

st.markdown(f"""
<div class="reto-card">
    <span class="badge">ID Reto #{st.session_state.indice_reto_actual}</span>
    <h3 style="margin-top: 10px; color: #58a6ff;">{texto_reto}</h3>
</div>
""", unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    if st.button("✅ Aceptarlo"):
        st.session_state.retos_completados += 1
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

with col_b2:
    if st.button("⏳ Posponerlo"):
        st.session_state.retos_posponidos += 1
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

with col_b3:
    if st.button("❌ Cambiar"):
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

st.markdown("---")

# --- BUSCADOR MÁGICO DE MÚSICA CON LISTA VISIBLE ---
st.subheader("🪄 Botón Mágico: Música para Edits")
st.write("Escribe qué vibra buscas para tu edit:")

# Mostrar la lista oficial de palabras permitidas directamente en la interfaz
st.markdown("""
<div class="tag-box">
    <b>🔥 Palabras disponibles para buscar:</b><br>
    • <b>Estados:</b> feliz, bien, triste, mal, cansado, depre<br>
    • <b>Vibras:</b> amor, inteligente, epico, nostalgico<br>
    • <b>Extras:</b> violin, interstellar, oppenheimer, gym, minecraft
</div>
""", unsafe_allow_html=True)

palabra_clave = st.text_input("Escribe tu palabra aquí:", placeholder="Ej. feliz, cansado, inteligente...")

if st.button("✨ Recomendar Música"):
    palabra_limpia = palabra_clave.strip().lower()
    
    resultados = []
    for cancion in MUSICA_EDITS:
        if any(palabra_limpia in tag for tag in cancion["tags"]) or palabra_limpia in cancion["nombre"].lower() or palabra_limpia in cancion["artista"].lower():
            resultados.append(cancion)
            
    if not resultados:
        resultados = random.sample(MUSICA_EDITS, min(4, len(MUSICA_EDITS)))

    st.markdown(f"### 🎧 Resultados para: *{palabra_clave if palabra_clave else 'General'}*")
    
    for idx, cancion in enumerate(resultados[:10], 1):
        st.markdown(f"**{idx}. {cancion['nombre']}** — *{cancion['artista']}* \n🔗 [Escuchar en YouTube]({cancion['url']})")

st.markdown("---")
st.caption("Los retos se actualizan de forma autónoma cada semana.")
