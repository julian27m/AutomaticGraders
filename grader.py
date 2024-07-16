#!/usr/bin/python3

# Dependencias
import os
import re
from util import send_feedback, print_stderr, initialize_feedback, finalize_feedback, append_feedback

def main(partId):
    # Directorio de envío
    submission_location = "/shared/submission/"
    test_directory = "/autograder/source/Tests"
    expected_filename = "ControladorLetreroPropiedad.cs"

    # Feedback
    initialize_feedback()
    print_stderr("Feedback initialized")

    # Verificar si existe el directorio de pruebas
    if not os.path.isdir(test_directory):
        send_feedback(0.0, f"El directorio de pruebas '{test_directory}' no existe.")
        return

    # Obtener todos los archivos en el directorio de pruebas
    test_files = [f for f in os.listdir(test_directory) if os.path.isfile(os.path.join(test_directory, f))]
    print_stderr(f"Test files found: {test_files}")

    if not test_files:
        send_feedback(0.0, "No se encontraron archivos en el directorio de pruebas.")
        return

    # Definir los patrones de expresiones regulares para los elementos requeridos y sus respectivos mensajes de retroalimentación
    checks = [
        {
            "pattern": r"using System.Collections;\s*using System.Collections.Generic;\s*using UnityEngine;\s*using TMPro;",
            "error_message": "El código debe incluir las siguientes declaraciones al inicio: using System.Collections, using System.Collections.Generic, using UnityEngine, using TMPro.",
            "points_deducted": 10
        },
        {
            "pattern": r"public class ControladorLetreroPropiedad\s*:\s*MonoBehaviour\s*{",
            "error_message": "La clase debe declararse como 'public class ControladorLetreroPropiedad : MonoBehaviour {'.",
            "points_deducted": 10
        },
        {
            "pattern": r"public string nombrePropietario;",
            "error_message": "La clase debe contener la variable pública 'public string nombrePropietario;'.",
            "points_deducted": 20
        },
        {
            "pattern": r"public TextMeshPro propietarioTexto3D;",
            "error_message": "La clase debe contener la variable pública 'public TextMeshPro propietarioTexto3D;'.",
            "points_deducted": 20
        },
        {
            "pattern": r"void Start\s*\(\)\s*{\s*propietarioTexto3D\.text\s*=\s*DarMensajePropiedad\(nombrePropietario\);\s*}",
            "error_message": "La función 'Start' debe contener 'propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);'.",
            "points_deducted": 10
        },
        {
            "pattern": r"public string DarMensajePropiedad\s*\(\s*string nombrePropietario\s*\)\s*{\s*string respuesta\s*=\s*\"Propiedad de \"\s*\+\s*nombrePropietario;\s*return respuesta;\s*}",
            "error_message": "La función 'DarMensajePropiedad' debe declararse correctamente y retornar el mensaje 'Propiedad de ' más el nombre del propietario.",
            "points_deducted": 20
        },
        {
            "pattern": r"}\s*$",
            "error_message": "El código contiene elementos adicionales fuera de la clase ControladorLetrero.",
            "points_deducted": 10
        }
    ]

    total_points = 100

    # Procesar cada archivo en el directorio de pruebas
    for test_file in test_files:
        test_file_path = os.path.join(test_directory, test_file)
        with open(test_file_path, 'r') as file:
            submission_content = file.read()

        errors = []
        file_points = total_points

        # Verificar los elementos requeridos usando expresiones regulares
        for check in checks:
            if not re.search(check["pattern"], submission_content):
                errors.append(check["error_message"])
                file_points -= check["points_deducted"]

               
        

        # Si hay errores, enviar retroalimentación con los errores encontrados
        if errors:
            feedback = f"Archivo: {test_file}\nSe encontraron los siguientes errores:\n" + "\n".join(errors)
            append_feedback(file_points / 100.0, feedback, test_file)
        else:
            # Si todo es correcto...
            append_feedback(1.0, f"Archivo: {test_file}\n¡Buen trabajo! El script contiene todos los elementos requeridos y no tiene errores de sintaxis.", test_file)

    # Finalizar feedback
    finalize_feedback()
    print_stderr("Feedback finalized")

if __name__ == '__main__':
    try:
        partId = os.environ['partId']
    except Exception as e:
        print_stderr("Por favor proporciona el partId.")
        send_feedback(0.0, "Por favor proporciona el partId.")
    else:
        main(partId)