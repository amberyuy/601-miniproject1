#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:05:38 2018

@author: wangyuying
"""

from skimage import io,transform
import tensorflow as tf
import numpy as np


path1 = "/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/roses/873660804_37f5c6a46e_n.jpg"
path2 = "/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/roses/921138131_9e1393eb2b_m.jpg"
path3 = "/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/roses/1445228333_59a07e0801.jpg"
path4 = "/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/sunflowers/29972905_4cc537ff4b_n.jpg"
path5 = "/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/sunflowers/40411100_7fbe10ec0f_n.jpg"

flower_dict = {0:'roses',1:'sunflowers'}

w=100
h=100
c=3

def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)

with tf.Session() as sess:
    data = []
    data1 = read_one_image(path1)
    data2 = read_one_image(path2)
    data3 = read_one_image(path3)
    data4 = read_one_image(path4)
    data5 = read_one_image(path5)
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)

    saver = tf.train.import_meta_graph('/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/model.h5.meta')
    saver.restore(sess,tf.train.latest_checkpoint('/Users/wangyuying/Downloads/pe/tensor/flower/flower_photos/model'))

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(logits,feed_dict)

    #print prediction array
    #print(classification_result)
    #print prediction label
    #print(tf.argmax(classification_result,1).eval())
    #print flower type
    output = []
    output = tf.argmax(classification_result,1).eval()-2
    #print (output)
    for i in range(len(output)):
        print("Flower",i+1,"prediction:"+flower_dict[output[i]])