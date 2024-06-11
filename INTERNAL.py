import random

# 
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
        # Avoid division by zero, what this part of the code does for the primary questions is that
        # as it quiz asks the user questions, what it does is it does not ask the user and number divided
        # by 0. Because that is not possible in maths, so the user will not have an answer to give the quiz.
        #Which is why I have removed those questions on the primary quiz.
        if num2 == 0:
            num2 = 1
        answer = num1 / num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

# Function to generate intermediate math questions. What this function does is it generates the questions for when
#the user chooses the intermediate math quiz so they can have generated questions with the infinite mode.
def generate_intermediate_question():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    answer = num1 + num2 if operator == '+' else num1 - num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

# Function to generate secondary math questions. What this function does is it generates the questions for when
#the user chooses the secondary math quiz so they can have generated questions with the infinite mode.
def generate_secondary_question():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 10)
    operator = random.choice(['*', '/'])
    if operator == '*':
        answer = num1 * num2
    else:
        # Avoid division by zero, what this part of the code does for the primary questions is that
        # as it quiz asks the user questions, what it does is it does not ask the user and number divided
        # by 0. Because that is not possible in maths, so the user will not have an answer to give the quiz.
        #Which is why I have removed those questions on the primary quiz.
        if num2 == 0:
            num2 = 1
        answer = num1 / num2
    answer = round(answer, 1)
    question = f"{num1} {operator} {num2}"
    return question, answer

# Function to generate a math quiz, this is the overall part of this code that helps generate the quiz, what
# it does is it welcomes the user to the quiz and tells them to round their answers to 1 decimal place. As
# Said in the Instructions. Then, it makes the variables for the generating the questions for the three quizzes,
# and it also makes our infinite mode for the three quizzes and the option to leave the quiz during infinite mode.
#As we need that otherwise the user cannot leave the infinite quiz, which is not ideal. I have used a while loop here,
# because if the user enters an invalid input, then it will tell the user a fun comment to make sure they enter numbers instead
# of letters, (excluding "c").
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

# Function to display quiz history, what this part of our code does is it prints and shows our user the history of the
# previous quiz they have done and their answer, the correct answer, and the overall percentage and fraction of the questions
# they have answered correctly, and the amount of questions they have answered. This part of the quiz is crucial. Because
# i want to make sure the history works properly for the user because they should have the right to know what they have gotten
# right and wrong on the quiz they have answered. I have used a for loop, because it is the best loop to use because we want
# the user to have the right answered and the right questions so it satisfies the user, which is what the for loop is meant
# to do.
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

# Function to get the number of questions from the user, what this function does is that it asks the user just before
# the quiz they have selected for how many questions they will prefer to answer. If they enter 'i', it will activate infinite
# mode, which means infinite amount of questions until the user enters 'c' on the keyboard, which cancels it. This is important,
# because the user should be asked how many questions they like because it is more preferable for the user, because they may
# be short on time or would like to do heaps of learning for maths from the quiz. So giving them the option is very good.
# I have used a while loop, because I have made it a loop so that if the user enters something incorrect, what it does is it
# tells the user to enter a correct input so that the quiz will continue. It is helpful because the user can make a mistake
# which is not ideal. The while loop is the best for this situation.
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

# Main function, this is the most important function of this quiz as this is the menu, where the user can see the instructions,
# the quizzes, the history, and can exit the quiz if they wish. This part of my quiz is in a while loop, because what I have done
# is I have used "if", "elif", as variables so it sends the user directly into the instructions, quizzes, history, or exiting the
# quiz if they desire. If the user does not enter a number between 1 and 6, as those are the numbers I have chosen to make it easy.
# It will tell the user to enter something valid to the context and will continue looping the menu until something valid has been
# been entered to the menu.
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
                display_history(quiz_history[-1][1])  # This line of code does show the history of the latest quiz the user has done.
            else:
                print("No quiz history yet.")
        elif choice == '6':
            print("Aw leaving already???... That's ok! Thank you for playing and make sure to come back again!!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
