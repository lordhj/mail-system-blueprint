from tkinter import *
from tkinter import messagebox
import smtplib
window = Tk()
window.title("MAIL System")
window.config(width=640, height=480, padx=20, pady=20)

#--------UI Elements--------#

#Labels
logo_text = Label(text="Mail System", font=("Arial", 22, "bold"), fg="blue")
logo_text.grid(row=0, column=1)
from_mail_label = Label(text="Email Address")
from_mail_label.grid(row=1, column=0)
to_mail_label = Label(text="Password")
to_mail_label.grid(row=2, column=0)

#Entries
to_mail_label_entry = Entry(width=30)
to_mail_label_entry.grid(row=2, column=1)
from_mail_label_entry = Entry(width=30)
from_mail_label_entry.grid(row=1, column=1)
message_entry = Text(height=5, width=40)
message_entry.focus()
message_entry.insert(END, "Type your message here")
message_entry.grid(row=4, column=0, columnspan=2)

#Functions
def login():
    mail_addr = from_mail_label_entry.get()
    passwd = to_mail_label_entry.get()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        try:
            connection.login(user=mail_addr, password=passwd)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure you have allowed"
            " you account to use SMTP and you are entering the correct details.")


#Buttons
login_button = Button(text="Login", command=login)
login_button.grid(row=3, column=0)
send_button = Button(text="Send")
send_button.grid(row=5,column=0)


window.mainloop()
