import os
import pathlib

print(os.getcwd())
if not os.path.isdir('sample_dir'):
  os.mkdir('sample_dir')# mkdirsで複数、ネストしたディレクトリも作ってくれる

p = pathlib.Path('./sample_dir/sample1.txt')
p.touch()

with p.open(mode='w') as f:
  f.write('Good morning.')
with p.open(mode='r') as f:
  print(f.read())

#text = p.read_text() こちらではファイルを開かず読み込める
#count = p.write_text('文字列')　これで書き込める。printすると文字数が出力される
# p.unlink()でファイル削除できる
#os.rmdir('sample_dir')

os.makedirs('sample_dir/sample_dir1', exist_ok=True)
chrs = ['a','b','c','d']

for ch in chrs:
  pathlib.Path(f'sample_dir/{ch * 3}.txt').touch()

pathlib.Path(f'sample_dir/sample_dir1/eee.txt').touch()
pathlib.Path(f'sample_dir/sample_dir1/fff.csv').touch()
