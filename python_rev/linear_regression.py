data={
    'age':[2,4,6,8],
    'height':[4,7,9,12]
}

import pandas as pd
df=pd.DataFrame(data)
print(df)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(df[['age']],df['height'])
predicted_value=lr.predict(df[['age']])
print(predicted_value)

from matplotlib import pyplot
pyplot.scatter(df['age'],df['height'])
pyplot.plot(df['age'],predicted_value,color='r')
pyplot.title('Age v/s Height')
pyplot.xlabel('Age')
pyplot.ylabel('Height')
pyplot.show()