def simpleinterest(p,r,t):
    SI=(p*r*t)/100
    return SI
p=int(input("enter the principal"))
r=int(input("enter the rate"))
t=int(input("enter the time"))

SI=simpleinterest(p,r,t)
print(SI)