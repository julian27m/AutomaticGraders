// Importaciones
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

// Clase ControladorLetreroPropiedad
public class ControladorLetreroPropiedad : MonoBehaviour
{   
    // Asignación de variables
    public string nombrePropietario;

    public TextMeshPro propietarioTexto3D; 

    // Metodo Start
    void Start()
    {
        propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);
    }
    
    // Método DarMensajePropiedad
    public string DarMensajePropiedad(string nombrePropietario)
    {
        string respuesta = "Propiedad de " + nombrePropietario;
        return respuesta;
    }
}

