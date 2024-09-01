import sqlite3
import pandas as pd

# Leer el archivo Excel (cambia el nombre del archivo al que estás usando)
file_path = 'C:/Users/Jcnaz/SQLLite/espe_chatbot.xlsx'
df = pd.read_excel(file_path)

# Conectar a la base de datos SQLite (esto creará el archivo si no existe)
conn = sqlite3.connect('espe_data.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS espe_dataset (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        respuesta TEXT
    )
''')

# Insertar los datos de Excel en la base de datos SQLite
for index, row in df.iterrows():
    pregunta = row['Pregunta']  # Cambia según el nombre de la columna en tu Excel
    respuesta = row['Respuesta']  # Cambia según el nombre de la columna en tu Excel
    cursor.execute('''
        INSERT INTO espe_dataset (pregunta, respuesta)
        VALUES (?, ?)
    ''', (pregunta, respuesta))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados exitosamente")
