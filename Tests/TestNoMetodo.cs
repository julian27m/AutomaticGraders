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
        propietarioTexto3D.text = DarMensajePropiedad(nombrePropietario);
    }

    
}