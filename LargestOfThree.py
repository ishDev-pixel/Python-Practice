a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))

if a>b and a>c:
    print(f'{a} is the largest of three')
elif b>a and b>c:
    print(f'{b} is the largest of three')
else:
    print(f'{c} is the largest of three')        