# print(5/0)

# Handle exception that might be raised.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")