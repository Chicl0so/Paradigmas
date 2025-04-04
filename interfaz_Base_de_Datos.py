import practica 
Ferreteria = practica.BaseDeDatos()
def Interfaz():
    respuesta = "0"
    while respuesta != "8":
        respuesta = input("1.Comprar\n2.Cambiar Algo\n3.Agregar Articulo\n4.Dar de baja algun articulo\n5.Listar\n6.Crear Repositorio\n7.Borrar Repositorio\n9.Sair")
        if respuesta == "1":
            Ferreteria.Venta()
            
        if respuesta == "2":
            Ferreteria.cambios()
            
        if respuesta == "3":
            Ferreteria.Altas()
            
        if respuesta == "4":
            Ferreteria.Bajas()
            
        if respuesta == "5":
            Ferreteria.Listar()
           
        if respuesta == "6":
            Ferreteria.CrearRepositorio()
          
        if respuesta == "7":
            Ferreteria.DelRepositorio()
            
    
Interfaz()
