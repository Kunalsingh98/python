d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=input("Enter the key to delete:")
if key in d: 
    del d[key]
else:
    print("Key not found!")

print("Updated dictionary")
print(d)