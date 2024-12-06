#Dictionary
#key value pair collection
#we can manipulate and retrive by key 
#mutable ,unorderd
# create using curly brackets and using the "dict" function

birthday={
    "chandan":"07-06-2002",
    "darshan":"27-09-2004",
    "virat":"05-10-1988"
}

meanings={
    #key:value
    "bat":"used to hit",
    "ball":"this is hit",
    "wicket":"to be protected"
}

########   Acessing dictionary elements   ###########
print(type(birthday))
print(birthday['virat'])
print(birthday.get('viratp','not found'))  #safe acessing ,default defining 

birthday['sudeep']='02-09-1973'   #run time accesing
print(birthday)
#####updating####
print("updating")
birthday['sudeep']='02-09-1888' 
print(birthday)

x= birthday.pop("chandan")
print(x)                                 #removing the chandan ,we must give the key 
# del birthday["chandan"]
print(birthday)

print(birthday.keys())
print(birthday.values())  
print(birthday.items())  

birthday.update(meanings)  #adding the meanings dictionary to birthday dictionary
print(birthday)

Data ={
    "str":"str",
    "st":123,
    "f":10.22,
    "is":True,
    (1): "hmm",    #tuple
    12:88,
    "friends":["chandan","prabhu"]
}


item1={
    "name":"milk",
    "weigt":1,
    "price":50
}

item2={
    "name":"suagr",
    "weigt":5,
    "price":90
}

items=[item1,item2]
print(items)
print(f"Total Weight:{item1["weigt"]+item2["weigt"]} Kg")  ###adding the values by using the keys  
                                                           ##adding the unit aas  kg int he result 


##  DO  experiments in list of dictionary   [  ]
