import tkinter as tk
from tkinter import ttk

class LanguageSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Selector")

        self.languages = {
            "English": "USA",
            "Spanish": "Spain",
            "French": "France",
            "German": "Germany",
            "Italian": "Italy",
            "Portuguese": "Portugal",
            "Chinese": "China",
            "Japanese": "Japan",
            "Korean": "South Korea"
        }

        self.flag_images = {
            "USA": tk.PhotoImage(file="usa_flag.png"),
            "Spain": tk.PhotoImage(file="spain_flag.png"),
            "France": tk.PhotoImage(file="france_flag.png"),
            "Germany": tk.PhotoImage(file="germany_flag.png"),
            "Italy": tk.PhotoImage(file="italy_flag.png"),
            "Portugal": tk.PhotoImage(file="portugal_flag.png"),
            "China": tk.PhotoImage(file="china_flag.png"),
            "Japan": tk.PhotoImage(file="japan_flag.png"),
            "South Korea": tk.PhotoImage(file="south_korea_flag.png")
        }

        self.language_var = tk.StringVar()
        self.language_var.set(list(self.languages.keys())[0])

        self.flag_label = tk.Label(self.root, image=self.flag_images[self.languages[self.language_var.get()]])
        self.flag_label.pack()

        self.language_menu = ttk.OptionMenu(self.root, self.language_var, *self.languages.keys())
        self.language_menu.pack()

        self.language_var.trace("w", self.update_flag)

    def update_flag(self, *args):
        self.flag_label.config(image=self.flag_images[self.languages[self.language_var.get()]])
        self.flag_label.image = self.flag_images[self.languages[self.language_var.get()]]

root = tk.Tk()
language_selector = LanguageSelector(root)
root.mainloop()
