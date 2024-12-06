# i=0
# while i<=5:
#       print(i)
#       i+=1
#       print(i)
# print(i)     


# def add_numbers(a, b):
#  if not isinstance(a, int) or not isinstance(b, int):
  
#   raise TypeError("Both arguments must be integers.")
#  return a + b


# try:
#  print(add_numbers(5, 10))
# except TypeError as e:
#  print(e)



try:
 num = int(input("Enter a number: "))
 result = 10 / num
except ZeroDivisionError:
 print("Cannot divide by zero.")
except ValueError:
 print("Invalid input; please enter a number.")
