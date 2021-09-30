from tkinter import *
window = Tk()
window.title("MAIL System")
window.config(width=640, height=480, padx=20, pady=20)

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

message_entry = Text(height=5, width=40)
message_entry.focus()
message_entry.insert(END, "Type your message here")
message_entry.grid(row=4, column=0, columnspan=2)

send_button = Button(text="Send")
send_button.grid(row=5,column=0)

window.mainloop()
