# apple_price = 100
# apple_num = 2
# tax = 1.1
from ch5_4_1layer_naive import MulLayer

#forward
apple_price = 100
apple_num = 2
tax = 1.1

mul_apple = MulLayer()
mul_tax = MulLayer()

two_apple_price = mul_apple.forward(apple_price, apple_num)
apple_price_with_tax = mul_tax.forward(two_apple_price, tax)

print(apple_price_with_tax)


#backward
dapple_price_with_tax = 1
dtwo_apple_price, dtax = mul_tax.backward(dapple_price_with_tax)
dapple_price, dapple_num = mul_apple.backward(dtwo_apple_price)

print(dapple_price, dapple_num, dtax)