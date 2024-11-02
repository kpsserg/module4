from fake_math import  devide as fake_devide
from true_math import devide as true_devide

print(globals())

result1 = fake_devide(69, 3)
result2 = fake_devide(3, 0)
result3 = true_devide(49, 7)
result4 = true_devide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)