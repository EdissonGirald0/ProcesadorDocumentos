# Proyecto de Procesamiento de Documentos

Este proyecto tiene como objetivo procesar archivos de diferentes formatos (RTF, DOC, PDF) y convertirlos a HTML. Utiliza herramientas como `libreoffice`, `pdftohtml` y `pandoc` para realizar las conversiones.

## Requisitos del Sistema

- Linux
- Bash
- LibreOffice (para la conversión de archivos DOC)
- Poppler-utils (para la conversión de archivos PDF)
- Pandoc (para la conversión general de documentos)

## Estructura del Proyecto

.
├── procesar_documentos.sh 
# Script principal para procesar documentos
├── TempDOCX 
# Directorio temporal para archivos DOCX
├── ResultadosCSJ 
# Directorio de salida para archivos HTML procesados
├── registroSentenciasCSJ.txt 
# Archivo de registro
├── README.md 
# Este archivo de documentación


## Instrucciones de Uso
Accede al directorio del proyecto:

cd procesar-documentos
Ejecuta el script para procesar tus documentos:

./procesar_documentos.sh
Los resultados se almacenarán en el directorio ResultadosCSJ y el registro estará disponible en registroSentenciasCSJ.txt.

Notas Importantes
Asegúrate de tener los requisitos del sistema instalados antes de ejecutar el script.
El script puede requerir ajustes según las necesidades específicas de tu proyecto.
La conversión de PDF a HTML puede tener limitaciones en la preservación del formato.
Contribuciones
Si encuentras problemas o mejoras potenciales, ¡no dudes en contribuir! Abre un issue o envía una pull request.


Procesamiento de Archivos HTML y Limpieza de Contenido
Este script de Python se encarga de procesar archivos HTML y realizar una limpieza del contenido, eliminando estilos en línea, scripts, etiquetas de formato y atributos innecesarios. El objetivo es obtener un HTML simplificado y legible.

Requisitos
Python 3
Biblioteca BeautifulSoup para el análisis HTML
Biblioteca chardet para detectar la codificación de los archivos
Puedes instalar las bibliotecas necesarias utilizando el siguiente comando:

      

    pip install beautifulsoup4 chardet
        
Uso
Clona o descarga este repositorio en tu máquina local.

Asegúrate de tener los requisitos instalados.

Modifica las rutas de las carpetas de entrada y salida en el script según tus necesidades:


 carpeta_html_entrada = '/ruta/de/tu/carpeta/entrada/'
carpeta_textos_limpios_salida = '/ruta/de/tu/carpeta/salida/'
Ejecuta el script:

python nombre_del_script.py
El script procesará los archivos HTML en la carpeta de entrada, realizará la limpieza correspondiente y guardará los resultados en la carpeta de salida.

Funciones Principales
obtener_codificacion(ruta_archivo): Detecta la codificación del archivo utilizando chardet.

limpiar_html(html): Utiliza BeautifulSoup para eliminar estilos en línea, scripts, etiquetas de formato y atributos innecesarios, conservando títulos y listas.

procesar_archivos_html(carpeta_entrada, carpeta_salida): Itera sobre los archivos HTML en la carpeta de entrada, aplica la limpieza y guarda los resultados en la carpeta de salida.

Notas Importantes
Asegúrate de tener los permisos necesarios para leer y escribir en las carpetas especificadas.

El script utiliza la detección automática de codificación, pero puede haber casos donde se necesite especificar la codificación manualmente.

Ajusta las funciones según tus necesidades específicas.

Este script es una herramienta útil para limpiar y simplificar archivos HTML, especialmente útil cuando se desea procesar y analizar el contenido de manera más eficiente. ¡Disfruta del procesamiento de tus archivos HTML de forma más limpia y estructurada!



Procesamiento y Exportación de Datos de Sentencias

Este script de Python se encarga de procesar archivos HTML limpios, extraer su contenido y almacenarlo en un formato JSON. Además, proporciona opciones adicionales para exportar los datos a un archivo CSV o insertarlos en una base de datos MongoDB.

Requisitos
Python 3
Bibliotecas: pandas, pymongo
Puedes instalar las bibliotecas necesarias utilizando el siguiente comando:

bash
pip install pandas pymongo
Uso
Clona o descarga este repositorio en tu máquina local.

Asegúrate de tener los requisitos instalados.

Modifica las rutas de los archivos y carpetas en el script según tus necesidades:

python
carpeta_textos_limpios = '/ruta/de/tu/carpeta/limpios/'
json_output_file = '/ruta/de/tu/archivo/Sentencias.json'
csv_output_file = '/ruta/de/tu/archivo/Sentencias.csv'
mongodb_collection_name = 'nombre_de_tu_coleccion_en_mongodb'
Ejecuta el script:

bash
python nombre_del_script.py
El script procesará los archivos HTML en la carpeta de entrada, generará un archivo JSON con el contenido de las sentencias y proporcionará opciones para exportar a CSV o insertar en MongoDB.

Funciones Principales
convertir_a_json(html_folder, json_file): Convierte los archivos HTML limpios a un formato JSON.

exportar_a_csv(json_file, csv_file): Exporta los datos del archivo JSON a un archivo CSV.

insertar_en_mongodb(json_file, collection_name): Inserta los datos del archivo JSON en una colección de MongoDB.

Notas Importantes
Asegúrate de tener los permisos necesarios para leer y escribir en las carpetas especificadas.

Las opciones adicionales (exportar_a_csv y insertar_en_mongodb) son comentadas. Descomenta la opción que desees utilizar.

Ajusta las funciones según tus necesidades específicas.

Si usas la opción de MongoDB, asegúrate de tener MongoDB ejecutándose localmente.

Este script simplifica el procesamiento de archivos HTML limpios, permitiendo una fácil conversión y exportación de datos. ¡Disfruta de la versatilidad para adaptar tus datos a diferentes formatos y almacenarlos en MongoDB!

