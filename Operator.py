a=5
b=6
c=9.8
d=20

#Arithmetic Operator
print(a+b)  #addition operator
print(a-c)  #Subtraction operator
print(a*d)  #Multiplication operator
print(a/b)  #Divsion Operator
print(c%d)  #Modulus operator  #Returns the remainder

#Comparison Operator
equal_to=a==2                    #equal to 
print(equal_to)

not_equal_to=a!=b                #not equal to
print(not_equal_to)

greater_than=c>b                 #greater than
print(greater_than)

less_than=a<d                    #less than
print(less_than)

greater_than_equal_to=d>=a       #greater than equal to
print(greater_than_equal_to)

less_than_equal_to=c<=a          #less than equal to
print(less_than_equal_to)

#Logical Operator
#1.and 2.or 3.not
x=True
y=False

print(x and y)      #logical and 
print(y or x)       #logical or
print(not x)        #logical not

#Membership operator
#1.in
#2.not in

n=[1,2,3]
print(1 in n)
print(6 not in n)

#Assignment operator
f=a
a+=b
d-=c
a*=a
a/=d
a%=d
