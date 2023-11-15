import math
from modulo import *
from validacion import *
def escribirArchivo():
    """La función se encarga de, en un archivo aparte, escribir
    el título del juego, calificación del crítico, del usuario y además hacer un promedio"""
    try:
        with open("NintendoData.csv", "wt", encoding='UTF-8') as archivo:
            lista_total = leerLineas("NintendoGames.csv", ",")
            archivo.write(f"Juego,Calificacion Critico,Calificacion Usuario,Promedio\n")
            
            for lista in lista_total:
                # Verificamos si las calificaciones existen
                calificacion_critico = lista[0]
                calificacion_usuario = lista[4]
                promedio = 0
                #Calculamos el promedio de las calificaciones
                try:
                    promedio = (float(calificacion_critico) + float(calificacion_usuario)) / 2
                    promedio = int(promedio) if not math.isnan(promedio) else 0
                except ValueError:
                    pass
                #Volcamos todo en el archivo nuevo
                archivo.write(f"{lista[1]},{calificacion_critico},{calificacion_usuario},{promedio}\n")
    except IOError:
        print("No se pudo abrir el archivo de escritura")

def main():
    usuario = input("Ingrese el usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    resultado = validacion(usuario, contraseña)
    if resultado:
        escribirArchivo()

if __name__ == "__main__":
    main()