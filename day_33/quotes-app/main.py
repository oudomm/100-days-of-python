from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    quote = data[0]["q"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Random Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click to get a random quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

button_img = PhotoImage(file="random-button.png")
random_button = Button(image=button_img, highlightthickness=0, command=get_quote)
random_button.grid(row=1, column=0)


window.mainloop()
