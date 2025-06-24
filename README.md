# Proyecto de Procesamiento y Limpieza de Documentos Jurídicos

Este proyecto permite procesar archivos de diferentes formatos (PDF, DOC, DOCX, RTF) y convertirlos a texto plano o HTML, así como limpiar y estructurar el contenido para su posterior análisis o almacenamiento. Utiliza herramientas como `libreoffice`, `pdftotext`, `docx2txt`, `unrtf`, `pandoc` y scripts en Python con `BeautifulSoup` y `pandas`.

---

## Requisitos del Sistema

- Linux
- Bash
- LibreOffice (`libreoffice`) para conversión de archivos DOC/DOCX
- Poppler-utils (`pdftotext`, `pdftohtml`) para conversión de PDF
- Pandoc para conversión general de documentos
- Python 3
- Bibliotecas Python: `beautifulsoup4`, `chardet`, `pandas`, `pymongo` (opcional)

Instala las dependencias de Python con:

```bash
pip install beautifulsoup4 chardet pandas pymongo
```

---

## Estructura del Proyecto

```
.
├── agrupar500.sh                  # Agrupa archivos en carpetas de hasta 500 archivos
├── processTotext.sh               # Convierte PDF, DOC, DOCX y RTF a texto plano (.txt)
├── batch_convert_rtf.sh           # Convierte archivos a HTML en lote
├── procesar_documentos.sh         # Script principal para procesar documentos a HTML
├── TempDOCX/                      # Directorio temporal para archivos DOCX
├── ResultadosCSJ/                 # Directorio de salida para archivos HTML procesados
├── registroSentenciasCSJ.txt      # Archivo de registro de conversiones
├── README.md                      # Este archivo de documentación
└── scripts_python/
    ├── limpiar_html.py            # Limpieza y simplificación de archivos HTML
    └── exportar_sentencias.py     # Exporta datos a JSON, CSV o MongoDB
```

---

## Instrucciones de Uso

### 1. Conversión de documentos a texto o HTML

1. **Accede al directorio del proyecto:**
    ```bash
    cd /ruta/a/ProcesadorDocumentos
    ```

2. **Ejecuta el script de conversión según tu necesidad:**

    - Para convertir a texto plano:
        ```bash
        ./processTotext.sh
        ```
        Los archivos `.txt` se almacenarán en la carpeta de destino configurada en el script.

    - Para convertir a HTML:
        ```bash
        ./procesar_documentos.sh
        ```
        Los archivos `.html` se almacenarán en el directorio `ResultadosCSJ`.

    - Para agrupar archivos en carpetas de hasta 500 archivos:
        ```bash
        ./agrupar500.sh
        ```

3. **Verifica el registro de conversiones:**
    - Consulta el archivo `registroSentenciasCSJ.txt` para ver el estado de cada conversión.

---

### 2. Limpieza y procesamiento de archivos HTML

1. **Instala las dependencias de Python si no lo has hecho:**
    ```bash
    pip install beautifulsoup4 chardet
    ```

2. **Edita las rutas de entrada y salida en el script Python (`limpiar_html.py`):**
    ```python
    carpeta_html_entrada = '/ruta/de/tu/carpeta/entrada/'
    carpeta_textos_limpios_salida = '/ruta/de/tu/carpeta/salida/'
    ```

3. **Ejecuta el script de limpieza:**
    ```bash
    python scripts_python/limpiar_html.py
    ```

    El script eliminará estilos, scripts y etiquetas innecesarias, dejando un HTML limpio y legible.

---

### 3. Exportación de datos a JSON, CSV o MongoDB

1. **Instala las dependencias adicionales si vas a exportar:**
    ```bash
    pip install pandas pymongo
    ```

2. **Configura las rutas y parámetros en el script Python (`exportar_sentencias.py`):**
    ```python
    carpeta_textos_limpios = '/ruta/de/tu/carpeta/limpios/'
    json_output_file = '/ruta/de/tu/archivo/Sentencias.json'
    csv_output_file = '/ruta/de/tu/archivo/Sentencias.csv'
    mongodb_collection_name = 'nombre_de_tu_coleccion_en_mongodb'
    ```

3. **Ejecuta el script:**
    ```bash
    python scripts_python/exportar_sentencias.py
    ```

    El script generará un archivo JSON, y opcionalmente exportará a CSV o insertará en MongoDB.

---

## Funcionalidades Principales

- **Conversión masiva** de documentos PDF, DOC, DOCX y RTF a texto plano o HTML.
- **Agrupación automática** de archivos en carpetas para facilitar su manejo.
- **Limpieza de HTML** para obtener contenido estructurado y sin etiquetas innecesarias.
- **Exportación de datos** a formatos JSON, CSV o bases de datos MongoDB para su análisis.

---

## Notas Importantes

- Asegúrate de tener los permisos necesarios para leer y escribir en las carpetas especificadas.
- La conversión de PDF a HTML o texto puede tener limitaciones en la preservación del formato original.
- Ajusta las rutas y parámetros de los scripts según las necesidades de tu proyecto.
- Si usas la opción de MongoDB, asegúrate de tener el servicio ejecutándose localmente.

---

## Contribuciones

¿Tienes mejoras o encontraste algún problema? ¡Contribuye! Abre un issue o envía una pull request.

---

**¡Disfruta del procesamiento y análisis eficiente de tus documentos jurídicos!**