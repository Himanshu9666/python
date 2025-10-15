'''other methods in lists'''
'''reverse of list using append'''
# data=[1,22,3,4,5]
# new=[]
# for i in range(-1,-len(data)-1,-1):
#     new.append(data[i])
# print(new)

'''Tupple'''
t1={23,45,65,66,45} 
'''Tis immutuable and ordered'''
# print(t1.count(45))  count occurence of 45
#print(ti.index(45)) gives index of 45

'''set'''  #mutuable and unordered

# set1={12,43,55,6}
# print(type(set1))
# for i in set1:
    # print(i)
# print(set1[0]) #indexing is not allowed
# data={1,2,1,2}
# print(data) #duplicate valeues are not allowed

# data={23,54,45,5}
# data.add(90)
# print(data) #mutable

# data.pop()
# print(data) #removes end value


s1={1,2,3,4}
s2={3,5,6,6}
# print(s1.difference(s2)) #removes elemnt that are not in  common
# print(s2.difference(s1))

# s1.discard(4)
# s1.remove(5)
# print(s1)

# print(s1.intersection(s2))
# print(s1.intersection_update(s2))

# s1.isdisjoint(s2)  #fales s2 and s1 have common element


# print(s1.union(s2))  #prints common in both the set

# s1={23,4,54,56,6}
# s2={2,4,5,6,3,0,90,9}
# print(s1.subset(s2)) #true


'''dictionary'''

'''example'''
'''1'''
# data={'a':45,'b':91,'c':56}
# for k,v in data.items():
#     print(k,'---',v)
'''2'''
# data=[('a',43),('b',45),('c',89)]   #tupple
# for i,j,k in data:
#     print(i,j,k)

'''3'''
# data=[(12,234,5),(45,4,54),(67,89,54),(7,78,546)]   #tupple
# for i,j,k in data:
#     print(i,j,k)

#if dupicate keys then  right most key value can access only
#values can be duplicate

'''zip function '''
# keys=['a','b','c','d']
# values=[25,45,6,3]    #a--> 25  b-->45 c-->6 d-->3
# data=zip(keys,values)
# print(data)

#we can assing list to ,set tupple ,dict

# print(dict(data))
# print(set(data))
# print(list(data))
# print(tuple(data))



'''Ques --> count the occurencce of char in string'''


# data='abcghacbba'
# char='abcdeifghijklmnopqrstuvwxyz'
# count=0
# for i in data:
#     if i.lower() in char:
#         count=count+1

# print("",count) 

# data='abcghacbba'
# keys=list(data)
# values=[]
# for i in keys:
#     count=0
#     for j in data:
#         if i==j:
#             count=count+1
#     values.append(count)
# print(dict(zip(keys,values)))



string = "abchhahhabaa"
counts = {}

for char in string:
    count = 0
    for i in string:
        if i == char:
            count += 1
    counts[char] = count

print(counts)
print(type(counts))




for i in range(1,5):
    for j in range(1,5):
        for k in range(1,3):
            print("*",end=' ')
    print()
































