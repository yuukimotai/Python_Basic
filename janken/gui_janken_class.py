import tkinter as tk
import random
from PIL import Image, ImageTk

GU, CHOKI, PA = "グー", "チョキ", "パー"
hands = [GU, CHOKI, PA]
WIN, DRAW, LOSE = "勝ち", "あいこ", "負け"
rules = {#辞書型
  (0,0): DRAW, (0,1): WIN, (0,2): LOSE,
  (1,0): LOSE,(1,1): DRAW,(1,2): WIN,
  (2,0): WIN, (2,1): LOSE,(2,2): DRAW
}
root = tk.Tk()

class View():
    def __init__(self):
        self.gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
        self.gu_image = ImageTk.PhotoImage(self.gu_image)

        self.choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
        self.choki_image = ImageTk.PhotoImage(self.choki_image)

        self.pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
        self.pa_image = ImageTk.PhotoImage(self.pa_image)

        self.images = [self.gu_image, self.choki_image, self.pa_image]

        self.gu_label = tk.Label(root, image=self.gu_image)
        self.gu_label.place(x=30,y=200)

        self.choki_label = tk.Label(root, image=self.choki_image)
        self.choki_label.place(x=150,y=200)

        self.pa_label = tk.Label(root, image=self.pa_image)
        self.pa_label.place(x=270,y=200)

        self.gu_btn = tk.Button(root, text="グー")
        self.gu_btn.place(x=50,y=320)

        self.choki_btn = tk.Button(root, text="チョキ")
        self.choki_btn.place(x=160,y=320)

        self.pa_btn = tk.Button(root, text="パー")
        self.pa_btn.place(x=290,y=320)

        self.enemy_label = tk.Label(root, image=self.gu_image)
        self.enemy_label.place(x=160,y=20)

        self.text_label = tk.Label(root, text="最初はグー、じゃんけん！")
        self.text_label.place(x=160,y=140)
        
        self.retry_btn = tk.Button(root, text="リトライ")
    def reset(self):
      pass
    def display(enemy, result):
      self.enemy_label.configure(image=self.images[enemy])
      if result == DRAW:
        self.text_label.configure(text="あいこ")
      elif result == WIN:
        self.text_label.configure(text="勝ち")
      else:
        self.text_label.configure(text="負け")
         


class Application(tk.Frame):
  def ___init__(self, master=None):
    super().__init__(master)
    master.geometry('420x400')
    master.title('じゃんけんゲーム')

    self.view = View()

    self.view.gu_btn['command'] = lambda: self.judge(0)
    self.view.choki_btn['command'] = lambda: self.judge(1)
    self.view.pa_btn['command'] = lambda: self.judge(2)

    def judge(self, my_hand):
      enemy = random.randint(0,2)
      result = rules[my_hand, enemy]
      self.view.display()
    def retry():
      self.view.reset()

app = Application(master=root)
app.mainloop()