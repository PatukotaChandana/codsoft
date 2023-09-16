#Creating a multiple-choice quiz game using Python and tkinter can be a fun project. Below is a simple example of how you can create a basic MCQ quiz game using tkinter. In this example, we'll create a quiz with three questions and display the user's score at the end.


import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "correct_answer": "4"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 10), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.next_question_button = tk.Button(root, text="Next Question", font=("Arial", 12), command=self.next_question)
        self.next_question_button.pack(pady=10)
        
        self.display_question()
    
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.show_score()
    
    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["correct_answer"]
        if self.option_buttons[selected_option]['text'] == correct_answer:
            self.score += 1
        self.current_question += 1
        self.display_question()
    
    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.destroy()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_score()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

#This code creates a basic tkinter application for a multiple-choice quiz game. You can expand it by adding more questions and customizing the user interface to your liking.
