from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
prac_lang = ""


language = None


def set_language(x):
    global language
    language = x
    print(language)




selection_window = Tk()
selection_window.title("Choose a language!")
selection_window.config(padx=20, pady=20)


fr = Button(text="French", highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=lambda: set_language("French"))
fr.grid(column=0, row=0)

es = Button(text="Spanish", highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=lambda: set_language("Spanish"))
es.grid(column=1, row=0)

de = Button(text="German", highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=lambda: set_language("German"))
de.grid(column=0, row=1)

ko = Button(text="Korean", highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=lambda: set_language("Korean"))
ko.grid(column=1, row=1)

it = Button(text="Italian", highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=lambda: set_language("Italian"))
it.grid(column=0, row=2)

selection_window.mainloop()