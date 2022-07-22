def isprime(n:int):
    if(n<=1):
            return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
def issemiprime(n:int):
    i=2
    while(i<int(n**0.5)+1):
        if(n%i==0):
            if(isprime(n//i) and isprime(i)):
                return True
        i+=1
    return False



n=int(input("enter the number:"))
print(issemiprime(n))
