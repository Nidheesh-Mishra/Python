a=0
b=1
n = int(input("Enter the Number of Terms of the series : "))
if (n>2):
    print(a)
    print(b)
for i in range(2,n):
    sum=a+b
    print(sum)
    a=b
    b=sum

