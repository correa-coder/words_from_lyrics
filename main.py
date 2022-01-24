from tkinter import Tk, Toplevel, Frame, Label, Button
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
        self.result_label = Label(self,
                             text='Result will show here',
                             font=FONT,
                             fg=SETTINGS['color']['text'],
                             bg=SETTINGS['color']['background']
        )
        self.result_label.pack(padx=PADX, pady=PADY)
        

def show_result():
    file_path = filedialog.askopenfilename(
        filetypes=(('txt files', '*.txt'), ('all files', '*.*'))
    )

    lyrics = module.load_txt(file_path)
    words = module.extract_words(lyrics)
    words_listed = module.itemize(words)

    window = Toplevel()
    window.title('Extracted words')
    frm = FrameResult(
        window, bg=SETTINGS['color']['background'],
    )
    frm.pack(fill="both", expand=True)

    frm.result_label['text'] = words_listed


root = Tk()
root.title('Words from Lyrics')
# root.geometry('250x100')

frame = Frame(root, bg=SETTINGS['color']['background'])
frame.pack(fill="both", expand=True)

ButtonPrimary(frame, text='Open lyrics file', command=show_result).pack(padx=PADX, pady=PADY)

root.mainloop()
