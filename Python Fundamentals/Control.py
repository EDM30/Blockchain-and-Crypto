# Control Flow Example: Boolean, Comparison Operators, and If Statements

# Boolean values
is_sunny = True
is_raining = False

# Comparison operators
temperature = 25
is_warm = temperature > 20  # True
is_cold = temperature < 10  # False

# If statements using boolean and comparison operators
if is_sunny and is_warm:
    print("It's a nice day to go outside!")
elif is_raining:
    print("Don't forget your umbrella.")
elif is_cold:
    print("Wear a jacket, it's cold!")
else:
    print("Weather is moderate.")

# More comparison examples
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Boolean NOT operator
if not is_raining:
    print("No rain today!")