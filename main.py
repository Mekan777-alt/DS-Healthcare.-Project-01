import pandas as pd
import scipy
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score # пакет сравнение правильных ответов, и точность


df = pd.read_csv("Training.csv")   # Открытие и чтение файла

df['Unnamed: 133'] = df['Unnamed: 133'].replace(np.nan, 0)  # Меняем NaN на ноль, обращаясь к калоне
x = df.drop('prognosis', axis=1)   # вытаскиваем таблису прогнозы, на котором ждем прогнозы
y = df['prognosis']   # и вставляем сюда правильные ответы

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)  # далее мы сравниваем train на test
RFC = RandomForestClassifier(n_estimators=100) # алгоритм классификасии, он предсказывет вероятность
RFC.fit(x_train, y_train)  # обучаем модель

prediction = RFC.predict(x_test)
a = accuracy_score(y_test, prediction)
print(a)
print(prediction)


