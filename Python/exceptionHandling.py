# Errors:
# Errors represent severe, unrecoverable problems that generally indicate an issue beyond the scope of the application code itself. They often stem from system-level problems or resource exhaustion.
# Characteristics:
# Typically unrecoverable by the program.
# Often indicate fatal issues like out-of-memory errors, stack overflow, or hardware failures.
# The program usually terminates immediately when an error occurs.
# Examples:
# OutOfMemoryError: The Java Virtual Machine (JVM) runs out of memory.
# StackOverflowError: The call stack overflows, often due to infinite recursion.
# Exceptions:
# Exceptions represent problems that occur during the normal execution flow of a program, but are often recoverable or can be handled gracefully by the application code. They typically arise from issues within the program's logic or unexpected external conditions. 
# Characteristics:
# Can often be caught and handled using try-catch blocks.
# Allow the program to continue execution, possibly by providing alternative behavior or displaying informative messages.
# Can be categorized into checked (must be handled) and unchecked (runtime) exceptions.
# Examples:
# ArithmeticException: Attempting to divide by zero.
# FileNotFoundException: Trying to access a file that does not exist.
# NullPointerException: Attempting to access a member of a null object.

# a=b NameError: name 'b' is not defined

'''
# try else
try:
    # codeblock where exception can occur
    a=1
    c=a+'s' # type error
    d=a/0 # Exception - division by zero
    a=b # Name error
except NameError:
    # Name error will give this msg
    print("The user has not defined variable")
except TypeError:
    # Type error will give this msg
    print("Try to make data type similar")
except Exception as ex:
    print(ex)
else:
    #successful execution
    print(c,d)
'''  

'''   
# try else finally
try:
    a=int(input("enter num 1:"))
    b=int(input("enter num 2:"))
    c=a/b
except NameError:
    # Name error will give this msg
    print("The user has not defined variable")
except TypeError:
    # Type error will give this msg
    print("Try to make data type similar")
except Exception as ex:
    print(ex)
else:
    print(c)
finally:
    print("Execution done")
'''

# Custom Exception
class Error(Exception):
    pass
class dobException(Error):
    pass

year=int(input("Enter year of birth: "))
age=2025-year
try:
    if age<30 and age>20:
        pass
    else:
        raise dobException
except dobException:
    print("Year range not valid")