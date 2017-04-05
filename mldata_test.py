#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chainer import serializers, FunctionSet, Variable
from sklearn.datasets import fetch_mldata
import chainer.functions as F
import matplotlib.pyplot as plt
import numpy as np

def draw_digit3(data, n, ans, recog):
	size = 28
	plt.subplot(10,10,n)
	Z = data.reshape(size,size)
	Z = Z[::-1,:]
	plt.xlim(0,27)
	plt.ylim(0,27)
	plt.pcolor(Z)
	plt.title("ans=%d, recog=%d"%(ans,recog), size=8)
	plt.gray()
	plt.tick_params(labelbottom="off")
	plt.tick_params(labelleft="off")

mnist = fetch_mldata('MNIST original')
# mnist.data : 70,000件の784次元ベクトルデータ
mnist.data = mnist.data.astype(np.float32)
mnist.data /= 255 # 0-1のデータに変換

# mnist.target : 正解データ(教師データ)
mnist.target = mnist.target.astype(np.int32)

n_units = 1000
N = 60000
x_train, x_test = np.split(mnist.data, [N])
y_train, y_test = np.split(mnist.target, [N])
N_test = y_test.size

model = FunctionSet(l1=F.Linear(784, n_units),
					l2=F.Linear(n_units, n_units),
					l3=F.Linear(n_units,10))

serializers.load_npz("mnist_model.npz", model)

# 答え合わせ
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15,15))
cnt = 0
for idx in np.random.permutation(N)[:100]:
	xxx = x_train[idx].astype(np.float32)
	h1 = F.dropout(F.relu(model.l1(Variable(xxx.reshape(1,784)))), train=False)
	h2 = F.dropout(F.relu(model.l2(h1)), train=False)
	y = model.l3(h2)
	cnt += 1
	draw_digit3(x_train[idx], cnt, y_train[idx], np.argmax(y.data))
plt.show()

