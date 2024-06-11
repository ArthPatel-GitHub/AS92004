import random

INSTRUCTIONS = """
This is a game that has three quizzes. What you need to do is enter a number (2 - 4)
for which quiz level you would like to do, then the quiz you have selected will start. You
will then be asked how many questions you would like to answer (please enter a positive integer
or 'i' for infinite amount of questions) and then the quiz will start! If you would like to exit 
the quiz while answering the questions, please enter 'c' on the question you are on and the quiz will finish.
At the end of the quiz, your score will be tallied and shown to you. If you would like too see the full results
you must play at least one quiz, then enter the number '5' on the menu to see the history. If you would like to
leave our awesome quiz. Please enter '6' on the menu. We strongly recommend that you use a calculator for our
quizzes, because we are known for having the most difficult quizzes on the planet! (Not really, but they are 
challenging!) And thats all there is too it! Please have fun and as always, do your best!!!!!

Note: Please round your answers to 1 decimal place if necessary.
"""

def generate_primary_question():
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
        
        if num2 == 0:
            num2 = 1
        answer = num1 / num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

def generate_intermediate_question():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    answer = num1 + num2 if operator == '+' else num1 - num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer


def generate_secondary_question():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 10)
    operator = random.choice(['*', '/'])
    if operator == '*':
        answer = num1 * num2
    else:
        
        if num2 == 0:
            num2 = 1
        answer = num1 / num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer


def generate_quiz(level, infinite=False, num_questions=0):
    print(f"Welcome to the {level} level Math Quiz!")
    print("Please round your answers to 1 decimal place if necessary.")
    score = 0
    history = []

    question_generator = {
        "Primary": generate_primary_question,
        "Intermediate": generate_intermediate_question,
        "Secondary": generate_secondary_question
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
            history.append((question, user_answer, answer))
        except ValueError:
            print("You silly one! Enter a number! Not a letter!!!! Its Maths!!!!!!.")

    print(f"You scored {score}/{len(history)} in the {level} level Math Quiz.")
    return score, history

def display_history(history):
    print("Quiz History:")
    correct_count = 0
    for question, user_answer, correct_answer in history:
        print(f"Question: {question} - Your Answer: {user_answer} - Correct Answer: {correct_answer}")
        if abs(user_answer - correct_answer) < 0.1:
            correct_count += 1

    if len(history) > 0:
        percentage = (correct_count / len(history)) * 100
        print(f"Score: {percentage:.2f}% ({correct_count}/{len(history)})")
    else:
        print("No questions answered.")
  
def get_num_questions():
    while True:
        num_questions = input("How many questions would you like to answer on this phenomenal quiz?? (Enter 'i' for infinite questions) ")
        if num_questions.lower() == 'i':
            return 'i'
        try:
            num_questions = int(num_questions)
            if num_questions > 0:
                return num_questions
            else:
                print("Woah! Good job for knowing that! But for now, let's stick to positive numbers!")
        except ValueError:
            print("Please enter the right answer you silly one! There's only one right answer to maths!")


def main():
    quiz_history = []
    while True:
        print("\nSelect a Math Quiz level:")
        print("1. Instructions")
        print("2. Primary")
        print("3. Intermediate")
        print("4. Secondary")
        print("5. View History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(INSTRUCTIONS)
        elif choice == '2':
            num_questions = get_num_questions()
            if num_questions == 'i':
                quiz_history.append(generate_quiz("Primary", infinite=True))
            else:
                quiz_history.append(generate_quiz("Primary", num_questions=num_questions))
        elif choice == '3':
            num_questions = get_num_questions()
            if num_questions == 'i':
                quiz_history.append(generate_quiz("Intermediate", infinite=True))
            else:
                quiz_history.append(generate_quiz("Intermediate", num_questions=num_questions))
        elif choice == '4':
            num_questions = get_num_questions()
            if num_questions == 'i':
                quiz_history.append(generate_quiz("Secondary", infinite=True))
            else:
                quiz_history.append(generate_quiz("Secondary", num_questions=num_questions))
        elif choice == '5':
            if quiz_history:
                display_history(quiz_history[-1][1])  
            else:
                print("No quiz history yet.")
        elif choice == '6':
            print("Aw leaving already???... That's ok! Thank you for playing and make sure to come back again!!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
