#from PIL import Image
import random
import tkinter as tk

win = tk.Tk()
win.geometry("480x360")

btn1 = tk.Button(win, text="click")
btn1.grid()

btn2 = tk.Button(win, text="click", bg="red")
btn2.grid()

btn3 = tk.Button(win, text="click", activebackground="red")
btn3.grid()

btn4 = tk.Button(win, text="click", bg="red", activebackground="red")
btn4.grid()

win.mainloop()