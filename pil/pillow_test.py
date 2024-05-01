from PIL import Image, ImageTk
import tkinter as tk

img = Image.open('choki.png')

#img.convert('L').show() 白黒
#img.point(lambda x: x * 0.5).show() 明度を落とす
#img.rotate(-90, expand=True).show() 回転
img.resize([x // 20 for x in img.size]).resize(img.size).show()# モザイク