import tkinter as tk
from tkinter import ttk, messagebox
class SistemaPacientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Pacientes")
        self.root.geometry("700x250")
        self.root.configure(bg = "turquoise")
        self.contador = 1
        self.pacientes = []
        self.camillas_ocupadas = set()
        self.menu_principal()
    def menu_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Menú Principal", font=("Arial", 18)).pack(pady=20)
        tk.Button(self.root, text="Registrar Paciente", command=self.ventana_registro, width=30).pack(pady=10)
        tk.Button(self.root, text="Ver Pacientes Registrados", command=self.ventana_tabla, width=30).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit, width=30).pack(pady=10)
    def ventana_registro(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Registro de Paciente", font=("Arial", 16)).grid(row=0, column=1, pady=10)
        tk.Label(self.root, text="Nombre:").grid(row=1, column=0, sticky='e')
        nombre = tk.Entry(self.root)
        nombre.grid(row=1, column=1)
        tk.Label(self.root, text="Apellido Paterno:").grid(row=2, column=0, sticky='e')
        apellidop = tk.Entry(self.root)
        apellidop.grid(row=2, column=1)
        tk.Label(self.root, text="Apellido Materno:").grid(row=3, column=0, sticky='e')
        apellidom = tk.Entry(self.root)
        apellidom.grid(row=3, column=1)
        tk.Label(self.root, text="Área médica:").grid(row=4, column=0, sticky='e')
        areas = ["Urgencia", "Hospitalización", "Cuidados Intensivos", "Pediatría", "Fisioterapia", "Radiología", "Neurología", "Médico Familiar"]
        area_var = tk.StringVar()
        area_menu = ttk.Combobox(self.root, textvariable=area_var, values=areas, state="readonly")
        area_menu.grid(row=4, column=1)
        tk.Label(self.root, text="Camilla (1 a 10):").grid(row=5, column=0, sticky='e')
        camilla_var = tk.StringVar()
        camillas_disp = [f"C{i}" for i in range(1, 11) if f"C{i}" not in self.camillas_ocupadas]