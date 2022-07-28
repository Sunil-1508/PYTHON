
def mul(a,b,r):
    if a==0:
        return r
    else:
        if(a%2):
            r+=b
        return mul(a//2,b*2,r)

a,b=map(int,input().split())
if a>b:
    a,b=b,a
res=mul(a,b,r=0)
print(res)
