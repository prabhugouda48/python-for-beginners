######### FOR LOOPS IN PYTHON #########
  #Basic structure of for lop

# cities=["bengalore","Tumkur","Mandya"]  #list
# for city in cities:
#     print(city)

#################### RANGE ###########
# for i in range(1,11): #rangeee
#     print(i,end=" ")

for i in range(1,11,2):
    print(i)


########### MULTIPLY NUMBER OF TIMES ###########
#     name="Prabhu"
#     for letter in name:
#         print(letter*5)


########## BREAK ##########
# l=[12,34,56,88]
# for num in l:
#     print(num)
#     if num==14:
#         break
# print("All printed")    


########### LOOPING OVER STRINGS ########
name ="karnataka"
for letter in name:
    print(letter)


################### Nested for loop #################
 #multiplication Table  Let’s print the multiplication table from 1 to 5 using a nested for loop.
for i in range(1,6):
    for j in range(1,6):
        print(f"{i}*{j}={i*j}")
print()       # To print an empty line after each table   


################# BREAK IN FOR LOOP #############
cities=["bengalore","Tumkur","Mandya","Hubballi"]  #list
for city in cities:
     if city=="Hubballi":
         print(f"Found {city}!")
         break
     print(city)

############ Uisng continue in a for loop ##############
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        continue
    print(city)

################# ENUMERATE() #####################
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}") 

################### ELSE WITH FOR LOOPS ###############
for city in cities:
    print(city)
else:
    print("NO more cities!")    


############### real life Example: Distributing Laddus ###########
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!") 