import os
import unittest
import matplotlib.pyplot as plt
from model_instance import model_manager

class TestIntegration(unittest.TestCase):

    def test_model_initialization(self):
        """Prueba si el modelo y el índice Chroma se inicializan correctamente."""
        try:
            model = model_manager.initialize_chroma()
            self.assertIsNotNone(model, "El modelo no debería ser None después de la inicialización.")
        except Exception as e:
            self.fail(f"Error al inicializar el modelo: {e}")

    def test_user_interaction_becas(self):
        """Prueba si la aplicación responde correctamente a una consulta sobre becas."""
        try:
            response = model_manager.get_response("¿La ESPE ofrece becas a sus estudiantes?")
            self.assertIn("becas", response.lower(), "La respuesta debería contener información sobre becas.")
        except Exception as e:
            self.fail(f"Error en la interacción con el usuario: {e}")

    def test_user_interaction_carreras(self):
        """Prueba si la aplicación responde correctamente a una consulta sobre carreras."""
        try:
            response = model_manager.get_response("¿Qué carreras de ingeniería ofrece la ESPE?")
            self.assertIn("ingeniería", response.lower(), "La respuesta debería contener información sobre carreras de ingeniería.")
        except Exception as e:
            self.fail(f"Error en la interacción con el usuario: {e}")

    def test_user_interaction_admision(self):
        """Prueba si la aplicación responde correctamente a una consulta sobre admisión."""
        try:
            response = model_manager.get_response("¿Cuáles son los requisitos de admisión en la ESPE?")
            self.assertIn("admisión", response.lower(), "La respuesta debería contener información sobre admisión.")
        except Exception as e:
            self.fail(f"Error en la interacción con el usuario: {e}")

    def test_user_interaction_campus(self):
        """Prueba si la aplicación responde correctamente a una consulta sobre campus."""
        try:
            response = model_manager.get_response("¿Dónde están ubicados los campus de la ESPE?")
            self.assertIn("campus", response.lower(), "La respuesta debería contener información sobre los campus.")
        except Exception as e:
            self.fail(f"Error en la interacción con el usuario: {e}")

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.makeSuite(TestIntegration))
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    successes = total_tests - failures - errors

    # Calcular precisión
    precision = successes / total_tests

    results = {
        'Éxitos': successes,
        'Fallos': failures,
        'Errores': errors,
        'Precisión': precision
    }

    print(f"Precisión: {precision * 100:.2f}%")

    labels = list(results.keys())
    values = list(results.values())

    plt.bar(labels[:-1], values[:-1], color=['green', 'red', 'orange'])
    plt.title('Resultados de Pruebas de Integración')
    plt.ylabel('Número de Casos')
    plt.xlabel('Resultados')
    
    # Verificar si la carpeta existe y crearla si no existe
    save_path = r'C:\Users\Jcnaz\Desktop\resultados_pruebas.png'  # Cambia la ruta aquí si es necesario
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    print(f"Intentando guardar el gráfico en: {save_path}")
    try:
        plt.savefig(save_path)
        print(f"Gráfico guardado exitosamente en: {save_path}")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")
    plt.show()
