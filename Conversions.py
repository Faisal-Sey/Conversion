
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from utils.convert_main import convert_dim
from utils.constants import list_units


app = tk.Tk()
app.title("Converter")
app.geometry("1920x1080")



def converts(dimension, unit_from, unit_to):
    return convert_dim(unit_from, unit_to, dimension)


def current_dim_convert(dim):
    clean_dim = dim.lower().split()
    _dim = '_'.join(clean_dim)
    _var = list_units(_dim)
    return _dim, _var


def getab(drop):
    current_dim, current_var = current_dim_convert(drop.get())
    previous = ttk.Combobox(app, textvariable=drop2, values=current_var, font=myFont, width=28)
    previous.place(x=80, y=200)
    fv = tk.DoubleVar()
    from_value = Entry(app, font=myFont, textvariable=fv)
    from_value.place(x=150, y=300)
    next = ttk.Combobox(app, textvariable=drop3, values=current_var, font=myFont, width=25)
    next.place(x=500, y=200)
    tv = tk.DoubleVar()
    to_value = Entry(app, font=myFont, textvariable=tv, width=25)
    to_value.place(x=560, y=300)
    label1 = Label(app, text="Input: ", font=myFont)
    label1.place(x=50, y=300)
    label2 = Label(app, text="Output: ", font=myFont)
    label2.place(x=450, y=300)

    def calculate_current_dim():
        converted_result = converts(current_dim, previous.get(), next.get())
        result = float(from_value.get()) * converted_result
        to_value.delete(0, END)
        to_value.insert(0, result)

    calculate_button = Button(app, fg='white', bg='blue', command=calculate_current_dim, text="Calculate", font=myFont)
    calculate_button.place(x=400, y=400)

top_label = Label(app, text="CONVERSIONS FROM ONE UNIT TO ANOTHER", fg="blue")
top_label.pack(padx=10, pady=10)

myFont = font.Font(family='Courier', weight="bold")
top_label['font'] = myFont
drop = tk.StringVar()
drop.set("Select Quantity")
drop.trace("w", lambda name, index, mode, drop=drop: getab(drop))
values=["Length", "Area", "Volume", "Mass", "Temperature", "Force", "Pressure", "Work and Energy", "Density", "Power", "Time", "Speed", "Plane angle",
        "Angular Velocity", "Acceleration", "Moment of Inertia", "Kinematic Viscosity", "Fuel Efficiency to Mass", "Fuel Efficiency to Volume", "Specific Volume Converter",
        "Flow rate", "Electrical resistance","Dynamic viscosity", "Mass Flow rate", "Molar Flow rate", "Molarity", "Molality", "Surface Tension",
        "Specific Heat Capacity", "Heat Transfer Coefficient"]
categories = ttk.Combobox(app, textvariable=drop, values=values, font = myFont, justify=tk.CENTER)
categories.pack(padx=10, pady=30)
drop2 = tk.StringVar()
drop3 = tk.StringVar()
drop2.set("Select unit to convert from")
drop3.set("Select unit to convert to")
app.mainloop()


