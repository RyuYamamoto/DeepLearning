import numpy as np
import matplotlib.pyplot as plt

class SimplePerceptron:
    def __init__(self, filepath, rate):
        self.rate = rate
        self.data = np.loadtxt(filepath)
        self.bias = 1
        self.w = [0.1, 0.1]
        self.x = []
        self.label = []

        for index in self.data:
            self.x.append([index[0], index[1]])
            self.label.append(index[2])

    def sigmoid(self, x): 
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_dot(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))
    
    def train(self, iteration):
        for i in range(iteration):
            L = 0
            for index in range(len(self.data)):
                y_ = self.w[0]*self.x[index][0]+self.w[1]*self.x[index][1]
                L = L + ((self.label[index]-self.sigmoid(y_))*self.sigmoid_dot(y_-self.bias))
                self.w[0] = self.w[0] + self.rate*L*self.x[index][0]
                self.w[1] = self.w[1] + self.rate*L*self.x[index][1]

    def plot(self):
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for i in range(len(self.data)):
            if self.data[i][2] == 1:
                x1.append(self.x[i][0])
                y1.append(self.x[i][1])
            else:
                x2.append(self.x[i][0])
                y2.append(self.x[i][1])

        xfig = range(-2, 6)
        yfig = [ (self.w[1]/self.w[0])*xi for xi in xfig]
        plt.scatter(x1, y1, marker='o', color='r')
        plt.scatter(x2, y2, marker='o', color='b')
        plt.plot(xfig, yfig)
        plt.show()

if __name__ == '__main__':
    sp = SimplePerceptron('input.txt', 0.3)
    sp.train(1000)
    sp.plot()
