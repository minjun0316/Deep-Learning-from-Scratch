import sys, os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from ch4_2_1CEE import mini_batch_CCE
from Ch3_Neural_Network.ch3_2_4Sigmoid import sigmoid
from Ch3_Neural_Network.ch3_5_5softmax import softmax
from ch4_4_1partial_derivative import partial_derivative

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # Initialize the weights with small random values.
        # np.random.randn() generates random values from a standard normal distribution
        # with a mean of 0 and a standard deviation of 1.
        # Multiplying by weight_init_std scales the standard deviation to 0.01.
        # Random initialization prevents neurons from learning identical features.
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    def loss(self, x, t):
        y = self.predict(x)
        return mini_batch_CCE(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t, verbose=False):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        total = sum(param.size for param in self.params.values())
        offset = 0
        last_report = time.perf_counter()

        def report(completed, size):
            nonlocal last_report
            now = time.perf_counter()
            if now - last_report >= 5 or completed == size:
                print(
                    f"  {key}: {completed}/{size} | "
                    f"이번 반복 기울기 {offset + completed}/{total} "
                    f"({(offset + completed) / total:.1%})",
                    flush=True,
                )
                last_report = now

        for key in ('W1', 'b1', 'W2', 'b2'):
            grads[key] = partial_derivative(
                loss_W, self.params[key],
                progress_callback=report if verbose else None,
            )
            offset += self.params[key].size

        return grads
                                
