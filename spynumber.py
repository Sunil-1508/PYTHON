def isspy(n:int):
    s=0
    p=1
    while n>0:
        s+=(n%10)
        p*=(n%10)
        n=(n//10)
    if s==p:
        return True
    else:
        return False




n=int(input("enter a number"))
print(isspy(n))
