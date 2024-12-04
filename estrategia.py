import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivina:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Mental")

        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.max_rango = None
        self.numero_a_adivinar = None
        self.intentos_maximos = None
        self.intentos = 0
        self.resultados = []

        self.iniciar_juego_button = tk.Button(self.root, text="Iniciar Juego", command=self.configurar_rango, width=20, height=2)
        self.iniciar_juego_button.pack(pady=20)

        self.numero_label = tk.Label(self.root, text="Introduce un número", font=("Arial", 12))
        self.numero_label.pack(pady=10)

        self.numero_entry = tk.Entry(self.root, font=("Arial", 14), width=10)
        self.numero_entry.pack(pady=10)

        self.intentos_label = tk.Label(self.root, text="Intentos: 0", font=("Arial", 12))
        self.intentos_label.pack(pady=10)

        self.comprobar_button = tk.Button(self.root, text="Comprobar", command=self.comprobar_intento, state=tk.DISABLED, width=20, height=2)
        self.comprobar_button.pack(pady=20)

        self.resultados_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.resultados_label.pack(pady=10)

        self.intentos_maximos = 5  # Máximo de intentos
        self.intentos = 0
        self.numero_a_adivinar = 0

    def configurar_rango(self):
        try:
            self.max_rango = int(self.numero_entry.get())
            if self.max_rango <= 0:
                messagebox.showerror("Error", "El número máximo debe ser mayor que 0.")
                return
            self.intentos_maximos = self.max_rango // 20
            self.numero_a_adivinar = random.randint(1, self.max_rango)
            self.resultados = ["falló"] * self.max_rango
            self.resultados[self.numero_a_adivinar - 1] = "acertó"

            self.numero_label.config(text=f"Adivina el número entre 1 y {self.max_rango}")
            self.comprobar_button.config(state=tk.NORMAL)
            self.iniciar_juego_button.config(state=tk.DISABLED)
            self.numero_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar un número entero válido.")

    def comprobar_intento(self):
        try:
            numero_usuario = int(self.numero_entry.get())
            if numero_usuario < 1 or numero_usuario > self.max_rango:
                messagebox.showerror("Error", f"Introduce un número entre 1 y {self.max_rango}.")
                return
        except ValueError:
            messagebox.showerror("Error", "Debes introducir un número entero válido.")
            return

        self.intentos += 1

        self.intentos_label.config(text=f"Intentos: {self.intentos} de {self.intentos_maximos}")

        if numero_usuario == self.numero_a_adivinar:
            messagebox.showinfo("¡Felicidades!", f"¡Has acertado el número {self.numero_a_adivinar} en {self.intentos} intentos!")
            self.mostrar_resultados()
            self.iniciar_juego()
        else:
            if numero_usuario < self.numero_a_adivinar:
                self.resultados_label.config(text="""¡Tu número es demasiado bajo! 
            Intenta con un número más alto.""")
            else:
                self.resultados_label.config(text="""¡Tu número es demasiado alto! 
            Intenta con un número más bajo.""")

            if self.intentos >= self.intentos_maximos:
                messagebox.showinfo("¡Juego terminado!", f"Se acabaron los intentos. El número correcto era: {self.numero_a_adivinar}")
                self.mostrar_resultados()
                self.iniciar_juego()

    def mostrar_resultados(self):
        resultados_str = "Resultados:\n" + ", ".join(self.resultados)
        messagebox.showinfo("Estado del Juego", resultados_str)

    def iniciar_juego(self):
        self.numero_label.config(text="Introduce un número")
        self.numero_entry.delete(0, tk.END)
        self.comprobar_button.config(state=tk.DISABLED)
        self.iniciar_juego_button.config(state=tk.NORMAL)


root = tk.Tk()
juego = JuegoAdivina(root)
root.mainloop()