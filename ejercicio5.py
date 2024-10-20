import tkinter as tk

class VentanaConfiguracionElectronica:
    def __init__(self, root):
        root.title("Configuración Electrónica")
        root.geometry("400x200")
        
        tk.Label(root, text="Configuración Electrónica", font=("Arial", 14)).pack(pady=10)
        tk.Button(root, text="Determinar configuración electrónica", command=self.determinar_configuracion).pack(pady=10)
        self.resultado_label = tk.Label(root, text="Configuración electrónica = ...")
        self.resultado_label.pack(pady=10)
    
        tk.Button(root, text="Volver", bg="red", command=root.quit).pack(pady=10)

    def determinar_configuracion(self):
        configuracion = "1s2 2s2 2p6 3s2 3p6"
        self.resultado_label.config(text=f"Configuración electrónica = {configuracion}")

root = tk.Tk()
app = VentanaConfiguracionElectronica(root)
root.mainloop()
