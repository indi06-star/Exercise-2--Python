# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x=5
x=+3
print(x)

# TODO: Multiply y by 2 using the *= operator
x= 4
x *=2
print(x)

# TODO: Divide x by y and store the result in a variable called 'result
x=4
y=2
result=x/y 

# TODO: Print the value of 'result'
print(result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

a= 10
b= 5
c= 15

# TODO: Create a condition that checks if a is greater than b
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")



# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b=5
modulus = b%2

if modulus==0:
    print("b is even")
else:
    print ("b is not even")
# TODO: Create a condition that checks if c is less than or equal to a
if c<=a:
    print("c is less than or equal to a")
else:
    print("c is not less than or equal to a")

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

final_condition=a>b or modulus==0 and c<=a 
# TODO: Print the value of 'final_condition'

print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score= int(input("enter a test score (0-100) "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score >=90 and score <=100:
    print("Congradulations you have obtained an A")
elif score >= 80 and score <=89:
    print("Excellent you have obtained a B")
elif score>=70 and score <=79:
    print ("Good work you have obtained a C")
elif score >=60 and score <=69 :
    print("You need to put in more work , youve obtained a D") 
else:
    print("You need to focus or youre going to fail  you have obtained an F")


# TODO: Print the grade for the given score
print(score)

# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("enter num1 "))
num2 =int(input("enter num2 "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation =input("enter an operation +,-,*,/  " )

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
#result=0
if operation =="+":
    print(num1 + num2)#result=num1+num2
if operation =="-":
    print(num1 -num2)
if operation == "*":
    print(num1 *num2)
if operation=="/":
    if  num2 == 0:
        print("cannot be solved ")
    else:
        print(num1/num2 )
# TODO: Print the result of the operation 
#print(result)
