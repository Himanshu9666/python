'''examples'''
# a=12345
# sum=0
# while a>0:
#     last_d=a%10
#     sum+=last_d
#     a//=10
# print(sum)
'''nested while in sum of digit'''
# a=12345
# while a>=10:
#     sum=0
#     while a>0:
#         last_d=a%10
#         sum+=last_d
#         a//=10
#     a=sum
# print(sum)


'''armstrong number'''

# a=145
# count=0
# while a>0:
#      count=count+1
#      a//=10
# sum=0
# a=145
# while a>0:
#        last_d=a%10
#        sum+=last_d**count
#        a//=10
# if sum==a:
#         print("armstrong no ")
# else:print('not armstrong')

'''simpler '''

# a = 145
# original = a  
# count = 0

# temp = a
# while temp > 0:
#     count += 1
#     temp //= 10


# sum = 0
# temp = a
# while temp > 0:
#     last_d = temp % 10
#     sum += last_d ** count
#     temp //= 10

# if sum == original:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")

'''reverse a string'''

a='welcome to space'
reverse=''
for i in a:
       reverse+=i
print(reverse)

''''''


