import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generates a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

def calculate_result(num1, num2, operator):
    """
    Calculates the result of a mathematical operation.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2

def math_quiz():
    """
    Main function for the Math Quiz Game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        operand1 = generate_random_integer(1, 10)
        operand2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_result(operand1, operand2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
