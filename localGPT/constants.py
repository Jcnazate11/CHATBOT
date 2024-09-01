import os
from dotenv import load_dotenv
from chromadb.config import Settings
from langchain_community.document_loaders import CSVLoader, PDFMinerLoader, TextLoader, UnstructuredExcelLoader, Docx2txtLoader, UnstructuredFileLoader, UnstructuredMarkdownLoader, UnstructuredHTMLLoader


# Cargar variables de entorno desde el archivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ROBERTA_MODEL_NAME = "deepset/roberta-base-squad2"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Directorio raíz
ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Definir directorios para los documentos y la base de datos persistente
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/SOURCE_DOCUMENTS"
PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/DB"
MODELS_PATH = "./models"

# Número de hilos de procesamiento
INGEST_THREADS = os.cpu_count() or 8

# Configuración de Chroma
CHROMA_SETTINGS = Settings(
    anonymized_telemetry=False,
    is_persistent=True,
)

# Tamaño de la ventana de contexto y número máximo de nuevos tokens
CONTEXT_WINDOW_SIZE = 8096
MAX_NEW_TOKENS = CONTEXT_WINDOW_SIZE

# Capas de GPU y tamaño del lote
N_GPU_LAYERS = 100  # Dependiendo del modelo
N_BATCH = 512

# Definir los formatos de documentos compatibles
DOCUMENT_MAP = {
    ".html": UnstructuredHTMLLoader,
    ".txt": TextLoader,
    ".md": UnstructuredMarkdownLoader,
    ".py": TextLoader,
    ".pdf": UnstructuredFileLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".docx": Docx2txtLoader,
    ".doc": Docx2txtLoader,
}
