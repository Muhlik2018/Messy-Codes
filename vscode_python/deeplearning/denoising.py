import numpy as np
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
 
mnist = input_data.read_data_sets('MNIST_data', validation_size=0)
 
#mnist = tf.keras.datasets.mnist # 包含了很多数据集，第一次使用需要下载
#(X_train, y_train), (X_test, y_test) = mnist.load_data()
#print(X_train.shape) # out: (60000, 28, 28)
#print(y_train.shape) # out: (60000,)



inputs_ = tf.placeholder(tf.float32, (None, 28, 28, 1), name='inputs')
targets_ = tf.placeholder(tf.float32, (None, 28, 28, 1), name='targets')



 
### 编码器
conv1 = tf.layers.conv2d(inputs_, 32, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 28x28x32
maxpool1 = tf.layers.max_pooling2d(conv1, (2,2), (2,2), padding='same')
# 当前shape: 14x14x32
conv2 = tf.layers.conv2d(maxpool1, 32, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 14x14x32
maxpool2 = tf.layers.max_pooling2d(conv2, (2,2), (2,2), padding='same')
# 当前shape: 7x7x32
conv3 = tf.layers.conv2d(maxpool2, 16, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 7x7x16
encoded = tf.layers.max_pooling2d(conv3, (2,2), (2,2), padding='same')
# 当前shape: 4x4x16
 
 
### 解码器
upsample1 = tf.image.resize_nearest_neighbor(encoded, (7,7))
# 当前shape: 7x7x16
conv4 = tf.layers.conv2d(upsample1, 16, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 7x7x16
upsample2 = tf.image.resize_nearest_neighbor(conv4, (14,14))
# 当前shape: 14x14x16
conv5 = tf.layers.conv2d(upsample2, 32, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 14x14x32
upsample3 = tf.image.resize_nearest_neighbor(conv5, (28,28))
# 当前shape: 28x28x32
conv6 = tf.layers.conv2d(upsample3, 32, (3,3), padding='same', activation=tf.nn.relu)
# 当前shape: 28x28x32
 
 
logits = tf.layers.conv2d(conv6, 1, (3,3), padding='same', activation=None)
#当前shape: 28x28x1
 
 
decoded = tf.nn.sigmoid(logits, name='decoded')
 
 
loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=targets_, logits=logits)
cost = tf.reduce_mean(loss)
opt = tf.train.AdamOptimizer(0.001).minimize(cost)
 
 
sess = tf.Session()
epochs = 1
batch_size = 200
# Set's how much noise we're adding to the MNIST images
noise_factor = 0.5
sess.run(tf.global_variables_initializer())
for e in range(epochs):
    for ii in range(mnist.train.num_examples // batch_size):
        batch = mnist.train.next_batch(batch_size)
        # Get images from the batch
        imgs = batch[0].reshape((-1, 28, 28, 1))
        # Add random noise to the input images
        noisy_imgs = imgs + noise_factor * np.random.randn(*imgs.shape)
        # Clip the images to be between 0 and 1
        noisy_imgs = np.clip(noisy_imgs, 0., 1.)
        # Noisy images as inputs, original images as targets
        batch_cost, _ = sess.run([cost, opt], feed_dict={inputs_: noisy_imgs,
                                                         targets_: imgs})
        print("Epoch: {}/{}...".format(e + 1, epochs),
              "Training loss: {:.4f}".format(batch_cost))
 
 
in_imgs = mnist.test.images[:10]
noisy_imgs = in_imgs + noise_factor * np.random.randn(*in_imgs.shape)
noisy_imgs = np.clip(noisy_imgs, 0., 1.)
reconstructed = sess.run(decoded, feed_dict={inputs_: noisy_imgs.reshape((10, 28, 28, 1))})
plt.figure(figsize=(20,4))
for i in range(10):
    #画原始图像
    ax=plt.subplot(2,10,i+1)
    plt.imshow(in_imgs[i].reshape((28,28)))
    plt.gray()#只有黑白两色，没有中间色
    #重建图像
    ax=plt.subplot(2,10,i+10+1)
    plt.imshow(reconstructed[i].reshape((28,28)))
    plt.gray()
    ax.get_xaxis().set_visible(False) #不显示x轴
    ax.get_yaxis().set_visible(False)#不显示y轴
plt.show()
sess.close()