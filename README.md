# Proyecto: Impresión Automática de Imágenes Aleatorias

Este proyecto es un script de Python que automatiza la impresión de imágenes seleccionadas aleatoriamente desde una carpeta especificada. Utiliza bibliotecas como `Pillow` para manejar imágenes y `pywin32` para interactuar con la impresora predeterminada en sistemas Windows.

## Características Principales

1. **Impresión Directa:** Imprime imágenes directamente en la impresora predeterminada sin necesidad de cuadros de diálogo.
2. **Selección Aleatoria:** Selecciona una imagen aleatoria de la carpeta especificada y evita repetir las ya impresas.
3. **Redimensionado Automático:** Ajusta la imagen al tamaño de la impresora manteniendo la proporción.
4. **Automatización por Tiempo:** Configurado para imprimir una imagen cada cierto intervalo de tiempo.

## Requisitos del Sistema

- **Sistema Operativo:** Windows
- **Python:** Versión 3.7 o superior
- **Librerías Python:**
  - `Pillow`
  - `pywin32`

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. Descárgalo desde [python.org](https://www.python.org/).
2. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install pillow pywin32
   ```
3. Clona o descarga este repositorio en tu sistema.

## Uso

1. **Configura la ruta de la carpeta:**
   - Actualiza la variable `folder_path` en el código con la ruta de tu carpeta de imágenes:
     ```python
     folder_path = "D://ruta//a//tu//carpeta"
     ```

2. **Ejecuta el script:**
   - Abre una terminal en el directorio del script y ejecuta:
     ```bash
     python print_random_images.py
     ```

3. **Automatización:**
   - El script imprimirá una imagen al azar cada 60 segundos por defecto. Puedes ajustar este intervalo modificando la línea:
     ```python
     time.sleep(60)
     ```

## Estructura del Código

### 1. `print_image_directly(image_path)`
- **Propósito:** Imprime una imagen en la impresora predeterminada.
- **Detalles:**
  - Convierte la imagen a RGB si es necesario.
  - Redimensiona la imagen para ajustarse al tamaño de la impresora.
  - Envía la imagen a la cola de impresión.

### 2. `print_random_image_from_folder(folder_path)`
- **Propósito:** Selecciona aleatoriamente una imagen de la carpeta especificada y la imprime.
- **Detalles:**
  - Filtra solo los formatos de archivo válidos.
  - Evita imprimir imágenes que ya han sido procesadas.

### 3. Bucle Principal
- **Función:** Ejecuta el proceso de selección e impresión de imágenes en intervalos regulares.

## Personalización
- **Extensiones Válidas:** Puedes agregar o eliminar extensiones de imagen modificando la lista `valid_extensions` en el código.
- **Intervalo de Tiempo:** Ajusta el tiempo de espera entre impresiones cambiando el valor de `time.sleep()`.

## Notas Importantes

- Asegúrate de que la impresora predeterminada esté configurada correctamente en tu sistema.
- Si encuentras errores relacionados con las imágenes o la impresora, verifica los permisos de acceso a la carpeta y los controladores de la impresora.
