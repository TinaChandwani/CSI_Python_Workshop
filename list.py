# lists
# What is a list?
#list and arrays? 

# Declare a list
courses = ['History', 'Math', 'Physics', 'CompSci']

# Traversing a list
for i in courses:
    print(i)
for i in range(len(courses)):
    print(courses[i])
# SLicing and indexing
print(courses[-1])  # last value
print(courses[0:2:2])  # Inclusive:Not Inclusive step-size

# Methods on list
courses.append('Art')  # add new elements to list
courses.insert(0, 'Chemistry')  # (index, name)
li




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
print(min(nums))  # prints the min number in the list
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

# list comprehension
even = [2 * x for x in range(10)]
print(even)
