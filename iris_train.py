#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from chainer import cuda, Variable, FunctionSet, optimizers, serializers
import chainer.functions as F
import sys
import pickle

plt.style.use('ggplot')

# 確率的勾配降下法で学習させる際の一回分のバッチサイズ
batchsize = 5

# 学修の繰り返し回数
n_epoch = 1000

# 中間層の数
n_units = 10

iris = load_iris()
x = iris.data.astype(np.float32)
y = iris.target
y = y.flatten().astype(np.int32)

# 学習用データをN個、検証用データを残りの個数と設定
index = np.arange(y.size)
x_train = x[index % 2 != 0, :]
x_test = x[index % 2 == 0, :]
y_train = y[index % 2 != 0]
y_test = y[index % 2 == 0]
N_test = y_test.size
N = y_train.size

# Prepare multi-layerr perceptron model
# 多層パーセプトロンモデルの設定
model = FunctionSet(l1=F.Linear(4, n_units),
					l2=F.Linear(n_units, n_units),
					l3=F.Linear(n_units,3))

# Neural net architecture
# ニューラルネットワークの構造
def forward(x_data, y_data, train=True):
	x, t = Variable(x_data), Variable(y_data)
	h1 = F.dropout(F.relu(model.l1(x)), train=train)
	h2 = F.dropout(F.relu(model.l2(h1)), train=train)
	y = model.l3(h2)
	# 他クラス分類なので誤差関数としてソフトマックス関数の
	# 交差エントロピー関数を用いて、誤差を導出
	return F.softmax_cross_entropy(y, t), F.accuracy(y, t)
	
optimizer = optimizers.SGD()
optimizer.setup(model.collect_parameters())
optimizer.zero_grads()

train_loss = []
train_acc = []
test_loss = []
test_acc = []

l1_W = []
l2_W = []
l3_W = []

for epoch in xrange(1, n_epoch+1):
	print 'epoch', epoch

	# training
	# N個の順番をランダムに並び替える
	perm = np.random.permutation(N)
	sum_accuracy = 0
	sum_loss = 0
	# 0~Nまでのデータをバッチサイズごとに使って学習
	for i in xrange(0, N, batchsize):
		x_batch = x_train[perm[i:i+batchsize]]
		y_batch = y_train[perm[i:i+batchsize]]
	
		# 勾配を初期化
		optimizer.zero_grads()
		# 順伝播させて誤差と精度を算出
		loss, acc = forward(x_batch, y_batch)
		# 誤差逆伝播で勾配を計算
		loss.backward()
		optimizer.update()

		sum_loss += float(cuda.to_cpu(loss.data)) * len(y_batch)
		sum_accuracy += float(cuda.to_cpu(acc.data)) * len(y_batch)
	train_loss.append(sum_loss/N)
	train_acc.append(sum_accuracy/N)
	# 訓練データの誤差と、正解精度を表示 
	print 'train mean loss={}, accuracy={}'.format(sum_loss / N, sum_accuracy / N)
	
	# evaluation
	# テストデータで誤差と、正解精度を算出し汎化性能を確認
	sum_accuracy = 0
	sum_loss = 0
	for i in xrange(0, N_test, batchsize):
		x_batch = x_test[i:i+batchsize]
		y_batch = y_test[i:i+batchsize]

		# 順伝播させて誤差と精度を算出
		loss, acc = forward(x_batch, y_batch, train=False)

		sum_loss += float(cuda.to_cpu(loss.data)) * len(y_batch)
		sum_accuracy += float(cuda.to_cpu(acc.data)) * len(y_batch)
	test_loss.append(sum_loss/N_test)
	test_acc.append(sum_accuracy/N_test)
	# テストデータでの誤差と、正解精度を表示
	print 'test mean loss={}, accuracy={}'.format(sum_loss / N_test, sum_accuracy / N_test)

	# 学習したパラメータを保存
	l1_W.append(model.l1.W)
	l2_W.append(model.l2.W)
	l3_W.append(model.l3.W)

serializers.save_npz("iris_model.npz", model)

# 精度と誤差をグラフ描画
plt.figure(figsize=(8,6))
plt.plot(range(len(train_acc)), train_acc)
plt.plot(range(len(test_acc)), test_acc)
plt.legend(["train_acc", "test_acc"], loc=4)
plt.title("Accuracy of digit recognition.")
plt.plot()
plt.show()
