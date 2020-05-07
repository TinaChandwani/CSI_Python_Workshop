#  dir function
greeting = 'Hello'
name = "Tina"
print(dir(name))
# print(help(lower))

# Built In
#  Absolute
print(abs(-3))
# Round
print(round(3.75))
# print(round(3.75, 1))

# min number in the list
print(max(nums))  # prints the max number in the list
print(sum(nums))  # prints the sum of all the elems in the list

print(courses.index('Art'))  # Gives us the index of 'Art'

# Enumerator
# We can access value and index
for index, course in enumerate(courses, start=1):
    print(index, course)

# Convert List into strings separated by certain value
course_str = ' - '.join(courses)
print(course_str)

# String to List
new_list = course_str.split(' - ')
print(new_list)

# TUPLES
# We cannot modify Tuple (Immutable)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)# lists
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[-1])  # (len(courses))
print(courses[0:2:2])  # Inclusive:Not Inclusive step-size
courses.append('Art')  # add new elements to list
courses.insert(0, 'Chemistry')  # (index, name)

courses_2 = ["Education", 'English']
# courses.insert(0, courses_2)  # Adds two list
# print(courses)
courses.extend(courses_2)  # extends a list to another
courses.remove('Math')
popped = courses.pop()  # by default will remove last elem
print(popped)  # it will return the value which it popped or removed
courses.reverse()  # reverses the list
courses.sort()  # sorts in ascending order
nums = [1, 4, 5, 3, 2]
nums.sort()  # sorts in ascending order
nums.sort(reverse=True)  # sorts in descending order
print(nums)

# This function will return a sort list but will not alter the original list
sorted_courses = sorted(courses)
print(sorted_courses)
print(min(nums))  # prints the 

# Mutable
list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
print(tuple_1)  # Error will be shown
print(tuple_2)
# Cant remove, append

# SETS
cs_courses = {'History', 'Math', 'Physics'}
print(cs_courses)
# sets dont care about order

# remove duplicate values

# What value they share or dont share with other sets
art_courses = {'History', 'Chemistry', 'Design'}

print(cs_courses.intersection(art_courses))  # shows the common elems
print(cs_courses.union(art_courses))  # shows all the elems in both sets
print(cs_courses.difference(art_courses))  # difference between the two sets

# HOW TO CREATE:

# Empty Lists
empty_list = []  # OR
empty_list = list()

# Empty Tuples
empty_tuple = ()  # OR
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

# Dictionary
student = {'name': 'Tina', 'age': 19, 'list_dict': ['Math', 'CompSci']}
print(student)
print(student['list_dict'])
# student_1 = {1: 'Tina', 'age': 19, 'list_dict': ['Math', 'CompSci']}
# print(student_1[1])
# print(student['phone'])  # will show us error as phone key does not exist
# if we dont want an error and we want to return none or default value so in that case get method is used # by default this will give us output as None
print(student.get('phone'))
print(student.get('phone'))
# This will show us the message Not Found
print(student.get('phone', 'Not Found'))
student['phone'] = '555-5555'
student['name'] = 'Ekta'
# print(student.get('phone'))
print(student)
student.update({'name': 'Jai', 'age': 43,
                'phone': '455-445', 'gender': 'male'})
print(student)
del student['age']
name = student.pop('name')
print(name)
for key, value in student.items():  # items methos gives us the key and value of the dict
    print(key, value)


# String Formatting
tag = 'h1'
text = 'This is a headline'

# tag will go to {0} placeholders and text will go to {1}
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
person = {'name': 'Tina', 'age': 19}
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(
    person, person)
print(sentence)
lis = ['Tina', 19]
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(
    person)
print(sentence)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Tina', '19')
sentence = 'My name is {0.name} and i am {0.age} years old'.format(p1)
print(sentence)

x, y = eval(input("Enter two two numbers"))


# FUNCTIONS
def hello_func():
    pass


# print(hello_func())
print('Hello Function!')
# print(hello_funct())
hello_func()
hello_func()
hello_func()
hello_func()
# DRY (DONT REPEAT YOURSELF)


def hello_func(greeting):
    return '{} Function'.format(greeting)


print(hello_func('Hi'))


# if we want to pass another argument and if we not pass anything we dont need any error
def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi'))
# print(hello_func('Hi', name='Tina'))

""" Now you are required positional arguments have to come before your keyword arguments if you try to create function without that order it will give you an error """


# looks confusing but all its doing us allowing us to accept an arbitrary number of positional argumrnts
# def student_info(*args, **kwargs):

# Example - the student_info takes positional arguments that represent crisis the student is taking + keyword will be random info about student... We dont know how many keyword argu will be
# print(args)
# print(kwargs)
# args is Non Keyword argument
# kwargs is a Keyword Argument
# args and kwargs are just names..it can be anything..but its a covention..and it will be better if we stick with it

# In Python we can have variable number of arguments
# args and kwargs is a dyanamic way of calling functions in python as we do not know the number of arguements that will be passed to a function in advance.
# Python functions can have both positional and keyword arguments with default values
#
def person(name, msg):
    print(f"{msg}, I am {name}")


# Default Arguements
# RULE : All the defaut values must be present after the all non default values
# person('Tina')
person('Tina', 'Good Morning')
person(name='CSI', msg='Good Evening')
# Keyword Arguements
# When we call a function with some values, the values get assigned to the arguments according to their position


def person(*names):
    # return type will be tuple
    for name in names:
        print(f'Hello, {name}')


person("Monica", "Ross", "Joey")


def people(**names):
    # return type will be dict
    for key, value in names.items():
        print(f'Hello, {key} {value}')


people(Monica='Geller', Chandler="Bing")


def people(*args, **kwargs):
    print(args)
    print(kwargs)


# people("Monica", "Chandler", "Ross", Name="Pheobe", Age=34)
friends = ['Monica', 'Chandler', 'Ross']
info = {'Name': 'Pheobe', 'Age': 34}
people(*friends, **info)


# difference between str() and repr()
# str() - return a string containing nicely printable representation of an object
# Syntax is basically str(object= '')
# repr() - returns printable representation of a given object

# Lambda
# Lambda function - anonymous function is a function that is defined without a name.
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.
def double(x, y): return (x % 2) ** y


print(double(11, 2))


# Filter method
# This function has no name. It returns a function object which is assigned to the identifier double
my_list = [1, 2, 3, 4, 5, 6, 7]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

# map()
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda x: x**2, my_list))
print(new_list)
