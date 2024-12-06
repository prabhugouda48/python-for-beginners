# Lists in Python
item1="Bru"
item2="Sugar"
item3="Milk"

items=["bru","Sugar","Sugar","Soppu","Vegitable","Sugar"]  #there is no restriction that theri should be same datatypes 
print(items[0])    #accessing
print(items[-1])   #negative index
print(items)

#modifyng list
items.pop()  #removes the last item
print(items)
items.pop(0)
print(items) #removes the first item

items.append("moms magic") #adds the element
print(items)
items.remove("Sugar") #removes the perticular element
print(items)

items.insert(1,"Spoon")
print(items)
items[0]="coffee powder" #changing the perticular element
print(items)

# items.clear()
# print(list)

l=["a","b","c","d","h"]
print(l[0:])
print(l[0:3])
print(l[0::2]) #step works by adding 2

l2=l[1:3]
print(l2)

#common functions
print(len(items))

items2=[2,1,3,4,5,6,7]
sorted_items=sorted(items2) #sorted function is used to sort the items  we can use "sort" also 
print(sorted_items)

print(sum(items2))    #sum function is used to produce the sum of items2

rev=sorted_items.reverse()
print(sorted_items)

#matrixes
m=[[1,2],[3,4]]
print(m[0])  #nesting
print(m[0][1]) #acessing the oth matrix 1st element
print(type(m)) 