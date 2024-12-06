########--IF ELSE elif condition loop---#######

# x=20
# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")

# signal=input("what is the color of the signal:")

# if signal=="red":
#     print("stop")
# elif signal=="yellow":
#     print("ready")
# elif signal=="green":
#     print("GO")
# else:
#     print("Go")



# #ex-2

# time=15
# if time==8:
#     print("Its breakfast time")
# elif time ==13:
#     print("Its lunch time")
# elif time==20:
#     print("Its dinner time")
# else:
#     print("Its not a meal time.")

   ##############################-----Conditional operators in if else elif loop-------#####################
att=75
is_teacher_friend = True

if att>=75:
    print("EXAM")
# elif att<75 and is_teacher_friend==True: both are same   
elif att<75 and is_teacher_friend:    #AND both cons must sattisfy
    print("EXAM")
else:
    print("NO EXAM")


    age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")


#################################--------------------Nested If Statement-----------#################

day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")

    






