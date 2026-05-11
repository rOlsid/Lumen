import tkinter as tk
from tktimepicker import AnalogPicker, AnalogThemes

root = tk.Tk()
root.mainloop()

root.title("orari i barnave")
time_picker = AnalogPicker(root)
time_picker.pack(expand=True, fill="both")

root.mainloop()
