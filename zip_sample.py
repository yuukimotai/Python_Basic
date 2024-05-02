import zipfile as zp
import glob as gb

with zp.ZipFile('sample_dir/sample_zip.zip', mode='w') as zf:# mode='a'　だと既存のzipに追加できる
  for f in gb.glob('sample_dir/*.txt'): #zf.extractallでzipの解凍、抽出できる
    zf.write(f)