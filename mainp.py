import tkinter as tk
import random

# Setup main window
root = tk.Tk()
root.title("🧠 Memory Matching Game")
root.geometry("400x400")

# Prepare cards
emojis = ['🍎', '🚗', '🐶', '🎵', '🌟', '🍩', '🐱', '⚽']
cards = emojis * 2
random.shuffle(cards)

buttons = []
flipped = []
matched_indices = []

def flip_card(i):
    global flipped, matched_indices

    if i in matched_indices or len(flipped) == 2:
        return

    buttons[i].config(text=cards[i])
    flipped.append((i, buttons[i]))

    if len(flipped) == 2:
        root.after(800, check_match)

def check_match():
    global flipped, matched_indices

    i1, b1 = flipped[0]
    i2, b2 = flipped[1]

    if cards[i1] == cards[i2]:
        matched_indices.extend([i1, i2])
    else:
        b1.config(text="")
        b2.config(text="")

    flipped = []

    if len(matched_indices) == len(cards):
        win_label = tk.Label(root, text="🎉 You Won!", font=("Helvetica", 16), fg="green")
        win_label.place(relx=0.5, rely=0.95, anchor="center")

# Create buttons
for i in range(16):
    btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 20),
                    command=lambda i=i: flip_card(i))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()
