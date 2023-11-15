USUARIO: InnovaCode
CONTRASEÑA: CodingCorporation


Especificación Técnica
        
        Descripción General del Sistema
        
El sistema implementa un programa en Python que permite filtrar ciertos datos provenientes de una base de datos anteriormente dada.
    - Se encarga de filtrar por Nombre de juego, calificación del crítico, calificación del jugador y el promedio de ambas.
    - Se utilizan 3 módulos en todo el sistema, 2 creados por los programadores (modulo y validación) y el módulo math
    - En caso de no haber valor en alguna calificación el promedio = 0
    - Para utilizar el programa en otro archivo lo único que se debe hacer en la línea 9 del código principal (Donde actualmente dice "NintendoGames.csv" y ","), 
      la ubicación del archivo en primer lugar y luego el separador de las columnas que se utiliza (llámese por default una coma)

        Estructuras de Datos
  
Archivo NintendoGames.csv
- Este archivo contiene información sobre los juegos de Nintendo, con columnas separadas por comas.
Archivo NintendoData.csv
- Este archivo es generado por el programa principal y contiene información procesada de los juegos, con columnas separadas por comas.

        Técnicas y Herramientas
Manejo de Excepciones: 
  - Se utiliza el bloque try y except para manejar posibles errores de lectura y escritura de archivos.
Manejo de Archivos:
  - Se emplea el módulo open para la apertura y manipulación de archivos.
Operaciones con Listas y Strings:
  - Se utilizan diversas operaciones con listas y strings para procesar la información del archivo.
Validación de Acceso:
  - Se implementa una función de validación de acceso que compara el usuario y la contraseña ingresados con valores predefinidos.
Esta especificación técnica proporciona una visión general del sistema, detalla la estructura del código principal y de los módulos, así como las técnicas y herramientas utilizadas para la solución propuesta.
