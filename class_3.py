#fstring              #formatted string
# name ='mayank'
# intro=f'''my name is {name} i will make you expert in python {90+878}'''
# print(intro)


'''relational operator'''
'''
>
<
>=
<=
==
!=

'''

'''membership operators'''
'''
in 
not in

'''

# data=[12,35,56]
# print(12 in data) #true
# d={'a':35 b:44}
# print(34 in d)  #false becoz cannot cannot read values of dictionary

# data=[1,2,9,45,67,8,900,9]
# print(9 in data)


'''Identity operator'''
'''
is
is not

'''
#id or location of variableis same then it is true vice false
# a=10
# b=5
# print(a is b)  #false

# a=10
# b=10
# print(a is b)  #true

# d1={2,3}
# d2={2,3}
# print(d1 is not d2) #true


'''Logical Operator'''

'''
and 
or
not

'''
#and precendency is more as comapred to or
# print(45>5 and 50>3)
# print(True or False and false)
# print(True or True and False)#True

#area of traingle
# l=10
# b=7

# print('area of Triangle is')
# print(0.5*l*b)


#how take input from user
# a=input()
# print("your unput is :",a)

#or

# a=input("Enter a number : ")
# print("your input is :",a)

'''Type casting'''
'''
int()
float()
str()
list()
tuple()
dict()

'''

# a='112'
# b=90
# print(a+b) # not possible

# a=int('121')
# b=30
# print(a+b)  #type casting

# b=12.4
# print(float(b))


# #add of two number

# a=int(input("enter a number :"))
# b=input("enter a number")

# print(a+int(b))








#Write a program to take input in follwing intro
'''
my name is ----
i am ---- year old
i studying --- course
'''

name=input("Enter your name ")
age=input("Enter your age")
course=input("Enter your course")

intro = f'''
my name is {name}
i am {age} year old
i studying {course}'''
print(intro)