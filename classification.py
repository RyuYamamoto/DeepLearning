#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

def plot_decision_boundary(pred_func):
   # Set min and max values and give it some padding
   x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
   y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
   h = 0.01
   # Generate a grid of points with distance h between them
   xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
   # Predict the function value for the whole gid
   Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
   Z = Z.reshape(xx.shape)
   # Plot the contour and training examples
   plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
   plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

def calculate_loss(model):
	W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
	#予測を算出するためのForward Propagation
	z1 = X.dot(W1) + b1
	a1 = np.tanh(z1)
	z2 = a1.dot(W2) + b2
	exp_scores = np.exp(z2)
	probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
	#Lossを計算
	corect_logprobs = -np.log(probs[range(num_examples), y])
	data_loss = np.sum(corect_logprobs)
	#Lossにregulatization termを与える
	data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
	return 1./num_examples * data_loss

def predict(model, x):
	W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']	
	# Forward Propagation
	z1 = x.dot(W1) + b1
	a1 = np.tanh(z1)
	z2 = a1.dot(W2) + b2
	exp_scores = np.exp(z2)
	probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
	return np.argmax(probs, axis=1)

np.random.seed(0)
X, y = datasets.make_moons(200, noise=0.20)
num_examples = len(X) #学習用データサイズ
nn_input_dim = 2 #インプット層の次元数
nn_output_dim = 2 #アウトプット層の次元数

epsilon = 0.01 #勾配降下の学習率
reg_lambda = 0.01 #regularizationの強さ

clf = linear_model.LogisticRegressionCV()
clf.fit(X,y)

plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")
plt.show()
