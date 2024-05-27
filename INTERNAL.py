import random

# instructions for the quizes
INSTRUCTIONS = """
This is a game that has three quizes, what you need to do is enter a number for what quiz level 
you would like to do so you can proceed, then the quiz you have selected will start. You will 
answer the questions that the game gives you, with your score being tallied at the end, and thats 
all it is!!!
If you would like to see your quiz history, please enter '5' on your keyboard to see it. If you 
would like to exit this quiz, please enter '6' on your keyboard. Enjoy!!!
"""
# Define math questions for each level
primary_questions = {
    "1 + 1": 2,
    "2 * 3": 6,
    "5 - 3": 2,
    "8 / 2": 4,
    "10 - 5": 5,
    "20 - 10": 10,
    "4 * 5": 20,
    "12 / 3": 4,
    "3 * 5": 15,
    "9 + 8": 17,
    "14 - 8": 6,
    "5 * 2": 10,
    "19 - 11": 8,
    "1 * 2": 2,
    "9 / 3": 3,

}

intermediate_questions = {
    "2^3": 8,
    "10 * 5": 50,
    "sqrt(81)": 9,
    "15 / 3": 5,
    "81 / 9": 9,
    "4 * 8": 32,
    "(4 + 1) * 8": 40,
    "8 ^ 2:": 64,
    "8 * 9": 72,
    "7 * 11": 77,
    "55 / 11": 5,
    "156 + 48": 204,
    "200 - 76": 124,
    "19 * 2": 38,
    "100 / 5": 20,

}

secondary_questions = {
    "5^2": 25,
    "sqrt(16)": 4,
    "3 * (4 + 2)": 18,
    "9 / 3": 3,
    "5 ^ 3": 125,
    "10 * 13": 130,
    "sqrt(81)": 9,
    "15 / 3": 5,
    "5 * 25": 125,
    "(55 - 20) * 3 ": 105,
    "16 * 4": 64,
    "117 / 9": 13,
    "185 + 479": 664,
    "958 - 361": 597,
    "4!": 24

}

# Function to generate a math quiz
def generate_quiz(level, questions):
    print("Welcome to the {} level Math Quiz!".format(level))
    score = 0
    history = []

# Shuffle the questions
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    #answering questions, showing what question to answer, showing if question is correct or not, and overall score in quiz
    for question in question_keys:
        answer = input("What is {}? ".format(question))
        if answer.isdigit() and int(answer) == questions[question]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is {}.".format(questions[question]))
        history.append((question, answer))

    print("You scored {}/{} in the {} level Math Quiz.".format(score, len(questions), level))
    return history

# Function to display quiz history
def display_history(history):
    print("Quiz History:")
    for question, answer in history:
        print("Question: {} - Your Answer: {}".format(question, answer))

# Main function
def main():
    quiz_history = []
    while True:
        print("\nSelect a Math Quiz level:")
        print("1. Primary")
        print("2. Secondary")
        print("3. Intermediate")
        print("4. View History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            quiz_history.extend(generate_quiz("Primary", primary_questions))
        elif choice == '2':
            quiz_history.extend(generate_quiz("Secondary", secondary_questions))
        elif choice == '3':
            quiz_history.extend(generate_quiz("Intermediate", intermediate_questions))
        elif choice == '4':
            display_history(quiz_history)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()



