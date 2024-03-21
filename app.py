import streamlit as st
from yt_dlp import YoutubeDL
import os

# Configuramos la página
st.set_page_config(page_title="Descargador de YouTube", layout="wide")

# Añadimos algo de estilo con CSS
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="big-font">Descargador de Videos de YouTube</p>', unsafe_allow_html=True)

# Instrucciones
st.write("Ingresa la URL del video de YouTube que deseas descargar en la mejor calidad disponible.")

# Creamos la columna para el input y el botón
col1, col2 = st.columns([3,1])

with col1:
    video_url = st.text_input("", placeholder="Pega aquí la URL del video de YouTube")

with col2:
    # Botón para iniciar la descarga
    if st.button('Descargar'):
        if video_url:
            # Definimos la función de descarga dentro para evitar ejecuciones al cargar la página
            def descargar_video(url):
                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),  # Ajustamos la ruta de descarga
                }
                
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            
            # Llamamos a la función de descarga
            descargar_video(video_url)
            st.success('¡Descarga completada!')
        else:
            st.error('Por favor, ingresa una URL válida.')

# Información adicional
st.markdown("---")
st.write("Este es un proyecto simple para descargar videos de YouTube. Asegúrate de respetar los derechos de autor y las políticas de uso del contenido que descargas.")