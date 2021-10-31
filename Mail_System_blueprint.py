from tkinter import *
from tkinter import messagebox
import smtplib
import pandas

data = pandas.read_csv("squirrel_count.csv")

window = Tk()
window.title("MAIL System")
window.config(width=640, height=480, padx=20, pady=20)
mail_addr = ""
passwd = ""

#--------UI Elements--------#

#Labels
logo_text = Label(text="Mail System", font=("Arial", 32, "bold"), fg="blue")
logo_text.grid(row=0, column=1)
from_mail_label = Label(text="Email Address", font=("Arial", 12, "bold"), fg="blue")
from_mail_label.grid(row=1, column=0)
to_mail_label = Label(text="Password", font=("Arial", 12, "bold"), fg="blue")
to_mail_label.grid(row=2, column=0)

#Entries
to_mail_label_entry = Entry(width=30, show="*")
to_mail_label_entry.grid(row=2, column=1)
from_mail_label_entry = Entry(width=30)
from_mail_label_entry.grid(row=1, column=1)

#Functions

def send_msg():
    recepient = to_mail_label_entry.get()
    print(recepient)
    messg = message_entry.get("1.0", END)
    print(messg)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail_addr, password=passwd)
        connection.sendmail(from_addr=mail_addr, to_addrs=recepient, msg=messg)

def login():
    global mail_addr
    global passwd
    global message_entry
    mail_addr = from_mail_label_entry.get()
    passwd = to_mail_label_entry.get()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        try:
            connection.login(user=mail_addr, password=passwd)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure you have allowed"
            " your account to use SMTP and you are entering the correct details.")
        else:
            from_mail_label.config(text="From:")
            to_mail_label_entry.delete(0, "end")
            to_mail_label_entry.config(show="")
            to_mail_label.config(text="To:")
            login_button.config(image=send_img, command=send_msg)
            login_button.grid(row=5,column=0)
            print(data)
            message_entry = Text(height=5, width=60)
            message_entry.focus()
            message_entry.insert(END, "Type your message here")
            message_entry.grid(row=4, column=0, columnspan=2)



#Buttons
send_img = PhotoImage(file="send_img.png")
login_img = PhotoImage(file="login_img.png")
login_button = Button(image=login_img, command=login, highlightthickness=0)
login_button.grid(row=3, column=0)




window.mainloop()
