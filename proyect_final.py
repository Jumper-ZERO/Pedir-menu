# Programa de calculo de ventas
# Autor: Jerremi Aron Chancan Labajos
"""
    Trabajo final del curso de Introduccion a las tecnologias de información
"""

# Datos de prueba
menu = {
    "Desayunos": [
        ("Café", 4.5),
        ("Chocolate", 5),
        ("Jugo con Fresas", 9),
        ("Jugo de Papaya", 8),
        ("pan con pollo", 7),
        ("Pan con jamón", 7),
        ("Pan con tortilla", 7),
    ],
    "Almuerzos": [
        ("Sopa de res", 10),
        ("Ensalada de verdura", 8),
        ("Pachamanca de 2 carnes", 20),
        ("Trucha frita", 15),
        ("Costillar de cordero frito", 25),
        ("Arroz con mariscos", 20),
        ("Lomo saltado", 23),
    ],
    "Cenas": [
        ("Pizza Express", 9.50),
        ("Ensalada Campera", 7.50),
        ("Caldo de gallina", 6.00),
        ("Pollo al horno", 6.00),
        ("Menestrón", 5.50),
    ],
}

mensajes=[
    "Esta bien, vuelve cuando quieras",
    "Eso no esta en las opciones",
    "Vuelva pronto"
    "Escribe la letra: "
]

mensajes_error=[
    "Solo un caracter"
]

# Clases
class Pedido:
    """Clase Principal"""

    def __init__(self, datos: dict) -> None:
        self.datos = datos
        self.opciones = list(datos.keys())
        self.menu: str = ""
        self.opcion_actual: str = ""
        self.compras = []
        self.opcion_de_salida = ""
        self.mensajes={
            "salida": [
                "Esta bien, vuelve cuando quieras",
                "\nEntonces ahora le traigo su cuenta"
            ],
            "errores": [
                " no esta en las opciones aceptadas",
            ],
            "excepciones": [
                "\n# Debe aprecionar la letra correspondiente para salir #\n",
                "\n# Solo entiendo una letra a la vez #\n",
                "\n# Vuelva pronto #\n"
            ],
            "peticiones": [
                "¿Que quieres ordenar hoy?\n\t",
                "\n*=  Pide tus comidas con la letra asignada =*\n",
                "*= Si no quieres ordenar mas presiona",
                "¿Que desea ordenar algo mas?\n\t"
            ]
        }

    # Funciones
    def titulo(self, mjs: str):
        """Funcion para mostrar Titulos"""
        mensaje = mjs.capitalize()

        if len(mensaje) % 2 != 0:  # Error de espacio
            mensaje += " "

        mensaje = " " * 4 + mensaje + " " * 4
        lineas = 46
        lineas_por_lado = (lineas - len(mensaje)) // 2
        if len(mensaje) % 2 != 0:
            lineas_por_lado += 1
        print("+" + "=" * 46 + "+")
        print(f"|{'○'*lineas_por_lado}{mensaje}{'○'*lineas_por_lado}|")
        print("|" + "=" * 46 + "|")

    def listar(self, data):
        """Funcion para lista datos en pantalla"""
        inicio = 65  # = A
        final = 90  # = Z
        for i, item in enumerate(data):
            letra = i
            letra += inicio
            if letra == final:  # Solo hasta la "Z"
                self.salida(chr(final))
                break
            comida = item[0]
            precio = f"{item[1]:05.2f}"  # formatea el número a "00.00"
            espacios = 35 - (len(comida) + len(precio))
            print(f"| {chr(letra)} | {comida}{' '*espacios}| S/.{precio} |")
        self.salida(chr(inicio + len(data)))
        print("|" + "_" * 46 + "|")

    def salida(self, letra_final):
        """Funcion para mostrar el final y actualizar la opcion para terminar"""
        self.opcion_de_salida = abs((ord(letra_final) - 65))
        print(f"| {letra_final}", "|================= SALIR ==================|")

    def recibir_opcion(self, mjs: str):
        """Funcion para elegir las comidas"""
        en_bucle=True
        while en_bucle:
            try:
                opcion = input(mjs).upper()
                opcion = abs(ord(opcion) - 65)
                if 0 <= opcion <= self.opcion_de_salida:
                    if opcion == self.opcion_de_salida:
                        print(self.mensajes["salida"][1])
                        self.opcion_actual = self.opcion_de_salida
                        break
                    self.opcion_actual = opcion
                    self.compras.append(self.datos[self.menu][opcion][1])
                    print(f"\nPedistes -> {self.datos[self.menu][opcion][0]}\n")
                    break
                print("La opcion " + chr(opcion + 65) + self.mensajes["errores"][0])
            except KeyboardInterrupt:
                print(self.mensajes["excepciones"][0])
                en_bucle=False
                break
            except TypeError:
                print(self.mensajes["excepciones"][1])

    # Metodos a usar
    def mostrar_la_carta(self):
        """Metodo para las opciones del menu"""
        self.titulo("Menu")
        inicio = 65  # = A
        final = 90  # = Z
        for i, opcion in enumerate(self.opciones):
            letra = i
            letra += inicio
            if letra == final:  # Solo hasta la "Z"
                self.salida(chr(final))
                break
            espacios = 40 - len(opcion)
            print(f"| {chr(letra)} | {opcion}{' '*espacios} |")
        self.salida(chr(inicio + len(self.opciones)))
        print("|" + "_" * 46 + "|")

        while True:
            try:
                orden = input(self.mensajes["peticiones"][0]).upper()
                orden = abs(ord(orden) - 65)
                if 0 <= orden <= self.opcion_de_salida:
                    if orden == self.opcion_de_salida:
                        print(self.mensajes["salida"][0])
                        break
                    self.menu = self.opciones[orden]
                    break
                print("La opcion " + chr(orden + 65) + self.mensajes["errores"][0])
            except KeyboardInterrupt:
                print(self.mensajes["excepciones"][2])
                break
            except TypeError:
                print(self.mensajes["excepciones"][1])

    def mostrar_comidas(self):
        """Metodo para mostrar todas las comidas disponibles"""

        if self.menu == "":  # Solo valida si no presionaste "SALIR"
            return

        self.titulo(self.menu)
        self.listar(self.datos[self.menu])

        try:
            print(self.mensajes["peticiones"][1])
            self.recibir_opcion(self.mensajes["peticiones"][0])
            print(self.mensajes["peticiones"][2] + " " + chr(self.opcion_de_salida + 65) + " =*")
            while self.opcion_actual != self.opcion_de_salida:
                try:
                    self.recibir_opcion(self.mensajes["peticiones"][3])
                except KeyboardInterrupt:
                    print(self.mensajes["excepciones"][0])
                    break
                except TypeError:
                    print(self.mensajes["excepciones"][1])
        except KeyboardInterrupt:
            print(self.mensajes["excepciones"][0])
            return

    def dar_cuenta(self):
        """Metodo para mostrar la cuenta"""

        if self.menu == "":  # Solo valida si no presionaste "SALIR"
            return

        sumar_precios = sum(self.compras)
        igv = round(sumar_precios * 0.18, 2)
        total = sumar_precios + igv

        def mostrar_precio(subtitle, precio):
            """Funcion interna para dar formato a los precios"""
            format_precio = f"{precio:05.2f}"
            count_subtitle = len(subtitle)
            count_precio = len(format_precio)
            calcular_espacio = 40 - (count_precio + count_subtitle)
            print(f"| {subtitle}:{'_'*calcular_espacio}S/.{format_precio} |")

        print()
        print("+" + "=" * 46 + "+")
        print("|" + " " * 16 + "Boleta de pago" + " " * 16 + "|")
        print("|" + "=" * 46 + "|")
        mostrar_precio("Subtotal", sumar_precios)
        mostrar_precio("IGV", igv)
        mostrar_precio("Total", total)
        print("|" + "_" * 46 + "|")
        print()


# instancias
mi_pedido = Pedido(menu) # se inicia con todos los datos de "menu"
mi_pedido.mostrar_la_carta()
mi_pedido.mostrar_comidas()
mi_pedido.dar_cuenta()
