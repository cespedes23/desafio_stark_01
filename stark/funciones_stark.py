from data_stark import lista_personajes

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

def mostrar_lista_nombre(lista:list) -> list:
    """informa lista de nombres

    Args:
        lista (list): lista de diccionario a recorrer

    Returns:
        list: devuelve lista de nombres
    """
    lista_nombres = []
    for elemento in lista:
        for k,v in elemento.items():
            if k == "nombre":
                nombre = v
                lista_nombres.append(nombre)
    return lista_nombres
    

#print(mostrar_lista_nombre(lista_personajes))

#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

def obtener_nombre_altura(lista:list) -> dict:
    """imprime nombre y altura de personajes

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        dict: devuelve un diccionario
    """
    datos_c = {}
    for elemento in lista:
        nombre = elemento.get("nombre")
        altura = elemento.get("altura")
        altura = float(altura) * 100 // 100
        datos_c[nombre] = {"altura" : altura}
    return datos_c

#print(mostrar_nombre_altura(lista_personajes))

#D. Recorrer la lista de diccionarios y determinar cuál es el superhéroe más alto (MÁXIMO)

def personaje_altura_maximo(lista:list) -> str:
    """Informa el personaje con mayor altura

    Args:
        lista (list): lista de diccionario a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    mayor_altura = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if mayor_altura is None or mayor_altura < altura:
                    mayor_altura = altura
                    nombre_mayor_altura = nombre
    
    resultado = f"El personaje mas alto es: {nombre_mayor_altura} de {mayor_altura}"
    return resultado

#print(personaje_altura_maximo(lista_personajes))

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def personaje_altura_minima(lista: list) -> str:
    """Informa el personaje con menor altura

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuele la informacion obtenida
    """
    menor_altura = None
    nombre_menor_altura = None
    
    for e in lista:
        for key, value in e.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if menor_altura is None or menor_altura > altura:
                    menor_altura = altura
                    nombre_menor_altura = nombre
                    
    resultado = f"El personaje mas bajo es: {nombre_menor_altura} de {menor_altura}"
    return resultado

#print(personaje_minima_altura(lista_personajes))

#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def calcular_promedio_altura(lista:list) -> float:
    """calcula el promedio de altura de la lista recorrida

    Args:
        lista (list): lista de diccionario a recorrer

    Returns:
        float: devuelve el calculo obtenido
    """
    sumador_altura = 0
    cant = len(lista)
    
    for e in lista:
        for key, value in e.items():
            if key == "altura":
                entrada_altura = value
                sumador_altura += float(entrada_altura)
    resultado = f"El promedio de altura es: {(sumador_altura / cant) * 100 // 10}"
    return resultado
    
#print(calcular_promedio_altura(lista_personajes))

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def informar_maximo_minimo_alt(lista:list) -> str:
    """informa el personaje con mayor y menor altura

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve el resultado obtenido
    """
    mayor_altura = None
    menor_altura = None
    nombre_mayor_altura = None
    nombre_menor_altura = None
        
    for e in lista:
        for key, value in e.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if mayor_altura is None or mayor_altura < altura:
                    mayor_altura = altura
                    nombre_mayor_altura = nombre
                if menor_altura is None or menor_altura > altura:
                    menor_altura = altura
                    nombre_menor_altura = nombre
                
    
    resultado_mayor = f"Nombre con maxima altura: {nombre_mayor_altura}"
    resultado_menor = f"Nombre con minima altura: {nombre_menor_altura}"
    return f"{resultado_mayor}\n{resultado_menor}"
    
#print(informar_maximo_minimo_alt(lista_personajes))

#H. Calcular e informar cual es el superhéroe más y menos pesado.
def informar_mas_menos_pesado(lista:list) -> str:
    """Informa el personaje mas y menos pesado

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    mayor_peso = None
    menor_peso = None
    nombre_mayor_peso = None
    nombre_menor_peso = None
    
    for e in lista:
        for key, value in e.items():
            if key == "nombre":
                nombre = value
            elif key == "peso":
                 peso = float(value)
                 if mayor_peso is None or mayor_peso < peso:
                    mayor_peso = peso
                    nombre_mayor_peso = nombre
                 elif menor_peso is None or menor_peso > peso:
                    menor_peso = peso
                    nombre_menor_peso = nombre
    resultado_mayor = f"El personaje de mayor peso es: {nombre_mayor_peso} de {mayor_peso}"
    resultado_menor = f"El personaje de menor peso es: {nombre_menor_peso} de {menor_peso}"
    return f"{resultado_mayor}\n{resultado_menor}"

#print(informar_mas_menos_pesado(lista_personajes))

#---------------------------------------------------
#I. Ordenar el código implementando una función para cada uno de los valores informados.

def mostrar_nombre_altura(personajes:list) -> str:
    """muestra por consola los nombres y altura de cada personaje

    Args:
        personajes (list): lista de diccionario a recorrer

    Returns:
        str: inprime los datos obtenidos
    """
    print(" Nombre                |   Altura")
    print("----------------------------------")
    for personaje in personajes:
       print(f"{personaje['nombre']:<20}   |   {float(personaje['altura']) * 100 / 100} ")
       
def mostrar_nombre(personajes:list):
    print(" Nombre  ")
    print("----------------------------------")
    for personaje in personajes:
       print(f"{personaje['nombre']:<20} ")


def mostrar_mas_alto(personajes:list):
    print(personaje_altura_maximo(personajes))

def mostrar_mas_bajo(personajes:list):
    print(personaje_altura_minima(personajes))
    
def mostrar_promedio_altura(personajes:list):
    print(calcular_promedio_altura(personajes))
    
def mostrar_max_min_altura(personajes:list):
    print(informar_maximo_minimo_alt(personajes))

def mostrar_max_min_peso(personajes:list):
    print(informar_mas_menos_pesado(personajes))
    

# ---------------------------------- MENU -------------------------------
#J. Construir un menú que permita elegir qué dato obtener

def limpiar_pantalla():
    import os
    os.system("clear")

def menu():
    """menu de opciones

    Returns:
        _type_: devuelve respuesta seleccionada
    """
    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")
    print("01- Nombres")
    print("02- Nombres y Alturas")
    print("03- Superheroe mas alto")
    print("04- Superheroe mas bajo")
    print("05- Promedio de altura")
    print("06- Nombre del personaje mas alto y mas bajo")
    print("07- Nombre del mas y menos pesado")
    print("08- Nombres del genero 'M'")
    print("09- Nombres del genero 'F'")
    print("10- Superheroe mas alto de genero 'M'")
    print("11- Superheroe mas alto de genero 'F'")
    print("12- Superheroe mas bajo de genero 'M'")
    print("13- Superheroe mas bajo de genero 'F'")
    print("14- Promedio de altura genero 'M'")
    print("15- Promedio de altura genero 'F'")
    print("16- Informe de los puntos C a F")
    print("17- Cantidad de Superheroes por color de ojos")
    print("18- Cantidad de Superheroes por color de pelo")
    print("19- Cantidad de Superheroes por inteligencia")
    print("20- Informe de Superheroes por color de ojos")
    print("21- Informe de Superheroes por color de pelo")
    print("22- Informe de Superheroes por tipo de inteligencia")
    print("23- Salir")
    return input("Ingrese opcion: ")

def pausar():
    import time
    time.sleep(5)


