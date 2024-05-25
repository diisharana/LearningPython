# # print to use comments like this, we use print (), and within the brackets we can give data.
# # print()
# # print("Hello world")
# # a = 7
# # b = 10
# # print(a, b)
# # #we can create a variable name and use string using quotes
# # name = "disha"
# # print(name)
# # print("name:", name)
# # #print moves cursor to the next line
# # print("First line \n\n")
# # print("Second line")

# # # for comments command + forward slash or just use hash symbol

# # #input system for input from User
# # #in Python we can use the same variable multiple times
# # name = input("Enter name:")
# # print(name)
# # #whenever we give any input, it is stored as a string, input function stores in type string
# # print(type(name))

# # #Variables
# # #are used to store data or values
# # a = 10
# # #a is a variable storing value 10
# # b = 1.1
# # #b is a variable storing value 1.1 (float value)
# # #in Python we do not have to explicitly mention the type of value
# # a = 7
# # # it will change value of a from 10 to 7
# # #variable names cannot start with reserved keywords - this, if, else, try

# # #namingConventions
# # #cannot start with number, first_name
# # first_name = "disha"

# # #Literals are values stored in Variable eg: disha, 10, 7, are all literals, can be numeric Literals, string or boolean Literals.
# # #Numeric Literals- can be 10, 0, -10
# # #String literal name, character
# # name = "Python"
# # char = 'p'
# # #booleanliterals are true or false, case sensitive, t with lower case is not a Literal, capital T and add quotes will become a string
# # a = True
# # b = False

# # #Strings
# # name = "Disha"
# # char = 'A'
# # #If we have multi line string
# # multiline_string = """
# # name : Disha
# # subject: python
# # job: QA"""
# # print(multiline_string)

# # #Type Conversion
# # #we have Implicit and Explicit type conversion

# # num_int = 5
# # print(type(num_int))
# # # 5 is integer and data type is by default integer
# # num_float = 5.5
# # print(type(num_float))

# # sum = num_int + num_float
# # print(sum)
# # print(type(sum))
# # #Python is doing it itself

# # #Explicit we use pre-defined functions
# # int()
# # float()
# # str()  #to convert one data type to another

# # a = '77'  #this is a string
# # int_num = int(a)  #explicitly converting variable string to integer
# # print(int_num)
# # print(type(int_num))

# #convert to float
# # float_example = float(a)
# # print(float_example)
# # print(type(float_example))

# #OPERATORS- operator is a symbol to carry out arithmetical or logical operations

# a = 5
# b = 10
# sum = a + b
# print(sum)

# #Arithmetic Operators
# # + - * / %
# a = 1
# b = 2
# c = 3
# sum = a + b + c
# print("Sum is:", sum)

# #concatenate
# first_name = 'Disha'
# last_name = 'Rana'
# name = first_name + ' ' + last_name
# print("The Name is:", name)

# result = 5 * 1.5
# print("Multiply result is:", result)

# # star operator can also be used to repeat strings
# a = " Python"
# b = a * 3
# print(b)

# # a = "abc"
# # b = a * '3'
# # print(b)

# #/ and //
# result = 17 / 2
# print(result)

# result = 17 // 2
# print(result)
# #prints the Quotient

# result = 17 % 2
# print(result)

# # ** Operator
# #left operand is raised to the power of right operand
# result = 2**3
# print(result)

# #assign multiple values to multiple variables at a time in Python
# a, b, c = 1, 2, 3.5
# print(a, b, c)
# x = y = z = "python"
# print(x, y, z)
# print(x)
# #https://www.w3schools.com/python/gloss_python_assignment_operators.asp

# #Operator Precedence
# print(10 - 5 + 2 * 3)
# #order of precedence is resolve brackets >> raised to power * * >> +x, -x  >>
# #other arithmetic operators  *, /, //, %, +, -

# import booleanexpression
#import ifelse
# # import loops
# import functions
#import lists
import tuples