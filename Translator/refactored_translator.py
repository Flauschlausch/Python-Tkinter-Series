from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import os


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def start_translator():
    root_class = tk.Toplevel()
    logo_1_class = resource_path("translator.png")
    app_class = Application(logo_1_class, master=root_class)
    app_class.master.title("Translator")
    app_class.master.iconbitmap(resource_path("Logo.ico"))
    app_class.master.resizable(False, False)
    app_class.mainloop()


class Application(tk.Frame):
    def __init__(self, logo, master=None):
        super().__init__(master)
        self.master = master
        self.master['relief'] = SUNKEN
        self.master['bd'] = 2
        self.master['bg'] = "#89959f"
        self.master['pady'] = 2
        self.master['padx'] = 2
        self.pack()

        self.logo = logo
        img = tk.PhotoImage(file=self.logo)
        self.label = tk.Label(self, image=img)
        self.label.image = img
        self.label.grid(row=0, column=0, columnspan=2, sticky="news", pady=(2, 0))

        self.a = tk.StringVar(self)
        self.auto_detect = ttk.Combobox(self, width=20, textvariable=self.a, state='readonly',
                                        font=('verdana', 10, 'bold'), )

        self.auto_detect['values'] = (
            'Auto Detect',
        )

        self.auto_detect.grid(row=1, column=0, sticky="ew", pady=(2, 0))
        self.auto_detect.current(0)

        self.lang = tk.StringVar(self)
        self.choose_language = ttk.Combobox(self, width=20, textvariable=self.lang, state='readonly',
                                            font=('verdana', 10, 'bold'))

        self.choose_language['values'] = (
            'Afrikaans',
            'Albanian',
            'Arabic',
            'Armenian',
            'Azerbaijani',
            'Basque',
            'Belarusian',
            'Bengali',
            'Bosnian',
            'Bulgarian',
            'Catalan',
            'Cebuano',
            'Chichewa',
            'Chinese',
            'Corsican',
            'Croatian',
            'Czech',
            'Danish',
            'Dutch',
            'English',
            'Esperanto',
            'Estonian',
            'Filipino',
            'Finnish',
            'French',
            'Frisian',
            'Galician',
            'Georgian',
            'German',
            'Greek',
            'Gujarati',
            'Haitian Creole',
            'Hausa',
            'Hawaiian',
            'Hebrew',
            'Hindi',
            'Hmong',
            'Hungarian',
            'Icelandic',
            'Igbo',
            'Indonesian',
            'Irish',
            'Italian',
            'Japanese',
            'Javanese',
            'Kannada',
            'Kazakh',
            'Khmer',
            'Kinyarwanda',
            'Korean',
            'Kurdish',
            'Kyrgyz',
            'Lao',
            'Latin',
            'Latvian',
            'Lithuanian',
            'Luxembourgish',
            'Macedonian',
            'Malagasy',
            'Malay',
            'Malayalam',
            'Maltese',
            'Maori',
            'Marathi',
            'Mongolian',
            'Myanmar',
            'Nepali',
            'Norwegian'
            'Odia',
            'Pashto',
            'Persian',
            'Polish',
            'Portuguese',
            'Punjabi',
            'Romanian',
            'Russian',
            'Samoan',
            'Scots Gaelic',
            'Serbian',
            'Sesotho',
            'Shona',
            'Sindhi',
            'Sinhala',
            'Slovak',
            'Slovenian',
            'Somali',
            'Spanish',
            'Sundanese',
            'Swahili',
            'Swedish',
            'Tajik',
            'Tamil',
            'Tatar',
            'Telugu',
            'Thai',
            'Turkish',
            'Turkmen',
            'Ukrainian',
            'Urdu',
            'Uyghur',
            'Uzbek',
            'Vietnamese',
            'Welsh',
            'Xhosa'
            'Yiddish',
            'Yoruba',
            'Zulu',
        )

        self.choose_language.grid(row=1, column=1, sticky="ew", pady=(2, 0))
        self.choose_language.current(19)

        self.t1 = Text(self, width=30, height=10, borderwidth=5, relief=RIDGE)
        self.t1.grid(row=2, column=0, pady=(2, 0))

        self.t2 = Text(self, width=30, height=10, borderwidth=5, relief=RIDGE)
        self.t2.grid(row=2, column=1, pady=(2, 0))

        self.translate_btn = Button(self, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
                                    cursor="hand2", command=self.translate)
        self.translate_btn.grid(row=3, column=0, pady=(2, 2))

        self.clear_btn = Button(self, text="Clear", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
                                cursor="hand2",
                                command=self.clear)
        self.clear_btn.grid(row=3, column=1, pady=(2, 2))

    def clear(self):
        self.t1.delete(1.0, 'end')
        self.t2.delete(1.0, 'end')

    def translate(self):
        language_1 = self.t1.get("1.0", "end-1c")
        cl = self.choose_language.get()

        if language_1 == '':
            messagebox.showerror('Language Translator', 'please fill the box')
        else:
            self.t2.delete(1.0, 'end')
            translator = Translator()
            output = translator.translate(language_1, dest=cl)
            self.t2.insert('end', output.text)


if __name__ == '__main__':
    root = tk.Tk()
    logo_1 = resource_path("translator.png")
    app = Application(logo_1, master=root)
    app.master.title("Translator")
    app.master.iconbitmap(resource_path("Logo.ico"))
    app.master.resizable(False, False)
    app.mainloop()
