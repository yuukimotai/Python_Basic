# じゃんけんアプリの回

gu, choki, pa = ("グー", "チョキ", "パー")
win, draw, lose = ("勝ち", "あいこ", "負け")

my_hand = gu
enemy_hand = pa

if my_hand == enemy_hand:
  print(draw)
elif (my_hand == gu and enemy_hand == choki) or \
      (my_hand == choki and enemy_hand == pa) or \
      (my_hand == pa and enemy_hand == gu):
  print(win)
else:
  print(lose)
#辞書に勝敗表を書き込んで書くこともできる
# 0: グー, 1: チョキ, 2: パー　などとできる。
win, draw, lose = ("勝ち", "あいこ", "負け")
rules = {#辞書型
  (0,0): draw, (0,1): win, (0,2): lose,
  (1,0): lose,(1,1): draw,(1,2): win,
  (2,0): win, (2,1): lose,(2,2): draw
}

my_hand = 0
enemy_hand = 2
result = rules[(my_hand, enemy_hand)]
print(result)