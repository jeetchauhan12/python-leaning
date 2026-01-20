# If, Elif, and Else Statements in Python
# Syntax: if condition1: statement elif condition2: statement else: statement

# Example 1: Grade assignment based on score

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Example 2: Age category classification

age = 25

if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Example 3: Traffic light system

light_color = "green"

if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Get ready to stop")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid light color")

# Example 4: Weather recommendation

temperature = 15

if temperature > 30:
    print("It's hot! Drink water and stay in shade")
elif temperature > 20:
    print("It's warm. Nice weather to go out")
elif temperature > 10:
    print("It's cool. Wear a jacket")
elif temperature > 0:
    print("It's cold. Wear warm clothes")
else:
    print("It's freezing! Stay indoors")

# Example 5: Login system with role check

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Admin login successful")
elif username == "user" and password == "password":
    print("User login successful")
else:
    print("Invalid credentials")

# Example 6: Day of week

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

# Example 7: BMI calculation

weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.2f} - Underweight")
elif bmi < 25:
    print(f"BMI: {bmi:.2f} - Normal weight")
elif bmi < 30:
    print(f"BMI: {bmi:.2f} - Overweight")
else:
    print(f"BMI: {bmi:.2f} - Obese")

# Example 8: Movie rating classification

movie_rating = 12

if movie_rating == 'G':
    print("General Audiences - All ages")
elif movie_rating == 'PG':
    print("Parental Guidance - Some content may not suit children")
elif movie_rating == 'PG-13':
    print("Parents Strongly Cautioned - Some content not suitable for children under 13")
elif movie_rating == 'R':
    print("Restricted - Children under 17 need parent/guardian")
elif movie_rating == 'NC-17':
    print("Adults Only")
else:
    print("Unknown rating")

# Example 9: Discount calculation

purchase_amount = 150

if purchase_amount < 50:
    discount = 0
    print(f"No discount. Total: ${purchase_amount}")
elif purchase_amount < 100:
    discount = purchase_amount * 0.05
    print(f"5% discount. Total: ${purchase_amount - discount}")
elif purchase_amount < 200:
    discount = purchase_amount * 0.10
    print(f"10% discount. Total: ${purchase_amount - discount}")
else:
    discount = purchase_amount * 0.15
    print(f"15% discount. Total: ${purchase_amount - discount}")

