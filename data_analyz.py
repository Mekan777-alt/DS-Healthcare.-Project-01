import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

"""
Прочитайте оба набора данных - обучающий и тестовый - и проверьте их форму. 
Они должны иметь одинаковое количество столбцов. 
Если это не так, решите эту задачу. Сколько строк в обучающей и тестовой выборках
"""

df_test = pd.read_csv("Testing.csv")  # читаем файлы
df_train = pd.read_csv("Training.csv")
del df_train['Unnamed: 133']  # удаляем ненужные столбцы
count_row_test = df_test.shape[0]  # подсчет строк в каждом файле
count_row_train = df_train.shape[0]

#print(f'Количество строк в DF Training = {count_row_train}')      # Вывод на экран количество строк
#print(f'Количество строк в DF Testing = {count_row_test}')

"""
Подсчитайте, сколько единиц в каждом столбце. 
Какой симптом является наиболее популярным? Какой симптом наименее популярен?
Визуализируйте подсчеты каждого значения в столбцах наиболее 
популярного симптома и наименее популярного симптома в виде гистограммы.
"""
values_train = []
keys_train = []

values_test = []
keys_test = []

dict_train = df_train.to_dict("list")           # создаю словарь из ключей и значений
dict_test = df_test.to_dict("list")

# для тренировочных данных
for key, value in dict_train.items():           # разделяю ключи и значения
    a = value.count(1)                          # подсчет единичек в каждом столбсе
    values_train.append(a)
    keys_train.append(key)
    #print(f"{key}: {a}")

# для тестовых данных
for key, value in dict_test.items():
    a = value.count(1)
    values_test.append(a)
    keys_test.append(key)
    #print(f"{key}: {a}")

dict_train_hist = dict(zip(keys_train, values_train))                   # СОздаю словарь для построение гистограммы
dict_test_hist = dict(zip(keys_test, values_test))

min_val = min(dict_train_hist.items(), key=lambda x: x[1])  # Поиск минимального значение
keys_min, values_min = min_val                              # Разложил кортеж на переменные
print(min_val)
max_val = max(dict_train_hist.items(), key=lambda x: x[1])  # Поиск максимального значение
print(max_val)
keys_max, values_max = max_val                              # Разложил кортеж на переменные
x = [keys_min, keys_max]                                    # Преобразовываю с список
y = [values_min, values_max]

plt.bar(x, y, color=['red', 'blue'])
plt.show()

"""
Для каждого заболевания найдите симптом, который встречается чаще всего, 
и симптомы, которые вообще не встречаются.
Рассчитайте числовые характеристики распределения для каждого столбца: 
среднее, медиану, стандартное отклонение, дисперсию.
"""



