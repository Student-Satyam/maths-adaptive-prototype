# Import random module to generate random numbers
import random

# This function creates a math problem based on difficulty level
def generate_problem(level):

    # EASY LEVEL: small addition numbers
    if level == "Easy":
        # Generate two numbers between 1 and 10
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        # Return the question as text and the correct answer
        return f"{a} + {b}", a + b

    # MEDIUM LEVEL: multiplication with bigger numbers
    elif level == "Medium":
        # Generate numbers between 10 and 50
        a = random.randint(10, 50)
        b = random.randint(1, 10)

        # Return multiplication problem
        return f"{a} * {b}", a * b

    # HARD LEVEL: division problems
    else:
        # Generate larger numbers
        a = random.randint(50, 100)
        b = random.randint(1, 10)

        # Integer division to keep answer simple
        return f"{a} / {b}", a // b
