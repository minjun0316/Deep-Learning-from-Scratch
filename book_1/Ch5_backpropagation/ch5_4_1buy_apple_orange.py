from ch5_4_1layer_naive import MulLayer, AddLayer

apple = 100
orange = 150
apple_num = 2
orange_num = 3
tax = 1.1

#forward
mul_two_apple = MulLayer()
mul_three_orange = MulLayer()
two_apple = mul_two_apple.forward(apple, apple_num)
three_orange = mul_three_orange.forward(orange, orange_num)

add_apple_orange = AddLayer()
apple_orange = add_apple_orange.forward(two_apple, three_orange)

mul_tax = MulLayer()
price = mul_tax.forward(apple_orange, tax)

print(price)

#backward
dprice = 1
dapple_orange, dtax = mul_tax.backward(dprice)
dtwo_apple, dthree_orange = add_apple_orange.backward(dapple_orange)
dorange, dorange_num = mul_three_orange.backward(dthree_orange)
dapple, dapple_num = mul_two_apple.backward(dtwo_apple)

print(dapple, dapple_num, dorange, dorange_num, dtax)
