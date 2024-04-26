from PIL import Image
import random
import tkinter as tk

root = tk.Tk()
root.geometry("420x400")

img = Image.open('./img/gu.png')
print(img)