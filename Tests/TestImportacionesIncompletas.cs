using System.Collections;
using UnityEngine;
using TMPro;

public class ControladorLetrero : MonoBehaviour
{
    public string nombrePropietario;

    public TextMeshPro propietarioTexto3D; 

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
