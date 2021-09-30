from tkinter import *
window = Tk()
window.title("MAIL System")
window.config(width=640, height=480)

#--------UI Elements--------#

logo_text = Label(text="Mail System", font=("Arial", 22, "bold"), fg="blue")
logo_text.grid(row=0, column=1)
from_mail_label = Label(text="Email Address")
from_mail_label.grid(row=1, column=0)
from_mail_label_entry = Entry()
from_mail_label_entry.grid(row=1, column=1)
to_mail_label = Label(text="Password")
to_mail_label.grid(row=2, column=0)
to_mail_label_entry = Entry()
to_mail_label_entry.grid(row=2, column=1)

#Buttons
login_button = Button(text="Login")
login_button.grid(row=3, column=0)

window.mainloop()
