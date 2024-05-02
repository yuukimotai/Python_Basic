# pythonでも、構文エラーと例外がある

nums = [0,1,2]

try:
  print(nums[3])
except (IndexError, ZeroDivisionError) as e:# 書いたもの以外の例外は補足しない
  print(f'{e}: 例外が発生しました')
except TypeError as e:# exceptを書き分ける事で例外発生時の処理も分けられる　全て補足したい場合は　Exception（基底クラス）
  print('型が違います')

print('finish.')

def double(num):
  if not isinstance(num, int):
    raise TypeError(f'整数を入力して下さい。{type(num)}が入力されました。')
  return num * 2

a = double(9)
print(a)
