from tkinter import Tk, Frame, Label, Entry, Text, Button, END, StringVar, Toplevel, Radiobutton, IntVar
from tkinter.messagebox import showerror, showinfo
import smtplib
from email.message import EmailMessage

def check_info():
    if receiver_email.get() == "":
        showerror(
            "Empty Field", "Cannot send messsage.\nEmail-Address field is empty!")
    elif text.get(1.0, END) == "\n":
        showerror("Empty Field", "Cannot send empty message!")
    else:
        email()


def email():
    email = EmailMessage()
    email['from'] = sender_email.get()
    email['to'] = receiver_email.get()
    email['subject'] = email_subject.get()
    email.set_content(text.get(1.0, END))

    if account_type.get() == 1:
        smtp_host = 'smtp.gmail.com'
        smtp_port = 465
    elif account_type.get() == 2:
        smtp_host = 'smtp.mail.yahoo.com'
        smtp_port = 587
    else:
        showinfo("No Email Set", "Set sender's email under Reset-Email option below")

    try:
        with smtplib.SMTP(host=smtp_host, port=smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender_email.get(), sender_password.get())
            smtp.send_message(email)
            showinfo(
                "Message Sent", "Thank you for using our service!")
    except UnboundLocalError:
        pass
    except smtplib.SMTPRecipientsRefused:
        showerror("Wrong Email", "Enter a valid email address!")
    except OSError:
        showerror("Network Problem", "Error sending message!")
    except Exception:
        showerror("Unknown Error", "Cannot send message!")

def clear():
    receiver_email.set("")
    email_subject.set("")
    text.delete(1.0, END)

def reset():
    top = Toplevel(root)
    top.title("Reset Email")
    top.geometry("350x280")
    top.maxsize(350, 280)

    def set_email():
        if account_type.get() == 0 or sender_email.get() == "" or sender_password.get() == "":
            showerror("Field Missing", "Please fill all the fields")
        else:
            account_type.set(account_type.get())
            sender_email.set(sender_email.get())
            sender_password.set(sender_password.get())
            top.destroy()

    top_frame = Frame(top, borderwidth=1, relief="sunken")
    top_frame.pack(side="top", anchor="nw", fill='both', expand=True)
    top_frame.configure(bg="#b3f2d2")

    top_label1 = Label(top_frame, text="Reset Email", font="comicsansns 15 bold")
    top_label1.pack(side="top", fill="x")
    top_label1.configure(bg="#83f2b9", fg="#152238")

    top_label2 = Label(top_frame, text="Email :", font="comicsansns 10 bold")
    top_label2.pack(side="top", anchor="nw", padx=20, pady=7)
    top_label2.configure(bg="#b3f2d2", fg="#152238")

    top_entry1 = Entry(top_frame, font="comicsansns 10 bold", textvariable=sender_email)
    top_entry1.pack(side="top", fill="x", padx=20)

    top_label3 = Label(top_frame, text="Password :", font="comicsansns 10 bold")
    top_label3.pack(side="top", anchor="nw", padx=20, pady=7)
    top_label3.configure(bg="#b3f2d2", fg="#152238")

    top_entry2 = Entry(top_frame, font="comicsansns 10 bold", textvariable=sender_password)
    top_entry2.pack(side="top", fill="x", padx=20)

    top_label4 = Label(top_frame, text="Account Type :", font="comicsansns 10 bold")
    top_label4.pack(side="top", anchor="nw", padx=20, pady=7)
    top_label4.configure(bg="#b3f2d2", fg="#152238")

    radio1 = Radiobutton(top_frame, text="Gmail", variable=account_type, value=1)
    radio1.pack(side="top", padx=20, anchor="nw")
    radio1.configure(bg="#b3f2d2", fg="#152238", font="comicsansns 10 bold")
    radio2 = Radiobutton(top_frame, text="Yahoo", variable=account_type, value=2)
    radio2.pack(side="top", padx=20, anchor="nw")
    radio2.configure(bg="#b3f2d2", fg="#152238", font="comicsansns 10 bold")

    top_button = Button(top_frame, text="Set Email", padx=15, pady=1, fg="#fff", bg="#152238", font="comicsansns 10 bold", command=set_email)
    top_button.pack(side="top", pady=10)

    
root = Tk()
root.title("Email")
root.geometry("450x350")
root.maxsize(450, 350)

account_type = IntVar()
account_type.set(0)
sender_email = StringVar()
sender_password = StringVar()
receiver_email = StringVar()
email_subject = StringVar()

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

entry1 = Entry(frame, font="comicsansns 10",
               fg="#152238", textvariable=receiver_email)
entry1.pack(side='top', fill='x', padx=20)

label3 = Label(frame, text="Subject :", font="comicsansns 10 bold")
label3.pack(side='top', fill='x', pady=5)
label3.configure(bg="#b3f2d2", fg="#152238")

entry2 = Entry(frame, font="comicsansns 10",
               fg="#152238", textvariable=email_subject)
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

button1 = Button(frame2, padx=2, pady=3, text="Send Message",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=check_info)
button1.pack(side='left', padx=20, pady=5)

button2 = Button(frame2, padx=20, pady=3, text="Clear All",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=clear)
button2.pack(side='left',  padx=20, pady=5)

button3 = Button(frame2, padx=15, pady=3, text="Reset Email",
                font="comicsansns 10 bold", fg="#fff", bg="#152238", command=reset)
button3.pack(side='left',  padx=20, pady=5)

root.mainloop()
