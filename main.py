# Python program to create a simple GUI
# Simple Quiz using TKinter

# import everything from tkinter
from tkinter import *
from tkinter import messagebox as mb

#import json to use json file for data
import json

#class to define the components of the GUI
class Quiz:
    def __init__(self):

        # set question number to 0
        self.q_no = 0

        #assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    # This method is used to display the result.
    # It counts the number of correct and wrong answers
    # and display them at the end as a message box.
    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calculates the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        #shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # This method checks the answer after we click on Next.
    def check_ans(self, q_no):

        # checks if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            return True

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):

            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next question by incrementing the q_no counter
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()

            # destroys the GUI
            gui.destroy()
        else:
            #shows the next question
            self.display_question()
            self.display_options()

    # This method shows the two buttons on the screen
    def buttons(self):

        # The first button is the next button to move to the
        # next question.
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # Placing button on screen
        next_button.place(x=350, y=380)

        #second button which is used to quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)

    # This method is used to deselect the radio buttons on the screen.
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # This method shows the current question on the screen
    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    # This method is used to display title
    def display_title(self):
        title = Label(gui, text="QUIZ MODULE",
                      width=50, bg="orange", fg="black", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    # This method shows the radio buttons to select the question on the screen
    #at the specified position.
    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI window
gui.geometry("800x450")

# set the title of the window
gui.title("GET QUIZ")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

# set the questions, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# Create an object of the quiz class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM....