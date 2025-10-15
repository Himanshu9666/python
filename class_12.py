'''whiles example'''

# a=19
# sum_num=0
# while a>0:
#     last_digit=a%10
#     sum_num+=last_digit
#     a//=10
# print(sum_num)


# a=90
# while a>=20:
#     print(a)
#     a=a-1

# data='welcome to regex'
# for i in data:
#     if i==' ':
#         print()
#     print(i,end='')


'''string'''
# data='welcome to regex'
# a=(data.isupper())
# print(a)


'''count lowe casae and upper case'''


# data="REGex"
# countl=0
# countu=0
# for i in data:
#     if i.isupper():
#         countu=countu+1
#     elif i.islower():
#         countl=countl+1
# print("upper case is",countu)
# print("lower case is",countl)



'''reverse the string'''

# data='51263'
# reverse=''
# for i in data:
#     reverse=i+reverse
# print(reverse)    


# data='shekhar'
# for i in range(-1,-len(data)-1,-1):
#     print(data[i],end='')
#or
# for i in range(len(data)-1,-1-1):
#     print(data[i],end='')



'''palindrome'''

# data='madam'
# rev=''
# for i in range(-1,-len(data)-1,-1):
#     rev+=data[i]
# if data==rev:
#     print("palindrome")
# else: 
#     print("not palindrome")

# '''remove duplicate charachter'''



# data = "madam"
# newdata = ""
# for i in data:
#     if i not in newdata:
#         newdata += i
# print(newdata)  

'''filter digits from a string'''

# data="12345asdf"
# newdata=''
# for i in range(0,len(data)):
#     if not data[i].isdigit():
#         newdata+=data[i]
# print(newdata)

#or

# data="sheka34ff"
# digit=''
# for i in data:
#     if i.isdigit():
#         digit=digit+i
# print(digit)        

'''count vowel from a string '''

# data='aeiadou'
# vowels='aeiou'
# count=0
# for i in data:
#     if i.lower() in vowels:
#         count=count+1
      # else:
      # remove+=1  #it removes vowels from string
# print(count)        

'''remove spcae from string'''
# data="welcome to space"
# newdata=""
# for i in range(0,len(data)):
#     if data[i]!=" ":
#         newdata += data[i]
# print(newdata)

# or

'''print string words to next line'''
# data='welcome to regex'
# for i in data:
#     if i ==" ":
#         print()
#     else:
#         print(i,end='')



        

