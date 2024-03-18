# ! ------> common functions for list

#l1 = [6, 7, 8, 9, 0]
#print(len(l1))

#print(max(l1))
#print(min(l1))

#l1 = [6, 8, 9, "P", "u"]
#print(max(l1)) # --> error coz its a combination of list and string
#print(min(l1)) # --> error coz its a combination of list and string

#l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
#print(l1.index(9))

#l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count()--->how many num of times an element is repeated
# print(11.count(6))
#! some functions which is specifically used for list


# To add element inside list
# ? insert(index_value, element) --> to add element at specific index position
#11 = [6,6,6, 7, 8, 9,0, 8.89, -5, 0.78]
# 11.insert(2, "cars")
# print(11)
#? To delete element from list
#11 = [6,6,6, 7, 8, 9,0, 8.89, 5, 0.78]
#pop() ---> last element will be deleted
# 11.pop()
# print(11)
# pop(index_value) --> used to delete element at specific index
#11.pop(4)#4 is index value
#print(11)

#remove(element) --> used to delete element directly
#l1.remove(8.89)
#print(l1)

#*clear() --> to complete delete all element in list
#l1.clear()
#print(l1)
# ! ----------> common functions for list

l1 = [6,7,8,9,0]
# print(len(l1))

# print(max(l1))
# print(min(l1))

# l1 = [6,7,8,9,"p","u"]
# print(max(l1)) # --> error coz its a combination of int and string
# print(min(l1)) # --> error coz its a combination of int and string

# l1 = [6,7,8,9,0,8.89,-5,0.78]
# print(min(l1)) # -5

# l1 = [6,7,8,9,0,8.89,-5,0.78]
# index() --> to get index value of specific element
# print(l1.index(9))


# l1 = [6,7,8,9,0,8.89,-5,0.78]
# count() --> how many num o

# ? ---> copy()
# l1 = [6, 7, 8,9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))
# shallow copy
#import copy
#l1=[8,9,0,[5,6],[3,2,1]]
#l2=copy.copy(l1)
#l1.append(209)
#print(l1)
#print(l2)
# * deep copy --> used to copy the list with nested list
# * --> deep copy
#import copy
#l1 = [8,9,0,[5,6],[3,2,1]]
# print(l1[-1][1]) ---> to index nested list

#l2 = copy.deepcopy(l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)
# M:-2 --> descending order
'''
l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
# ! ----> nested list
# M:-1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[3][1])
'''
# M:-2
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:5])
'''
# M:-3
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:-1])
'''
#? sort --> arrange elelemts in list in ascending or descending order
#11 [9, 7, 45,0,-6, 5, 12 ]
# 11.sort() # tol arrange in ascending order
# print(11)

# 11.sort(reverse=True) # to sort in descending order
# print(11)

# 11 = ['z', 'i', 'o', 'p', 9]
# 11.sort()
# print(11) # --> error


#? list constructor
# * list() --> to conver other collection datatype to list
# 13 = ((8,9, 0))
#print(list(13))

#14 = 8
#print(list(14))

#!-----> nested list

#11=[8,9,[0,8,7],["p","o","y"],[8,'t']]
#print(11[-2][1]) #--->0

#print(11[1:4])
#print(11[1:-1])

#? to delete "t" from 11
l1=["p","o",'y']
l2=[8,'t']
l1.extend(l2)
print(l1)
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
# ! ------> Tuple
# * char of tuple

# 1.) Tuple have to be sourrund by ()
# 2.) the elements inside tuple are not chargable
# 3.) The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# * eg:1
t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))

# ? Indexing, slicing are all same as list
# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
# Iterate based on index value

l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# Iterate based on Elements

#l1 = [9, 8, 0, 6, 5]
#for i in l1:
    #print(i)

# * Iterate based on Index value
#l1 = [9, 8, 0, 6, 5]
#for i in range(0,5):
    #print(i)
# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord() --> used to find the ASCII value of a character
#ord()--->used to find the ASCII value of a character
s1='u'
print(ord(s1))

#strip()--->to eliminate the space in beginning and end of string
s1=" where are you"
print(s1.lstrip())
# --> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space
'''
s1 = "   where are you.?"
print(s1.lstrip())
'''
# M:-2
# --> to eliminate right space
'''
s1 = "where are you.?  "
print(s1.rstrip())
'''
# M:-3
# --> to eliminate right and left space
'''
s1 = "   where are you.?    "
print(s1.strip())
'''

# ---> split()-->
# --> to split the words in string based on a character
s1= "where are you.?"
print(s1.split(" "))
# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
# s1 = "welcome to all"
# * print(s1.endswith('1'))
# * print(s1.startswitch('w'))

# s1 = "67"
# print(type(s1))
# print(s1.isdigit))

# * print the string in reverse manner
s1 = "welcometo all"
print(s1[::-1])

        # ! -----> Eg:2
# s1 = "67"
# print(type(s1))
# print(s1.isdigit())


#print the string in reverse manner
s1 = "Welcome to all"
characters =len(s1)
#print(characters)
'''
words = s1.split(" ")
print(words)


words = s1.split(" ")
print(len(words))

'''
#sentences = s1.split('.')
#print(len(sentences))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))
