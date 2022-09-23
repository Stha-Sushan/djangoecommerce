#UserInput
'''
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
if(num1>=num2 and num1>=num3):
    print("{0} is greater than {1} and {2}".format(num1,num2,num3))
elif(num2>=num1 and num2>=num3):
    print("{0} is greater than {1} and {2}".format(num2,num1,num3))
else:
    print("{0} is greater than {1} and {2}".format(num3,num2,num1))

#OddEven

num = int(input("Enter a number: "))
if (num%2==0):
    print("{0} is even.".format(num))
else:
    print("{0} is odd.".format(num))

#Array in python

import array as myarray
abc = myarray.array('d',[2.5,4.9,6.7])
abc.append(10.2)
print(abc[3])
print(abc.count)
for x in abc:
    print(x)

import array as myarray
xyz = myarray.array('q',[3,9,6,5,20,13,19,22,30,25])
print(xyz[1:4])
print(xyz[7:10])

import array as ma
a = ma.array('i',[300,200,100])
a.insert(2,150)
a[0]=400        #replacing the items

#array conctanation

first = ma.array('b',[4,6,8])
second = ma.array('b',[9,15,12])
numbers = first + second
print(numbers)

#pop() method in Python to delete the array items by index

print("-----------")
numbers.pop(2)
print(numbers)'''

#del() method in Python to delete the array items by value
#Syntax: arrayName.remove(value)

#Check with
#arrayName.index(value)
#arrayName.reverse()
#Count the occurence of a value in Array
#array.count(x)


#Try it
#-Take users input and add the items into array then display it.
#-Sort thr array by ascending order
#-Sort the array by descending order
#-Try to findout the greatest number
#-Try to findout the smallest number

import array as a
a = []
n = int(input("How many numbers you want to input?: "))
for i in range(0,n):
    l = int(input())
    a.append(l)
print(a)
a.sort()                    #ascending order
print(a)
a.sort(reverse=True)        #descending order
print(a)
print(a[0])                 #Prints 1st character
print(a[-1])                #Prints last character


