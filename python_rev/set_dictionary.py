#set

x={2,2,4,5,5,66}
y={4,6,88,2,1,4}

""" print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
 """
#dictionary

z={'sakshi':20,'riya':25}
s={'riya':2,'rhea':4}

""" print(z.get('sakshi'))
print(z['sakshi'])
z['sakshi']=34
print(z)
z['rohit']=22
print(z) """

""" z.update(s)
print(z)
z.update({'rohit':33})
print(z)
 """
""" for i in z:
    print(i,z[i]) """

for i,j in z.items():
    if len(i)>5:
        print(j)

print(z.keys())
print(z.values())  