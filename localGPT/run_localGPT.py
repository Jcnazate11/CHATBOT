import logging
import click
from model_instance import model_manager
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from constants import EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY

def process_query(query):
    # Lógica para procesar la consulta y devolver una respuesta.
    response = model_manager.get_response(query)
    return response

@click.command()
def main():
    while True:
        query = input("Introduce una pregunta (o escribe 'exit' para salir): ")
        if query.lower() == 'exit':
            break
        response = process_query(query)
        print(f"> Pregunta: {query}")
        print(f"> Respuesta: {response}")

if __name__ == "__main__":
    main()
