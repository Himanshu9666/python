'''List''' #mutuable and ordered
'''It is a collection of data elements in [] which data element are separated by ,'''

# data=[63,True,'k',45.4]
# #print(data)
# for i in data:  #for var in collection/sequence
#     print(i)  # in that case i will be the data elements

# data=[1,'2',3,54,6]
# for i in data:
#     print[i]

#forward indexing  0 1 2 3 4 5
#reverse indexing -1 -2 -3 -4 -5 


# for i in range(0,len(data))
#     print(data[i])

# data=[1,15,7,8,3,54,6,7]
# for i in data:
#     if i%3==0 and i%5==0:
#         print(i)

'''methods of List'''
data=[1,4,88,7,5,54]
even=[]
# data.append(78)#add 78 last of the list
# print(data)
# for i in data:
#     if i%2==0:
#          even.append(i)
# print(even)
'''even no filter'''
# for i in data:
#     if i<10:
#         even.append(i)
# print(even)

#or

# for i in range(0 ,len(data)):
#     if data[i]<=10:
#         even.append(data[i])
# print(even)

'''filter string data in list'''

# data=['student',23 ,45,'scom']
# new_data=[]
# for i in range(0,len(data)):
#     if type(data[i])==str:
#         new_data.append(data[i])
# print(new_data)

'''insert method'''
# data=[3,2,4,2,7]
# data[-1]=data[2:5]  
# print(data) #[3, 2, 4, 2, [4, 2, 7]]

# data[1:4]=data[2:5]
# print(data)   #[3, 4, 2, 7, 7]


# data=[1,2,3,4,5,6]
# data.insert(2,90000)
# print(data)  #[3,55,6,8,7,5]


# data[1,2,3,4,5,6]
# new=[]
# for i in data:
#     new.insert(0,i)
# print(new)

# data.pop(index no)
# print(data)

#data.remove(data element)
#print(data)

#data.clear(empty the list)
#print(data)

#data.count(count the elemnt in the list)
#print(data)

'''filter out those data element whose count is  grreater then 1'''

# data=[1,2,5,1,2,3,3,3,4,5,6]
# new=[]
# for i in data:
#     if data.count(i)>1:
#         new.append(i)
# print(new)

'''We are having 2 operators that we can apply on our list are {+ and  -} + --> cancatioation  and * --> repeat that list multiple times '''
# d=[1,2,3]
# print(d*3)
# print(d+3)


# a=[1,2,2]
# b=[2,2,3]
# a.extend(b)
# print(a)

#data.reverse
#data.short

'''next day wali chez'''
# list1=[12,43,3,5]
# list1.append(90)
# new=list1.copy()
# new.append(190)
# print(list1)
# print(new)#a both are same
#change perfform in copy not in original











































































































































