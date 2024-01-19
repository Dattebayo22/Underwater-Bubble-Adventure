from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Users\AnubhavV\Desktop\testing\MyGame\"
image_path = "C:\Users\AnubhavV\Desktop\testing\MyGame\How-to-Make-Text-Stand-Out-And-More-Readable.webp"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])
