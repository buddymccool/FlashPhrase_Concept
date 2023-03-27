# import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
language = None
word_data = None
words_dict = {}

# -------------- DATA SETUP --------------- #


def cards_setup(x):
    selection_window.destroy()
    global language, word_data, words_dict
    try:
        with open(f"data/{x}_words_to_learn.csv") as f:
            word_data = pandas.read_csv(f)
            if word_data.empty:
                messagebox.showinfo(title="No more words to learn!", message="There are no words left in your list of words to learn. See if you can remember them all!")
                raise FileNotFoundError
    except FileNotFoundError:
        with open(f"data/{x}_words.csv") as f:
            word_data = pandas.read_csv(f)
    finally:
        words_dict = word_data.to_dict(orient="records")
        language = x

# --------------- FUNCTIONS --------------#


def get_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text=f"{language}", fill="black")
    canvas.itemconfig(card_word, text=current_card[language], fill="black")
    canvas.itemconfig(canvas_background, image=card_front)
    flip_timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=card_back)


def known_word():
    words_dict.remove(current_card)
    new_data = pandas.DataFrame(words_dict)
    new_data.to_csv(f"data/{language}_words_to_learn.csv", index=False)
    get_words()


def center_window(win, x_dim, y_dim):
    scr_x = win.winfo_screenwidth()
    scr_y = win.winfo_screenheight()
    x_cor = int((scr_x / 2) - (x_dim/2))
    y_cor = int((scr_y / 2) - (y_dim/2))
    win.geometry(f'{x_dim}x{y_dim}+{x_cor}+{y_cor-100}')


# ----------------- UI SETUP ----------------- #=
selection_window = Tk()
selection_window.title("Choose a language!")
selection_window.config(padx=20, pady=20)
center_window(selection_window, 220, 125)
# selection_window.eval('tk::PlaceWindow %s center' % selection_window.winfo_pathname(selection_window.winfo_id()))

fr = Button(text="French", command=lambda: cards_setup("French"))
fr.grid(column=0, row=0)

es = Button(text="Spanish", command=lambda: cards_setup("Spanish"))
es.grid(column=1, row=0)

de = Button(text="German", command=lambda: cards_setup("German"))
de.grid(column=0, row=1)

ko = Button(text="Korean", command=lambda: cards_setup("Korean"))
ko.grid(column=1, row=1)

it = Button(text="Italian", command=lambda: cards_setup("Italian"))
it.grid(column=0, row=2)

selection_window.mainloop()

# -------- MAIN WINDOW -------#
window = Tk()
window.title(f"learm {language}")
window.config(padx=30, pady=50, bg=BACKGROUND_COLOR)
center_window(window, 850, 750)

flip_timer = window.after(3000, card_flip)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)

card_back = PhotoImage(file="images/card_back.png")
correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

known_b = Button(image=correct, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
unknown_b = Button(image=wrong, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=get_words)
known_b.grid(column=1, row=1)
unknown_b.grid(column=0, row=1)

get_words()

window.mainloop()

# next steps:
# test for nicer/cleaner gui with ttk
# import library of common phrases in each language
