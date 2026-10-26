import tkinter as tk
from quizbrain import QuizBrain
THEME_COLOR = "#375362"

class Input:
    def __init__(self):
        self.params = {'num':None, 'cat':None, 'level':None}
        self.input_box1 = tk.Tk()
        self.input_box1.geometry("400x300")
        self.input_box1.title("Choose How many Questions")

        # variable storage and user entry box for typing number of questions and chosen category
        self.num_of_questions = tk.Entry(self.input_box1, width=50)
        self.num_of_questions.insert(0, 'Number of questions you want')
        self.num_of_questions.pack()
        self.difficulty = tk.Entry(self.input_box1, width=50)
        self.difficulty.insert(0, "(Easy/Medium/Hard)")
        self.difficulty.pack()
        self.def_category = tk.StringVar(self.input_box1)
        self.def_category.set("Select a category")
        self.options = [
            "Any Category",
            "General Knowledge",
            'Entertainment: Books',
            'Entertainment: Film',
            'Entertainment: Music',
            'Entertainment: Musicals and Theatres',
            'Entertainment: Television',
            'Entertainment: Video Games',
            'Entertainment: Board Games',
            "Science and Nature",
            'Science: Computers',
            'Science: Mathematics',
            'Mythology',
            'Sports',
            'Geography',
            'History',
            'Politics',
            'Art',
            'Celebrities',
            'Animals'
        ]
        menu = tk.OptionMenu(self.input_box1, self.def_category, *self.options)
        menu.pack()
        # button to close popup and open next

        true_img2 = tk.PhotoImage(file="save.png")
        self.input_button1 = tk.Button(self.input_box1, image=true_img2, command=self.store_var, highlightthickness=0)
        self.input_button1.pack()

        self.input_button2 = tk.Button(self.input_box1, text="Close", command=self.close_popup)
        self.input_button2.pack()
        self.input_box1.mainloop()







    def store_var(self):
        if type(self.num_of_questions.get()) == str and self.def_category.get() != "Select a category" and type(self.difficulty.get()) ==str:
            try:
                if int(self.num_of_questions.get()) > 0 and str(self.difficulty.get()) == "Easy" or "Medium" or "Hard":
                    num = self.num_of_questions.get()
                    category = self.options.index(self.def_category.get())
                    difficulty = self.difficulty.get().lower()
                elif int(self.num_of_questions.get()) == 0:
                    error = tk.Toplevel()
                    error.title = "Oops..."
                    error.label = tk.Label(text="0 Questions, really?")
                    error.label.pack()
                    error.after(2000, error.destroy)
                    error.mainloop()
            except ValueError:
                error = tk.Toplevel()
                error.title = "Oops..."
                error.label = tk.Label(text="Please enter the numbers and strings into the correct boxes")
                error.label.pack()
                error.after(2000, error.destroy)
                error.mainloop()
            else:
                self.params = {
                    "num": num,
                    'cat': category,
                    "level":difficulty
                }
        elif type(self.num_of_questions.get()) != str or self.num_of_questions.get() == 0:
            error = tk.Toplevel()
            error.title = "Error"
            error.label = tk.Label(error, bg="red", text="Please enter a number greater than 0", fg="white")
            error.label.pack()
            error.after(2000, error.destroy)
            error.mainloop()
        elif self.def_category == "Select a category":
            error = tk.Toplevel()
            error.title = "Error"
            error.label = tk.Label(error, bg="red", text="Please enter a category", fg="white")
            error.label.pack()
            error.after(2000, error.destroy)
            error.mainloop()
        else:
            pass

    def close_popup(self):
        if self.params != {'num':None, 'cat':None, 'level':None}:
            self.input_box1.destroy()
        else:
            lol = tk.Toplevel()
            lol.geometry("300x300")
            lol.title("Caught You")
            lol.label = tk.Label(lol, bg="red", text="A non-existent quiz wouldn't be very fun, now would it", fg="white")
            lol.label.pack()
            lol.after(2000, lol.destroy)
            lol.mainloop()
class UI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.canvas = tk.Canvas(self.window, bg="white", width = 300, height = 250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, width = 280, text="Insert Question Here", font=("Arial", 20, "italic"))

        self.label = tk.Label(self.window, text="Score: 0", bg=THEME_COLOR, font=("Arial", 15, 'bold'))
        self.label.grid(row=0, column=1)

        true_img = tk.PhotoImage(file="true.png")
        self.true_button = tk.Button(self.window, image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="false.png")
        self.false_button = tk.Button(self.window, image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.label.config(text= f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've Finished The Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(3000, self.window.destroy)
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
import random
print("IIIIIIII".lower())