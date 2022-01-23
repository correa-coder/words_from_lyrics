from tkinter import Tk, Toplevel, Frame, Label, Button
from tkinter import filedialog, messagebox
import module

SETTINGS_DATA = module.load_settings()

PADX = 100
PADY = 80
FONT_MD = (
    SETTINGS_DATA['font']['name'],
    SETTINGS_DATA['font']['size']['md']
)


class ButtonPrimary(Button):
    """customized tkinter button"""
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['fg'] = SETTINGS_DATA['color']['text']
        self['bg'] = SETTINGS_DATA['color']['button']
        self['font'] = FONT_MD
        self['bd'] = 0


class FrameResult(Frame):
    """displays the result"""

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        result_label = Label(self,
                             text='Result will show here',
                             font=FONT_MD,
                             fg=SETTINGS_DATA['color']['text'],
                             bg=SETTINGS_DATA['color']['background']
        )
        result_label.pack(padx=PADX, pady=PADY)
        

def show_result():
    extracted_words = []

    window = Toplevel()
    window.title('Extracted words')
    frm = FrameResult(
        window, bg=SETTINGS_DATA['color']['background'],
    )
    frm.pack(fill="both", expand=True)


root = Tk()
root.title('Words from Lyrics')
# root.geometry('250x100')

frame = Frame(root, bg=SETTINGS_DATA['color']['background'])
frame.pack(fill="both", expand=True)

ButtonPrimary(frame, text='Open lyrics file', command=show_result).pack(padx=PADX, pady=PADY)

root.mainloop()
