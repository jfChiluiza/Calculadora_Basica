import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
    if value == "C":
        entry_var.set("")
    elif value == "DEL":
        entry_var.set(entry_var.get()[:-1])
    elif value == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
        except Exception:
            messagebox.showerror("Error", "Entrada inválida")
    else:
        entry_var.set(entry_var.get() + value)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("400x600")
root.config(bg="black")

# Variable para mostrar el texto en la entrada
entry_var = tk.StringVar()

# Entrada para mostrar la expresión o el resultado
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 28), justify="right", bg="white", fg="black", bd=10, relief="ridge")
entry.pack(fill="both", padx=10, pady=10)

# Configuración de botones
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["C", "0", "DEL", "="],
    ["+"]
]

# Mapeo de operadores para eval
operator_map = {"÷": "/", "×": "*"}

# Creación de botones
for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand=True)
    for button in row:
        btn_color = "red" if button == "C" else "gold"
        btn = tk.Button(
            frame,
            text=button,
            font=("Arial", 20),
            bg=btn_color,
            fg="black",
            bd=5,
            relief="ridge",
            command=lambda value=operator_map.get(button, button): on_button_click(value)
        )
        btn.pack(side="left", padx=10, pady=10)
        btn.config(width=4, height=2)
        btn.config(borderwidth=2, highlightbackground="black", highlightcolor="black", relief="ridge")
        btn.config(height=2, width=2)
        btn.update_idletasks()
        btn.config(width=5, height=2)

# Bucle principal de la aplicación
root.mainloop()
