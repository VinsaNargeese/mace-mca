a=input("enter a list of numbers")
a=list(map(int,a.split()))
print("input list:",a)
b=[num for num in a if num>100]
print("output list:",b)
