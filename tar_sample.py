import tarfile as tf

# with tf.open('tar_sample.tar.gz', mode='w:gz') as tr:
#   tr.add('sample_dir')
with tf.open('tar_sample.tar.gz', mode='r:gz') as tr:
  tr.extractall('tar_sample_extract')# extract で一部解凍も可
