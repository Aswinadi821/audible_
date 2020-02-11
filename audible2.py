
import pytesseract 
from PIL import Image
import pyttsx3
from googletrans import Translator


img = Image.open('C:/Users/aswin/Desktop/7b4ed04d44d350ae14885ad15bcbed40eacdbf7c.png')
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/aswin/AppData/Local/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img, lang='eng',
                    config='--psm 7')
with open('abc.txt', mode='w') as file:
     file.write(result)
print(result)
p=Translator()
k=p.translate(result,dest='english')
print(k)
engine= pyttsx3.init()

engine.say(k)
engine.runAndWait()

 
