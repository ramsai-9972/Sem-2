n=99
temp=n
n1=len(str(n))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**n1)
    temp=temp//10
if sum==n:
        print(f"{n}is an Aemstrong number.")
else:
        print(f"{n}is not Armstrong number.")