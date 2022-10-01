# list & tuple
# set & dictionary

a=[3,4,1,88,1,0]
a.append(2)
a.insert(2,44)
print(a)
print(a.sort())
print(a.sort(reverse=True))
print(a.__len__())
del a[2]
print(a)
print(a[3:6])
print(type(a))
a[2]="sakshi"
print(a)
y=tuple(a)
print(y)

x=(3,6,1,8,0)
z=list(x)
print(z)

""" cannot insert update remove append in tuples 
can slice & index** """

