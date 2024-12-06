########## Lists and dictionaries with for loops,List compreshnsion,and Dictionary Comprehension.
#Looping through Lists

 #sum of all numbers in a lists
numbers=[10,20,30,40,50]
total=0

for num in numbers:
    total+=num

print("Total sum:",total)

#doubling each numbers in a list
numbers=[1,2,3,4,5]
doubled=[]
for num in numbers:
    doubled.append(num*2)
    print("Doubled List:",doubled)

foods=["dosa","Idli","vada","Bisibelebath"]

for food in foods:
    print(f"I like {food}")

########## LOOPING THROUGH DICTIONARIES ####################
#iterating over dictionary keys
student_marks={"Anand":85,"geetha":90,"kumar":78}
for student in student_marks:
    print(student)      ##### This gives only student name.


student_marks={"Anand":85,"geetha":90,"kumar":78}
for marks in student_marks.values():
    print(marks)      ######This gives the values of the dictionary


########## Iterating over both keys and values #######
student_marks={"Anand":85,"geetha":90,"kumar":78}

for student,marks in student_marks.items():
    print(f"{student} Scored {marks} marks") 

####### for loops with range ########
 
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)

#  list compresion
# syntax: new_list = [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

###### UPERCASING KANNADA CITY NAMES
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercased_cities = [city.upper() for city in cities]
print(uppercased_cities)


###### DICTIONARY COMPRESION ##########
# new_dict = {key_expression: value_expression for item in iterable if condition}
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)


city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

####### splitting strings to create lists ###########
 # syntax : string.split(separator, maxsplit)

 # spliting a sentence
sentence = "I love coding in Python"
words = sentence.split()
print(words)

#Example 2: Splitting a string with commas
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)

## limiting the number of splits ###.
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)




