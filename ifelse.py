#if..else
#used to create prog that makes some decisions

#age of a person and determine if the person is eligible to drive or not

# if boolean_exp: 
#   statements

age = 10
if (age >= 18):
  print("Eligible to Drive")
  #whether true or false it will do as per decision and will come out and run rest of the code
#if condition is false we use else
else:
  print("Not eligible to Drive")
print("I am outside if")

#elif
#we have one or two choices above, if we have more than 2 options to choose from then we use elif

num = 10
if (num > 0) :
  print("number is positive")
elif (num < 0):
  print("number is negative")
else:
  print("number is 0")

#nestedifelse
# one if else statement inside another
num = float(input ("Enter a number: "))

if (num >= 0):

  if num == 0:
    print("Zero")
  else:
    print("Number is positive")

else: 
  print("negative")