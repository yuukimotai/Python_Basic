import csv

nums = [
  [11,12,13,14],
  [21,22,23,24],
  [31,32,33,34]
]

header = ["","ONE","TWO","THREE","FOUR"]
index = ["one","two","three","four",]

# with open("sample2.csv", mode="w+", newline='') as f:
#   writer = csv.writer(f)
#   writer.writerow(header)
#   for i, row in zip(index, nums):
#     writer.writerow([i] + row)
#     f.seek(0)
#     print(f.read())

with open("sample3.csv", mode="w+", newline='') as f:
  writer = csv.writer(f)
  for row in nums:
    writer.writerow(row)
  f.seek(0)
  reader = csv.DictReader(f, fieldnames=['ONE','TWO','THREE','FOUR'])
  for row in reader:
    print(row)

with open("sample3.csv", mode="w+", newline='') as f:
  writer = csv.DictWriter(f, fieldnames=['ONE','TWO','THREE','FOUR'])#キー:バリューで対応する
  writer.writerow({'ONE':41,'TWO':42,'THREE':43,'FOUR':44})
  f.seek(0)
  reader = csv.DictReader(f, fieldnames=['ONE','TWO','THREE','FOUR'])
  for row in reader:
    print(row)