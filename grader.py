#!/usr/bin/python3

# Dependencies
import os
import shutil

# Import helper functions from util.py
from util import send_feedback, print_stderr

def main(partId):
    # The directory /shared/submission/ is the standard submission directory across all courses.
    submission_location = "/shared/submission/"
    expected_filename = "ControladorLetreroPropiedad.cs"
    
    # Check if the expected file is present in the submission
    if not os.path.exists(os.path.join(submission_location, expected_filename)):
        send_feedback(0.0, f"El archivo enviado no se llama {expected_filename}.")
        return

    # Read the content of the submission file
    with open(os.path.join(submission_location, expected_filename), 'r') as file:
        submission_content = file.read()

    # Check for the required elements in the file content
    required_elements = [
        'public string nombrePropietario;',
        'public TextMeshPro propietarioTexto3D;',
        'public string DarMensajePropiedad(string nombrePropietario)',
        'propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);'
    ]

    missing_elements = [element for element in required_elements if element not in submission_content]

    if missing_elements:
        feedback = f"Faltan los siguientes elementos en el script:\n" + "\n".join(missing_elements)
        send_feedback(0.0, feedback)
    else:
        send_feedback(1.0, "¡Buen trabajo! El script contiene todos los elementos requeridos.")

if __name__ == '__main__':
    try:
        partId = os.environ['partId']
    except Exception as e:
        print_stderr("Por favor proporciona el partId.")
        send_feedback(0.0, "Por favor proporciona el partId.")
    else:
        main(partId)
