"""""""""""""""""""""""""""""""""""""""""""""""
        Escuela Politécnica Nacional
                PROYECTO 
Nombre: Jared Isaac Benavides Gavilánez
Grupo: GR1
Tema: conversor de unidades con aproximación
"""""""""""""""""""""""""""""""""""""""""""""""

#Importar bibliotecas
import tkinter as tk


#Definir funciones para cada conversión que se desee
def metros_a_pies(metros):
    pies = metros * 3.2808398950131235
    return pies

def pies_a_metros(pies):
    metros = pies / 3.2808398950131235
    return metros

def kPa_a_psi (kPa):
    psi = kPa/6.89475729316836094
    return psi

def psi_a_kPa (psi):
    kPa = psi*6.8947572931683609
    return kPa

def C_a_F (C):
    F = (C*9/5)+32
    return F

def F_a_K (F):
    K = (F-32)*9/5+273.15
    return K

def C_a_K(C):
    K = C+273.15
    return K

def kJ_a_BTU(kJ):
    BTU = kJ*0.9478171000000001
    return BTU

def BTU_a_kJ(BTU):
    kJ= BTU/0.9478171000000001
    return kJ

def lbf_a_N(lbf):
    N= lbf*4.4482216152605005
    return N

def N_a_lbf(N):
    lbf = N/4.4482216152605005
    return lbf

def kW_a_hp(kW):
    hp = kW*1.3410220895950278
    return hp

def hp_a_kW(hp):
    kW = hp/1.3410220895950278
    return kW


def convertir():
    valor = float(input_entry.get()) #valor a transformar por el usuario
    cifras_decimales = int(cifras_decimales_entry.get()) #Entrada de cifras significativas que necesita el usuario.


#Generar las condiciones para cada conversión y que genere un resultado visible aproximado a las cifras significativas necesarias.
    if unidad_var.get() == "Metros a Pies":
        resultado = metros_a_pies(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} metros equivale a: {resultado_redondeado:.{cifras_decimales}f} pies.")
        
    elif unidad_var.get() == "Pies a Metros":
        resultado = pies_a_metros(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} pies equivale a: {resultado_redondeado:.{cifras_decimales}f} metros.")
        
    elif unidad_var.get() == "kPa a psi":
        resultado = kPa_a_psi(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} kPa equivale a: {resultado_redondeado:.{cifras_decimales}f} psi.")

    elif unidad_var.get() == "psi a kPa":
        resultado = psi_a_kPa(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} psi equivale a: {resultado_redondeado:.{cifras_decimales}f} kPa.")
        
    elif unidad_var.get() == "°C a °F":
        resultado = C_a_F(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} °C equivale a: {resultado_redondeado:.{cifras_decimales}f} °F.")

    elif unidad_var.get() == "°C a K":
        resultado = C_a_K(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} °C equivale a: {resultado_redondeado:.{cifras_decimales}f} K.")        

    elif unidad_var.get() == "°F a K":
        resultado = F_a_K(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} °F equivale a: {resultado_redondeado:.{cifras_decimales}f} K.")

    elif unidad_var.get() == "kJ a BTU":
        resultado = kJ_a_BTU(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} kJ equivale a: {resultado_redondeado:.{cifras_decimales}f} BTU.")

    elif unidad_var.get() == "BTU a kJ":
        resultado = BTU_a_kJ(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} BTU equivale a: {resultado_redondeado:.{cifras_decimales}f} kJ.")

    elif unidad_var.get() == "N a lbf":
        resultado = N_a_lbf(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} N equivale a: {resultado_redondeado:.{cifras_decimales}f} lbf.")

    elif unidad_var.get() == "lbf a N":
        resultado = lbf_a_N(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} lbf equivale a: {resultado_redondeado:.{cifras_decimales}f} N.")

    elif unidad_var.get() == "kW a hp":
        resultado = kW_a_hp(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} kW equivale a: {resultado_redondeado:.{cifras_decimales}f} hp.")

    elif unidad_var.get() == "hp a kW":
        resultado = hp_a_kW(valor)
        resultado_redondeado = round(resultado, cifras_decimales)
        output_label.config(text=f"{valor} hp equivale a: {resultado_redondeado:.{cifras_decimales}f} kW.")

# Crear ventana principal
root = tk.Tk()
root.title("Transformador de Unidades")

# Crear etiqueta y entrada para ingresar el valor
input_label = tk.Label(root, text="Ingrese el valor:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Agregar una entrada para ingresar el número de cifras decimales deseadas
cifras_decimales_label = tk.Label(root, text="Número de cifras decimales:")
cifras_decimales_label.pack()
cifras_decimales_entry = tk.Entry(root)
cifras_decimales_entry.pack()
 
# Crear lista desplegable para seleccionar la unidad de conversión
opciones_unidades = ["Metros a Pies", "Pies a Metros", "kPa a psi", "psi a kPa", "°C a °F", "°C a K", "°F a K", "kJ a BTU", "BTU a kJ", "N a lbf", "lbf a N", "kW a hp", "hp a kW" ]
unidad_var = tk.StringVar(value=opciones_unidades[0])
unidad_menu = tk.OptionMenu(root, unidad_var, *opciones_unidades)
unidad_menu.pack()

# Crear botón para realizar la conversión
convertir_button = tk.Button(root, text="Convertir", command=convertir)
convertir_button.pack()

# Crear etiqueta para mostrar el resultado de la conversión
output_label = tk.Label(root, text="")
output_label.pack()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
