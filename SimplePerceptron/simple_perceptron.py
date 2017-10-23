import numpy as np
import matplotlib.pyplot as plt

EPS = 0.000001

class SimplePerceptron:
    def __init__(self, data_num, w1, w2, rate):
        self.data_num = data_num
        self.w1 = w1
        self.w2 = w2
        self.rate = rate

        self.wold = [0.0, 0.0]

        self.data = []
        
    def train_data_load(self, filename):
        self.data = np.loadtxt(filename)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_dot(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def error_func(self):
        L = 0.0
        for i in range(self.data_num):
            fx = self.sigmoid(self.w1*self.data[i][0]+self.w2*self.data[i][1])
            L += 0.5*pow((self.data[i][2]-fx),2)
        return L

    def train(self):
        wx = 0.0
        w = [0,0]    
        for i in range(self.data_num):
            xi = [self.data[i][0], self.data[i][1]]
            wx = self.wold[0]*xi[0]+self.wold[1]*xi[1]
            w[0] = self.wold[0] + self.rate * (self.data[i][2]-self.sigmoid(wx))*self.sigmoid_dot(wx)*xi[0]
            w[1] = self.wold[1] + self.rate * (self.data[i][2]-self.sigmoid(wx))*self.sigmoid_dot(wx)*xi[1]
        self.w1 = w[0]
        self.w2 = w[1]
        self.wold = w

    def run(self, iteration):
        for i in range(iteration):
            self.train()
            print self.error_func()

    def plot(self):
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for i in range(self.data_num):
            if self.data[i][2] == 1:
                x1.append(self.data[i][0])
                y1.append(self.data[i][1])
            else:
                x2.append(self.data[i][0])
                y2.append(self.data[i][1])

        xfig = range(-2, 6)
        yfig = [ -(self.w2/self.w1)*xi for xi in xfig]
        plt.scatter(x1, y1, marker='o', color='r')
        plt.scatter(x2, y2, marker='o', color='b')
        plt.plot(xfig, yfig)
        plt.show()

if __name__ == '__main__':
    sp = SimplePerceptron(100, 0.5, 0.1, 0.1)
    
    #try:
    sp.train_data_load('input.txt')
    sp.run(1000)
    #except Exception, e:
    #    print "Faild."

    sp.plot()

