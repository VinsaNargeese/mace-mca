l1=list(map(int,input("enter list 1:").split()))
l2=list(map(int,input("enter list 2:").split()))
if(len(l1)==len(l2)):
    print("same length")
else:
    print("different length")
if(sum(l1)==sum(l2)):
    print("same sum")
else:
    print("different sum")
if(set(l1)&set(l2)):
    print("some values occur in both")
else:
    print("no common values")
