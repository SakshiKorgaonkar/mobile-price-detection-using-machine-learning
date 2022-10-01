#importing packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wine_data=pd.read_csv('python/winequality-red.csv')
print(wine_data.shape)

print(wine_data.head())

sns.catplot(x='quality',data= wine_data, kind = 'count')
plt.show()

# volatile acidity vs quality
plot = plt.figure(figsize=(6,6))
sns.barplot(x='quality', y='volatile acidity', data = wine_data)
plt.show()
# volatile acidity and quality inversely proportional

# alcohol vs quality
plot = plt.figure(figsize=(6,6))
sns.barplot(x='quality', y='alcohol', data = wine_data)
plt.show()
# alcohol and quality directly proportional

correlation = wine_data.corr()

# heat map to understand the correlation between columns
plt.figure(figsize=(12,12))
sns.heatmap(correlation, cbar=True, fmt=".1f",annot=True , square=True , annot_kws={'size': 8},cmap = 'PiYG')
plt.show()

# data preprocessing
X = wine_data.drop('quality', axis=1)
print(X)

# quality >=7 - good quality & quality < 7 - bad quality
Y = wine_data['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)
print(Y)

# splitting into test and train sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
print(Y.shape, Y_train.shape, Y_test.shape)

# random forest classifier instance & fitting with data
model = RandomForestClassifier()
model.fit(X_train, Y_train)

# predicting using classifier
X_prediction = model.predict(X_test)
test_data_acc = accuracy_score(X_prediction, Y_test)
print('Accuracy = ', test_data_acc)

input_data = (5.4,1.49,0.38,0.86,6.0,4.4,19.0,0.9234,1.68,0.5,6.4)

# passing input data to numpy array
input_data_to_numpy_array = np.asarray(input_data)

input_reshape = input_data_to_numpy_array.reshape(1, -1)
pred = model.predict(input_reshape)
print(pred)
if(pred[0]==1):
    print("Good Quality Wine.")
else:
    print("Bad Quality Wine.")