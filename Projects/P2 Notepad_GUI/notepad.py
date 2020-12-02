from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import time
import os


class Notepad:

    root = Tk()
    width = 300
    height = 300
    textarea = Text(root, undo=True)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    statsmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    # scroll bar
    scroll = Scrollbar(textarea)
    file = None

    def __init__(self):
        self.root.title("Untitled - Notepad")
        self.root.geometry("300x300")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.textarea.grid(sticky=N + E + S + W)

        # Adding in file menu

        self.filemenu.add_command(
            label="New", compound=LEFT, accelerator='Ctrl + N', command=self.newFile)
        self.filemenu.add_command(
            label="Open", compound=LEFT, accelerator='Ctrl + O', command=self.openFile)
        self.filemenu.add_command(
            label="Save", compound=LEFT, accelerator='Ctrl + S', command=self.saveFile)
        self.filemenu.add_command(label="Save As", compound=LEFT,
                                  accelerator='Ctrl + Shift + S', command=self.saveasFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Exit", compound=LEFT, accelerator='Ctrl + Q', command=self.exitApp)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Adding edit menu

        self.editmenu.add_command(
            label="Undo", compound=LEFT, accelerator='Ctrl + Z', command=self.undo)
        self.editmenu.add_command(
            label="Redo", compound=LEFT, accelerator='Ctrl + Y', command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(
            label="Cut", compound=LEFT, accelerator='Ctrl + C', command=self.cut)
        self.editmenu.add_command(
            label="Copy", compound=LEFT, accelerator='Ctrl + X', command=self.copy)
        self.editmenu.add_command(
            label="Paste", compound=LEFT, accelerator='Ctrl + V', command=self.paste)
        self.editmenu.add_command(
            label="Select All", compound=LEFT, accelerator='Ctrl + A', command=self.select_all)
        self.editmenu.add_separator()
        self.editmenu.add_command(
            label="Find", compound=LEFT, accelerator='Ctrl + F', command=self.find_text)
        self.editmenu.add_command(label="Replace", compound=LEFT,
                                  accelerator='Ctrl + H', command=self.find_and_replace)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Adding stats menu

        self.statsmenu.add_command(label="Word Count", command=self.word_count)
        self.statsmenu.add_command(label="Char Count", command=self.char_count)
        self.statsmenu.add_command(
            label="Created Time", command=self.created_time)
        self.statsmenu.add_command(
            label="Modified Time", command=self.modified_time)
        self.menubar.add_cascade(label="Stats", menu=self.statsmenu)

        # Adding help menu

        self.helpmenu.add_command(
            label="About Notepad", command=self.aboutNotepad)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scroll.set)

    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.textarea.delete(1.0, END)

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[
                                    ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.textarea.delete(1.0, END)
            fh = open(self.file, "r")
            self.textarea.insert(1.0, fh.read())
            fh.close()

    def saveFile(self):
        try:
            f = open(self.file, "w")
            f.write(self.textarea.get(1.0, END))
            f.close()
        except:
            self.saveasFile()

    def saveasFile(self):
        try:
            if self.file == None:
                self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                              ("All Files", "*.*"), ("Text Documents", "*.txt")])
                if self.file == "":
                    self.file = None
                else:
                    f = open(self.file, "w")
                    f.write(self.textarea.get(1.0, END))
                    f.close()
                    self.root.title(os.path.basename(self.file) + " - Notepad")
            else:
                self.file = asksaveasfilename(initialfile=self.file, defaultextension=".txt", filetypes=[
                                              ("All Files", "*.*"), ("Text Documents", "*.txt")])
                f = open(self.file, "w")
                f.write(self.textarea.get(1.0, END))
                f.close()
                self.root.title(os.path.basename(self.file) + " - Notepad")
        except:
            pass

    def exitApp(self):
        self.root.destroy()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def undo(self):
        self.textarea.event_generate("<<Undo>>")

    def redo(self):
        self.textarea.event_generate("<<Redo>>")

    def select_all(self):
        self.textarea.tag_add('sel', '1.0', 'end')

    def find_text(self):
        find_window = Toplevel(self.root)
        find_window.title("Find")
        find_window.geometry("300x80")
        find_window.transient(self.root)
        Label(find_window, text="Find All: ").grid(row=0, column=0, sticky='e')
        v = StringVar()
        e = Entry(find_window, width=25, textvariable=v)
        e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        e.focus_set()
        c = IntVar()
        Checkbutton(find_window, text="Ignore Case", variable=c).grid(
            row=1, column=1, sticky='e', padx=2, pady=2)
        Button(find_window, text="Find All", command=lambda: self.search_for(
            v.get(), c.get(), find_window, e)).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=2)

        def close_search():
            self.textarea.tag_remove('match', '1.0', END)
            find_window.destroy()

        find_window.protocol('WM_DELETE_WINDOW', close_search)

    def search_for(self, v, c, find_window, e):
        self.textarea.tag_remove('match', '1.0', END)
        count = 0
        if v:
            pos = '1.0'
            while True:
                pos = self.textarea.search(v, pos, nocase=c, stopindex=END)
                if not pos:
                    break
                lastpos = '{} + {}c'.format(pos, len(v))
                self.textarea.tag_add('match', pos, lastpos)
                count += 1
                pos = lastpos
        self.textarea.tag_config('match', foreground='blue', background='pink')
        e.focus_set()
        find_window.title('{} matches found' .format(count))

    def find_and_replace(self):
        find_replace_window = Toplevel(self.root)
        find_replace_window.title("Find and Replace")
        find_replace_window.geometry("350x100")

        Label(find_replace_window, text="Find: ").grid(
            row=0, column=0, sticky='e')
        find_var = StringVar()
        replace_var = StringVar()
        find_entry_widget = Entry(
            find_replace_window, width=25, textvariable=find_var)
        find_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        find_entry_widget.focus_set()
        Label(find_replace_window, text="Replace With: ").grid(
            row=1, column=0, sticky='e')
        replace_entry_widget = Entry(
            find_replace_window, width=25, textvariable=replace_var)
        replace_entry_widget.grid(row=1, column=1, padx=2, pady=2, sticky='we')
        case = IntVar()
        Checkbutton(find_replace_window, text="Ignore Case", variable=case).grid(
            row=2, column=1, padx=2, pady=2, sticky='e')
        Button(find_replace_window, text="Find", command=lambda: self.find_for_replace(find_var.get(), case.get(
        ), find_replace_window, find_entry_widget)).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=2)
        Button(find_replace_window, text="Replace with", command=lambda: self.replace_with(find_var.get(), replace_var.get(), case.get(
        ), find_replace_window, find_entry_widget, replace_entry_widget)).grid(row=1, column=2, sticky='e'+'w', padx=2, pady=2)

    def find_for_replace(self, v, c, find_replace_window, e):
        self.textarea.tag_remove('found', '1.0', END)
        count = 0
        if v:
            pos = '1.0'
            while True:
                pos = self.textarea.search(v, pos, nocase=c, stopindex=END)
                if not pos:
                    break
                lastpos = '{} + {}c'.format(pos, len(v))
                self.textarea.tag_add('found', pos, lastpos)
                count += 1
                pos = lastpos
        self.textarea.tag_config('found', foreground='red', background='blue')
        e.focus_set()
        find_replace_window.title('{} matches found' .format(count))

    def replace_with(self, find_var, replace_var, case, find_replace_window, find_entry_widget, replace_entry_widget):
        self.textarea.tag_remove('found', '1.0', END)
        count = 0
        if (find_var, replace_var):
            pos = '1.0'
            while True:
                pos = self.textarea.search(
                    find_var, pos, nocase=case, stopindex=END)
                if not pos:
                    break
                lastpos = '{} + {}c'.format(pos, len(find_var))
                self.textarea.delete(pos, lastpos)
                self.textarea.insert(pos, replace_var)
                lastpos = '{} + {}c'.format(pos, len(replace_var))
                self.textarea.tag_add('found', pos, lastpos)
                count += 1
                pos = lastpos
        self.textarea.tag_config(
            'found', foreground='green', background='pink')
        find_entry_widget.focus_set()
        find_replace_window.title(
            '{} strings of {} are replaced with {}'.format(count, find_var, replace_var))

    def word_count(self):
        f = open(self.file, 'r')
        text_string = f.read()
        word_list = text_string.split(' ')
        ans = "The number of words present in this file are: " + \
            str(len(word_list))
        showinfo("Word count of the text in this file", ans)
        f.close()

    def char_count(self):
        f = open(self.file, 'r')
        text_string = f.read()
        ans = "The number of characters, including spaces and new lines, present in this file are: " + \
            str(len(text_string)-1)
        showinfo("Character count of the file", ans)
        f.close()

    def created_time(self):
        created_time = time.ctime(os.path.getctime(self.file))
        showinfo("Created time of this file", created_time)

    def modified_time(self):
        modified_time = time.ctime(os.path.getmtime(self.file))
        showinfo("Modified time of this file", modified_time)

    def aboutNotepad(self):
        showinfo("NotePad", "This Notepad is Created by Anonymous Shadow Masters")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    notepad = Notepad()
    notepad.run()
