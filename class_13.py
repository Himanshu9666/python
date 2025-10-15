'''WAP to print fibbonaci series 0 1 1 2 3 5 8 13 '''

# n=int(input("enter a number "))
# a=0
# b=1
# sum=1
# print(a,end=' ')
# print(b,end=' ')
# for i in range(n):
#     result=a+b
#     print(result,end=' ')
#     a=b
#     b=result



'''using while loop'''
# n=int(input("enter a number "))
# a=0
# b=1
# sum=1
# i=0
# print(a)
# print(b)
# while i<n-1:
#     sum=a+b
#     print(sum)
#     a=b
#     b=sum
#     i+=1
'''write a program to print the sum of prime numbers from 1 to n'''
# a=2
# i=0
# sum=0
# while a<=20:
#     if a%i==0:
#         print(a)
#         sum=sum+1
#     else:break
#     print(sum)
#     i=+1

# n = int(input("Enter n: "))
# sum = 0

# for num in range(2, n + 1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         sum += num

# print("Sum:", sum)




'''factorial using while'''

# n=int(input("enter a number "))
# fact=1
# while(n>0):
#     fact=fact*n
#     n=n-1
# print(fact)

'''sum of odd'''
# sum = 0
# for n in range(1, 6):      
#     if n % 2 ==1:         
#         sum = sum+n
# print("Sum of odd numbers from 1 to 5:", sum)