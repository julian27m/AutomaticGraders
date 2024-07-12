using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class ControladorLetrero : MonoBehaviour
{
    void Start()
    {
        propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);
    }

    public string DarMensajePropiedad(string nombrePropietario)
    {
        string respuesta = "Propiedad de " + nombrePropietario;
        return respuesta;
    }
}
