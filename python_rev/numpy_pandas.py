""" numpy array
pandas dataframe """

#list=[[5,3],[7,7]]
#list1=[[3,4],[4,7]]

""" for count,i in enumerate(list):
    for count2,j in enumerate(i):
        list[count][count2]=j+2

print(list) """

import numpy
""" array_x=numpy.array(list)
print(array_x+2) """

""" array1=numpy.array(list)
array2=numpy.array(list1)
final_list=array1+array2+2
print(final_list)
print(final_list.dtype) """

""" array1=numpy.array(['20',300])
print(array1.dtype,array1)

print(numpy.zeros((3,3)))
print(numpy.ones((3,3)))
print(numpy.eye(3,3))
print(numpy.array([20,30,40,30,55,88]).reshape(3,2))

del numpy.array([]) """

import pandas as pd

data = {
      'name' : ['sara','jaya','ram','ved'],
        'age': [2,4,5,7]
}
df=pd.DataFrame(data)
print(df.iloc[3])
print(df[df['city']=='bengaluru'])