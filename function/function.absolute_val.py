def distance_from_zero(s):
    if type(s)==int or type(s)==float:
        return abs(s)
    else:
        return "Nope"
s="what?"
print(distance_from_zero(s))