from sklearn import datasets
diabetes = datasets.load_diabetes()

print(diabetes.DESCR)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes  # Завантажуємо датасет

# Завантаження набору даних про діабет
diabetes = load_diabetes()

# Створення DataFrame
db_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(db_df.sample(5))

# Додаємо колонку 'Progression' (цільова змінна)
db_df['Progression'] = diabetes.target  
print(db_df.sample(2))  # Перевіряємо набір даних

# Незалежні змінні (фактори)
x = db_df.drop(labels='Progression', axis=1)  # Відкидаємо колонку 'Progression'
# Залежна змінна (цільова)
y = db_df['Progression']

# Розбиття на навчальну та тестову вибірки (75% - тренування, 25% - тест)
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25, random_state=999)

# Вивід розмірів вибірок
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

print(lm)
print(type(lm))
lm.fit(train_x, train_y)
predicted_y = lm.predict(test_x)
import numpy as np  # Додаємо імпорт numpy
from sklearn import metrics as mt

# Припустимо, що test_y та predicted_y вже визначені у вашому коді

print("1) The model explains,", np.round(mt.explained_variance_score(test_y, predicted_y) * 100, 2), 
      "% variance of the target w.r.t features is")

print("2) The Mean Absolute Error of model is:", np.round(mt.mean_absolute_error(test_y, predicted_y), 2))

print("3) The R-Square score of the model is ", np.round(mt.r2_score(test_y, predicted_y), 2))
