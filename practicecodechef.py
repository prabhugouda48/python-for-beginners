
## printing right angled triangle
num =5
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end="")
    print()

## printing two numbers in same line
print(8)
print(13, end=" ")
print(21)


###Printing squares 
i=1
num=6
for i in range (1,num):
    
    ans=i**2
    print(f"{i}-{ans}")
    i+=1


##### Mapping problem
x, y = map(int,input().split())
print(x * y)

# ########## if else #########
# x = 62
# y = 62
# if x > y:
#     print("x is greater")
# else y > x:
#     print("y is greater")
# else:
#     print("both are equal")

#######-- Average of marks#
x, y, z = map(float,input("").split())
average=(x+y+z)/3
print(f"{average}")

####-- brain speed
x,y = map(int,input().split())
# write your code here
if x>y:
    print("yes")
elif x<y:
    print("No")
elif x==y:
    print("No")

###---Alice ,Boobs marks twise of Boobs.
x,y = map(int,input().split())
# write your code here
if x>=2*y:
    print("yes")
elif x<2*y:
    print("No")

###--- One full pair
a,b = map(int,input().split())

# write your code here
result=a+b+(a*b)
if result==111:
    print("Yes")
else:
    print("No")

##--Squares of numbers.
num = int(input())
# Update your code below this line
i = 1
while i <= num:
    square = i ** 2
print(square)
i += 1

##-- Factorial of number
num = int(input())
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(factorial)

##-----Counting the vowels
# Solution
str = input()
ans = 0
i = 0
while i < len(str):
    c = str[i]
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        ans += 1
    i += 1
    
print(ans)

# The first line contains an integer ad two numbers for t testcases.get the sum

t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    # write your code here
    print(a+b)