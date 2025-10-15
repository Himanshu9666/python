'''dictionary'''
# it is collection of keys and values
# data={}    # it is mutuable and ordered
# print(type(data))
# data={'name':['mayank','shekhar'],'aadhar':123456,"mkbile_no":136546}
# print(type(data))
# print(data['aadhar'])#acces the keys values ferom the components

# # data['aadhar']=1234567890
# # print(data)

# print(data['name'][-1])  #shekhar

# #if there is duplicate vales in components then rightmost values will print 

# data={'a':'shekhar','b':[34,5,6],'c':{45,56,7},'t':(34,56,5)}
# data['t'][-1]=90
# print(data['t'][-1]) # error

#we can make dictionary using single values datatypes like int ,float,boolean,string

# data={'a':34,12:'twelve',True:344,4.5:[235,34]}
# print(data[True])
# print(data[4.5])




'''methods'''

# data={'a':123,'b':354,'c':456}
# data.clear()
# print(data)

# print=(data.items()) # gives data item in keys in list

# print(data.values())  #shows all values in keys have

# print(data.keys())  #shows all the keys

# print(data.get('a'))  #show the values of a(key)

# print(data.setdefault('x',566))

# data['pqr']=jaipur
# print(data)  ## add this in main dictonary




'''loops'''
'''range'''
# data=list(range(10))
# data=tuple(range(5,10))
# data=set(range(1,10,2))# {1,3,5,7,9}
# data=list(range(10,0,-1))  #ulta
# data=list(range(4,41,4))
# print(data)

'''For loop'''
#only for collection and range
#toatl elemts = totaol loop runs
#for variable_nam in collection_name:




# fruits=['apple','orange','papya','guava','litchi']
# for fruit in fruits:
#     print(fruits)

# for var in fruits:
#     print("hello",var) #hello apple and runs loops

table=int(input("enter the no :"))
for i in range(1,11):
    print(f"2 x {i} ={table*i}")