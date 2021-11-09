import pandas as pd
#from matplotlib import pyplot as plt


'''
Прочитайте оба набора данных - обучающий и тестовый - и проверьте их форму. 
Они должны иметь одинаковое количество столбцов. 
Если это не так, решите эту задачу. Сколько строк в обучающей и тестовой выборках?
'''

df_test = pd.read_csv("Testing.csv")  # читаем файлы
df_train = pd.read_csv("Training.csv")
del df_train['Unnamed: 133']  # удаляем ненужные столбцы
count_row_test = df_test.shape[0]  # подсчет строк в каждом файле
count_row_train = df_train.shape[0]

#print(f'Количество строк в DF Training = {count_row_train}')      # Вывод на экран количество строк
#print(f'Количество строк в DF Testing = {count_row_test}')

'''
Подсчитайте, сколько единиц в каждом столбце. 
Какой симптом является наиболее популярным? Какой симптом наименее популярен?
Визуализируйте подсчеты каждого значения в столбцах наиболее 
популярного симптома и наименее популярного симптома в виде гистограммы.
'''

count = 0

with open("Testing.csv", "r") as f:           # читаем данные
    headers_test = next(f).split(",")         # далее берем все хэдары
    #print(headers_test)

with open("Training.csv", "r") as f:          # читаем данные
    headers_train = next(f).split(",")        # далее берем все хэдары
    #print(headers_train)



