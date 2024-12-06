first_name="prabhu"
last_name="gouda"
full_name=first_name+" "+last_name #"" provide space b/w two strings
print(full_name)

# print(full_name*10)

# print(full_name.upper())
# print(full_name.lower())
# print(full_name.strip())

# print(full_name.replace("prabhu gouda","you"))
  
a=full_name.replace("prabhu gouda","you")
print(a)

name="prabhu sad 'Hello'"                                #using coluns they should be diffrent 
print(name)
name='''prabhu sad 'Hello' darshan said "hi" '''   
print(name)                                       #should use single,double,triple qoutes

print(len(name))
    #-6-5-4-3-2-1
    # 012345 index 
name="prabhu"
print(name[1])
print(name[4])      # index =position - 1 
print(name[2:6])    #from 2 to last 6
print(name[:7])     #upto 7th  index
print(name[2:])     #from 2nd 

#[start:end:step]   end should be +1,  step means skiping the items 
print(name[1::3])
print(name[-2])


s= "prabhu \n gouda"   # \n using enter means next line
print(s)
s= "prabhu \t gouda"   # \t using enter means tab or space  
print(s)