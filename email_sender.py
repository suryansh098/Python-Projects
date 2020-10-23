from tkinter import Tk, Frame, Label, Entry, Text, Button, END, StringVar
from tkinter.messagebox import showerror, showinfo
import smtplib
from email.message import EmailMessage


def check_validity():
    if entered_email.get() == "":
        showerror(
            "Empty Field", "Cannot send messsage.\nEmail-Address field is empty!")
    elif text.get(1.0, END) == "\n":
        showerror("Empty Field", "Cannot send empty message!")
    else:
        email()


def email():
    email = EmailMessage()
    email['from'] = 'your-email'
    email['to'] = entered_email.get()
    email['subject'] = entered_subject.get()
    email.set_content(text.get(1.0, END))
    try:
        with smtplib.SMTP(host='smtp.mail.yahoo.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('your-email@yahoo.com', 'your-password')
            smtp.send_message(email)
            showinfo(
                "Message Sent", "Thank you for using our service!")
    except smtplib.SMTPRecipientsRefused:
        showerror("Wrong Email", "Enter a valid email address!")
    except OSError as e:
        print(e)
        showerror("Network Problem", "Error sending message!")
    except Exception as e:
        showerror("Unknown Error", "Cannot send message!")
        print(e)

def clear():
    entered_email.set("")
    entered_subject.set("")
    text.delete(1.0, END)

def reset():
    print("hello")
    
root = Tk()
root.title("Email")
root.geometry("450x350")
root.maxsize(450, 350)

frame = Frame(root, borderwidth=1, relief="sunken")
frame.pack(side="top", anchor="nw", fill='both', expand=True)
frame.configure(bg="#b3f2d2")

label1 = Label(frame, text="Send Email Using Python",
               font="comicsansns 15 bold")
label1.pack(side='top', fill='x')
label1.configure(bg="#83f2b9", fg="#152238")

label2 = Label(frame, text="Receiver's Email Address :",
               font="comicsansns 10 bold")
label2.pack(side='top', fill='x', pady=5)
label2.configure(bg="#b3f2d2", fg="#152238")

entered_email = StringVar()
entry1 = Entry(frame, font="comicsansns 10",
               fg="#152238", textvariable=entered_email)
entry1.pack(side='top', fill='x', padx=20)

label3 = Label(frame, text="Subject :", font="comicsansns 10 bold")
label3.pack(side='top', fill='x', pady=5)
label3.configure(bg="#b3f2d2", fg="#152238")

entered_subject = StringVar()
entry2 = Entry(frame, font="comicsansns 10",
               fg="#152238", textvariable=entered_subject)
entry2.pack(side='top', fill='x', padx=20)

label4 = Label(frame, text="Message :", font="comicsansns 10 bold")
label4.pack(side='top', fill='x', pady=5)
label4.configure(bg="#b3f2d2", fg="#152238")

text = Text(frame, padx=5, pady=5, height=7, width=50,
            font='comicsansns 10', bd=2, fg="#152238")
text.pack(side='top', fill='x', padx=20)

frame2 = Frame(frame, borderwidth=1, relief="sunken")
frame2.pack(side="bottom", fill='both', expand=True)
frame2.configure(bg="#b3f2d2", bd=0)

button1 = Button(frame2, padx=3, pady=3, text="Send Message",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=check_validity)
button1.pack(side='left', padx=20, pady=5)

button2 = Button(frame2, padx=3, pady=3, text="Reset Email",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=reset)
button2.pack(side='left',  padx=20, pady=5)

button3 = Button(frame2, padx=3, pady=3, text="Clear All",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=clear)
button3.pack(side='left',  padx=20, pady=5)


root.mainloop()
