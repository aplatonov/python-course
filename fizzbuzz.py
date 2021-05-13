print(
"""
Написать программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz. 
Если число кратно и 3, и 5, то программа должна выводить слово FizzBuzz.

Пример:
7
8
Fizz      # вместо 9
Buzz      # вместо 10
11
Fizz      # вместо 12
13
14
FizzBuzz  # вместо 15
"""
)

for x in range(1, 100):
    if x % 15 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    else:
        print(x)
