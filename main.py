from temperatura_conversao import (
    Celsius_para_Fahrenheit, Celsius_para_Kelvin,
    Fahrenheit_para_Celsius, Fahrenheit_para_Kelvin,
    Kelvin_para_Celsius, Kelvin_para_Fahrenheit
)

def main():
    e = input("Escolha uma letra\na - Celsius para Fahrenheit\nb - Celsius para Kelvin\nc - Fahrenheit para Celsius\nd - Fahrenheit para Kelvin\ne - Kelvin para Celsius\nf - Kelvin para Fahrenheit\n")
    x = float(input("Digite a temperatura: "))
    
    if e == 'a':
        print("em Celsius.")
        x = Celsius_para_Fahrenheit(x)
        print("Em Fahrenheit:\n{:.2f}".format(x))
    elif e == 'b':
        print("em Celsius.")
        x = Celsius_para_Kelvin(x)
        print("Em Kelvin:\n{:.2f}".format(x))
    elif e == 'c':
        print("em Fahrenheit.")
        x = Fahrenheit_para_Celsius(x)
        print("Em Celsius:\n{:.2f}".format(x))
    elif e == 'd':
        print("em Fahrenheit.")
        x = Fahrenheit_para_Kelvin(x)
        print("Em Kelvin:\n{:.2f}".format(x))
    elif e == 'e':
        print("em Kelvin.")
        x = Kelvin_para_Celsius(x)
        print("Em Celsius:\n{:.2f}".format(x))
    elif e == 'f':
        print("em Kelvin.")
        x = Kelvin_para_Fahrenheit(x)
        print("Em Fahrenheit:\n{:.2f}".format(x))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
