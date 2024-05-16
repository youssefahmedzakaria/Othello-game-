from tkinter import Tk, Label, Button
from OthelloGUI import OthelloGUI

class DifficultyWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Select Difficulty")
        self.master.geometry("300x150")

        self.label = Label(self.master, text="Select Difficulty Level")
        self.label.pack()

        self.easy_button = Button(self.master, text="Easy", command=lambda: self.set_difficulty(1))
        self.easy_button.pack(pady=5)

        self.medium_button = Button(self.master, text="Medium", command=lambda: self.set_difficulty(3))
        self.medium_button.pack(pady=5)

        self.hard_button = Button(self.master, text="Hard", command=lambda: self.set_difficulty(5))
        self.hard_button.pack(pady=5)

    def set_difficulty(self, level):
        self.master.destroy()
        main(level)

def main(difficulty):
    root = Tk()
    app = OthelloGUI(root, difficulty)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    difficulty_window = DifficultyWindow(root)
    root.mainloop()