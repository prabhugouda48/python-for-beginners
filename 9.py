#While loops in python 

#syntax 
# while condition repeatedly executes a block of code as long as the condition is true.

# A)
# i=1   #starting of loop
# while i<=5:
#     print(i)
#     i+=1  #incrementing i by 1 after each iteration.


# B)
# sheep_count=1
# while sheep_count<=10:
#     print(f"TSheep {sheep_count}")
#     sheep_count+=1
# print("No sheep")   
    
# c)
# is_failed=True
# i=1

# while is_failed:
#     print(f"try{i}")
#     i=i+1


# is_failed=True #initialize
# i=1            #True

# while is_failed and i<=100:
#     print(f"try{i}")
#     i=i+1

# print("I gave up!") #after i value = 100 ,print 'I gave UP'


####################Avoiding Infinite Loops################

# i = 1
# while i <= 5:
#     print(i)
#     # Forgot to update i, so the condition remains True forever!


# D)
############### Using 'break' to exit a while Loop###############

# is_failed=True
# i=1

# while is_failed:
#     print(f"Try {i}")
#     i=i+1
#     if i>100:
#         break

# print("I gave UP!")    

##################### Using continue #############################
# is_failed=True
# i=1  #attempt

# while is_failed:
#     if i%2!=0: #is not even
#      i=i+1
#      continue
#     print(f"Attempt {i}")
#     i=i+1
#     if i>100:
#         break

# i=0

# while i<=10:
#     x=0
#     while x<i:
#       print("chandan",end="_")
#       x+=1
#     i+=1
# ###########USING WHILE LOOP FOR USER INPUT#################

# pin ="1234"
# while True:
#    input_pin=input("PIN >>")
#    if input_pin==pin:
#       print("CORRECT")
#       break
#    else:
#       print("INCORRECT")


# available_seats = 5

# while available_seats > 0:
#     print(f"{available_seats} seats available.")
#     booking = input("Do you want to book a seat? (yes/no): ").lower()
    
#     if booking == "yes":
#         available_seats -= 1
#         print("Seat booked!")
#     else:
#         print("No booking made.")

# print("All seats are booked!")

snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()
    
    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        
print("Either snacks are sold out or you are out of money.")