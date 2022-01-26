from tkinter import Tk, Toplevel, Frame, Button, Text, Scrollbar
from tkinter import filedialog, messagebox
import module

SETTINGS = module.load_settings()

PADX = 100
PADY = 80
FONT = (
    SETTINGS['font']['name'],
    SETTINGS['font']['size']
)


class ButtonPrimary(Button):
    """customized tkinter button"""
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['fg'] = SETTINGS['color']['text']
        self['bg'] = SETTINGS['color']['button']
        self['font'] = FONT
        self['bd'] = 0


class FrameResult(Frame):
    """displays the result"""

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        # create scroll bar
        text_scrollbar = Scrollbar(self)
        text_scrollbar.pack(side="right", fill="y")

        self.text_result = Text(self,
                             font=FONT,
                             fg=SETTINGS['color']['text'],
                             bg=SETTINGS['color']['background'],
                             width=10,
                             height=15,
                             yscrollcommand=text_scrollbar.set,
                             padx=PADX,
                             pady=PADY
        )
        self.text_result.pack()

        text_scrollbar.config(command=self.text_result.yview)
        

def show_result():
    file_path = filedialog.askopenfilename(
        filetypes=(('txt files', '*.txt'), ('all files', '*.*'))
    )

    lyrics = module.load_txt(file_path)

    if lyrics.startswith('ERROR'):
        messagebox.showerror(title='Wrong file format', message=lyrics)
    else:
        words = module.extract_words(lyrics)

        window = Toplevel()
        window.title('Extracted words')
        frm = FrameResult(
            window, bg=SETTINGS['color']['background'],
        )
        frm.pack(fill="both", expand=True)

        for word in words:
            frm.text_result.insert('end', f'- {word}\n')


root = Tk()
root.title('Words from Lyrics')
# root.geometry('250x100')

frame = Frame(root, bg=SETTINGS['color']['background'])
frame.pack(fill="both", expand=True)

ButtonPrimary(frame, text='Open lyrics file', command=show_result).pack(padx=PADX, pady=PADY)

root.mainloop()
