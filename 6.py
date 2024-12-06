#Tuples and sets operations and diffrence
#tuples are created using the round brakets they are not flexible (not changeble)(immutable)
#list are created using the square brakets and they are flexible and changeble

genders = ("male","female","others")
print(genders)     #basic
print(type(genders))
print(genders[0])#accesing
print(genders[1:3]) #slicing
# genders[0]="malev2" #we can change or assign item  it can be only available in list 

#we canot add item to the Tuple like append in list
#tuple operation 

##Tuple concatination
tup1=(1,2,3)
tup2=(5,4,9)
combine_tup=tup1+tup2
print(combine_tup)
##Tuple repitation
repeted_tuple=(1,2,3)*3
print(repeted_tuple)
#other way
repeted_tuple=tup1*3
print(repeted_tuple)
##checking membership
fruits=("apple","mango","grapes","grapes")
print("grapes" in fruits)
print("jack" in fruits)

##Methods
#count
print(fruits.count("grapes"))
print(fruits.index("grapes"))

fruits=("apple","mango","grapes","grapes",(1,2,3))
print(fruits)

##advantage 
#immutable
#faster than lists
#canbe used in key dictionaries 

########################Sets######################
#unorderd 
#unindex index not work here
#it should created using the flower brackets
#duplicates are not allowed 

fruits=("apple","mango","grapes","grapes",(1,2,3))

s={12,25,38}
print(s)
# print(s[0]) #not works
s2= set((1,2,3))
print(type(s2))
s=set()  #empty

#operation 
s1={1,2,3}
s2={3,12,24,34,3}
print(s1|s2) #UNION operation
print(s1&s2) #INTERSECTION operation
print(s1-s2) #substraction

s1.add(10)
print(s1)

s1.remove(10)#gives erroe because 10 is not in s1
s1.discard(10)#it do not show ERROR if there remove the element or it is quit

a=s1.pop() 
print(a)

s1.clear() #cleares the whole set
print(s2)