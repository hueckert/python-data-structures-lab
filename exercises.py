# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # Create a list of student names
    students = ["Alice", "Bob", "Charlie"]
    
    # Assign the second student's name to a variable
    first_student = students[1]
    
    # Assign the last student's name to a variable
    last_student = students[-1]
    
    # Return the variables as a tuple
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # Create a tuple of foods
    foods = ("Pizza", "Burger", "Pasta")
    
    # Initialize an empty string for the meal
    meal = ""
    
    # Use a for loop to concatenate each food to the meal string
    for food in foods:
        meal += food + " "
    
    # Return the concatenated meal string, stripped of trailing whitespace
    return meal.strip()

# Call the function and print the result
print('Exercise 2:', combine_foods())
