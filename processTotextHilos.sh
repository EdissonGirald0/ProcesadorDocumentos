#!/bin/bash

# Ruta de la carpeta que contiene los archivos originales
CARPETA_ORIGEN="/home/dev1/Documents/documentosAltasCortes/comision_diciplina_judicial"

# Ruta de la carpeta donde se guardarán todos los archivos de texto resultantes
CARPETA_DESTINO="/home/dev1/Documents/documentosAltasCortes/comision_diciplina_judicial_text"

# Crear la carpeta de destino si no existe
mkdir -p "$CARPETA_DESTINO"

# Función para convertir archivos de un lote
convertir_lote() {
    local archivos=("$@")
    for ARCHIVO in "${archivos[@]}"; do
        # Convertir el archivo y moverlo a la carpeta de destino
        case $ARCHIVO in
            *.pdf)
                pdftotext "$ARCHIVO" "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
                ;;
            *.docx)
                docx2txt "$ARCHIVO" "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
                ;;
            *.rtf)
                unrtf --text "$ARCHIVO" > "$CARPETA_DESTINO/$(basename "${ARCHIVO%.*}").txt"
                ;;
            *)
                echo "Extensión no compatible: $ARCHIVO"
                ;;
        esac
    done
}

# Obtener la lista de archivos en la carpeta de origen y procesarlos
find "$CARPETA_ORIGEN" -type f \( -name "*.pdf" -o -name "*.docx" -o -name "*.rtf" \) | 
while IFS= read -r ARCHIVO; do
    convertir_lote "$ARCHIVO" &
done

# Esperar a que todos los subprocesos terminen antes de salir del script
wait
