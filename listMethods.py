a=[1,2,3,4,5]
b=[8,9]
print(a)
#append():appends the item at the end of the list

if 6 not in a:
    a.append(6)
    print(a)

#insert():insert the item at the specified postion
while len(a)==6:
    a.insert(6,7)
    print(a)
    break


#extend():extend the list with list2
print(a.extend(b))

#count():returns the number of times the items is repeated 
c=[2,6,2,8,4,0,2,5,6]
print(c.count(2))

#index():returns the index of the specified item
print(a.index(5))

#reverse():reverse the list
name=["i","s","h","r","a","t"]
name1=name.reverse()
print(name1)
