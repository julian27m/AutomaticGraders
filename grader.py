#!/usr/bin/python3

# Dependencias
import os
import re
from util import send_feedback, print_stderr

def main(partId):
    # El directorio /shared/submission/ es el directorio de envío estándar en todos los cursos
    submission_location = "/shared/submission/"
    expected_filename = "ControladorLetreroPropiedad.cs"
    submission_filepath = os.path.join(submission_location, expected_filename)

    # Comprobar si el archivo esperado está presente en el envío
    if not os.path.isfile(submission_filepath):
        send_feedback(0.0, f"El archivo enviado no se llama {expected_filename}.")
        return

    # Leer el contenido del archivo de envío
    with open(submission_filepath, 'r') as file:
        submission_content = file.read()

    # Definir los patrones de expresiones regulares para los elementos requeridos y sus respectivos mensajes de retroalimentación
    checks = [
        {
            "pattern": r"using System.Collections;\s*using System.Collections.Generic;\s*using UnityEngine;\s*using TMPro;",
            "error_message": "El código debe incluir las siguientes declaraciones al inicio: using System.Collections, using System.Collections.Generic, using UnityEngine, using TMPro."
        },
        {
            "pattern": r"public class ControladorLetrero\s*:\s*MonoBehaviour\s*{",
            "error_message": "La clase debe declararse como 'public class ControladorLetrero : MonoBehaviour {'."
        },
        {
            "pattern": r"public string nombrePropietario;\s*public TextMeshPro propietarioTexto3D;",
            "error_message": "La clase debe contener las variables públicas 'public string nombrePropietario;' y 'public TextMeshPro propietarioTexto3D;'."
        },
        {
            "pattern": r"void Start\s*\(\)\s*{\s*propietarioTexto3D\.text\s*=\s*DarMensajePropiedad\(nombrePropietario\);\s*}",
            "error_message": "La función 'Start' debe contener 'propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);'."
        },
        {
            "pattern": r"public string DarMensajePropiedad\s*\(\s*string nombrePropietario\s*\)\s*{\s*string respuesta\s*=\s*\"Propiedad de \"\s*\+\s*nombrePropietario;\s*return respuesta;\s*}",
            "error_message": "La función 'DarMensajePropiedad' debe declararse correctamente y retornar el mensaje 'Propiedad de ' más el nombre del propietario."
        },
        {
            "pattern": r"}\s*$",
            "error_message": "El código contiene elementos adicionales fuera de la clase ControladorLetrero."
        }
    ]

    # Inicializar la puntuación
    total_points = 100
    points_deducted_per_error = 16
    errors = []

    # Verificar los elementos requeridos usando expresiones regulares
    for check in checks:
        if not re.search(check["pattern"], submission_content):
            errors.append(check["error_message"])
            total_points -= points_deducted_per_error

    # Si hay errores, enviar retroalimentación con los errores encontrados
    if errors:
        feedback = "Se encontraron los siguientes errores:\n" + "\n".join(errors)
        send_feedback(total_points / 100.0, feedback)
    else:
        # Si todo es correcto...
        send_feedback(1.0, "¡Buen trabajo! El script contiene todos los elementos requeridos y no tiene errores de sintaxis.")

if __name__ == '__main__':
    try:
        partId = os.environ['partId']
    except Exception as e:
        print_stderr("Por favor proporciona el partId.")
        send_feedback(0.0, "Por favor proporciona el partId.")
    else:
        main(partId)
