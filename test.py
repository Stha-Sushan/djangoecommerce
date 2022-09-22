print("I am print I am from testpy file")
#print 8 lines
print(8*"\n")
print("Welcome to Python Training")

#print end line
print("Welcome to", end = ' ')
print("Training", end='!')

paragraph="""This is a paragraph. It is made up of multiple lines and sentences."""
print(2 * paragraph, end="\n")

#multiple assignment
a=b=c=1

d,e,f=1,2,"John"
print(f);#John

str='Hello World'
print(str)      #Prints complete string
print(str[0])   #Prints first character of the string
print(str[2:5]) #Prints characters starting from 3rd to 5th
print(str[2:])    #Prints string starting from 3rd character
print(str * 2)  #Prints string two times
print(str + "TEST")#Prints concatenated string

list=['abcd',768,2.23,'john',70.2]
tinylist=[123,'john']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)


tuple=('abcd',768,2.23,'john',70.2)
tinytuple=(123,'john')
print(tuple)                    #Prints the complete tuple
print(tuple[0])                 #Prints first element of the tuple
print(tuple[1:3])               #Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])                #Prints elements of the tuple starting from 3rd character
print(tinytuple * 2)
print(tuple + tinytuple)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name':'john', 'code':6734,'dept':'sales'}

print(dict['one'])          #Prints value for 'one' key
print(dict[2])              #Prints value for 2 key
print(tinydict)             #Prints complete dictionary
print(tinydict.keys())      #Prints all the keys
print(tinydict.values())    #Prints all the values


#Python Membership operator 'in'

x=4
y=8
list=[1,2,3,4,5]
if (x in list):
    print("Line 1 - x is available in the given list.")
else:
    print("Line 1 - x is not available in the given list.")
if (y not in list):
    print("Line 2 - y is not available in the given list.")
else:
    print("Line 2 - y is available in the given list. ")


#Python Identity operator 'is'

x=2
y=2
if(x is y):
    print("x and y SAME identity")
y=3
if(x is not y):
    print("x and y have DIFFERENT identity")



