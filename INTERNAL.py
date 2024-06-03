import random

#The instructions for the three quizies, history, exiting the quiz, and other useful tips.

INSTRUCTIONS = """
This is a game that has three quizzes. What you need to do is enter a number (2 - 4)
for which quiz level you would like to do, then the quiz you have selected will start. You
will then be asked how many questions you would like to answer (please enter a positive integer
or 'i' for infinite amount of questions) and then the quiz will start! If you would like to exit 
the quiz while answering the questions, please enter 'c' on the question you are on and the quiz will finish.
At the end of the quiz, your score will be tallied and shown to you. If you would like too see the full results
you must play at least one quiz, then enter the number '5' on the menu to see the history. If you would like to
leave our awesome quiz. Please enter '6' on the menu. We strongly recommend that you use a calculator for our
quizes, because we are known for having the most difficult quizes on the planet! (Not really, but they are 
challenging!) And thats all there is too it! Please have fun and as always, do your best!!!!!

Please note that all questions should be rounded to one decimal place if it is neccesary!
"""

#The primary function to generate the primary quiz maths questions for the user.
def generating_primary_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 5)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Avoid division by zero to make the questions are solvable.
        if num2 == 0:
            num2 = 1
        answer = num1 / num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

#The primary function to generate the intermediate quiz maths questions for the user.
def generating_intermediate_question():
    num1 = random.randint(1, 15)
    num2 = random.randint (1, 10)
    operator = random.choice(['+', '-'])
    answer = num1 + num2 if operator == '+' else num1 - num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

#The primary function to generate the secondary quiz maths questions for the user.
def generating_secondary_question():
    num1 = random.randint(1, 40)
    num2 = random.randint(1, 10)
    operator = random.choice['*', '/']
    if operator == "*":
        answer = num1 * num2
    else:
         # Avoid division by zero to make the questions are solvable.
         if num2 == 0:
             num2 = 1
             answer = num1/ num2
             answer = round(answer, 1)
             question = f"{num1} {operator} {num2}"
             return question, answer

# Function to generate a math quiz
def generate_quiz(level, infinite=False, num_questions=0):
    print(f"Welcome to the {level} level Math Quiz!")
    print("Please round your answers to 1 decimal place if necessary.")
    score = 0
    history = []

    question_generator = {
        "Primary": generating_primary_question,
        "Intermediate": generating_intermediate_question,
        "Secondary": generating_secondary_question
    }[level]

    while infinite or len(history) < num_questions:
        question, answer = question_generator()
        user_answer = input(f"What is {question}? (Enter 'c' to cancel the quiz) ")
        if user_answer.lower() == 'c':
            print("See you next time!")
            print(f"You scored {score}/{len(history)} in the {level} level Math Quiz.")
            return score, history
        try:
            user_answer = round(float(user_answer), 1)
            if abs(user_answer - answer) < 0.1:
                print("Excellent Job!!! Keep going at it you smart one!!!!")
                score += 1
            else:
                print(f"Sorry!!! The correct answer is {answer}. You will get it next time!!! Keep going!!!!!")
            history.append((question, user_answer))
        except ValueError:
            print("You silly one! Enter a number! Not a letter!!!! Its Maths!!!!!!.")

    print(f"You scored {score}/{len(history)} in the {level} level Math Quiz.")
    return score, history










   
    


