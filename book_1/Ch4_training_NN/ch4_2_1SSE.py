import numpy as np

def SSE(y, t):
    # 1/2 cancels out the 2 that appears when differentiating the squared term.
    return 0.5 * np.sum((y-t)**2)