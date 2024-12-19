from Try import ints_try
from calc import adder, my_module, subtractor
x, y = input(), input()
ints_try.ints(x)
ints_try.ints(y)
print(adder.add(x,y))
print(subtractor.subtract(x,y))