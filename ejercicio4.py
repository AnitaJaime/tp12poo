import tkinter as tk

class VentanaAtomos:
    def __init__(self, root):
    
        root.title("Información del Átomo")
        root.geometry("400x400")
        
        tk.Label(root, text="Nombre del Átomo:").pack(pady=5)
        self.nombre_atomo = tk.Entry(root)
        self.nombre_atomo.pack(pady=5)

        tk.Label(root, text="Cantidad de electrones:").pack(pady=5)
        self.cantidad_electrones = tk.Entry(root)
        self.cantidad_electrones.pack(pady=5)

        tk.Label(root, text="Cantidad de protones:").pack(pady=5)
        self.cantidad_protones = tk.Entry(root)
        self.cantidad_protones.pack(pady=5)

        tk.Label(root, text="Cantidad de neutrones:").pack(pady=5)
        self.cantidad_neutrones = tk.Entry(root)
        self.cantidad_neutrones.pack(pady=5)

        tk.Label(root, text="Número del elemento:").pack(pady=5)
        self.numero_elemento = tk.Entry(root)
        self.numero_elemento.pack(pady=5)

      
        tk.Button(root, text="Agregar elemento", command=self.agregar_elemento).pack(pady=10)
        tk.Button(root, text="Volver", command=root.quit).pack(pady=10)

    def agregar_elemento(sel):
        print("Elemento agregado:")
        print(f"Átomo: {self.nombre_atomo.get()}")
        print(f"Electrones: {self.cantidad_electrones.get()}")
        print(f"Protones: {self.cantidad_protones.get()}")
        print(f"Neutrones: {self.cantidad_neutrones.get()}")
        print(f"Número del elemento: {self.numero_elemento.get()}")

root = tk.Tk()
app = VentanaAtomos(root)
root.mainloop()
