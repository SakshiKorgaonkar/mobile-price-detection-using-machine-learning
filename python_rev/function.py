def calc(x,y,z=9):
    a=x+y
    b=x*z
    return a,b

""" res=calc(2,4,7)  
print(res)
res=calc(3,6)
print(res) """

try:
    calc(2.4,6)
    res=26
    with open('ok.txt','w') as f:
        f.write(res)

except Exception as e:
    print("something went wrong.")
