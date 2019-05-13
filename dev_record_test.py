from utils import dataset
import tensorflow as tf
dataset.eval_input_fn
import os
params = {
    "data_dir":"./data/tfrecords",
"batch_size":128,
"max_length":256,
"num_parallel_calls":1,
"static_batch":False
}

#！！！file pattern会列举目录下的子目录文件，所以如果有子目录可能会引起另外的错误！！！
file_pattern = os.path.join(params["data_dir"] or "", "*dev*")

d =  dataset._read_and_batch_from_files(
      file_pattern, params["batch_size"], params["max_length"],
      1, shuffle=True, repeat=True,#params["num_parallel_calls"]
      static_batch=params["static_batch"])
#d.__iter__()
# d = tf.data.Dataset.list_files(file_pattern, shuffle=False)
# d = d.apply(dataset._load_records)
iterator = d.make_one_shot_iterator()
next_ele = iterator.get_next()
with tf.Session() as sess:
    for i in range(10):
        ele = sess.run(next_ele)
        print(ele)