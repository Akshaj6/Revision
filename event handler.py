from tkinter import *
window = Tk()
window.title("EVent Handler")
window.geometry("100x100")
def handle_keypress(event):
    """"Print the character associated with the key that is pressed"""
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nLes go the button was clicked!")
button = Button(text="I need to be clicked!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()