st=input("enter the word")
l=st.split()
k=""
s=""
for i in l:
    k=i.swapcase()
    s=k+" "+s
s=s[:-1]
print(s)
