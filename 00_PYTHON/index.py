# -*- coding: utf-8 -*-
# Не работали русские буквы
import sys
sys.path.append("/Users/a18826700/Library/Python/3.9/lib/python/site-packages")
from colorama import Fore, Back, Style
# Не подключался установленный пакет colorama
import math

# Введение
NUMBER_ONE = 1.6 # Число
MY_NAME = 'ALEXANDR' # Строка
X = (1, 2) # Кортеж, его значения нельзя менять
Y = {1, 2} # Множество, его значения нельзя менять
Z = {1: 'text', 'text': 2} # Словарь
ARRAY = [] # Список
status = True # Boolean
MY_REAL_NAME = raw_input("Write you name: ") # Строка
print('Hello, my name is ' + MY_REAL_NAME)
print('Number is string - ' + str(math.floor(-NUMBER_ONE)))

# Тупой калькулятор
print ( Back.RED )
what = raw_input('Удалить или вычесть (+/-)? ')
a = int(raw_input('Первое число: '))
b = int(raw_input('Второе число: '))

if what == '+':
    c = a + b
elif what == '-':
    c = a - b
else:
    c = 'Вы ввели какую-то дичь'

print('Result - ', str(c))