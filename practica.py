class BaseDeDatos:
    def __init__(self):
        self.ListaArt = []
        self.IVA = 17.5/100
        self.Lista =[]
        self.Tamaño = len(self.Lista)
        self.bandera = 0
    def Altas(self):
        respuesta = 0
        while respuesta == 0:
            articulo1 = input("articulo: ")
            Codigo = input("codigo: ")
            precio = int(input("precio: "))
            stock = int(input("stock: "))
            cupon = (1-float(input('descuento: ')))/100
            articulo = Articulo(articulo1,Codigo,precio,stock,cupon)
            self.Lista.append(articulo)
            self.ListaArt.append(articulo.Articulo)
            respuesta = int(input("1 para salir/n 0 para seguir"))
            
            self.Tamaño = len(self.Lista)
        self.CrearRepositorio()
            
        print(self.ListaArt)
    def buscar(self,buscador):
        print(self.Tamaño)
        
        for i in range (0,self.Tamaño):
            if self.Lista[i].Articulo == buscador:
                print("Articulo: ",self.Lista[i].Articulo,"\nPrecio: ",self.Lista[i].Precio,"\nCantidad en Stock: ",self.Lista[i].CTotal)
                self.bandera = i
      

    def Bajas(self):
        self.Baja = input("Articulo a dar de baja")
        self.buscar(self.Baja)
        if self.Lista[self.bandera] in self.Lista:
            self.Lista.remove(self.Lista[self.bandera])
            print(self.Lista)
        else:
            print("el elemento no esta en el almacen")
    def cambios(self):
        respuesta = 0
        while respuesta != 1:
            respuesta = input("Qué deseas cambiar /n Precio/nStock/nCupon/nIVA/nNada")
            if respuesta == "Precio":
                self.Precio = float(input("Precio:"))
            if respuesta == "Stock":
                self.CTotal = float(input("Stock:"))
            if respuesta == "Cupon":
                self.Cupon = float(input("Cupon:"))
            if respuesta == "IVA":
                self.IVA = float(input("IVA:"))/100
            if respuesta == "Nada":
                break
        pass
    def Listar(self):
        self.Tamaño = len(self.Lista)
        if self.Tamaño > 0:
            for i in range(0,self.Tamaño):
                print("Articulo:",self.Lista[i].Articulo)
                print("Clave:",self.Lista[i].Clave,"\nPrecio:",self.Lista[i].Precio,"\nStock:",self.Lista[i].CTotal)
        else:
            print("No hay algun objeto en el almacen")
    def ModificarIVA(self):
        self.IVA = float(input("IVA Nuevo: "))/100
    def CrearRepositorio(self):
        
        for i in range(0,self.Tamaño):
            self.repositorio = open('Tiendita_mia_como_te_quiero.txt', 'a')
            L1 = self.Lista[i].Articulo
            L2 = self.Lista[i].Clave
            self.repositorio.writelines(L1)
            self.repositorio.writelines("\n")
            self.repositorio.writelines(L2)
            self.repositorio.close
       
    def DelRepositorio(self):
        del self.repositorio
    def Venta(self):
        venta = input("articulo a comprar: ")
        self.buscar(venta)
        self.cantidad = int(input("cantidad a comprar: "))
        self.Lista[self.bandera].CTotal -= self.cantidad
        print("cantidad a pagar: ",self.Lista[self.bandera].Precio*self.cantidad)
        self.Lista[self.bandera].CVendida += self.cantidad
        if self.Lista[self.bandera].CTotal < 0:
            self.Lista[self.bandera].CTotal = self.Lista[self.bandera].CTotal+self.cantidad
            
            print("solo se puede comprar ",self.Lista[self.bandera].CTotal,"\n desea seguir comprando?")
            respuesta = input()
            if respuesta == "si":
                self.Venta()
            if respuesta == "no":
                pass




class Articulo:
    def __init__(self,Articulo,Clave,Precio,CTotal,Cupon):
        self.Articulo = Articulo
        self.Clave = Clave
        self.Precio = Precio
        self.CVendida = 0
        self.CTotal = CTotal-self.CVendida
        self.Cupon = Cupon
        pass
    def ModificarStock(self,):
        self.CTotal += int(input("Agregar a Srock:"))
    def ModificarCupon(self):
        self.Cupon = float(input("Nuevo Cupon: "))





