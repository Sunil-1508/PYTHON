def mult(a,b):
    r=0
    while a:
        if(a%2):
            r+=b
        a//=2
        b*=2
    return r
        
a,b=map(int,input().split())
if(a>b):
    a,b=b,a
r=mult(a,b)
print(r)
