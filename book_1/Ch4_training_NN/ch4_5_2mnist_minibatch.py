import sys, os
import time
from datetime import timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from Ch3_Neural_Network.mnist import load_mnist
from ch4_5_1two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

training_start = time.perf_counter()
for i in range(iters_num):
    iteration_start = time.perf_counter()
    print(f"[{i + 1}/{iters_num}] 기울기 계산 시작", flush=True)
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = network.numerical_gradient(x_batch, t_batch, verbose=True)

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    completed = i + 1
    elapsed = time.perf_counter() - training_start
    remaining = elapsed / completed * (iters_num - completed)
    print(
        f"[{completed}/{iters_num}] 완료 ({completed / iters_num:.2%}) | "
        f"loss={loss:.6f} | 이번 반복 {time.perf_counter() - iteration_start:.1f}초 | "
        f"경과 {timedelta(seconds=int(elapsed))} | "
        f"예상 남은 시간 {timedelta(seconds=int(remaining))}",
        flush=True,
    )
