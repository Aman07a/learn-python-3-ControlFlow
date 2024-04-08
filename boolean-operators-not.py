# Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

# Statement one:
statement_one = not (4 + 5 <= 9)

# Statement two:
statement_two = not (8 * 2) != 20 - 4

# Previous if statement with additional checks using and and not statements:

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")
