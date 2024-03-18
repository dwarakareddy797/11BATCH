#1.)Python program to captilalize the first and last character of each word in a string
#2.)Input:128
#ouput:Yes
#128%1==0,128%2==0, and 128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2 and ans=[6,8,10,12]


#n = 128
#for i in n:
#    print(i)


#n = 128
#while n!=0:
#    rem = n%10
#    print(rem)
#    n = n/10

#n = 128
#for i in str(n):
#    print(i)

n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % n
    n = n//10
n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")
l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)
# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)
# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)


# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))


s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)


# intersection() ---> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8, 9}
print(s1.intersection(s2))

# n1 = {1,2,3} --> s1

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
for val in s1:
    if val in s2:
        str1 = "its joint set"
print(str)


# ? char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key,value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed,
# 5.) Duplicate values are allowed
# 6.) It is unidexed
# 7.) It is ordered
# 8.) Key does nat allow mutable datatypes
# 9.) Values allow mutable datatypes


d1={1:100,2:200,3:300,-4:400}
#to access elements in dictionary
print(d1)
#or
#to access the values
print(d1[-4])#---->o/p is 100

#some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

#to find min,max based on values
print(min(d1.values))

# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300,4:400}
#pop item()
d1.popitem()
print(d1)


#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = "a","apple",


d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
'''
'''
d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
''

#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}




#pop
#d1.pop(2) #2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 ditionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple","b":"ball","c":"cat"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}



# to print all the values
#print(d1.values())


# to print all the keys
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())


# * Iterating dictionary
# for val in d1: # to Iterate keys alone
#   print(val)


# for val in d1.values(): # iterate values alone
#   print(val)

# to get both keys and values
# for key, val in d1.items():
#   print(key, val)


# ! Problem:1
# n = input()


#1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg", "is", "bBgst", "for", "eGGks"]


test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
 
# printing original lists
print("The original list is : " + str(test_list))
 
# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
 
# printing result 
print ("List after performing character swaps : " + str(res))

