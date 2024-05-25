#  Polymorphism in Python
#  What is Polymorphism?
# The literal meaning of polymorphism is the condition of occurrence in different forms.
# Polymorphism is a very important concept in programming. 
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

#  Method Overloading in Python

# Method Overloading in Python is a type of Compile-time Polymorphism using which we can define two or 
# more methods in the same class with the same name but with a different parameter list.
# We cannot perform method overloading in the Python programming language as everything is 
# considered an object in Python. Out of all the definitions with the same name, it uses the latest definition for the method. 
# Hence, we can define numerous methods with the same name, but we can only use the latest defined method.
# In Python, we can make our code have the same features as overloaded functions by defining a method in such
# a way that there exists more than one way to call it. For example:

# Function to take multiple arguments
def sum_number(*args):
    # variable to store the sum of numbers    
    result = 0
    
    # accessing the arguments
    for num in args:
        result += num
    
    # Output
    print("Sum : ", result)

    
# Driver Code
if(__name__ == "__main__"):
    print("Similar to Method Overloading\n")
    print("Single Argument    ->", end = " ")
    sum_number(10)

    print("Two Arguments      ->", end = " ")
    sum_number(30, 2)

    print("Multiple Arguments ->", end = " ")
    sum_number(1, 2, 3, 4, 5)

Output:
Similar to the Method of Overloading

Single Argument    -> Sum :  10
Two Arguments      -> Sum :  32
Multiple Arguments -> Sum :  15

