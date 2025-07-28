import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configurar la API de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Título de la aplicación
st.title("JobMate AI – Asistente de Escritura de CVs y Cartas")

# Descripción introductoria
st.write("Bienvenido a JobMate AI. Esta aplicación te ayuda a generar currículums y cartas de presentación profesionales con la ayuda de inteligencia artificial.")

# Formulario de entrada
with st.form("user_data"):
    nombre_completo = st.text_input("Nombre completo")
    correo_electronico = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono")
    perfil_profesional = st.text_area("Perfil profesional (breve párrafo)")
    experiencia_laboral = st.text_area("Experiencia laboral (texto largo)")
    formacion_academica = st.text_input("Formación académica")
    habilidades_clave = st.text_input("Habilidades clave")
    puesto_deseado = st.text_input("Puesto o rubro deseado")

    # Botones
    generar_cv_button = st.form_submit_button("Generar CV")
    generar_carta_button = st.form_submit_button(
        "Generar Carta de Presentación")

# Función para generar contenido con Gemini


def generar_contenido_con_gemini(prompt_usuario):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content(prompt_usuario)
    return response.text

# Funciones para crear prompts


def crear_prompt_cv(nombre_completo, correo_electronico, telefono, perfil_profesional, experiencia_laboral, formacion_academica, habilidades_clave, puesto_deseado):
    prompt = f"""
    Generar un CV detallado y profesional para:
    Nombre completo: {nombre_completo}
    Correo electrónico: {correo_electronico}
    Teléfono: {telefono}
    Perfil profesional: {perfil_profesional}
    Experiencia laboral: {experiencia_laboral}
    Formación académica: {formacion_academica}
    Habilidades clave: {habilidades_clave}
    Puesto deseado: {puesto_deseado}
    """
    return prompt


def crear_prompt_carta(nombre_completo, correo_electronico, telefono, perfil_profesional, experiencia_laboral, formacion_academica, habilidades_clave, puesto_deseado):
    prompt = f"""
    Generar una carta de presentación formal y convincente para:
    Nombre completo: {nombre_completo}
    Correo electrónico: {correo_electronico}
    Teléfono: {telefono}
    Perfil profesional: {perfil_profesional}
    Experiencia laboral: {experiencia_laboral}
    Formación académica: {formacion_academica}
    Habilidades clave: {habilidades_clave}
    Puesto deseado: {puesto_deseado}
    """
    return prompt


# Lógica para generar el CV o la carta de presentación
if generar_cv_button:
    # Crear el prompt
    prompt_cv = crear_prompt_cv(nombre_completo, correo_electronico, telefono, perfil_profesional,
                                experiencia_laboral, formacion_academica, habilidades_clave, puesto_deseado)

    # Generar el texto con Gemini
    cv_generado = generar_contenido_con_gemini(prompt_cv)

    # Mostrar el resultado en pantalla
    st.subheader("Currículum Vitae generado:")
    st.write(cv_generado)

    # Permitir que el usuario copie o descargue el resultado
    # (Implementar la funcionalidad de copia y descarga)
    st.write("Próximamente: podrás copiar o descargar este CV.")
    st.download_button(
        label="📄 Descargar CV",
        data=cv_generado,
        file_name="CV_Generado.txt",
        mime="text/plain"
    )

if generar_carta_button:
    # Crear el prompt
    prompt_carta = crear_prompt_carta(nombre_completo, correo_electronico, telefono, perfil_profesional,
                                      experiencia_laboral, formacion_academica, habilidades_clave, puesto_deseado)

    # Generar el texto con Gemini
    data = carta_generada = generar_contenido_con_gemini(prompt_carta)

    # Mostrar el resultado en pantalla
    st.subheader("Carta de Presentación generada:")
    st.write(carta_generada)

    # Permitir que el usuario copie o descargue el resultado
    # (Implementar la funcionalidad de copia y descarga)
st.write("Próximamente: podrás copiar o descargar esta carta de presentación.")

if "carta_generada" in st.session_state:
    st.download_button(
        label="📄 Descargar Carta de Presentación",
        data=st.session_state.carta_generada,
        file_name="Carta_de_Presentación_Generada.txt",
        mime="text/plain"
    )
else:
    st.warning("Primero debes generar la carta de presentación.")

# Sección "¿Cómo funciona?"
st.header("¿Cómo funciona?")
st.write("JobMate AI utiliza inteligencia artificial para analizar los datos que ingresas y transformarlos en un texto profesional y atractivo.")
st.write("Con JobMate AI, puedes crear CVs y cartas de presentación de alta calidad de forma rápida y sencilla, lo que te permitirá aplicar a trabajos de forma más eficiente.")
