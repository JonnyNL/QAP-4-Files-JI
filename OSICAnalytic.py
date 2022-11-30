# ONE STOP INSURANCE COMPANY
import matplotlib.pyplot as plt
from datetime import datetime


#  Program to process the total amount of claims per month and graph them

TodayYear = datetime.today().year

print("         ONE STOP INSURANCE COMPANY")
print("               CLAIM ANALYTICS      ")
print()

# Initialize lists
y_axis = []
x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# Take user input of total monthly claims and add it to the y axis list
# Validations are to make sure user inputs only integers
print(f"Enter total amount of claims per month of {TodayYear}")
print("----------------------------------------------")
while True:
    try:
        Jan = int(input("January: "))
        y_axis.append(Jan)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Feb = int(input("February: "))
        y_axis.append(Feb)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Mar = int(input("March: "))
        y_axis.append(Mar)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Apr = int(input("April: "))
        y_axis.append(Apr)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        May = int(input("May: "))
        y_axis.append(May)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Jun = int(input("June: "))
        y_axis.append(Jun)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Jul = int(input("July: "))
        y_axis.append(Jul)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Aug = int(input("August: "))
        y_axis.append(Aug)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Sep = int(input("September: "))
        y_axis.append(Sep)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Oct = int(input("October: "))
        y_axis.append(Oct)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Nov = int(input("November: "))
        y_axis.append(Nov)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")
while True:
    try:
        Dec = int(input("December: "))
        y_axis.append(Dec)
        break
    except ValueError:
        print("Invalid entry. Numbers only.")


# Plot our x and y values onto the graph to compare claims to months
plt.plot(x_axis, y_axis)

# Label our graph
plt.xlabel('Month')
plt.ylabel('Total Amount of claims ($)')

plt.title(f'Claim Analytics for {TodayYear}')
plt.grid(True)
# Display the graph
plt.show()