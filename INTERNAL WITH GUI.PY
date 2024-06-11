import random
import tkinter as tk
from tkinter import messagebox
# Instructions for the quizzes, I have used a constant here called "INSTRUCTIONS" because I want this
# just to be for the instructions without it changing, so that is why I have made is a constant.
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

Note: Please round your answers to 1 decimal place if it is necessary.
"""

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")
        self.quiz_history = []
        self.score = 0
        self.history = []
        self.num_questions = 0
        self.current_question = ""
        self.current_answer = 0
        self.infinite = False
        
        self.main_menu()

    
    def main_menu(self):
        self.clear_window()
        #What this part of the TKInter UI does is it shows the user the options for the menu so they can see
        # the instructions, the quizzes, the history, and exiting the quiz back into VS Code.
        title = tk.Label(self.root, text="Math Quiz Game", font=("Helvetica", 18))
        title.pack(pady=10)

        btn_instructions = tk.Button(self.root, text="Instructions", command=self.show_instructions)
        btn_instructions.pack(pady=5)

        btn_primary = tk.Button(self.root, text="Primary Level Quiz", command=lambda: self.start_quiz("Primary"))
        btn_primary.pack(pady=5)

        btn_intermediate = tk.Button(self.root, text="Intermediate Level Quiz", command=lambda: self.start_quiz("Intermediate"))
        btn_intermediate.pack(pady=5)

        btn_secondary = tk.Button(self.root, text="Secondary Level Quiz", command=lambda: self.start_quiz("Secondary"))
        btn_secondary.pack(pady=5)

        btn_history = tk.Button(self.root, text="View History", command=self.display_history)
        btn_history.pack(pady=5)

        btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        btn_exit.pack(pady=5)

    def show_instructions(self):
        messagebox.showinfo("Instructions", INSTRUCTIONS)

    def start_quiz(self, level):
        self.level = level
        self.clear_window()
        
        title = tk.Label(self.root, text=f"{level} Level Math Quiz", font=("Helvetica", 18))
        title.pack(pady=10)

        lbl_questions = tk.Label(self.root, text="How many questions would you like to answer? (Enter 'i' for infinite)")
        lbl_questions.pack(pady=5)

        self.entry_questions = tk.Entry(self.root)
        self.entry_questions.pack(pady=5)

        btn_start = tk.Button(self.root, text="Start Quiz", command=self.setup_quiz)
        btn_start.pack(pady=5)

    def setup_quiz(self):
        num_questions = self.entry_questions.get()
        if num_questions.lower() == 'i':
            self.infinite = True
        else:
            try:
                self.num_questions = int(num_questions)
                if self.num_questions <= 0:
                    raise ValueError
                self.infinite = False
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a positive integer or 'i' for infinite.")
                return

        self.score = 0
        self.history = []
        self.next_question()

    def next_question(self):
        if not self.infinite and len(self.history) >= self.num_questions:
            self.end_quiz()
            return
        
        self.clear_window()

        if self.level == "Primary":
            self.current_question, self.current_answer = self.generate_primary_question()
        elif self.level == "Intermediate":
            self.current_question, self.current_answer = self.generate_intermediate_question()
        else:
            self.current_question, self.current_answer = self.generate_secondary_question()
        
        lbl_question = tk.Label(self.root, text=f"What is {self.current_question}?", font=("Helvetica", 16))
        lbl_question.pack(pady=10)

        self.entry_answer = tk.Entry(self.root)
        self.entry_answer.pack(pady=5)

        btn_submit = tk.Button(self.root, text="Submit", command=self.check_answer)
        btn_submit.pack(pady=5)

    def check_answer(self):
        user_answer = self.entry_answer.get()
        if user_answer.lower() == 'c':
            self.end_quiz()
            return
        
        try:
            user_answer = round(float(user_answer), 1)
            if abs(user_answer - self.current_answer) < 0.1:
                messagebox.showinfo("Correct!", "Excellent Job!!! Keep going at it you smart one!!!!")
                self.score += 1
            else:
                messagebox.showinfo("Incorrect", f"Sorry!!! The correct answer is {self.current_answer}. You will get it next time!!! Keep going!!!!!")
            self.history.append((self.current_question, user_answer, self.current_answer))
            self.next_question()
        except ValueError:
            messagebox.showerror("Invalid Input", "You silly one! Enter a number! Not a letter!!!! Its Maths!!!!!!.")

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"You scored {self.score}/{len(self.history)} in the {self.level} level Math Quiz.")
        self.quiz_history.append((self.level, self.history))
        self.main_menu()

    def display_history(self):
        if not self.quiz_history:
            messagebox.showinfo("No History", "No quiz history yet.")
            return

        self.clear_window()
        
        title = tk.Label(self.root, text="Quiz History", font=("Helvetica", 18))
        title.pack(pady=10)
        
        history_text = tk.Text(self.root, width=80, height=20)
        history_text.pack(pady=10)

        for quiz_level, history in self.quiz_history:
            history_text.insert(tk.END, f"{quiz_level} Level Quiz:\n")
            correct_count = 0
            for question, user_answer, correct_answer in history:
                history_text.insert(tk.END, f"Question: {question} - Your Answer: {user_answer} - Correct Answer: {correct_answer}\n")
                if abs(user_answer - correct_answer) < 0.1:
                    correct_count += 1
            if len(history) > 0:
                percentage = (correct_count / len(history)) * 100
                history_text.insert(tk.END, f"Score: {percentage:.2f}% ({correct_count}/{len(history)})\n\n")

        btn_back = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        btn_back.pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def generate_primary_question(self):
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

    def generate_intermediate_question(self):
        num1 = random.randint(1, 15)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-'])
        answer = num1 + num2 if operator == '+' else num1 - num2
        answer = round(answer, 1)
        question = f"{num1} {operator} {num2}"
        return question, answer

    def generate_secondary_question(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
