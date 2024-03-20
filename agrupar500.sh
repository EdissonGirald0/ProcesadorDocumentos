#!/bin/bash

# Ruta de la carpeta que contiene los archivos
ruta_carpeta_origen="/home/dev1/Documents/documentosAltasCortes/corte_constitucional/sentencias/"

# Ruta de la carpeta donde se almacenarán las carpetas con los archivos agrupados
ruta_carpeta_destino="/home/dev1/Documents/documentosAltasCortes/corte_constitucional/sentencias_text/"

# Verificamos si la carpeta de destino existe, si no existe la creamos
mkdir -p "$ruta_carpeta_destino"

# Contador para el nombre de las carpetas de destino
contador_carpetas=1

# Contador para el número de archivos en la carpeta actual
contador_archivos=0

# Ruta de la carpeta de destino actual
ruta_carpeta_actual="$ruta_carpeta_destino/grupo_$contador_carpetas"

# Verificamos si la carpeta de destino actual existe, si no existe la creamos
mkdir -p "$ruta_carpeta_actual"

# Iteramos sobre los archivos en la carpeta de origen
for archivo in "$ruta_carpeta_origen"/*.txt; do
    # Verificamos si hay archivos .txt en la carpeta de origen
    [ -e "$archivo" ] || break

    # Movemos el archivo a la carpeta de destino actual
    mv "$archivo" "$ruta_carpeta_actual"
    contador_archivos=$((contador_archivos + 1))

    # Si llegamos a 500 archivos, creamos una nueva carpeta de destino
    if [ $contador_archivos -eq 500 ]; then
        contador_carpetas=$((contador_carpetas + 1))
        contador_archivos=0
        ruta_carpeta_actual="$ruta_carpeta_destino/grupo_$contador_carpetas"
        mkdir -p "$ruta_carpeta_actual"
    fi
done

echo "Proceso completado."

