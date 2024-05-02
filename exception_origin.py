# 独自の例外作成について
#raise TypeError('型が一致しません')
class TempError(Exception):# Exceptionを継承して
  pass

try:
  body_temperature = float(input())
except ValueError as ve:
  print('体温は数値を入力して下さい')
  exit()

if body_temperature < 35.9 or body_temperature > 41:
  raise TempError('体温が異常です。再度入力して下さい。')
elif body_temperature < 37.5:
  print('正常な範囲の体温です。')
else:
  ('発熱があります。療養が必要です。')