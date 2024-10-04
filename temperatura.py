import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow  imagens PNG

def Celsius_para_Fahrenheit(C):
    return (C * 9.0 / 5.0) + 32.0

def Celsius_para_Kelvin(C):
    return C + 273.0

def Fahrenheit_para_Celsius(F):
    return (F - 32.0) * (5.0 / 9.0)

def Fahrenheit_para_Kelvin(F):
    return (F - 32.0) * 5.0 / 9.0 + 273.15

def Kelvin_para_Celsius(K):
    return K - 273.0

def Kelvin_para_Fahrenheit(K):
    return (K - 273.15) * (9.0 / 5.0) + 32.0

def determinar_clima(temperatura):
    if temperatura < 15:
        return "Fria"
    elif 15 <= temperatura <= 25:
        return "Aconchegante"
    else:
        return "Quente"

def atualizar_imagem(temperatura):
    if temperatura < 15:
        img = img_fria
    elif 15 <= temperatura <= 25:
        img = img_aconchegante
    else:
        img = img_quente

    canvas.delete("all")  
    canvas.create_image(50, 50, image=img) 

def converter():
    try:
        valor = float(entry_value.get())
        if selected_conversion.get() == "Celsius para Fahrenheit":
            resultado = Celsius_para_Fahrenheit(valor)
        elif selected_conversion.get() == "Celsius para Kelvin":
            resultado = Celsius_para_Kelvin(valor)
        elif selected_conversion.get() == "Fahrenheit para Celsius":
            resultado = Fahrenheit_para_Celsius(valor)
        elif selected_conversion.get() == "Fahrenheit para Kelvin":
            resultado = Fahrenheit_para_Kelvin(valor)
        elif selected_conversion.get() == "Kelvin para Celsius":
            resultado = Kelvin_para_Celsius(valor)
        elif selected_conversion.get() == "Kelvin para Fahrenheit":
            resultado = Kelvin_para_Fahrenheit(valor)
        else:
            resultado = "Opção inválida."
        
       
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
        
      
        clima = determinar_clima(resultado)
        label_clima.config(text=f"Clima: {clima}")
        
       
        atualizar_imagem(resultado)

    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.")
        label_clima.config(text="Clima: ")


root = tk.Tk()
root.title("Conversor de Temperatura")
root.configure(bg="black")


style = ttk.Style()
style.configure("TButton", foreground="white", background="black")
style.configure("TLabel", foreground="white", background="black")


entry_value = ttk.Entry(root)
entry_value.grid(column=1, row=0, padx=10, pady=10)


label_instructions = ttk.Label(root, text="Digite a temperatura:")
label_instructions.grid(column=0, row=0, padx=10, pady=10)

selected_conversion = tk.StringVar()
combo_conversao = ttk.Combobox(root, textvariable=selected_conversion)
combo_conversao['values'] = [
    "Celsius para Fahrenheit",
    "Celsius para Kelvin",
    "Fahrenheit para Celsius",
    "Fahrenheit para Kelvin",
    "Kelvin para Celsius",
    "Kelvin para Fahrenheit"
]
combo_conversao.grid(column=0, row=1, padx=10, pady=10)
combo_conversao.current(0)  

# Botão 
button_converter = ttk.Button(root, text="Converter", style="TButton", command=converter)
button_converter.grid(column=1, row=1, padx=10, pady=10)

# Label 
label_resultado = ttk.Label(root, text="Resultado: ", style="TLabel")
label_resultado.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Label quente ou fria
label_clima = ttk.Label(root, text="Clima: ", style="TLabel")
label_clima.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

#  exibir a imagem
canvas = tk.Canvas(root, width=100, height=100, bg="black", highlightthickness=0)
canvas.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Carregar imagens
img_fria = ImageTk.PhotoImage(Image.open("Cold Emoji.png").resize((100, 100)))
img_aconchegante = ImageTk.PhotoImage(Image.open("Relieved Emoji.png").resize((100, 100)))
img_quente = ImageTk.PhotoImage(Image.open("Hot Emoji.png").resize((100, 100)))

# Iniciar o loop da interface
root.mainloop()
