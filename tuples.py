print('Hello from tuples.py')
#a tuple is similar to a list
#Unlike Lists , elements once assigned to a tuple cannot be changed
#Tuples are immutable
#to define a tuple we place elements inside parenthesis

my_tuple = (1, 2, 3, 4, 5)
my_emptytuple = ()
my_tuple2 = (1, 2, 'red', 'green', 0.4, True)
my_tuple3 = (1, 2, (3.9, 22.9, 5000, 'banana'), 1540)
my_tuple4 = (1, 2, 3, ['peanuts, almonds'])
print(my_tuple)
print(my_emptytuple)
print(my_tuple2)
print(my_tuple3)
print(my_tuple4)


#we can also have 1 item in a tuple
t1= ('python')
#this looks valid but wont be considered as a tuple
print(type(t1))
#have to add comma for single tuple
t2 = ('disha',)
print(type(t2))

#access elements in a tuple
tuple1= ('a', 'b', 'c', 'd')
print(tuple1[0])
#print(tuple1[5]) #error, index out of bounds

#negative indexing
print(tuple1[-1]) #-1 index accesses the last item
print(tuple1[-2])

#slicing a tuple, to access a range of elements- slicing operator :

my_tuple =('h', 'e', 'l', 'l','o')
print(my_tuple[1:4]) #this will print 2nd to 4th element
print(my_tuple[:-3]) #no starting index,which means start from begining to -3 
print(my_tuple[2:]) # no ending index, which means start from 2nd to end
print(my_tuple[:]) #no starting and ending index, which means start from begining to end

#change elements of a tuple
#tuples are immutable- elements once assigned cannot be changed, however if a tuple contains any mutable elements like lists, they can be changed


my_tuple = (1, 2, 3, ['h', 'e', 'l', 'l', 'o'], 5, 8)
print(my_tuple)
my_tuple[3][3] = 'x'
print(my_tuple)

#+ and * operators
#concatenate tuples using +
#repeat tuple using *

my_tuple = (1, 2, 3)
print(my_tuple + (4, 5, 6))
print(my_tuple * 3)

#looping through a tuple

for item in my_tuple:
  print(item)


#deleting a tuple, tuples are immmutable, cannot be changed or delete items or elements in a tuple, however we can delete the tuple itself

del my_tuple
# print(my_tuple) will throw an error



