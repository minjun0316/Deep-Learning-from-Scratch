# Skipped because mnist.py was copied from the original deep-learning-from-scratch repository.
# See the original location for this example.

from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_test.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)