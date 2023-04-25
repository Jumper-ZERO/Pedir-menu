class Facturacion:
    def __init__(self):
        pass 

    def Menu(self):
        print("------------------------------------------------")
        print("|○○○○○○○○○○             Cena         ○○○○○○○○○○|")
        print("|==============================================|")
        print("| A |Pizza Express                    |S/.9.50 |")
        print("| B |Ensalada Campera                 |S/.7.50 |")
        print("| C |Gazpacho                         |S/.6.00 |")
        print("| D |Caldo de gallina                 |S/.6.00 |")
        print("| E |Pollo al horno                   |S/.6.00 |")
        print("| F |Menestrón                        |S/.5.50 |")
        print("| G |====================SALIR=================|")
        print("|==============================================|")
        input("\nPresione ENTER para continuar.......!!!\n")
    
    def Desayuno(self):
        print("------------------------------------------------")
        print("|○○○○○○○○○○           Desayuno       ○○○○○○○○○○|")
        print("|==============================================|")
        print("| A |Café                             |S/.4.50 |")
        print("| B |Chocolate                        |S/.5.00 |")
        print("| C |Jugo con Fresas                  |S/.9.00 |")
        print("| D |Jugo de Papaya                   |S/.8.00 |")
        print("| E |Pan con pollo                    |S/.7.00 |")
        print("| F |Pan con jamón                    |S/.7.00 |")
        print("| G |Pan con tortilla                 |S/.7.00 |")
        print("| J |===================SALIR==================|")
        print("|==============================================|")

    def Almuerzo(self):
        print("------------------------------------------------")
        print("|○○○○○○○○○○          Almuerzo        ○○○○○○○○○○|")
        print("|==============================================|")
        print("| A |Sopa de res                     |S/.10.00 |")
        print("| B |Ensalada de verdura             |S/.8.00  |")
        print("| C |Pachamanca de 2 carnes          |S/.20.00 |")
        print("| D |Trucha frita                    |S/.15.00 |")
        print("| E |Costillar de cordero frito      |S/.25.00 |")
        print("| F |Arroz con mariscos              |S/.20.00 |")
        print("| G |Lomo saltado                    |S/.23.00 |")
        print("| J |====================SALIR=================|")
        print("|==============================================|")

    def Cena(self):
        print("------------------------------------------------")
        print("|○○○○○○○○○○             Cena         ○○○○○○○○○○|")
        print("|==============================================|")
        print("| A |Pizza Express                    |S/.9.50 |")
        print("| B |Ensalada Campera                 |S/.7.50 |")
        print("| C |Gazpacho                         |S/.6.00 |")
        print("| D |Caldo de gallina                 |S/.6.00 |")
        print("| E |Pollo al horno                   |S/.6.00 |")
        print("| F |Menestrón                        |S/.5.50 |")
        print("| G |====================SALIR=================|")
        print("|==============================================|")

    def Boleta(self):
        print("================================================")
        print("|○○○○○○○○○○      BOLETA DE VENTA     ○○○○○○○○○○|")
        print("|==============================================|")
        print("| Subtotal       :                             |")
        print("| IGV            :                             |")
        print("| Total a pagar  :                             |")
        print("|                                              |")
        print("|             Gracias por tu compra            |")
        print("|==============================================|")

# Bloque principal
Factura1=Facturacion()
Factura1.Menu()
Factura1.Desayuno()
Factura1.Almuerzo()
Factura1.Cena()
Factura1.Boleta()
