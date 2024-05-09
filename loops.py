print("I am inside loops")

#while loop
# while boolean_expression : 
#   statements
  #until the expre is true it will keep running the loop unless false


a = 4
b = 1
while (b <= a) :
  print("I am inside while loop", b)
  b = b + 1

#find sum of natural numbers
n = 10
sum = 0
i = 1
while(i <= n):
  sum = sum + i
  i = i + 1
  
print("Sum of the natural numbers:", sum)

# while loop with else (optional else block)
#else is executed when condition in while FALSE

i = 0
while(i >= 3) :
  print("I am inside while loop")
  i = i + 1

else:
  print("I am outside while, I am inside else")


#for loop
# for value in the sequence (list or ranges):
# statements

#range is used to create sequence of numbers :last number is not included, so the numbers are 1-10
numbers = range(1, 11)
sum = 0
for i in numbers:
  sum = sum + i
  # sum += i
print("Sum is", sum)


#fibonacci series
# 1, 2, 3, 4
# num = num++

#for with else 
numbers = range (1,4)
for i in numbers:
  print('inside for loop')

else:
  print('inside else')

my_list = [1, 3, 4, 8]
for item in my_list:
  print(item)
else:
  print('items completed')

#fibonacci series
fibonacci_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in fibonacci_list:
  print('The Fibonacci series are', item)
else:
  print('Fibonacci series completed')


# break continue pass
#break and continue can alter the flow of a normal loop

numbers = [1, 3, 6, -3, 0, 7, 10]

for i in numbers:
  if (i < 0):
    print('value is negative')
    break
  print (i)    

#continue statement is used
  

