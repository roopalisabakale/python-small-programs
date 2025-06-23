# Program to check if a number is even or odd

# Take input from the user and convert it to an integer
num = int(input("Enter a number: "))

# Use modulus operator to check if remainder is 0 when divided by 2
if num % 2 == 0:
    # If true, it's an even number
    print("Even")
else:
    # Otherwise, it's an odd number
    print("Odd")
