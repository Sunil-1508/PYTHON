st=input("enter the word")
print(len(st))
l=st.split()
k=""
s=""
print(l)
for i in l:
    k=i.swapcase()
    s=k+" "+s
print(s)
print(len(s))
