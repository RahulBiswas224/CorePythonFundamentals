# GuiApplications.py
import tkinter as tk
from tkcalendar import Calendar # Requires: pip install tkcalendar

def createCalculator():
    root = tk.Tk()
    root.title("Calculator")
    # Add logic here...
    root.mainloop()

def createCalendar():
    root = tk.Tk()
    cal = Calendar(root, selectmode='day')
    cal.pack(pady=20)
    root.mainloop()
