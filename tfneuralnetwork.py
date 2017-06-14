# Import Tensorflow
import tensorflow as tf
# Import Numpy
import numpy as np

# Setup Data is in 3 lists, input a, input b, and output
# Must cast values to type float32 for proper functioning of Numpy
input_a = [np.float32(0.0), np.float32(0.0), np.float32(1.0), np.float32(1.0)]
input_b = [np.float32(0.0), np.float32(1.0), np.float32(0.0), np.float32(1.0)]
outputs = [np.float32(0.0), np.float32(1.0), np.float32(1.0), np.float32(0.0)]

# Initialize our weights
weight_1a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight_1b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight_2a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight_2b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight_oa = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight_ob = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
bias_a = tf.Variable(tf.zeros([1]))
bias_b = tf.Variable(tf.zeros([1]))
bias_c = tf.Variable(tf.zeros([1]))

# Initialize error tracking variable
err_total = 0
for i in range(3):

    # Neural Network Formula for Nodal Value 
    output = weight_a * input_a[i] + weight_b * input_b[i] + biases
    err_total += tf.square(output - outputs[i])

# Divide error to get the mean for each configuration
err_total /= 4

# Training Setup
optimization = tf.train.GradientDescentOptimizer(learning_rate=0.5)
training = optimization.minimize(err_total)

# Initialization
init = tf.global_variables_initializer()
runtime = tf.Session()
runtime.run(init)

# Training Loop
for i in range(10000):
    runtime.run(training)
    if i % 1000 == 0:
        print(i, runtime.run(weight_a), runtime.run(weight_b), runtime.run(biases))

print(np.float32((runtime.run(weight_a)).tolist()[0]) * 0 +
      np.float32((runtime.run(weight_b)).tolist()[0]) * 0 +
       (np.float32((runtime.run(biases)).tolist()[0])))
print(np.float32((runtime.run(weight_a)).tolist()[0]) * 0 +
      np.float32((runtime.run(weight_b)).tolist()[0]) * 1 +
       (np.float32((runtime.run(biases)).tolist()[0])))
print(np.float32((runtime.run(weight_a)).tolist()[0]) * 1 +
      np.float32((runtime.run(weight_b)).tolist()[0]) * 0 +
       (np.float32((runtime.run(biases)).tolist()[0])))
print(np.float32((runtime.run(weight_a)).tolist()[0]) * 1 +
      np.float32((runtime.run(weight_b)).tolist()[0]) * 1 +
       (np.float32((runtime.run(biases)).tolist()[0])))