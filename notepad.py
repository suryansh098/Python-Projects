from tkinter import Tk, Menu, Scrollbar, Text, END, ttk, font
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
from ttkthemes import ThemedStyle
import os

if __name__ == '__main__':
    root = Tk()
    root.geometry("800x400")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("bolt.ico")
    root.configure(bg='black')

    style = ThemedStyle(root)
    style.set_theme("blue")

    fontExample = font.Font(family="Arial", size=13, slant="italic")

    # For normal white background :
    scroll = Scrollbar(root)
    scroll.pack(side='right', fill='y')
    TextArea = Text(root, yscrollcommand=scroll.set)
    TextArea.pack(expand=True, fill='both')
    TextArea.configure(font=fontExample, padx=10, pady=5)

    # For dark background :
    # scroll = ttk.Scrollbar(root)
    # scroll.pack(side='right' ,fill='y')
    # TextArea = Text(root, yscrollcommand=scroll.set, bg='#152238', fg='#fff')
    # TextArea.configure(insertbackground='white', font=fontExample, padx=10, pady=5)
    # TextArea.pack(expand=True, fill='both')

    file = None

    scroll.config(command=TextArea.yview)

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
            showinfo("Error!", "Cannot open files of this format")
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
        pass

    def about_file():
        showinfo("Surya-Notepad", "This is a simple text editing software created using tkinter library of python language")

    MenuBar = Menu(root, bg='#444444', fg='#fff')
    FileMenu = Menu(MenuBar, tearoff=0, bg='#444444', fg='#fff')
    FileMenu.add_command(label="New", command=new_file)
    FileMenu.add_command(label="Open", command=open_file)
    FileMenu.add_command(label="Save", command=save_file)
    FileMenu.add_command(label="Save As", command=save_as)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0, bg='#444444', fg='#fff')
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Dark Bg", command=dark_mode)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0, bg='#444444', fg='#fff')
    HelpMenu.add_command(label="About", command=about_file)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    root.mainloop()
