import calculator

print(calculator.add(10, 5))
print(calculator.subtract(20, 7))

from calculator import add

print(add(10, 20))


from calculator import add, subtract

print(add(4, 5))
print(subtract(10, 3))