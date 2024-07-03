import os

pedidos = []
cilindro_2 = 25500
cilindro_1 = 12500

def salir():
    print("Gracias por usar el sistema de pedido GAXPLOSIVE")
    exit()


def registrar_pedido():
    os.system('cls')
    rut = (input("Ingrese rut (sin guión y sin punto): "))
    if not rut ==9:
         print("ERROR! ingrese rut de 9 digitos")
    else:
         return
    
    nombre = input("Ingrese nombre: ")
    if len(nombre) <= 3:
        print("Ingrese nombre de mas de 3 caracteres")
    else:
        return

    direccion = input("Ingrese dirección: ")
    if direccion == str(1):
         print(f"su dirección: {direccion}")
    else:
         print("Ingrese dirección")
         return(direccion)

    comuna = input("Ingrese una opción de las siguientes comunas (s: santiago, p: pirque, c: colina): ").lower
    if comuna =="s":
         print("comuna seleccionada: santiago")
    elif comuna =="p":
         print("comuna seleccionada: pirque")
    elif comuna =="c":
         print("comuna seleccionada: colina")
    else: 
         print("seleccione comuna")

    comuna_seleccionada = comuna
    comuna_seleccionada.append(comuna)
    while True:  
        gas = int(input("Ingrese una de las opciones: (1: 5kg, 2: 15kg)"))
        if gas==1:
                cantidad_gas_1 = int(input("Indique cantidad de cilindros que desea pedir: "))
                total_1 = cantidad_gas_1*cilindro_1
        elif gas==2:
                cantidad_gas_2 = int(input("Ingrese cantidad de cilindros que desea pedir: "))
                total_2 = cantidad_gas_2*cilindro_2 
        else:
            si_o_no= input("desea volver a pedir cilindros (s: si, n: no)").lower
            if si_o_no =="s":
                 return gas
                    
            else:
                pedidos.append(rut,nombre,direccion,comuna, cantidad_gas_1, cantidad_gas_2, total_1, total_2)

                print("PEDIDO COMPLETADO! ")
                print(f"PEDIDO: RUT:{rut}, Nombre: {nombre}, DIRECCIÓN:{direccion}, COMUNA:{comuna}, CIL.5KG: {total_1} CIL. 15KG: {total_2}, TOTAL: {total_1+total_2}")


def listar_pedidos():
    os.system('cls')
    print("\tPEDIDOS")
    for p in pedidos:
        print(p)
    print(pedidos)


def buscar_pedido_rut():
    os.system('cls')
    rut = input("ingrese rut: ")
    rut_buscado= pedidos.index(rut)
    print(rut_buscado)



def imprimir_hoja_ruta():
    os.system('cls')
    import csv
    
    comuna = input("Ingrese comuna (s: santiago, p: pirque, c: colina): ").lower
    if comuna =="s":
         print("comuna seleccionada: santiago")
    elif comuna =="p":
         print("comuna seleccionada: pirque")
    elif comuna =="c":
         print("comuna seleccionada: colina")
    else: 
         print("seleccione comuna")

    comuna_seleccionada = comuna
    comuna_seleccionada.append(comuna)     

    with open ('imprimir_hoja_de_ruta.csv','a', newline='') as archivo:
         escritor= archivo(pedidos)
         



