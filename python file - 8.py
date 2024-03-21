def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("dwaraka", 21,"KSRM")



# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement


#def f1(a, b):
#    c = a*b
#    return c
# # print(f1(6,8))
# obj = f1(6, 8)
# obj1 = f1(4, 6)

# def gracemark(object):
# print(object+4)
# gracemark(obj)
# gracemark(obj1)

#123

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("enter the value: "))
palindrome(a)

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args


# * Positional args
# ? The position of parameter have to be same as position as arguments
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile(96668686,"Usman",100) #unexpected


def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

profile(8074884522,"naruto",95)

#? functions are divided into 5 catagories

# postal args
# keywords args
# defalt args
# variable length args
# keyword variable length args

# * Positional args
#Eg:1;
##def profile(name, phone, mark):
##    txt ="My name is {}. My phone number is {}. I got {} marks."
##    print(txt.format(name, phone, mark))
##
##    profile(9704984013, "mani", 92)


# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)

# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
profile("shashank",mark=98,phone=9876543210)



    
# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("reddy", 'dwaraka', 'Alone')


# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1

def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    

# Eg:-2

d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)


# ex:3
# create of a method
#When the function is created with a class is called as method
#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p=person()
#p.display()
