t=(1,2,3,4,5,)


#copying tuples
print("copying tuples")
t2=t
print(t2)

#concatenation
print("concatenation of tuples")
tuples=t+t
print(tuples)

#postive indexing
print("positive indexing")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

#negative slicing
print("negative indexing")
print(t[-2])
print(t[-3])
print(t[-4])
print(t[-5])

#positive slicing
print("negative slicing")
print(t[2:4])

#negative slicing
print("negative slicing")
print(t[-5:-1])

#traversing of tuples
print("traversing tuple")
for tuples in t:
    print(t)
    break

#membership operators in and not in
print("in membership operator")
print(5 in t)

print("not in membership operator")
print(5 not in t)