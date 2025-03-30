class BaseDeDatos:
    def __init__(self,Articulo,Clave,Precio,CVendida,CTotal,Cupon):
        self.ListaArt = []
        self.Articulo = Articulo
        self.Clave = Clave
        self.Precio = Precio
        self.CVendida = CVendida
        self.CTotal = CTotal
        self.Cupon = Cupon
        self.IVA = 17.5/100
        self.Lista =[]
        self.Tamaño = len(self.Lista)
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
      

    def Bajas(self,Baja):
        self.Lista.remove(Baja)
        print(self.Lista)
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
        
        for i in range(0,self.Tamaño):
            print(self.ListaArt[i])
            print(self.Lista[i].Clave,"\n",self.Lista[i].Precio,"\n",self.Lista[i].CTotal)
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
      
        cantidad = int(input("cantidad a comprar: "))
        self.Lista[self.bandera].CTotal -= cantidad
        if self.Lista[self.bandera].CTotal < 0:
            print("solo se puede comprar ",self.Lista[self.bandera].CTotal+cantidad,"\n desea seguir comprando?")
            respuesta = input()
            if respuesta == "no":
                self.Lista[self.bandera].CTotal = self.Lista[self.bandera].CTotal+cantidad
            if respuesta == "si":
                self.Venta()




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





Jugo = Articulo("Jugo","001",12,100,0.75)
dulce = Articulo("Dulce","002",5,100,0.5)
Base = BaseDeDatos(0,0,0,0,0,0)

print(Jugo.CTotal)
Base.Altas()

Base.Venta()
Base.Listar()
