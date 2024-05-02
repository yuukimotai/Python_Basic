import csv

data = '''11,12,13,14
21,22,23,24
31,32,33,34
'''
data2 = [41, 42, 43, 44]

with open('sample.csv', mode='r') as f:
  #f.write(data)
  reader = csv.reader(f)# [delimiter= ' '] で空白区切りなどにする事も可
  for row in reader:
    print(row)
data = [41, 42, 43, 44]

with open('sample.csv', mode='a+', newline='') as f:# a+ 追記の読み書き両用
  writer = csv.writer(f)
  writer.writerow(data2)

  f.seek(0)
  print(f.read())