from question import Question
from data import get_data
from quizbrain import QuizBrain
from ui import UI
import tkinter as tk
def run_game():
    quiz = QuizBrain(question_bank)
    quiz_ui = UI(quiz)
restart = True

def restart_game():
    global restart
    restart = True
    restart_window.destroy()
def close_game():
    global restart
    restart = False
    restart_window.destroy()
while restart:
    question_data = get_data()
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    run_game()
    restart = False
    restart_window = tk.Tk()
    restart_window.title("Restart?")
    restart_window.geometry("200x200")
    restart_window.label = tk.Label(restart_window, text="Do You Want to Restart The Quiz?")
    restart_window.label.pack()
    restart_window.yes = tk.Button(restart_window, text="Yes", command=restart_game)
    restart_window.yes.pack()
    restart_window.no = tk.Button(restart_window, text="No", command=close_game)
    restart_window.no.pack()
    restart_window.mainloop()
thanks_window = tk.Tk()
thanks_window.title("Credits")
thanks_window.label = tk.Label(thanks_window, text="Made by Ishaan Nair")
thanks_window.label.pack()
thanks_window.after(2000, thanks_window.destroy)
thanks_window.mainloop()