#Data types are used to represent the different data types used in python.

#1.Numeric Data typ
#1.1.Numeric
int=12
print(int+6)

#1.2.float
b=3.9
print(b*6)

#1.3.complex
c=2-b+int
print(c)

#2.Mapping
#Dictionary :Key value-pairs
student_info={
 'name':"Kavya",
  'Roll_No':2,
  "age":13
}
print(student_info)
#3.Boolean
x=True
y=False

print(x and y)
print(x or y)
print(not y)
#4.set
n={1,2,3,4}
fruit={"apple","banana","kiwi"}
print(10 not in n)
print("kiwi" in fruit)

#5.Sequence
#5.1.List
i=[1,2,3,4,5]
print("list",i)

#5.2.tupple
j=(1,2,3,4,5)
print("tuple",j)

#5.3Strings

name="Ishrat"
print("Im",name)