#Given the “gross” salary of a person, calculate the “net”.
#• Here are the constrains:
#1. If the gross is less than 1000, then the income tax is 10%
#2. If the gross is less than 2000, then the income tax is 12%
#3. If the gross is less than 4000, then the income tax is 14%
#4. If the gross is more than 4000, then the income tax is 18%
#5. If the gross is less than 2000, every child gets you a tax cut of 1%
#6. If the gross is more than 2000, every child gets you a tax cut of 0.5%
#• Read the “gross” and the number of children
#• Print the “net”
#• Use try/except when reading the inputs

try:
    gross = float(input("Enter gross salary: "))  # Convert input to float
    children = int(input("Enter number of children: "))  # Convert input to int
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()  # Stop execution if input is invalid

# Determine base tax rate
if gross < 1000:
    tax_rate = 10
elif gross < 2000:
    tax_rate = 12
elif gross < 4000:
    tax_rate = 14
else:
    tax_rate = 18

# Apply child tax reduction
if gross < 2000:
    tax_rate -= children * 1  # Reduce 1% per child
else:
    tax_rate -= children * 0.5  # Reduce 0.5% per child

# Calculate net salary
net = gross - (gross * tax_rate / 100)

# Print final net salary
print(f"Net salary after tax: {net}")
