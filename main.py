import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import cv2

def upload():
    global file_path
    file_path = filedialog.askopenfilename()
    print(f"selected file :-  {file_path}")

    if file_path:
        root.destroy()

root = tk.Tk()
root.geometry("300x200")
root.title("upload an image")

button = tk.Button(root, text="select img", command=upload)
button.pack(padx= 10, pady = 90)

root.mainloop()

originalImage = cv2.imread(file_path)
originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

if originalImage is None:
    print("no image found. please select an Image to Cartoonify")
    exit()


resized1 = cv2.resize(originalImage, (960,540))

grayScaleImg = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
resized2 = cv2.resize(grayScaleImg, (960,540))

smoothGrayScale = cv2.medianBlur(grayScaleImg, 5)
resized3 = cv2.resize(smoothGrayScale, (960,540))

GetEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
resized4 = cv2.resize(GetEdge, (960, 540))


colorImg = cv2.bilateralFilter(originalImage, 9, 500, 500)
resized5 = cv2.resize(colorImg, (960, 540))

cartoonImage = cv2.bitwise_and(colorImg, colorImg, mask=GetEdge)
resized6 = cv2.resize(cartoonImage, (960,540))

plt.imshow(resized6)
plt.show()

