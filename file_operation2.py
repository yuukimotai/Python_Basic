with open('sample.txt', mode='r+') as f:
  print(f.tell())
  data = f.read()# ファイルポインターのある位置からファイルの末尾まで読み込むので注意
  print(f.tell())# ファイルポインターの位置が最後に行く
  f.write('Good morning\n')
  f.seek(0)#ファイルの先頭へファイルポインターを移動する
  data2 = f.read()
  print(f.tell())
  print(data2)
# modeは a+ もある