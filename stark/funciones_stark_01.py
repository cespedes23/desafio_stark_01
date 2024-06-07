from funciones_stark import *


#Desafío #01:
#Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
#utilizando un menú que permita acceder a cada uno de los puntos por separado.
#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
#I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
#M. Listar todos los superhéroes agrupados por color de ojos.
#N. Listar todos los superhéroes agrupados por color de pelo.
#O. Listar todos los superhéroes agrupados por tipo de inteligencia

#-------


#print(obtener_nombre_altura_f(lista_personajes))

#--------

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

def mostrar_nombre_altura_m(personajes:list, target:any) -> str:
    """recorre la lista e imprime los nombres y altura de genero masculino

    Args:
        personajes (list): lista de diccionarios a recorrer
        target (any): valor a comparar del personaje de genero masculino

    Returns:
        list: imprime la informacion obtenida
    """
    print(f"Nombre de genero {target}  |   Altura")
    print("----------------------------------")
    for personaje in personajes:
        for key, value in personaje.items():
            if key == "genero":
                if value == "M":
                    value = target
                    print(f"{personaje['nombre']:<20} |   {float(personaje['altura']) * 100 / 100} ")
         
#mostrar_nombre_altura_m(lista_personajes, "M")


#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

def mostrar_nombre_altura_f(personajes:list, target:any) -> str:
    """recorre la lista e imprime los nombres y altura de genero femenino

    Args:
        personajes (list): lista de diccionarios a recorrer
        target (any): valor a comparar del personaje con genero femenino

    Returns:
        list: imprime la informacion obtenida
    """
    print(f"Nombre de genero {target}  |   Altura")
    print("----------------------------------")
    for personaje in personajes:
        for key, value in personaje.items():
            if key == "genero":
                if value == "F":
                    value = target
                    print(f"{personaje['nombre']:<20} |   {float(personaje['altura']) * 100 / 100} ")
         
#mostrar_nombre_altura_f(lista_personajes, "F")


#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

def personaje_altura_maximo_m(lista:list) -> str:
    """recorre la lista e imprime la altura maxima de los personajes de genero masculino

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    mayor_altura = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "genero":
                genero = value
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if (mayor_altura is None or mayor_altura < altura) and (genero == "M"):
                    mayor_altura = altura
                    nombre_mayor_altura = nombre
    
    resultado = f"El personaje mas alto de genero M es: {nombre_mayor_altura} de {mayor_altura}"
    return resultado

#------------
def mostrar_personaje_max_altura_m(lista:list) -> str:
    print(personaje_altura_maximo_m(lista))

#mostrar_personaje_max_altura_m(lista_personajes)
#------------

#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

def personaje_altura_maximo_f(lista:list) -> str:
    """recorre la lista e imprime la altura maxima de los personajes de genero femenino

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    mayor_altura = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "genero":
                genero = value
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if (mayor_altura is None or mayor_altura < altura) and (genero == "F"):
                    mayor_altura = altura
                    nombre_mayor_altura = nombre
    
    resultado = f"El personaje mas alto de genero F es: {nombre_mayor_altura} de {mayor_altura}"
    return resultado
    
#------------
def mostrar_personaje_max_altura_f(lista:list) -> str:
    print(personaje_altura_maximo_f(lista))

#mostrar_personaje_max_altura_f(lista_personajes)
#------------

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M

def personaje_altura_minimo_m(lista:list) -> str:
    """recorre la lista e imprime la altura minima de los personajes de genero masculino

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    menor_altura = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "genero":
                genero = value
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if (menor_altura is None or menor_altura > altura) and (genero == "M"):
                    menor_altura = altura
                    nombre_menor_altura = nombre
    
    resultado = f"El personaje mas bajo de genero M es: {nombre_menor_altura} de {menor_altura}"
    return resultado
    
#------------
def mostrar_personaje_min_altura_m(lista:list) -> str:
    print(personaje_altura_minimo_m(lista))

#mostrar_personaje_min_altura_m(lista_personajes)
#------------
#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F

def personaje_altura_minimo_f(lista:list) -> str:
    """recorre la lista e imprime la altura minima de los personajes de genero femenino

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve la informacion obtenida
    """
    menor_altura = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "genero":
                genero = value
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if (menor_altura is None or menor_altura > altura) and (genero == "F"):
                    menor_altura = altura
                    nombre_menor_altura = nombre
    
    resultado = f"El personaje mas bajo de genero F es: {nombre_menor_altura} de {menor_altura}"
    return resultado
    

#------------
def mostrar_personaje_min_altura_f(lista:list) -> str:
    print(personaje_altura_minimo_f(lista))
    
#mostrar_personaje_min_altura_f(lista_personajes)
#------------

#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M

def calcular_promedio_altura_m(lista:list) -> float:
    """calcula el promedio de altura de genero masculino

    Args:
        lista (list): lista de diccionarios

    Returns:
        float: devuelve el promedio de la altura de genero masculino
    """
    sumador_altura = 0
    cant = 0
    
    for e in lista:
        for key, value in e.items():
            if key == "genero":
                genero = value
        for key, value in e.items():
            if key == "altura" and genero == "M":
                cant += 1
                entrada_altura = value
                sumador_altura += float(entrada_altura)
    resultado = f"El promedio de altura en 'M' es: {sumador_altura / cant}"
    return resultado


#------------
def mostrar_promedio_m(lista:list) -> int:
    print(calcular_promedio_altura_m(lista))

#mostrar_promedio_m(lista_personajes)
#------------
#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F

def calcular_promedio_altura_f(lista:list) -> float:
    """calcula el promedio de altura de genero femenino

    Args:
        lista (list): lista de diccionarios

    Returns:
        float: devuelve el promedio de la altura de genero femenino
    """
    sumador_altura = 0
    cant = 0
    
    for e in lista:
        for key, value in e.items():
            if key == "genero":
                genero = value
        for key, value in e.items():
            if key == "altura" and genero == "F":
                cant += 1
                entrada_altura = value
                sumador_altura += float(entrada_altura)
    resultado = f"El promedio de altura en 'F' es: {sumador_altura / cant}"
    return resultado

#------------
def mostrar_promedio_altura_f(lista:list) -> str:
    print(calcular_promedio_altura_f(lista))

#mostrar_promedio_altura_f(lista_personajes)
#------------
#I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

def informe_punto_i(lista:list) -> str:
    """informa los resultados obtenidos en los puntos C a F

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        str: devuelve los datos obtenidos
    """
    mayor_altura_m = None
    mayor_altura_f = None
    menor_altura_m = None
    menor_altura_f = None
    
    for personaje in lista:
        for key, value in personaje.items():
            if key == "genero":
                genero = value
        for key, value in personaje.items():
            if key == "nombre":
                nombre = value
            elif key == "altura":
                altura = float(value)
                if genero == "M":
                   if (mayor_altura_m is None or mayor_altura_m < altura):
                      mayor_altura_m = altura
                      nombre_mayor_altura_m = nombre
                   if (menor_altura_m is None or menor_altura_m > altura):
                      menor_altura_m = altura
                      nombre_menor_altura_m = nombre
                elif genero == "F":
                   if (mayor_altura_f is None or mayor_altura_f < altura):
                      mayor_altura_f = altura
                      nombre_mayor_altura_f = nombre
                   if (menor_altura_f is None or menor_altura_f > altura):
                      menor_altura_f = altura
                      nombre_menor_altura_f = nombre
    
    resultado = (f"Nombre de mayor altura 'M':{nombre_mayor_altura_m}\n"
                f"Nombre de menor altura 'F':{nombre_mayor_altura_f}\n"
                f"Nombre de mayor altura 'M':{nombre_menor_altura_m}\n"
                f"Nombre de menor altura 'F':{nombre_menor_altura_f}")
    return resultado

#------------
def mostrar_informe_punto_i(lista:list) -> list:
    print(informe_punto_i(lista))

#mostrar_informe_punto_i(lista_personajes)
#------------
#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def obtener_cant_color_ojos(lista:list) -> dict:
    """recorre la lista de personajes e informa la cantidad por color de ojos

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        dict: devuelve diccionario 
    """
    color_ojos = {}
    for elemento in lista:
        for key, value in elemento.items():
            if key == "color_ojos":
                color = value
                if color in color_ojos:
                    color_ojos[color] += 1
                else:
                    color_ojos[color] = 1
    return color_ojos
#-----------
def mostrar_cant_color_ojos(lista:list) -> list:
    print(obtener_cant_color_ojos(lista))

#mostrar_cant_color_ojos(lista_personajes)
#------------
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

def obtener_cant_color_pelo(lista:list) -> dict:
    """recorre la lista de personajes e informa la cantidad por color de pelo

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        dict: devuelve diccionario 
    """
    color_pelo = {}
    for elemento in lista:
        for key, value in elemento.items():
            if key == "color_pelo":
                color = value
                if color in color_pelo:
                    color_pelo[color] += 1
                else:
                    color_pelo[color] = 1
    return color_pelo

def mostrar_cant_color_pelo(lista:list) -> list:
    print(obtener_cant_color_pelo(lista))

#mostrar_cant_color_pelo(lista_personajes)

#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).

def obtener_cant_tipo_inteligencia(lista:list) -> dict:
    """recorre la lista de personajes e informa la cantidad por tipo de inteligencia

    Args:
        lista (list): lista de diccionarios a recorrer

    Returns:
        dict: devuelve diccionario 
    """
    tipo_inteligencia = {}
    no_tiene = 0
    for elemento in lista:
        if "inteligencia" in elemento:
            tipo = elemento["inteligencia"]
            if tipo in tipo_inteligencia:
                tipo_inteligencia[tipo] += 1
            else:
                tipo_inteligencia[tipo] = 1
        else:
            no_tiene += 1
            
    if no_tiene > 0:
        tipo_inteligencia['No tiene'] = no_tiene
            
    return tipo_inteligencia

def mostrar_cant_tipo_inteligencia(lista:list) -> list:
    print(obtener_cant_tipo_inteligencia(lista))

#mostrar_cant_tipo_inteligencia(lista_personajes)
#M. Listar todos los superhéroes agrupados por color de ojos.
#--------------------
def mostrar_personaje_por_color(personajes_color:dict) -> str:
    """muestra los personajes agrupados por color

    Args:
        personajes_color (dict): lista de diccionario a recorrer

    Returns:
        str: informa nombre de personajes por color
    """
    
    for color,nombres in personajes_color.items():
        print()
        color = color.upper()
        print(f"Color: {color}")
        for nombre in nombres:
            print(f"- {nombre}")
#--------------------

def ordenar_por_color_ojos(lista:list) -> dict:
    """ordena por grupos a personajes por color de ojos

    Args:
        lista (list): lista de diccionario a recorrer

    Returns:
        dict: devuelve diccionario
    """
    color_ojos = {}
    for elemento in lista:
        for key, value in elemento.items():
            if key == "nombre":
                nombre = value
            if key == "color_ojos":
                color = value.lower()
                
                if color:
                   if color in color_ojos:
                     color_ojos[color].append(nombre)
                   else:
                    color_ojos[color] = [nombre]
                        
    return color_ojos
#mostrar_personaje_por_color(ordenar_por_color_ojos(lista_personajes))

#N. Listar todos los superhéroes agrupados por color de pelo.

def ordenar_color_pelo(lista:list) -> dict:
    """ordena en grupos a personajes por color de pelo

    Args:
        lista (list): lista de diccionario a recorrer

    Returns:
        dict: devuelve un diccionario
    """
    color_pelo = {}
    for elemento in lista:
        for key, value in elemento.items():
            if key == "nombre":
                nombre = value
            if key == "color_pelo":
                color = value.lower()
                
                if color:
                   if color in color_pelo:
                     color_pelo[color].append(nombre)
                   else:
                    color_pelo[color] = [nombre]
                        
    return color_pelo

#mostrar_personaje_por_color(ordenar_color_pelo(lista_personajes))


#O. Listar todos los superhéroes agrupados por tipo de inteligencia

def ordenar_tipo_inteligencia(lista:list) -> dict:
    """ordena por grupos a personajes por tipo de inteligencia

    Args:
        lista (list): lista a recorrer

    Returns:
        dict: devuelve un diccionario
    """
    tipo_inteligencia = {}
    for elemento in lista:
        for key, value in elemento.items():
            if key == "nombre":
                nombre = value
            if key == "inteligencia":
                tipo = value.lower()
                
                if tipo:
                   if tipo in tipo_inteligencia:
                     tipo_inteligencia[tipo].append(nombre)
                   else:
                     tipo_inteligencia[tipo] = [nombre]
                        
    return tipo_inteligencia

def mostrar_personaje_por_tipo(personajes_color:dict, target:any) -> str:
    """informa por grupos de personajes por tipo

    Args:
        personajes_color (dict): lista de diccionario a recorrer 
        target (any): valor a comparar

    Returns:
        str: imprime por consola
    """
    for value,nombres in personajes_color.items():
        print()
        value = value.upper()
        print(f"{target}: {value}")
        for nombre in nombres:
            print(f"- {nombre}")


#mostrar_personaje_por_tipo(ordenar_tipo_inteligencia(lista_personajes), "INTELIGENCIA")


