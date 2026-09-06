import numpy as np

def CEE(y, t):
# If y = 0, log(y) becomes -inf, so we add a small delta to prevent this.
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

def mini_batch_CCE(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch_size
    # no one-hot
    # return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size