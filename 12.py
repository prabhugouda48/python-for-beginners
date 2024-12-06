# #functions 
# def marriage(boy,girl):
#     print(f"Girl is {girl}")
#     print(f"Boy is {boy}")
#     print(f"{boy} married {girl}")

# marriage("chandan","sneha")  #positional argument
# marriage("chandan","chandana")
# marriage(boy="naresh",girl="sneha") #keyword argument

##-default name of girl when girl name is not defined.
#def marriage(boy,girl="girl"):
        #same print statements
#marriage("chandan")

# This gives the table sof 2 and 3 using for loop
# for i in range(1,11):
#     print(f"2x{i}={2*i}")
# for i in range(1,11):
#     print(f"3x{i}={3*i}")

# def tables(num):
#     for i in range(1,11):
#         print(f"{num}x{i}={num*i}")

# tables(5)
# tables(6)
# tables(7)

# def func(num):
#     print(int(str(num)*5))
# # func(2)


def func(num):
   return(int(str(num)*5))
a=100
b=func(1)
c=a+b
# OR  a=100 c=a+func(2) 
print(c)

def func():
   x="chandan" #locl variable
   print("Hello world")
   print(y)

y="darshan"  #global var  
print(x)  #we canot call local variable outside the function.