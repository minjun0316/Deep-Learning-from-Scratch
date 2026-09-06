import numpy as np

def partial_derivative(f, x, progress_callback=None):
    h = 1e-4
    grad = np.zeros_like(x)

    for completed, idx in enumerate(np.ndindex(x.shape), start=1):
        # Partial differentiation changes only one variable at a time
        # while keeping all other variables fixed.
        # Save the original value because x[idx] will be temporarily changed
        # to x[idx] - h and x[idx] + h for numerical differentiation.
        tmp_val = x[idx]

        x[idx] = tmp_val-h
        fxh1 = f(x)

        x[idx] = tmp_val+h
        fxh2 = f(x)

        # Use f(x), not f(x[idx]), because f is a multivariable function.
        # The entire vector x must be passed so that all other variables
        # remain fixed while only x[idx] is changed.
        grad[idx] = (fxh2 - fxh1) / (2*h)
        x[idx] = tmp_val
        if progress_callback is not None:
            progress_callback(completed, x.size)

    return grad
