f = open('sample.txt', mode='w')
f.write('Hello Python!\n')# 同じファイル名のものがすでにある場合は中身が一度全消去されて再書き込みされる
f.close()# メモリを食うため、必ず閉じる
# print(f)
# print(type(f))
with open('sample.txt', mode='w') as f:
  f.write('Hello World\n')
  f.write('Good evening World\n')

with open('sample.txt', mode='r') as f:
  # data = f.read()
  # print(data)
  lines = f.readlines()
  for line in lines:
    print(line, end="")#end に空文字を入れないと改行コードが入り、改行される
