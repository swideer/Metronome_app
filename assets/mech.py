from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import ImageTk, Image
import math

class metronome_app:
    def __init__(self):
        self.root = Tk()
        style = Style('darkly')
        self.root.geometry('500x500+10+101')
        self.root.resizable(width=True, height=True)

        #VARIABLES
        self.var_tempo = StringVar(self.root, '120')
        self.var_numerator = StringVar(self.root, '4')
        self.var_note = StringVar(self.root, '1')

        #REGISTER FUNCTIONS
        self.check_digit = (self.root.register(self.check_if_digit))
        self.change_value = (self.root.register(self.change_entry_value))

        #MAIN FRAME holding all together
        self.frame_main = ttk.Frame(self.root, relief='solid')
        self.frame_main.grid(row=0, column=0, sticky='wens')

        #FLASH LIGHTS FRAME holding place for tempo lights
        self.frame_lights = ttk.Frame(self.frame_main, relief='solid', width=430, height=480)
        self.frame_lights.grid(row=1, column=1, columnspan=4, rowspan=9, sticky='wens')

        self.label_title = ttk.Label(self.frame_main, text='Easy Metronome', relief='solid')
        self.label_title.grid(row=0, column=0, columnspan=5, sticky='wens')

        #TEMPO SECTION
        self.label_tempo = ttk.Label(self.frame_main, text='Tempo', relief='solid')
        self.label_tempo.grid(row=1, column=0, sticky='wens')
        self.frame_tempo = ttk.Frame(self.frame_main, relief='solid')
        self.frame_tempo.grid(row=2, column=0)
        self.button_minus_tempo = ttk.Button(self.frame_tempo, text='-', command=(self.change_value, 'minus', 'tempo'))
        self.button_minus_tempo.grid(row=0, column=0)
        self.entry_tempo = ttk.Entry(self.frame_tempo, textvariable=self.var_tempo, validate='focus', validatecommand=(self.check_digit, '%P', 'tempo'))
        self.entry_tempo.bind('<Return>', self.remove_focus_on_return)
        self.entry_tempo.grid(row=0, column=1)
        self.button_plus_tempo = ttk.Button(self.frame_tempo, text='+', command=(self.change_value, 'plus', 'tempo'))
        self.button_plus_tempo.grid(row=0, column=2)

        #NUMERATOR SECTION
        self.label_numerator = ttk.Label(self.frame_main, text='Numerator', relief='solid')
        self.label_numerator.grid(row=3, column=0, sticky='wens')
        self.frame_numerator = ttk.Frame(self.frame_main, relief='solid')
        self.frame_numerator.grid(row=4, column=0)
        self.buton_minus_numerator = ttk.Button(self.frame_numerator, text='-', command=(self.change_value, 'minus', 'numerator'))
        self.buton_minus_numerator.grid(row=0, column=0)
        self.entry_numerator = ttk.Entry(self.frame_numerator, textvariable=self.var_numerator, validate='focus', validatecommand=(self.check_digit, '%P', 'numerator'))
        self.entry_numerator.bind('<Return>', self.remove_focus_on_return)
        self.entry_numerator.grid(row=0, column=1)
        self.button_plus_numerator = ttk.Button(self.frame_numerator, text='+', command=(self.change_value, 'plus', 'numerator'))
        self.button_plus_numerator.grid(row=0, column=2)

        #VALUE NOTE SECTION
        self.label_note = ttk.Label(self.frame_main, text='Note value', relief='solid')
        self.label_note.grid(row=5, column=0, sticky='wens')
        self.frame_note = ttk.Frame(self.frame_main, relief='solid')
        self.frame_note.grid(row=6, column=0)
        self.button_minus_note = ttk.Button(self.frame_note, text='-', command=(self.change_value, 'minus', 'note'))
        self.button_minus_note.grid(row=0, column=0)
        self.entry_note = ttk.Entry(self.frame_note, textvariable=self.var_note)
        self.entry_note.grid(row=0,column=1)
        self.button_plus_note = ttk.Button(self.frame_note, text='+', command=(self.change_value, 'plus', 'note'))
        self.button_plus_note.grid(row=0, column=2)

        self.button_tap = ttk.Button(self.frame_main, text='Tap')
        self.button_tap.grid(row=7, column=0)

        self.populate_lights_frame(int(self.var_numerator.get()))

        self.label_self = ttk.Label(self.frame_main, text='by swDEVr', relief='solid')
        self.label_self.grid(row=8, column=0, sticky='wens')

        self.button_quit = ttk.Button(self.frame_main, text='Quit', command=self.root.destroy)
        self.button_quit.grid(row=9, column=0)

        self.root.mainloop()

    #HELPER FUNCTIONS
    def check_if_digit(self, P, field):
        if str.isdigit(P) and int(P)>0:
            return True
        else:
            if field =='tempo':
                self.var_tempo.set('120')
            elif field =='numerator':
                self.var_numerator.set('4')
            return False
    
    def remove_focus_on_return(self, *event):
        self.root.focus_set()
    
    def clear_frame(self, frame):
        '''
        Clears frame before populating it again. This way it prevents overlaping frames, with each user action.
        '''
        for widget in frame.winfo_children():
            widget.destroy()

    #BUILD LAYOUT FUNCTIONS
    def populate_lights_frame(self, numerator_value):
        control_value = 1
        for r in range(0,math.ceil(numerator_value/4)+1):
            for c in range(0,5):
                print(f'control value: {control_value} row: {r}. column: {c}')
                canvas = Canvas(self.frame_lights)
                canvas.grid(row=r, column=c, sticky='wens')
                canvas.create_oval(0,0,20,20,fill='yellow')
                control_value+=1
                if control_value>=numerator_value:
                    break

    #LOGIC FUNCTIONS
    def change_entry_value(self, direction, entry_field):
        def value_change(direction, value):
            if direction == 'minus':
                value = str(int(value) - 1)
            elif direction == 'plus':
                value = str(int(value)+1)
            return value
        if entry_field == 'tempo':
            value = self.var_tempo.get()
            value_new = value_change(direction, value)
            if int(value_new) <= 0:
                self.var_tempo.set('0')
            else:
                self.var_tempo.set(value_new)
        elif entry_field == 'numerator':
            value = self.var_numerator.get()
            value_new = value_change(direction, value)
            if int(value_new)<=0:
                self.var_numerator.set('1')
            elif int(value_new)>16:
                self.var_numerator.set('16')
            else:
                self.var_numerator.set(value_new)
        elif entry_field == 'note':
            value = self.var_note.get()
            value_new = value_change(direction, value)
            self.var_note.set(value_new)
        self.clear_frame(self.frame_lights)
        self.populate_lights_frame(int(self.var_numerator.get()))
        

if __name__=='__main__':
    metronome_app()