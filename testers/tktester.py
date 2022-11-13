from tkinter import *
from tkinter import ttk

WIN=Tk()
_button_style=ttk.Style()
_button_style.configure("But.TLabel",fg="white")
button_style=ttk.Style(_button_style)
button_style.configure("Butt.Tlabel",bg="black", text="Close")

form= ttk.Frame(WIN,padding=10)
text_var=StringVar(form,"Hello world!")
form.pack()
ttk.Label(form, text=text_var.get(),style="But.TLabel").pack(side="left")
ttk.Button(form, text="QUIT",style="Butt.TLabel",command=WIN.destroy).pack(side="right")

WIN.mainloop()