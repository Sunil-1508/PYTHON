def perfect(n:int):
    r=1
    i=2
    while(i<=int(n**0.5)):
        if(n%i==0):
            if(n//i!=i):
                r+=((n//i)+i)
            else:
                r+=i
        i+=1
    if(r==n):
        return True
    else:
        return False


n=int(input())
print(perfect(n))



1,2,3,4,6,6,9,12,18
1,2,4,7,14,
