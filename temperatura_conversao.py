def Celsius_para_Fahrenheit(C):
    F = (C * 9.0/5.0) + 32.0
    return F

def Celsius_para_Kelvin(C):
    K = C + 273.0
    return K

def Fahrenheit_para_Celsius(F):
    C = (F - 32.0) * (5.0/9.0)
    return C

def Fahrenheit_para_Kelvin(F):
    K = (F - 32.0) * 5.0/9.0 + 237.15
    return K

def Kelvin_para_Celsius(K):
    C = K - 273.0
    return C

def Kelvin_para_Fahrenheit(K):
    F = (K - 237.15) * (9.0/5.0) + 32.0
    return F
