n = int(input("enter the number :"))
while n >9:
    total = (n%10+n//10)
    n = total
print("sum of digits is : ",n)