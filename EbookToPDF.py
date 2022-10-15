import numpy as np 
import cv2 
import pyautogui 
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
mergedObject = PdfFileMerger()

n = 1177
pyautogui.click(x=100, y=200)
for x in range(n):
    image1 = pyautogui.screenshot(region=(555,0,810,1080))  #screenshot page
    im1 = image1.convert('RGB') #prepare image
    im1.save('C:/Users/joepr/Downloads/test/' +str(x)+".pdf") #convert to pdf
    pyautogui.press('right') #turn page

for x in range(n):
    mergedObject.append(PdfFileReader("C:/Users/joepr/Downloads/test/" + str(x)+ '.pdf', 'rb')) #append pdf file with page
mergedObject.write("C:/Users/joepr/Downloads/output.pdf") #save result to file

