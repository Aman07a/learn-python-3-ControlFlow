# Fortune Cookie Program 🥠

import random

fortune = random.randint(0, 4)

if fortune == 0:
    # Added colon ":" after the if statement
    print("May you one day be carbon neutral")
elif fortune == 1:
    print("You have rice in your teeth")
elif fortune == 2:
    # Corrected "eli" to "elif" for the third condition
    print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
    # Added closing parenthesis ")"
    print("You can only connect the dots looking backwards")
elif fortune == 4:
    print("The fortune you seek is in another cookie")
