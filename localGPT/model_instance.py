from models import ModelManager
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from constants import EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY, CHROMA_SETTINGS

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
model_manager = ModelManager(db)