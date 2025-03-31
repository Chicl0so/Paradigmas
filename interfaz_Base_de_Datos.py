import practica 
Ferreteria = practica.BaseDeDatos()
def Interfaz():
    respuesta = input("1.Comprar\n2.Cambiar Algo\n3.Agregar Articulo\n4..Dar de baja algun articulo\n5.Listar\n6.Salir")
    if respuesta == "1":
        Base1.Venta()
        Interfaz()
    if respuesta == "2":
        Base1.Cambios()
        Interfaz()
    if respuesta == "3":
        Base1.Altas()
        Interfaz()
    if respuesta == "4":
        Base1.Bajas()
        Interfaz()
    if respuesta == "5":
        Base1.Listar()
        Interfaz()
    
Interfaz()
