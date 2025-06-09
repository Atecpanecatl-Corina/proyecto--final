import tkinter as tk
from tkinter import simpledialog, messagebox
pacientes = [[str() for _ in range(6)] for _ in range(100)]
contador = [1] 
areas = [
    "urgencia", "hospitalizacion", "cuidados intensivos", "pediatria",
    "fisioterapia", "radiologia", "neurologia", "medico familiar"
]
def registrar_paciente():
    nombre = simpledialog.askstring("nombre", "ingrese nombre del paciente:")
    if not nombre: return
    apellidop = simpledialog.askstring("apellido paterno", "ingrese apellido paterno:")
    if not apellidop: return
    apellidom = simpledialog.askstring("apellido materno", "ingrese apellido materno:")
    if not apellidom: return
    area_opcion = simpledialog.askinteger(
        "area medica", 
        "seleccione un area:\n" +
        "\n".join([f"{i+1}. {a}" for i, a in enumerate(areas)])
    )