from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from constants import EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY, CHROMA_SETTINGS

class ModelManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        self.db = self.initialize_chroma()

    def initialize_chroma(self):
        return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=self.embeddings, client_settings=CHROMA_SETTINGS)

    def get_response(self, query):
        results = self.db.similarity_search(query)
        if results:
            return results[0].page_content
        return "Lo siento, no pude encontrar una respuesta adecuada en este momento."

# Aquí se crea la instancia del ModelManager
model_manager = ModelManager()
