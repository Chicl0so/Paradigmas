import practica 
Ferreteria = practica.BaseDeDatos()
def Interfaz():
    respuesta = input("1.Comprar\n2.Cambiar Algo\n3.Agregar Articulo\n4.Dar de baja algun articulo\n5.Listar\n6.Salir")
    if respuesta == "1":
        Ferreteria.Venta()
        Interfaz()
    if respuesta == "2":
        Ferreteria.cambios()
        Interfaz()
    if respuesta == "3":
        Ferreteria.Altas()
        Interfaz()
    if respuesta == "4":
        Ferreteria.Bajas()
        Interfaz()
    if respuesta == "5":
        Ferreteria.Listar()
        Interfaz()
    
Interfaz()
