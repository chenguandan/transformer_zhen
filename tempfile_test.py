import tempfile
import os
import tensorflow as tf
tmp = tempfile.NamedTemporaryFile(delete=False)
tmp_filename = tmp.name
# tmp.close()
with tf.gfile.Open(tmp_filename, "w") as f:
    for i in range(10):
        f.write("%d\n" % i)
# tmp.close()
os.remove(tmp_filename)