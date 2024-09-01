import streamlit as st
from model_instance import model_manager

# Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot ESPE", layout="centered")

# Título de la aplicación
st.title("Chatbot Educativo - ESPE")

# Instrucción al usuario
st.write("Haz una pregunta sobre la Universidad de las Fuerzas Armadas ESPE:")

# Recoger la pregunta del usuario mediante un campo de texto
user_input = st.text_input("Introduce tu pregunta aquí", "")

# Botón para enviar la pregunta
if st.button("Enviar"):
    if user_input:
        # Obtener la respuesta del modelo
        response = model_manager.get_response(user_input)
        
        # Mostrar la respuesta al usuario
        st.write(f"**Pregunta:** {user_input}")
        st.write(f"**Respuesta:** {response}")
    else:
        st.write("Por favor, introduce una pregunta.")

# Añadir algunas preguntas sugeridas
st.write("### Ejemplos de preguntas:")
st.write("- ¿Qué campus tiene la ESPE?")
st.write("- ¿Qué servicios ofrece bienestar estudiantil en la ESPE?")
st.write("- ¿Cuánto cuesta la matrícula en la ESPE?")
st.write("- ¿La ESPE ofrece becas a sus estudiantes?")
