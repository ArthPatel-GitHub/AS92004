import random

# Define math questions for each level
primary_questions = {
    "1 + 1": 2,
    "2 * 3": 6,
    "5 - 3": 2,
    "8 / 2": 4
}

secondary_questions = {
    "5^2": 25,
    "sqrt(16)": 4,
    "3 * (4 + 2)": 18,
    "9 / 3": 3
}

intermediate_questions = {
    "2^3": 8,
    "10 * 5": 50,
    "sqrt(81)": 9,
    "15 / 3": 5
}

# Function to generate a math quiz
def generate_quiz(level, questions):
    print("Welcome to the {} level Math Quiz!".format(level))
    score = 0
    history = []

    # Shuffle the questions
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for question in question_keys:
        answer = input("What is {}? ".format(question))
        if answer.isdigit() and int(answer) == questions[question]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is {}.".format(questions[question]))
            history.append((question, answer))

    print("You scored {}/{} in the {} level Math Quiz.".format(score, len(questions), level))
    return level, history

# Function to display quiz history
def display_history(history):
    print("Quiz History:")
    for level, level_history in history:
        print("Level: {}".format(level))
        for question, answer in level_history:
            print("Question: {} - Your Answer: {}".format(question, answer))
        print()

# Main function
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
            print("""This is a game that has three quizzes. What you need to do is enter a number for what quiz level
            you would like to do so you can proceed. Then the quiz you have selected will start. You will answer the
            questions that the game gives you, with your score being tallied at the end. If you would like to see your 
            quiz history, you can enter '5' to see it. If you would like to exit this quiz, please enter '6'. Enjoy!!!""")
        elif choice == '2':
            level, history = generate_quiz("Primary", primary_questions)
            quiz_history.append((level, history))
        elif choice == '3':
            level, history = generate_quiz("Intermediate", intermediate_questions)
            quiz_history.append((level, history))
        elif choice == '4':
            level, history = generate_quiz("Secondary", secondary_questions)
            quiz_history.append((level, history))
        elif choice == '5':
            display_history(quiz_history)
        elif choice == '6':
            print("Exiting the game... Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
