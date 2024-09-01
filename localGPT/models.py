from transformers import pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from constants import ROBERTA_MODEL_NAME, EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY, CHROMA_SETTINGS
import logging

class ModelManager:
    def __init__(self, db=None):
        logging.info("Inicializando ModelManager")
        
        # Modelo de preguntas y respuestas con RoBERTa
        logging.info(f"Cargando modelo RoBERTa: {ROBERTA_MODEL_NAME}")
        self.qa_model = pipeline('question-answering', model=ROBERTA_MODEL_NAME, tokenizer=ROBERTA_MODEL_NAME)
        logging.info("Modelo RoBERTa cargado exitosamente")
        
        # Embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        
        # Inicializar Chroma
        self.db = db if db is not None else self.initialize_chroma()

    def initialize_chroma(self):
        logging.info("Cargando el índice Chroma persistido")
        return Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=self.embeddings,
            client_settings=CHROMA_SETTINGS
        )

    def get_similar_context(self, query):
        logging.info(f"Buscando contexto similar para: {query}")
        if self.db:
            results = self.db.similarity_search_with_score(query, k=1)
            if results:
                doc, score = results[0]
                logging.info(f"Documento similar encontrado. Puntuación: {score}")
                return doc.page_content
            else:
                logging.warning("No se encontraron documentos similares en Chroma")
        else:
            logging.error("Chroma index no inicializado")
        return ""

    def get_response(self, query):
        logging.info(f"Generando respuesta para: {query}")
        try:
            similar_context = self.get_similar_context(query)
            
            if similar_context:
                logging.info(f"Contexto similar encontrado: {similar_context}")
                # Devolver directamente el contexto encontrado
                return similar_context
            else:
                logging.warning("No se encontró un contexto similar")
            
            return "Lo siento, no pude encontrar una respuesta adecuada en este momento."
        except Exception as e:
            logging.error(f"Error al generar respuesta: {str(e)}")
            return "Ocurrió un error al procesar tu pregunta. Por favor, inténtalo de nuevo."