import random

hands = ["グー", "チョキ", "パー"]

while True:
  enemy_hand = random.randint(0,2)
  my_hand = int(input("0~2の数字を入力して下さい\n0:グー 1: チョキ 2: パー >>>\n"))
  win, draw, lose = ("勝ち", "あいこ", "負け")
  rules = {#辞書型
    (0,0): draw, (0,1): win, (0,2): lose,
    (1,0): lose,(1,1): draw,(1,2): win,
    (2,0): win, (2,1): lose,(2,2): draw
  }
  result = rules[(my_hand, enemy_hand)]

  print("自分 " + hands[my_hand] + " / " + "相手 " + hands[enemy_hand])
  print(result)
  
  if enemy_hand != my_hand:
    break