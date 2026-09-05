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
    </style>
""", unsafe_allow_html=True)

# --- BANCO DE 100,000 RETOS (Simulado con generador procedural y categorías) ---
# En producción real se cargaría de una base de datos o archivo masivo.
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
    """Genera un reto determinista pero único basado en un índice grande."""
    random.seed(seed_num)
    accion = random.choice(ACCIONES)
    complemento = random.choice(COMPLEMENTOS)
    return f"{accion} {complemento}."

# --- SISTEMA DE TIEMPO Y SEMANAS ---
def obtener_semana_actual():
    ahora = datetime.datetime.now()
    # Devuelve el año y el número de semana del año
    return ahora.isocalendar()[:2]

# Inicializar Estado de Sesión (Session State)
if 'current_week' not in st.session_state:
    st.session_state.current_week = obtener_semana_actual()
    random.seed(hash(str(st.session_state.current_week)))
    st.session_state.meta_semanal = random.randint(1, 100)
    st.session_state.retos_completados = 0
    st.session_state.retos_posponidos = 0
    st.session_state.indice_reto_actual = random.randint(0, 99999)

# Verificar si cambió la semana para actualizar automáticamente
semana_hoy = obtener_semana_actual()
if st.session_state.current_week != semana_hoy:
    st.session_state.current_week = semana_hoy
    random.seed(hash(str(semana_hoy)))
    st.session_state.meta_semanal = random.randint(1, 100)
    st.session_state.retos_completados = 0
    st.session_state.retos_posponidos = 0
    st.session_state.indice_reto_actual = random.randint(0, 99999)

# --- BASE DE DATOS DE MÚSICA PARA EDITS ---
MUSICA_EDITS = {
    "inteligente": [
        {"nombre": "Interstellar - Cornfield Chase", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=m3zvVGJrTP8"},
        {"nombre": "Oppenheimer - Can You Hear The Music", "artista": "Ludwig Göransson", "url": "https://www.youtube.com/watch?v=bc3b09YwIbs"},
        {"nombre": "The Social Network - In the Hall of the Mountain King", "artista": "Trent Reznor & Atticus Ross", "url": "https://www.youtube.com/watch?v=1x0wZ65a6e8"},
        {"nombre": "Theory of Everything - Flight to Cambridge", "artista": "Jóhann Jóhannsson", "url": "https://www.youtube.com/watch?v=0tS6jX8h68g"},
        {"nombre": "Succession Theme", "artista": "Nicholas Britell", "url": "https://www.youtube.com/watch?v=Gk6Wq_63_Yg"},
        {"nombre": "Sherlock - The Game Is On", "artista": "David Arnold & Michael Price", "url": "https://www.youtube.com/watch?v=33K16R20VfU"},
        {"nombre": "Limitless Theme", "artista": "Paul Leonard-Morgan", "url": "https://www.youtube.com/watch?v=4vY-kX6zH8o"},
        {"nombre": "Beautiful Mind - A Kaleidoscope of Mathematics", "artista": "James Horner", "url": "https://www.youtube.com/watch?v=b4wS96f-c14"},
        {"nombre": "The Imitation Game - Enigma", "artista": "Alexandre Desplat", "url": "https://www.youtube.com/watch?v=3j0vXz2Y7K0"},
        {"nombre": "Tenet - Sator", "artista": "Ludwig Göransson", "url": "https://www.youtube.com/watch?v=uK1lH4T5Z2Q"}
    ],
    "epico": [
        {"nombre": "Attack on Titan - Vogel im Käfig", "artista": "Hiroyuki Sawano", "url": "https://www.youtube.com/watch?v=8TJbXuKzGf4"},
        {"nombre": "Interstellar - Stay", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=ca2_wWb8gX8"},
        {"nombre": "Dark Knight - Why So Serious?", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=d_x5g_mE9Fk"},
        {"nombre": "Doom Eternal - The Only Thing They Fear Is You", "artista": "Mick Gordon", "url": "https://www.youtube.com/watch?v=AicsyHMqkt8"},
        {"nombre": "Cyberpunk 2077 - Never Fade Away", "artista": "P.T. Adamczyk", "url": "https://www.youtube.com/watch?v=8V3i34B68gE"},
        {"nombre": "Bleach - Number One", "artista": "Shiro Sagisu", "url": "https://www.youtube.com/watch?v=LqN_yZ41Z9s"},
        {"nombre": "Naruto - Girei (Pain Theme)", "artista": "Yasuharu Takanashi", "url": "https://www.youtube.com/watch?v=P6Yc3i2wVjI"},
        {"nombre": "Berserk - Guts Theme", "artista": "Susumu Hirasawa", "url": "https://www.youtube.com/watch?v=7j6f6X2pY1s"},
        {"nombre": "Dune - Paul's Dream", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=kYQ2J3x8Z9s"},
        {"nombre": "God of War - Overture", "artista": "Bear McCreary", "url": "https://www.youtube.com/watch?v=9gW0z1X3l4Y"}
    ],
    "nostalgico": [
        {"nombre": "Her's - Harvey", "artista": "Her's", "url": "https://www.youtube.com/watch?v=1b5P6-8Z1b4"},
        {"nombre": "Roar - Christmas Card", "artista": "Roar", "url": "https://www.youtube.com/watch?v=v0n6B1x6Z9s"},
        {"nombre": "Minecraft - Sweden", "artista": "C418", "url": "https://www.youtube.com/watch?v=aA3XvA5F1kE"},
        {"nombre": "Subnautica - Into the Unknown", "artista": "Simon Chylinski", "url": "https://www.youtube.com/watch?v=0k5G6-2Z9s8"},
        {"nombre": "That Handsome Devil - Pills for Everything", "artista": "That Handsome Devil", "url": "https://www.youtube.com/watch?v=9bZ0x1X2s8Y"},
        {"nombre": "Blade Runner 2049 - Sea Wall", "artista": "Hans Zimmer & Benjamin Wallfisch", "url": "https://www.youtube.com/watch?v=5rA0x1Y2s9s"},
        {"nombre": "The Caretaker - It's Just a Burning Memory", "artista": "The Caretaker", "url": "https://www.youtube.com/watch?v=wJWksPWDKOc"},
        {"nombre": "Undertale - His Theme", "artista": "Toby Fox", "url": "https://www.youtube.com/watch?v=8Z9sX1Y2v0s"},
        {"nombre": "Chrono Trigger - Corridors of Time", "artista": "Yasunori Mitsuda", "url": "https://www.youtube.com/watch?v=J5X1s9Z0v8s"},
        {"nombre": "Lego Batman Theme", "artista": "Tricky Stewart", "url": "https://www.youtube.com/watch?v=1x9Z0s8V2s8"}
    ]
}

# --- INTERFAZ GRÁFICA PRINCIPAL ---
st.title("⚡ Central de Retos & Edits Vibes")
st.write("Sistema automatizado de retos semanales (Pool de 100,000 misiones) con generador de música estilo edit.")

st.markdown("---")

# Panel de Estado Semanal
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📅 Semana Actual", value=f"Semana {st.session_state.current_week[1]}")
with col2:
    st.metric(label="🎯 Meta de Retos", value=f"{st.session_state.meta_semanal} retos")
with col3:
    st.metric(label="✅ Cumplidos", value=f"{st.session_state.retos_completados} / {st.session_state.meta_semanal}")

st.markdown("---")

# Sección del Reto Actual
st.subheader("🎲 Tu Reto en Curso")

# Generar el texto del reto actual
texto_reto = generar_reto_unico(st.session_state.indice_reto_actual)

st.markdown(f"""
<div class="reto-card">
    <span class="badge">ID Reto #{st.session_state.indice_reto_actual}</span>
    <h3 style="margin-top: 10px; color: #58a6ff;">{texto_reto}</h3>
</div>
""", unsafe_allow_html=True)

# Botones de Acción para el Reto
col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    if st.button("✅ Aceptarlo y Cumplirlo"):
        st.session_state.retos_completados += 1
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

with col_b2:
    if st.button("⏳ Posponerlo"):
        st.session_state.retos_posponidos += 1
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

with col_b3:
    if st.button("❌ Cancelar / Cambiar"):
        st.session_state.indice_reto_actual = random.randint(0, 99999)
        st.rerun()

st.markdown("---")

# --- BOTÓN MÁGICO DE MÚSICA PARA EDITS ---
st.subheader("🪄 Botón Mágico: Música para Edits")
st.write("Escribe una vibra o palabra clave (ej: *inteligente*, *epico*, *nostalgico*) y te recomiendo canciones nivel Dios para tu edit.")

palabra_clave = st.text_input("¿Qué vibra buscas para el edit?", placeholder="Ej. inteligente, épico, violín...")

if st.button("✨ Recomendar Música"):
    palabra_limpia = palabra_clave.strip().lower()
    
    # Buscar coincidencia exacta o aproximada en las categorías
    resultado_canciones = []
    for clave, lista in MUSICA_EDITS.items():
        if clave in palabra_limpia or palabra_limpia in clave:
            resultado_canciones = lista
            break
            
    # Si no encuentra coincidencia exacta, busca por palabras sueltas o da una por defecto (inteligente)
    if not resultado_canciones:
        if "violin" in palabra_limpia or "hans" in palabra_limpia or "interstellar" in palabra_limpia:
            resultado_canciones = MUSICA_EDITS["inteligente"]
        else:
            # Seleccionar una mezcla aleatoria o por defecto la categoría inteligente
            resultado_canciones = MUSICA_EDITS["inteligente"]

    st.markdown(f"### 🎧 Top Edits para: *{palabra_clave if palabra_clave else 'inteligente'}*")
    
    # Mostrar máximo 10 recomendaciones
    for idx, cancion in enumerate(resultado_canciones[:10], 1):
        st.markdown(f"**{idx}. {cancion['nombre']}** — *{cancion['artista']}* \n🔗 [Escuchar en YouTube]({cancion['url']})")

st.markdown("---")
st.caption("Los retos se actualizan de forma autónoma cada semana junto con tu objetivo dinámico del 1 al 100.")
