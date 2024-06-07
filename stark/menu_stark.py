from funciones_stark import *
from funciones_stark_01 import *

while True:
    match menu():
        case "1":
            print()
            mostrar_nombre(lista_personajes)
        case "2":
               print()
               mostrar_nombre_altura(lista_personajes)
        case "3":
                print()
                mostrar_mas_alto(lista_personajes)
        case "4":
                print()
                mostrar_mas_bajo(lista_personajes)
        case "5":
                print()
                mostrar_promedio_altura(lista_personajes)
        case "6":
                print()
                mostrar_max_min_altura(lista_personajes)
        case "7":
                print()
                mostrar_max_min_peso(lista_personajes)
        case "8":
                print()
                mostrar_nombre_altura_m(lista_personajes, "M")
        case "9":
                print()
                mostrar_nombre_altura_f(lista_personajes, "F")
        case "10":
                print()
                mostrar_personaje_max_altura_m(lista_personajes)
        case "11":
                print()
                mostrar_personaje_max_altura_f(lista_personajes)
        case "12":
                print()
                mostrar_personaje_min_altura_m(lista_personajes)
        case "13":
                print()
                mostrar_personaje_min_altura_f(lista_personajes)
        case "14":
                print()
                mostrar_promedio_m(lista_personajes)
        case "15":
                print()
                mostrar_promedio_altura_f(lista_personajes)
        case "16":
                print()
                mostrar_informe_punto_i(lista_personajes)
        case "17":
                print()
                mostrar_cant_color_ojos(lista_personajes)
        case "18":
                print()
                mostrar_cant_color_pelo(lista_personajes)
        case "19":
                print()
                mostrar_cant_tipo_inteligencia(lista_personajes)
        case "20":
                print()
                mostrar_personaje_por_color(ordenar_por_color_ojos(lista_personajes))
        case "21":
                print()
                mostrar_personaje_por_color(ordenar_color_pelo(lista_personajes))
        case "22":
                print()
                mostrar_personaje_por_tipo(ordenar_tipo_inteligencia(lista_personajes), "INTELIGENCIA")
        case "23":
                print()
        case "":
            pregunta = input("Esta seguro de que desea salir? (si/no): ")
            if pregunta.lower() == "si":
                break
            else:
                continue
            pausar()
    print("El programa continuara en un momento...")
    pausar()
    
print("Fin del programa")