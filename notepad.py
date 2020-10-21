from tkinter import Tk, Menu, Scrollbar, Text, END, ttk, font, BooleanVar, Toplevel, Label, Button, Frame
from tkinter.messagebox import showinfo, showerror
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
import smtplib
from email.message import EmailMessage
import os

if __name__ == '__main__':
    root = Tk()
    root.geometry("1100x600")
    root.title("Untitled : Surya-Notepad")
    # root.wm_iconbitmap("icon_name.ico") # add your icon

    fontExample = font.Font(family="Arial", size=13, slant="italic")

    scroll = Scrollbar(root)
    scroll.pack(side='right', fill='y')

    TextArea = Text(root, yscrollcommand=scroll.set)
    TextArea.pack(expand=True, fill='both')
    TextArea.configure(font=fontExample, padx=10, pady=5)
    scroll.config(command=TextArea.yview)

    file = None

    def new_file():
        global file
        root.title("Untitled : Surya-Notepad")
        file = None
        TextArea.delete(1.0, END)

    def open_file():
        try:
            global file
            file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                root.title(os.path.basename(file) + " : Surya-Notepad")
                TextArea.delete(1.0, END)
                f = open(file, "r")
                TextArea.insert(1.0, f.read())
                f.close()
        except UnicodeDecodeError:
            showerror("Error!", "Cannot open files of this format")
            f.close()
            file = None
            root.title("Untitled : Surya-Notepad")

    def save_file():
        global file
        if file is None:
            file = asksaveasfilename(initialfile="Untitled.txt",
                                     defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"), ('Python Files', '*.py'), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + ' : Surya-Notepad')

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def save_as(): 
        global file
        filetype = [('All Files', '*.*'),  
                ('Python Files', '*.py'), 
                ('Text Document', '*.txt')] 
        file = asksaveasfilename(filetypes = filetype, defaultextension = filetype)
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + ' : Surya-Notepad')
        
    def cut():
        TextArea.event_generate("<<Cut>>")

    def copy():
        TextArea.event_generate("<<Copy>>")

    def paste():
        TextArea.event_generate("<<Paste>>")

    def dark_mode():
        global TextArea, dark_bg, root
        if dark_bg.get() == True :
            TextArea.configure(bg='#444444', fg='#fff', insertbackground='white')
            FileMenu.configure(bg='#444444', fg='#fff', bd=0)
            EditMenu.configure(bg='#444444', fg='#fff', bd=0)
            HelpMenu.configure(bg='#444444', fg='#fff', bd=0)
        else :
            TextArea.configure(bg='#fff', fg='#000', insertbackground='black')
            FileMenu.configure(bg='#fff', fg='#000')
            EditMenu.configure(bg='#fff', fg='#000')
            HelpMenu.configure(bg='#fff', fg='#000')
            

    def about_file():
        showinfo("Surya-Notepad", "This is a simple text editing software created using tkinter library of python language")

    def send_feedback():
        top = Toplevel(root) 
        top.title("Send Feedback")
        top.geometry("400x280")
        top.maxsize(400, 280)

        label = Label(top, text="Message", bg="white", fg="#152238", padx=10, pady=8, font="comicsansns 15 bold")
        label.pack(side='top', fill='x')

        frame = Frame(top, borderwidth=1, relief="sunken", bg="#152238")
        frame.pack(side="top", anchor="nw", fill='both')

        label = Label(frame, text="Enter your email :", fg="white", bg="#152238", font="comicsansns 8 bold")
        label.pack(side='top', fill='x', padx=15, pady=3)

        sender_email = Text(frame, padx=10, pady=5, height=1, width=50, font="comicsansns 10")
        sender_email.pack(fill='x', side='top', padx=15, pady=8)

        label = Label(frame, text="Enter your feedback :", fg="white", bg="#152238", font="comicsansns 8 bold")
        label.pack(side='top', fill='x', padx=15)

        feedback = Text(frame, padx=10, pady=5, height=5, width=50, font="comicsansns 10")
        feedback.pack(fill='x', side='top', padx=15, pady=10)

        def email():
            email = EmailMessage()
            email['from'] = 'yahoo_email@yahoo.com'
            email['to'] = 'yahoo_email@yahoo.com'
            email['subject'] = 'Feedback : Surya-Notepad'
            email.set_content("Sender Email : " + sender_email.get(1.0, END) + "\n\nFeedback : " + feedback.get(1.0, END))
            try:
	            with smtplib.SMTP(host='smtp.mail.yahoo.com', port=587) as smtp:
		            smtp.ehlo()
		            smtp.starttls()
		            smtp.login('yahoo_email@yahoo.com', 'password')
		            smtp.send_message(email)
		            print('All Good')
            except OSError:
	            showerror("Network Problem", "Error sending message!")
            except Exception:
                showerror("Unknown Error", "Cannot send message!")

        button = Button(frame, fg="#152238", bg="white", padx=5, pady=5, text="Send Message",font="comicsansns 10 bold", command=email)
        button.pack(side='bottom', padx=10)

    MenuBar = Menu(root, bg='#444444', fg='#fff')
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=new_file)
    FileMenu.add_command(label="Open", command=open_file)
    FileMenu.add_command(label="Save", command=save_file)
    FileMenu.add_command(label="Save As", command=save_as)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    dark_bg = BooleanVar()
    dark_bg.set(False)
    EditMenu.add_checkbutton(label="Dark Bg", onvalue=1, offvalue=0, variable=dark_bg, command=dark_mode)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about_file)
    HelpMenu.add_command(label="Feedback", command=send_feedback)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    root.mainloop()
