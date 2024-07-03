import os, time

from funciones import *

while True:
    os.system('cls')
    print("\tGAXPLOSIVE")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")

    opc=int(input("ingrese opción:"))

    if opc ==1:
        registrar_pedido()
    elif opc==2:
        listar_pedidos()
    elif opc==3:
        buscar_pedido_rut()
    elif opc==4:
        imprimir_hoja_ruta()
    elif opc==5:
        salir()
    else:
        print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!!")
    time.sleep(3)