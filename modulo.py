def leerLineas(ubicacion, separador):
    """La función se encarga de realizar una lectura de las líneas 
    y dividirlas con el separador indicado en los parámetros, además
    tiene la ubicación colocada en los parámetros para que sea
    reutilizable"""
    try: 
        lista_total = []
        # Abrimos el archivo en modo lectura
        with open(ubicacion, 'rt', encoding='UTF-8') as archivo:
            next(archivo)
            #Chequeamos si las columnas que contienen "" tienen comas adentro para que no se corrompa el codigo
            for linea in archivo:
                lista = []
                #Bandera para ver si estamos en un bloque dentro de comillas
                dentro_comillas = False
                partes = linea.strip().split(separador)
                for parte in partes:
                    if parte.startswith('"'):
                        dentro_comillas = True
                        columna = parte
                    elif parte.endswith('"'):
                        dentro_comillas = False
                        columna += separador + parte
                        lista.append(columna[1:-1])
                    elif dentro_comillas:
                        columna += separador + parte
                    else:
                        lista.append(parte)
                lista_total.append(lista)
    except IOError:
        print("No se pudo abrir el archivo de lectura de la ubicación")
    return lista_total

