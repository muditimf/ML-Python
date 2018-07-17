#!/usr/bin/python3

import tensorflow as tf

x=tf.constant([2,3])
y=tf.constant([3,4])

process=tf.add(x,y)

#t=tf.Session()
#print(t.run(process))


with tf.Session() as ss:
	output=ss.run(process)
	print(output)
