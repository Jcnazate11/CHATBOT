import streamlit as st
from model_instance import model_manager

def init_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy el asistente virtual de la ESPE. ¿En qué puedo ayudarte?"}
        ]
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

def is_valid_question(question):
    # Lista de palabras clave relacionadas con la universidad
    keywords = [
        # Nombres y acrónimos
        'espe', 'universidad de las fuerzas armadas', 'escuela politécnica del ejército', 'politécnica',
        # Campus
        'sangolquí', 'latacunga', 'santo domingo', 'campus matriz', 'campus', 'extensión',
        # Carreras y áreas de estudio
        'ingeniería', 'sistemas', 'computación', 'mecatrónica', 'electrónica',
        'software', 'civil', 'mecánica', 'petroquímica', 'biotecnología',
        'agropecuaria', 'comercial', 'finanzas', 'seguridad', 'ambiental',
        'telecomunicaciones', 'redes', 'informática', 'ciencias económicas', 'gestión ambiental',
        'química', 'tecnologías de la información', 'agronomía', 'nutrición', 'medicina veterinaria',
        # Términos académicos
        'pregrado', 'posgrado', 'maestría', 'doctorado', 'tecnología', 'técnico',
        'laboratorio', 'investigación', 'proyecto', 'tesis', 'titulación',
        'sílabos', 'calificaciones', 'currículo', 'plan de estudios', 'clases',
        'profesores', 'docentes', 'becarios', 'asistentes de cátedra', 'directores de carrera',
        # Servicios estudiantiles
        'biblioteca', 'bienestar estudiantil', 'deportes', 'cultura',
        'residencia', 'comedor', 'transporte', 'consejería estudiantil', 'psicología',
        'orientación vocacional', 'seguro estudiantil', 'actividades extracurriculares',
        # Procesos administrativos
        'admisión', 'matrícula', 'beca', 'créditos', 'horario', 'examen',
        'inscripción', 'pago de matrícula', 'certificados', 'solicitud', 'trámite',
        'registro académico', 'carnet estudiantil', 'historial académico',
        # Investigación y extensión
        'centro de investigación', 'publicación', 'congreso', 'seminario',
        'vinculación', 'prácticas pre-profesionales', 'proyectos de vinculación',
        'convocatoria', 'fondos de investigación', 'transferencia tecnológica',
        # Eventos y actividades
        'casa abierta', 'graduación', 'feria de ciencias', 'concurso',
        'conferencia', 'charla', 'taller', 'día de la ciencia', 'expoferia',
        'jornadas académicas', 'semana cultural', 'gala de graduación',
        # Departamentos y unidades
        'rectorado', 'vicerrectorado', 'departamento', 'facultad', 'carrera',
        'escuela', 'centro de servicios académicos', 'unidad de bienestar estudiantil',
        'oficina de admisiones', 'oficina de registros', 'oficina de movilidad estudiantil',
        'biblioteca central', 'centro de cómputo', 'centro de idiomas',
        # Términos militares (dado el contexto de la universidad)
        'fuerzas armadas', 'ejército', 'militar', 'defensa', 'formación militar',
        'instrucción militar', 'disciplina', 'valores militares', 'oficial',
        'suboficial', 'cadete', 'tropa', 'escuadra', 'brigada',
        # Otros términos relacionados con la universidad
        'malla curricular', 'programa académico', 'aulas', 'campaña de reciclaje', 'responsabilidad social',
        'voluntariado', 'clubes estudiantiles', 'asociación de estudiantes', 'elecciones estudiantiles',
        'cursos de nivelación', 'evaluación académica', 'expediente académico'
    ]
    
    # Convertir la pregunta a minúsculas para una comparación sin distinción de mayúsculas
    question_lower = question.lower()
    
    # Comprobar si alguna palabra clave está presente en la pregunta
    return any(keyword in question_lower for keyword in keywords)


def handle_input():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.messages.append({"role": "user", "content": user_message})

        if is_valid_question(user_message):
            # Usar DistilBERT para todas las preguntas válidas
            response = model_manager.get_response(user_message)
            
            # Procesar la respuesta
            if "?" in response:
                # Eliminar la parte de la pregunta si está presente
                response = response.split("?")[-1].strip()
            
            # Verificar si la respuesta es relevante
            if len(response) < 10 or not any(keyword in response.lower() for keyword in ['espe', 'universidad', 'campus']):
                response = "Lo siento, no puedo proporcionar una respuesta precisa a esa pregunta. Te sugiero consultar el sitio web oficial de la ESPE (https://www.espe.edu.ec) para obtener la información más actualizada y precisa."
            
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.session_state.messages.append({"role": "assistant", "content": "Lo siento, solo puedo responder preguntas relacionadas con la Universidad de las Fuerzas Armadas ESPE."})
        
        st.session_state.user_input = ""

st.set_page_config(page_title="ESPE Chatbot", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #1c2833;
        color: #ffffff;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        background-color: #1c2833;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background: linear-gradient(90deg, #ba4a00, #f5b041);
        align-items: flex-end;
    }
    .chat-message.assistant {
        background: linear-gradient(90deg, #f5b041, #1c2833);
        align-items: flex-start;
    }
    .chat-message .message {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .chat-message.user .message {
        text-align: right;
    }
    .stTextInput > div > div > input {
        background-color: #34495e;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #ba4a00;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("ESPE Chatbot")
st.subheader("Asistente virtual para la Universidad de las Fuerzas Armadas ESPE")

init_chat_history()

for message in st.session_state.messages:
    with st.container():
        st.markdown(f'<div class="chat-message {message["role"]}"><div class="message">{message["content"]}</div></div>', unsafe_allow_html=True)

st.text_input("Escribe tu pregunta aquí:", key="user_input", on_change=handle_input)

st.markdown("### Ejemplos de preguntas:")
st.markdown("- ¿Qué carreras de computación ofrece la ESPE?")
st.markdown("- ¿Cuáles son los requisitos para la carrera de Ingeniería en Sistemas?")
st.markdown("- ¿Qué oportunidades de prácticas hay para estudiantes de computación?")
st.markdown("- ¿Cómo es el proceso de admisión para las carreras de tecnología?")