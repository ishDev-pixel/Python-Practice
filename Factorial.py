n=int(input("enter a number "))
fact=1
if n<=0:
    print("enter non negative numbers")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f'factorial of {n} is {fact}') 
