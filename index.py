from PIL import Image 

import pytesseract 

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ruta_imagen = "img1.jpg"
imagen_abierta =Image.open(ruta_imagen)
texto = pytesseract.image_to_string(imagen_abierta)
print(texto)
