# Встроенные модули сайт docs.python.org (https://docs.python.org/3/py-modindex.html)

# Импорт модуля math
import math

def f1(a=2):
  return math.factorial(a)
print('f1(a) = ', f1(3), '\n')

# Импорт модуля math как m
import math as m

def f2(a=2):
  return m.factorial(a)
print('f2(a) = ', f2(4), '\n')

# Импорт одной функции factorial модуля math
from math import factorial

def f3(a=2):
  return factorial(a)
print('f3(a) = ', f3(5), '\n')

# Импорт одной функции factorial как m2 модуля math
from math import factorial as m2

def f4(a=2):
  return m2(a)
print('f4(a) = ', f4(6), '\n')

# Импорт собственного модуля lesson_module2
import lesson_module2 as lm

print('lesson_module2 = ', lm.func(), '\n')

