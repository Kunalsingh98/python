d1={}
k=input("key: ")
v=input("value: ")
d1[k]=v
d2={}
k2=input("key:")
v2=input("value:")
d2[k2]=v2
d=d1.copy()
d.update(d2)
print(d)