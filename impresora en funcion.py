import os
import random
import win32print
import win32ui
from PIL import Image, ImageWin
import time

# Lista para almacenar las imágenes ya impresas
printed_images = []

# Función para imprimir una imagen directamente sin mostrar el cuadro de diálogo
def print_image_directly(image_path):
    printer_name = win32print.GetDefaultPrinter()  # Obtener la impresora predeterminada
    print(f"Imprimiendo {image_path} en: {printer_name}")
    
    # Cargar la imagen
    img = Image.open(image_path)
    img = img.convert("RGB")  # Convertir la imagen a RGB por si acaso

    # Obtener el tamaño de la impresora
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    printer_size = hdc.GetDeviceCaps(110), hdc.GetDeviceCaps(111)

    # Redimensionar la imagen para ajustarla al tamaño de la página
    img_ratio = img.size[0] / img.size[1]
    printer_ratio = printer_size[0] / printer_size[1]
    
    if img_ratio > printer_ratio:
        new_width = printer_size[0]
        new_height = int(new_width / img_ratio)
    else:
        new_height = printer_size[1]
        new_width = int(new_height * img_ratio)

    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Imprimir la imagen
    hdc.StartDoc(image_path)
    hdc.StartPage()
    dib = ImageWin.Dib(img)
    dib.draw(hdc.GetHandleOutput(), (0, 0, new_width, new_height))
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()

# Función para seleccionar e imprimir una imagen al azar sin repetir
def print_random_image_from_folder(folder_path):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    all_images = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if any(filename.lower().endswith(ext) for ext in valid_extensions)]
    
    # Filtrar las imágenes que no han sido impresas
    unprinted_images = [img for img in all_images if img not in printed_images]

    if not unprinted_images:
        print("Todas las imágenes ya fueron impresas.")
        return
    
    random_image = random.choice(unprinted_images)  # Seleccionar una imagen aleatoria
    print_image_directly(random_image)
    
    # Agregar la imagen impresa a la lista de impresas
    printed_images.append(random_image)

# Ruta de la carpeta con las imágenes
folder_path = "D://010111010//algo//Ganyu"  # Cambia esta ruta por la ubicación de tu carpeta de imágenes

# Ejemplo: imprimir una imagen al azar cada hora
while True:
    print_random_image_from_folder(folder_path)
    time.sleep(60)  # Pausar durante 1 hora (3600 segundos) antes de imprimir la siguiente

