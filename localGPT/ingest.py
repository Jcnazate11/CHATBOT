import logging
import sqlite3
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from constants import (
    CHROMA_SETTINGS,
    EMBEDDING_MODEL_NAME,
    PERSIST_DIRECTORY
)

# Configuración de logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Definir la ruta correcta a la base de datos
DB_PATH = os.path.join("C:", os.sep, "Users", "Jcnaz", "SQLLite", "espe_data.db")

def load_documents(db_path: str) -> list[Document]:
    """Cargar documentos desde la base de datos SQLite."""
    logging.info(f"Intentando cargar documentos desde {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if not tables:
            raise ValueError("No hay tablas en la base de datos")
       
        table_name = tables[0][0]
        logging.info(f"Usando la tabla: {table_name}")
       
        cursor.execute(f"SELECT pregunta, respuesta FROM {table_name}")
        rows = cursor.fetchall()
        conn.close()
        
        documents = []
        for row in rows:
            pregunta, respuesta = row
            doc = Document(page_content=pregunta + "\n" + respuesta, metadata={"pregunta": pregunta, "respuesta": respuesta})
            documents.append(doc)
        
        logging.info(f"Se cargaron {len(documents)} documentos")
        return documents
    except Exception as e:
        logging.error(f"Error al cargar documentos: {e}")
        raise

def main():
    try:
        documents = load_documents(DB_PATH)
        
        logging.info(f"Dividiendo documentos en chunks...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        logging.info(f"Indexando {len(texts)} documentos con Chroma")
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
       
        # Crear el índice Chroma y persistirlo
        db = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIRECTORY,
            client_settings=CHROMA_SETTINGS,
        )
        db.persist()
        logging.info("Chroma index creado y persistido.")
    except Exception as e:
        logging.error(f"Error en el proceso principal: {e}")

if __name__ == "__main__":
    main()