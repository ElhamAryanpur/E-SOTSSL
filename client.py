from requests import post
from random import randint
from tkinter import Tk, Button, Entry, Label, font, END
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from os.path import basename
import file_ext

class Client():
    def __init__(self):
        self.file_name = "GOALS"
        self.salt = "T#3-CR34T0R"
        self.url = "http://127.0.0.1:5000"

    def run(self):
        try:
            with open(self.file_name, "r") as f:
                d = f.readlines()

            read = "".join(d)

        except FileNotFoundError:
            print("FILE {} NOT FOUND!".format(self.file_name))

        f = file_ext.FileStuff()
        f.level = randint(0, 1000000000000)
        salt = f.encrypt_salt(self.salt)
        data = f.encrypt_string(salt, str(read))

        place = randint(0, len(data))
        data = data[:place] + "<{} {} {}>".format(f.level, self.salt, self.file_name) + data[place:]

        f.level = 38245
        salt = f.encrypt_salt("Suck on this!5")
        data = f.encrypt_string(salt, data)

        data = data.encode('utf-8')
        print("SENDING...")
        try:
            post(self.url, data)
            print("SENT!")
            return True
        except Exception:
            return False

if __name__ == "__main__":
    root = Tk()

    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb   

    def load_file():
        fname = askopenfilename()
        if fname:
            try:
                load_entry.delete(0, END)
                load_entry.insert(0, fname)
            except Exception as e:
                showerror("Open Source File", e)
    
    def send_to_server():
        p = load_entry.get()
        p = basename(p)
        c = Client()
        c.file_name = p
        c.salt = salt.get()
        c.url = url.get()
        process = c.run()
        if process:
            showinfo("SUCCESS!", "FILE HAS BEEN SENT SUCCESSFULLY")
        else:
            showerror("FAILED", "FILE HAS NOT BEEN SENT... POSSIBLY SERVERSIDE PROBLEM!")

    root.maxsize(500,300)
    root.minsize(500,300)
    root.title("E-SOTSSL Client")
    root.configure(background=_from_rgb((39, 79, 97)))

    fnt = font.Font(weight="bold", size=15)
    fg = "#6AAAC9"
    bg = "#2E5A6F"

    load_label = Label(text="BROWSE THE FILE: ", fg=fg, bg=bg, font=fnt)
    load = Button(text="OPEN FILE", command=load_file, fg=fg, bg=bg, font=fnt, border=0)
    load_entry = Entry(fg=fg, bg=bg, font=fnt, border=0)

    salt_label = Label(text="SALT: ", fg=fg, bg=bg, font=fnt)
    salt = Entry(fg=fg, bg=bg, font=fnt, border=0)

    url_label = Label(text="URL: ", fg=fg, bg=bg, font=fnt)
    url = Entry(fg=fg, bg=bg, font=fnt, border=0)

    send = Button(text="SEND", command=send_to_server, fg=fg, bg=bg, font=fnt, border=0)

    load_label.place(x=10, y=25)
    load.place(x=250, y=20)
    load_entry.place(x=20, y=70, width=460)
    salt_label.place(x=10, y=120)
    salt.place(x=100, y=120, width=350)
    url_label.place(x=10, y=170)
    url.place(x=100, y=170, width=350)
    send.place(x=200, y=230, height=50, width=100)

    salt.insert(END, "T#3-CR34T0R")
    url.insert(END, "http://127.0.0.1:5000")

    root.mainloop()