a=int(input("enter a number"))
c=0
for i in range(1,int((a/2)+2)):
    print("*")
    if(i*i==a):
        c+=1
        break;

if(c>0):
    print("yes")
else:
    print("No")
