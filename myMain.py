# Programa de calculo de ventas
# Autor: Jerremi Aron Chancan Labajos

#Datos de prueba
cena=[
    ("Pizza Express", 9.50),
    ("Ensalada Campera",7.50),
    ("Caldo de gallina",6.00),
    ("Pollo al horno",6.00),
    ("Menestrón",5.50)
]
desayuno=[
    ("Café", 4.5),
    ("Chocolate", 5),
    ("Jugo con Fresas", 9),
    ("Jugo de Papaya", 8),
    ("pan con pollo", 7),
    ("Pan con jamón", 7),
    ("Pan con tortilla", 7)
]
almuerzo=[
    ("Sopa de res", 10),
    ("Ensalada de verdura", 8),
    ("Pachamanca de 2 carnes", 20),
    ("Trucha frita", 15),
    ("Costillar de cordero frito", 25),
    ("Arroz con mariscos", 20),
    ("Lomo saltado", 23)
]

#Definir funciones

    
def Titulo(mjs):
    mensaje=mjs.capitalize() 
    
    if len(mensaje) % 2 != 0: # Error de espacio
        mensaje += " "
    
    mensaje=" "*4+mensaje+" "*4
    lineas=46
    lineas_por_lado=((lineas-len(mensaje))//2)
    if len(mensaje) % 2 != 0:
        lineas_por_lado += 1
    print("|"+"="*46+"|")
    print(f"|{'○'*lineas_por_lado}{mensaje}{'○'*lineas_por_lado}|")
    print("|"+"="*46+"|")

def Salida(Letra_final):
    print(f"| {Letra_final}","|================= SALIR ==================|")
    
def Listar(data):
    inicio=65 # = A
    final=90  # = Z
    for i in range(len(data)):
        letra = i
        letra += inicio
        if letra == final: # Solo hasta la "Z"
            Salida(chr(final))
            break
        comida=data[i][0]
        precio=f"{data[i][1]:05.2f}" #formatea el número a "00.00"
        espacios= 35 - (len(comida)+len(precio))
        print(f"| {chr(letra)} | {comida}{' '*espacios}| S/.{precio} |" )
    Salida(chr(inicio+len(data)))
    print("|"+"_"*46+"|")
    
def Mostrar(titulo,datos):
    Titulo(titulo)
    Listar(datos)

def Iniciar(carta) -> list:
    Titulo("Menu")
    inicio=65 # = A
    final=90  # = Z
    for i in range(len(carta)):
        letra = i
        letra += inicio
        if letra == final: # Solo hasta la "Z"
            Salida(chr(final))
            break
        comida=carta[i]
        espacios= 40 - len(comida)
        print(f"| {chr(letra)} | {comida}{' '*espacios} |" )
    Salida(chr(inicio+len(carta)))
    print("|"+"_"*46+"|")
    

def Ordenar():
    
    # instancias
    desayunos=Menu("Desayuno", desayuno)
    almuerzos=Menu("Almuerzo", almuerzo)
    cenas=Menu("Cenas", cena)
    
    carta=[desayunos,almuerzos,cenas]
    
    Iniciar([i.name for i in carta])
    
    try:
        while True:
            orden=input("\n\tCual es tu orden: ").upper()
            orden = ord(orden) - 65
            if 0 <= orden <= len(carta):
                if orden == len(carta):
                    break
                carta[orden].Dar_factura()
                break
            else:
                print("\t\nNo esta en las opciones\n")              
    except:
        print("Solo lo que esta en el menu")
        

# Clases
class Lista_de_comida:
    def __init__(self,name,data):
        self.name = name
        self.data = data
    
    def add(self, dato):
        self.data.append(dato)
 
class Menu(Lista_de_comida):
    def __init__(self,name,data):
        self.data= data # Esto es una lista
        self.name= name
        self.compras= []

    def Dar_factura(self):
        Mostrar(self.name,self.data)
        while True:
            respuesta=input("¿Que desea ordenar?: ").upper()
            if respuesta == "":
                break
            elif self.Verificador(respuesta):
                index=ord(respuesta)-65
                self.compras.append(self.data[index][1])
                print(self.compras)
            else:
                print("Solo las comidas disponibles")
            print("Presione enter para cobrar")
                
        self.Calcular_boleta()

    def Verificador(self,letra) -> str:
        inicio=65 # A
        valor=ord(letra) - inicio
        if 0 <= valor < len(self.data):
            return True
        else:
            return False
        

    def Calcular_boleta(self):
        data=self.compras
        suma_de_precios=sum(data)
        igv=round(suma_de_precios*.18,2)
        total=suma_de_precios + igv
        
        def Mostrar_precio(subtitle, precio):
            format_precio = f"{precio:05.2f}"
            count_subtitle = len(subtitle)
            count_precio = len(format_precio)
            calcular_espacio = 40 - (count_precio + count_subtitle)
            print(f"| {subtitle}:{'_'*calcular_espacio}S/.{format_precio} |")
        
        print()
        print("|"+"="*46+"|")
        print("|"+" "*16+"Boleta de pago"+" "*16+"|")
        print("|"+"="*46+"|")
        Mostrar_precio("Subtotal",suma_de_precios)    
        Mostrar_precio("IGV",igv)    
        Mostrar_precio("Total",total)
        print("|"+"_"*46+"|")
        print()
    

# Declarar funciones
Ordenar()