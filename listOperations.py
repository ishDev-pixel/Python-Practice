n=[2,4,6,2,7,8]

#copying list
a=list(n)
print(a)

#addition of list
c=a+n
print(c)

#membership operators
#.in
print(2 in n)

#not in
print(2 not in n)

#looping 
for l in n:
    print(l)

#positive indexing
print(n[0])
print(n[1])
print(n[2])
print(n[3])
print(n[4])
print(n[5])

#negative indexing
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

#negative slicing
print(n[-6:-1])

#positive slicing
print(a[1:4])