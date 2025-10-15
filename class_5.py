'''decision making'''

# a=int(input("Enter a number :" ))
# b=int(input("Enter a number : "))

# print(a+b)

# a,b=int(input("Enter a number :")),int(input("Enter a number :"))


# result=a+b
# if result>=33:
#     print('Pass')
# else:print("fail")

"""operattors used in if and else"""
"""
identity
membership
relational
logical
boolean
"""

# a=int(input("enter  :"))
# if (a%5==0):
#     print("Yes")
# else:print("NO")

# a,b=int(input("enter a number :")),int(input("enter a number :"))
# if(a>b):
#     print(a)
# else:
#     print(b)


# a=int(input("enter a number :"))
# if(a%3==0 & a%5==0):
#     print("yes")
# else:
#     print("no")




# a=int(input("Enter a number :"))  #this cannot run in negative
# if(a>=2000):
#     b=a-(a/10)
    
#     print("final discount is ",b)
# else:
#     print("final bill iss",a)




# """Elif"""   
# a=int(input("enter a number :"))
# if a>0 and a>=2000:
#     new_amount=a-(a/10)
#     print("you have to pay",new_amount)
# elif a>0 and a<2000:
#     print("final bill is",a)
# else: 
#     print("invalid input")



# n1,op,n2=int(input("enter a number :")),(input("enter a number :")),int(input("enter a number :"))
# if op=='+':
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)


a=(input("enter a character :"))
if a in 'aeiouAEIOU':
    print("Vowel")
else:print("Consonant")