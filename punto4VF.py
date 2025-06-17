import random
from pathlib import Path
import json

def iniciar_juego():
    valor_secreto=random.randint(1000,9999)
    intentos=0
    intento_usuario = 0
    while intento_usuario != -1 and valor_secreto != intento_usuario:
        intento_usuario = solicitar_numero()
        comparar_numeros(intento_usuario, valor_secreto)
        intentos += 1
    if (intento_usuario != -1):
        mejores_puntajes = ordenar_puntajes(intentos)
        mostrar_puntajes(mejores_puntajes)
    jugar_de_nuevo();

def solicitar_numero():
    numero_solicitado = int(input("Ingrese un número positivo de 4 cifras o -1 para salir: "))
    while numero_solicitado != -1 and (numero_solicitado < 1000 or numero_solicitado > 9999):
        print("Error de ingreso, ingrese un número de 4 cifras o -1 para salir: ")
        numero_solicitado = int(input("Ingrese un número de 4 cifras o -1 para salir: "))
    return numero_solicitado

def solicitar_dni():
    dni_solicitado = int ( input ( "Ingrese su numero de documento : " ))
    while dni_solicitado < 10000000 or dni_solicitado > 99999999 :
        print("Error de ingreso, ingrese su numero de documento: ")
        dni_solicitado = int ( input ( "Ingrese su numero de documento : " ))
    return dni_solicitado

def comparar_numeros(intento_usuario, valor_secreto):
    if intento_usuario > valor_secreto:
        print("El numero ingresado es mayor")
    elif intento_usuario < valor_secreto and intento_usuario > 0:
        print ("el numero ingresado es menor")
    elif valor_secreto == intento_usuario:
        print("¡Ganaste!")
    else:
        print("Saliste del juego.");

def mostrar_puntajes(mejores_puntajes):
    print(" Mejores puntajes:")
    for i, (pts, dni) in enumerate(mejores_puntajes, start=1):
        print(f"{i}. {dni} - {pts} intentos");

def ordenar_puntajes(intentos_usuario,):
    mejores_puntajes = get_ranking();
    if len(mejores_puntajes) >= 5: 
        for i, (pts,dni) in enumerate(mejores_puntajes):
            if (pts > intentos_usuario):
                guardar_nuevo_puntaje(mejores_puntajes, intentos_usuario)
                break;
    else:
        guardar_nuevo_puntaje(mejores_puntajes, intentos_usuario)
    mejores_puntajes.sort();
    save_ranking(mejores_puntajes[:5]);
    return mejores_puntajes[:5]

def guardar_nuevo_puntaje(array_puntajes, intentos_usuario):
    dni_usuario = solicitar_dni()
    array_puntajes.append((intentos_usuario, dni_usuario))

def get_ranking():
    ruta = Path.cwd() / "mejores_puntajes.json"
    # Si no existe, lo creo vacio
    if not ruta.exists():
        puntajes_por_defecto = []
        ruta.write_text(json.dumps(puntajes_por_defecto))
        return puntajes_por_defecto

    # Si ya existe lo abre y cargo
    contenido = ruta.read_text()
    return [tuple(p) for p in json.loads(contenido)]

def save_ranking(puntajes):
    # Guardado en path donde esté el archivo .py
    ruta = Path.cwd() / "mejores_puntajes.json"
    datos = [list(p) for p in puntajes]
    ruta.write_text(json.dumps(datos))

def jugar_de_nuevo():
    eleccion = int(input("¿Desea jugar de nuevo? (1 Sí - 2 No) "))
    if (eleccion == 1):
        iniciar_juego();
    else:
        return;

iniciar_juego();