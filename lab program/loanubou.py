lb =int(input("enter the lb value"))
ub =int(input("enter the ub value"))
for num in range(lb,ub+1):
    is_prime = True
    for i in range(2,(num//2)+1):
        if num % i ==0:
            is_prime =False
            break
    if is_prime:
        print(num,end="")
        