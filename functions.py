print("hello from Functions")
# a block of code which runs only when called is called a Function and we can pass data 
#to a function using arguments or parameters and we can also get a rerurn value from a function

# def func_name(parameters):
#   statements


def hello(name):
  print("Hello", name)


hello("Python")
hello ("Disha")
#reusable code 


#write a fucntion to add two numbers

def add (num1, num2):
  return( num1+ num2)

print(add( 2, 5))
print (add( 4, 9))

#builtin Functions
#print(), input (), range ()

#variables of function and their scope
x= 10
def my_func():
   x= 5
   print ('value of x inside fucntion is:', x)
my_func()
print('value of x outside function is:', x)
  
#Arguments or parameters
def hello(name, message):
  print('hello', name + ', ' + message)

hello('Disha', 'Function example')


def hello(name, message='how are you?'):
  print('hello', name + ', ' + message)
  
hello('Disha')



#positional arguments
def hello(name, message):
  print("Hello", name + ', ' + message)

hello('Disha', 'Good evening')
hello(message = "how are you?", name = "Elvis")


#Arbitrary arguments
#when we are not sure about the number of arguments

def hello(*names):
  print ("Hello", names)

hello('Eric', "monica", "elvis", "tom")
#when we call the function with the argument

#anonymouse fucntion | Lambda functions
#we can define a func without a name

# lambda arguments: expression

sum = lambda a,b,c: a + b + c
print (sum (2, 3, 4))


#recursive functions
# a function can call other func and also itself
# a func that calls itself 
#process- recursionError

#prog to find sum of natural numbers
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10


def calculation_sum(n):
  if n == 1:
    return 1
  else:
   return n + calculation_sum(n -1)


sum = calculation_sum(10)
print(sum)
  
