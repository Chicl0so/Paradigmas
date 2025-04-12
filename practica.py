class BaseDeDatos:
    def __init__(self):
        self.ListaArt = []
        self.IVA = 1+17.5/100
        self.Lista =[]
        self.Tamaño = len(self.Lista)
        self.bandera = 0
        self.Veces =0
        self.repositorio = ""
    def Altas(self):
        respuesta = 0
        while respuesta == 0:
            articulo1 = input("articulo: ")
            Codigo = input("codigo: ")
            precio = int(input("precio: "))
            stock = int(input("stock: "))
            cupon = 1-(float(input('descuento: ')))/100
            articulo = Articulo(articulo1,Codigo,precio,stock,cupon)
            self.Lista.append(articulo)
            self.ListaArt.append(articulo.Articulo)
            respuesta = int(input("1 para salir/n 0 para seguir"))
            
            self.Tamaño = len(self.Lista)
            self.CrearRepositorio()
        
            
        print(self.ListaArt)
    def buscar(self,buscador):
        if self.Tamaño == 0:
            print("No hay objetos en el almacen")
            self.bandera = 0
            
        else:
            for i in range (0,self.Tamaño):
                if self.Lista[i].Articulo == buscador:
                    print("Articulo: ",self.Lista[i].Articulo,"\nPrecio: ",self.Lista[i].Precio,"\nCantidad en Stock: ",self.Lista[i].CTotal)
                    self.bandera = i
        

    def Bajas(self):
        self.Baja = input("Articulo a dar de baja")
        self.buscar(self.Baja)
        if self.Tamaño != 0:
            if self.Lista[self.bandera] in self.Lista:
                self.Lista.remove(self.Lista[self.bandera])
                self.Tamaño = len(self.Lista)
                self.Listar()
                self.CrearRepositorio()
        else:
            print("el elemento no esta en el almacen")
    def cambios(self):
        respuesta = 0
        while respuesta != 1:
            respuesta = input("Qué deseas cambiar /n Precio/nStock/nCupon/nIVA/nNada")
            if respuesta == "Precio":
                busca = input("objeto a cambiar:")
                self.buscar(busca)
                self.Lista[self.bandera].Precio = float(input("Precio:"))
            if respuesta == "Stock":
                busca = input("objeto a cambiar:")
                self.buscar(busca)
                self.Lista[self.bandera].Stock = int(input("Stock:"))
            if respuesta == "Cupon":
                busca = input("objeto a cambiar:")
                self.buscar(busca)
                self.Lista[self.bandera].Cupon = 1-float(input("descuento:"))/100
            if respuesta == "IVA":
                self.ModificarIVA()
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
        self.IVA =1+ float(input("IVA Nuevo: "))/100
        self.CrearRepositorio()
    def CrearRepositorio(self):
        self.Veces += 1
        self.trrrr = str(self.Veces)
        nombre = "Tiendita_mia_como_te_quiero"+self.trrrr+".txt"
        for i in range(0,self.Tamaño):
            self.repositorio = open("Tiendita_mia_como_te_quiero.txt", 'a')
            L1 = self.Lista[i].Articulo
            L2 = self.Lista[i].Clave
            L3 = str(self.Lista[i].Precio)
            L4 = str(self.Lista[i].CVendida)
            L5 = str(self.Lista[i].CTotal)
            L6 = str(self.Lista[i].Cupon)
            L7 = str(self.IVA)

            self.repositorio.write(L1)
            self.repositorio.write(" ")
            self.repositorio.write(L2)
            self.repositorio.write(" ")
            self.repositorio.write(L3)
            self.repositorio.write(" ")
            self.repositorio.write(L4)
            self.repositorio.write(" ")
            self.repositorio.write(L5)
            self.repositorio.write(" ")
            self.repositorio.write(L6)
            self.repositorio.write(" ")
            self.repositorio.write(L7)
            self.repositorio.write("\n")
            
            self.repositorio.close
       
    def DelRepositorio(self):
        borrar = input("Repositorio a borrar: ")
        os.remove(borrar)
    def Venta(self):
        venta = input("articulo a comprar: ")
        self.buscar(venta)
        if venta in self.Lista:
            self.cantidad = int(input("cantidad a comprar: "))
            if self.cantidad >= 3:
                self.Lista[self.bandera].CTotal -= self.cantidad
                print("cantidad a pagar: ",self.Lista[self.bandera].Precio*self.cantidad*self.Lista[self.bandera].Cupon*self.IVA)
                self.Lista[self.bandera].CVendida += self.cantidad
            if self.cantidad < 3:
                self.Lista[self.bandera].CTotal -= self.cantidad
                print("cantidad a pagar: ",self.Lista[self.bandera].Precio*self.cantidad*self.IVA)
                self.Lista[self.bandera].CVendida += self.cantidad

            if self.Lista[self.bandera].CTotal < 0:
                self.Lista[self.bandera].CTotal = self.Lista[self.bandera].CTotal+self.cantidad
                
                print("solo se puede comprar ",self.Lista[self.bandera].CTotal,"\n desea seguir comprando?")
                respuesta = input()
                if respuesta == "si":
                    self.Venta()
                if respuesta == "no":
                    pass
            self.CrearRepositorio()
        else:
            print("El objeto no esta disponible")            



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





