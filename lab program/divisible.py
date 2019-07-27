lb =int(input("enter the lb value"))
ub =int(input("enter the ub value"))

res = " ",join(i for in range(lb,ub+1)if i%9==0 and i%5!=0)
print(res)

