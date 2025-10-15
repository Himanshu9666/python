
# original_email=input("enter your email : ")
# original_password=input("enter your password : ")
# print("""
# press 1 for login
# press 2 for exit """)
# desicion=int(input(" enter : "))
# if desicion==1:
#     new_email=input("verify your email : ")
#     new_password=input("verify your password : ")
#     if new_email == original_email and new_password == original_password:
#         print("login successfull")
#     else:
#         print("login failed")
# elif desicion == 2:
#     print("exit ......")
# else:
#     print("wrong input")
"""string"""
data='welcome to regex'
# print(len(data))
# print(data.split(' '))
"""list"""
data=[123,3,4,5,5,6,6,5] #list is mutable and it is ordered
# data.sort()
# data.reverse()
# print(data)
# print(data[::-1])

# print(data)
# data[0]=123456
# print(data)
# print(data[-2])
# print(data[3])
# print(data[::-1])
data.append(45)
# print(data)
# data.clear() #it will remove all the elements
# print(data)
data_copy=data.copy()
data_copy.append(34)
# print(data_copy)
# print(data)
# print(data.count(5)) # it will count occurnace of a element
# data.extend([12,3])
# print(data)
# print(data.index(5))
# data.pop()
# print(data)
# data.remove(5)
# print(data)
# data.reverse()
# print(data)
# data.sort()
# print(data)
# data.insert(1,450)
# print(data)
"""tuples"""
data=(23,34,4,5,6,5,5,5) #it is immutable and ordered
# data[0]=90
# print(data)
# print(data.index(34))
# print(data.count(5))
"""set"""
# data={234,12,34,7,23,7,90} # it is mutable and unordered
# data.add(45622)
# print(data)
# data.clear()
# print(data)
d1={1,2,3,4}
d2={3,4,5,6}
# print(len(d1))
# print(d2.difference(d1))
# d1.difference_update(d2)
# print(d1)
# d1.discard(40)
# print(d1)
# d1.remove(40)
# print(d1)
# print(data)
# print(data[0]) #TypeError: 'set' object is not subscriptable
# data={1,2,1,2,4} # duplicate dataelement are not allowed
# print(data)
# empty_set=set() # this is how we create empty set
# print(type(empty_set))

d1={1,2,3,4,5,6}
d2={4,5,6,7,8,9}
# print(d1.intersection(d2))
# d1.intersection_update(d2)
# print(d1)
# print(d1.isdisjoint(d2))
# print(d2.issubset(d1))
# print(d1.issuperset(d2))
# d1.pop()
# print(d1)
# print(d1.union(d2))
# d1.update(d2)
# print(d1)

# print(d1.symmetric_difference(d2))
