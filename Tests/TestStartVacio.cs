using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class ControladorLetrero : MonoBehaviour
{
    public string nombrePropietario;

    public TextMeshPro propietarioTexto3D; 

    void Start()
    {
        
    }

    public string DarMensajePropiedad(string nombrePropietario)
    {
        string respuesta = "Propiedad de " + nombrePropietario;
        return respuesta;
    }
}