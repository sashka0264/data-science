# npm start
import sys
sys.path.append("/Users/a18826700/Library/Python/3.9/lib/python/site-packages")
import keras as k
import numpy as np

model = k.Sequential()
model.add(k.layers.Dense(2, input_dim=2, use_bias=False))
model.add(k.layers.Dense(1, use_bias=False))
model.summary() # Выводим в консоль данные созданной модели, пока все пусто

# Генерим случайные коэффициенты
weights = model.get_weights()
print('Random weights:')
print(weights)

# Генерим свои коэффициенты и заменяем созданные ранее
w1 = 0.42
w2 = 0.15
w3 = -0.56
w4 = 0.83
w5 = 0.93
w6 = 0.02
custom_weights = [np.array([[w1, w3],[w2, w4]]), np.array([[w5],[w6]])]
print('Custom weights:')
print(custom_weights)
model.set_weights(custom_weights)

# Генерим значения на вход
x1 = 7.2
x2 = -5.8
x_train = np.expand_dims(np.array([x1, x2]), 0) # Создаем набор данных для обучения

# Подаем значения на вход
y_linear
