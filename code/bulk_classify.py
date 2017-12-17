from __future__ import absolute_import

from __future__ import division
from __future__ import print_function

import argparse
import sys
import time

import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

for k in range(4):
    path_of = '/home/adil/image_classification/supporting_files/data_set/sc5-2013-Mar-Apr-Test-20130412/'
    with open('/home/adil/image_classification/supporting_files/data_set/sc5-2013-Mar-Apr-Test-20130412/ground_truth.txt') as f:
          lines = f.readlines()
          newlist = []
          for word in lines:
                  word = word.split(";")
                  newlist.extend(word)
    listOdd = newlist[1::2]
    listEven = newlist[::2]
    path_file = path_of+listEven[k]
    #print (path_file)
    #print (listOdd[k])
    def load_graph(model_file):
      graph = tf.Graph()
      graph_def = tf.GraphDef()

      with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
      with graph.as_default():
        tf.import_graph_def(graph_def)

      return graph

    def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
    				input_mean=0, input_std=255):
      input_name = "file_reader"
      output_name = "normalized"
      #print (file_name)
      file_reader = tf.read_file(file_name, input_name)
      image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                            name='jpeg_reader')
      float_caster = tf.cast(image_reader, tf.float32)
      dims_expander = tf.expand_dims(float_caster, 0);
      resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
      normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
      sess = tf.Session()
      result = sess.run(normalized)

      return result

    def load_labels(label_file):
      label = []
      proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
      for l in proto_as_ascii_lines:
        label.append(l.rstrip())
      return label

    if __name__ == "__main__":
      file_name = path_file
      model_file = "supporting_files/retrained_graph.pb"
      label_file = "supporting_files/retrained_labels.txt"
      input_height = 299 #change this according to your image for the image in the boat classifier the values are 229
      input_width = 299
      input_mean = 128
      input_std = 128
      input_layer = "Mul"
      output_layer = "final_result"

      graph = load_graph(model_file)
      t = read_tensor_from_image_file(file_name,
                                      input_height=input_height,
                                      input_width=input_width,
                                      input_mean=input_mean,
                                      input_std=input_std)

      input_name = "import/" + input_layer
      output_name = "import/" + output_layer
      input_operation = graph.get_operation_by_name(input_name);
      output_operation = graph.get_operation_by_name(output_name);

      with tf.Session(graph=graph) as sess:
        start = time.time()
        results = sess.run(output_operation.outputs[0],
                          {input_operation.outputs[0]: t})
        end=time.time()
      test = np.squeeze(results)

      results = np.squeeze(results)

      top_k = results.argsort()[-1:][::-1]
      d = np.amax(top_k)
      #print (d)

      labels = load_labels(label_file)


    #  if ((labels[d]+'\r\n') or labels[d] ) == (listOdd[k] or (list[k]+'\r\n')):
    #        print ('yeaaasss!!')
     # else:
    #        print ('Tty harder ')
      #print (labels[])
     # print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
      asd = open('/home/adil/Image_classification/supporting_files/results/pre_result.csv', 'a+')
      for i in top_k:
        print(labels[i])

        asd.write(labels[i]+','+listOdd[k])

    #print (listOdd[k])
f.close()
