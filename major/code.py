import pandas as pd
import matplotlib.pyplot as plt

data_train=pd.read_csv(r'C:\Users\sakshi\OneDrive\Desktop\python\major\train.csv')
print(data_train)
print(data_train.shape)
print(data_train.info())
print(data_train.describe())
data_train.plot(x='price_range',y='ram',kind='scatter') #ram and price range directly proportional
plt.show()
data_train.plot(x='price_range',y='battery_power',kind='scatter')
plt.show()
data_train.plot(x='price_range',y='fc',kind='scatter')
plt.show()
data_train.plot(x='price_range',y='n_cores',kind='scatter')
plt.show()
X=data_train.drop('price_range',axis=1)
print(X)
Y=data_train['price_range']
print(Y)

data_test=pd.read_csv(r'C:\Users\sakshi\OneDrive\Desktop\python\major\test.csv')
print(data_test)
print(data_test.shape) #for rows and columns
print(data_test.info()) #for checking null values
print(data_test.describe()) #for calculating statiscal data i.e. mean , std
data_test=data_test.drop('id',axis=1)
print(data_test)

#scaling x and test data
from sklearn.preprocessing import StandardScaler
std=StandardScaler()
X_std=std.fit_transform(X)
data_test_std=std.transform(data_test)
print(X_std)
print(data_test_std)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_std,Y)
print(dt.predict(data_test_std))
print(dt.score(X_std,Y))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X_std,Y)
knn.predict(data_test_std)
print(knn.score(X_std,Y))

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_std,Y)
lr.predict(data_test_std)
print(lr.score(X_std,Y))

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
dt.fit(X_train,Y_train)
Y_pred=dt.predict(X_test)
print(Y_pred)

from sklearn.metrics import accuracy_score
dt_acc=accuracy_score(Y_test,Y_pred)
print(dt_acc)

X_train_std=std.fit_transform(X_train)
X_test_std=std.transform(X_test)
knn.fit(X_train_std,Y_train)
Y_pred_knn=knn.predict(X_test_std)
print(Y_pred_knn)
knn_acc=accuracy_score(Y_test,Y_pred_knn)
print(knn_acc)

lr.fit(X_train_std,Y_train)
Y_pred_lr=lr.predict(X_test_std)
lr_acc=accuracy_score(Y_test,Y_pred_lr)
print(lr_acc) #highest accuracy

plt.bar(x=['dt','knn','lr'],height=[dt_acc,knn_acc,lr_acc])
plt.xlabel('Algorithms')
plt.ylabel('Accuracy Score')
plt.show()