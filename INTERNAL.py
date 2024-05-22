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
