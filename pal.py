n=int(input())
c=n
s=0
while(n!=0):
    r=n%10
    s=s*10+r
    t=n//10
    n=t
if(c==s):
    print("yes")
else:
    print("no")
