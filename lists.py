print('I am inside lists.py')

#datastructure in Python used to store list of items in Python. it is created by putting items inside square bracs  [ ]

# list1= [ ] empty list
list2 = [1, 2, 3, 4, 5]  #list of integers
colors = ['red', 'blue', 'orange', 'green']  #list of strings
mixed_list = [1, 2, 3.8, 'red']

print(colors)

my_list = ['python', 'java', [1, 2, 3], 'disha']
#a list can have another list as an item
print(my_list)

#access elements from a list
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[2])  #prints index position 2 item
print(numbers[-1])  #prints last item
print(numbers[-2])
# print(numbers[5]) # results in an error- index out of bounds

#Slicing a list
print(numbers[2:5])
# from index position 2 until index position 4, 3rd to 5th element
print(numbers[2:])  #3rd to last
print(numbers[:3])
print(numbers[3:])
print(numbers[:-2])  #begining to 3rd
print(numbers[:])

#lists are mutable- change the items in the list
my_colors = ['red', 'blue', 'green', 'yellow']
print(my_colors)
my_colors[2] = 'black'
print(my_colors)
my_colors[1:3] = ['white', 'purple']  #2nd to 3rd item
print(my_colors)

#add items to a list
numbers = [1, 2, 3, 4]
print(numbers)
numbers.append(5)
print(numbers)
numbers.extend([6, 7, 8])
print(numbers)

#combine lists using + operator
print(numbers + [9, 10])
#repeat items using the  *
print(numbers * 3)
#insert an item at a desired location insert()
numbers.insert(2, 2.5)
print(numbers)

#delete items- del
del numbers[2]  #delete the third item
print(numbers)
del numbers[2:4]  #delete multiple items as per the range given
print(numbers)
del numbers
# print(numbers) #error- list not defined

print('-------------------')

numbers = [1, 2, 3, 4, 5]
numbers.remove(1)  #remove item 1
print(numbers)
numbers.pop(2)  #remove item at index positio 2
print(numbers)
numbers.pop()  #will remove last item
print(numbers)
numbers.clear()  #lear the list
print(numbers)

#copy list using = sign
list1 = [1, 2, 3, 4, 5]
list2 = list1
print(list1)
print(list2)
print('-------------------------')

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)


#loop through a list
fruits = ['apple', 'banana', 'orange']
for item in fruits:
  print(item)

#check item in list
print('apple' in fruits)
print('grapes' in fruits)


#nested lists
my_list =[1, 2, 3, [2.0, 5.0, 6.7], 7, [8, 9, 10]]
print(my_list[3][1])
