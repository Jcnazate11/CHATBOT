import logging
import click
from model_instance import model_manager
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from constants import EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY

@click.command()
def main():
    logging.info("Inicializando el modelo y el índice Chroma...")
    
    # Inicializar embeddings
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    
    # Cargar el índice Chroma existente
    db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
    
    # Inicializar ModelManager con el índice Chroma
    model_manager = ModelManager(db)
    
    logging.info("Modelo y Chroma listos para consultas.")
    
    # Bucle principal para interactuar con el usuario
    while True:
        query = input("Introduce una pregunta (o escribe 'exit' para salir): ")
        if query.lower() == 'exit':
            break
        
        logging.info(f"Pregunta del usuario: {query}")
        
        # Obtener respuesta del modelo
        response = model_manager.get_response(query)
        logging.info(f"Respuesta generada: {response}")
        
        # Mostrar la respuesta al usuario
        print(f"> Pregunta: {query}")
        print(f"> Respuesta: {response}")
        print()  # Línea en blanco para separar las interacciones

if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    
    # Ejecutar la aplicación
    main()