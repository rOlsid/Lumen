import os
import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame


pygame.mixer.init()


alarm_path = "/home/flatratedijes/alarm.mp3"


medications = []

def play_alarm():
    try:
        pygame.mixer.music.load(alarm_path)
        pygame.mixer.music.play()
        time.sleep(10)  
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Error playing sound: {e}")

def add_medication():
    name = med_name_entry.get()
    interval = interval_entry.get()
    unit = time_unit.get()

    if not name or not interval.isdigit():
        messagebox.showerror("Error", "Ju lutem shkruani emër dhe interval të vlefshëm.")
        return

    minutes = int(interval)
    if unit == "ore":
        minutes *= 60

    medications.append({
        "name": name,
        "interval": minutes * 60,
        "start_time": time.time()
    })

    med_name_entry.delete(0, tk.END)
    interval_entry.delete(0, tk.END)

def update_display():
    while True:
        time.sleep(1)
        current_time = time.time()
        meds_list.delete(0, tk.END)

        for med in medications:
            elapsed = int(current_time - med["start_time"])
            remaining = med["interval"] - elapsed

            if remaining <= 0:
                threading.Thread(target=play_alarm).start()  
                messagebox.showinfo("Kujtesë", f"Koha për të marrë: {med['name']}")
                med["start_time"] = current_time
                remaining = med["interval"]

            mins, secs = divmod(remaining, 60)
            meds_list.insert(tk.END, f"{med['name']} - pas {mins:02d}:{secs:02d}")


window = tk.Tk()
window.title("Kaltra")
window.geometry("400x400")

tk.Label(window, text="Emri i ilaçit:").pack()
med_name_entry = tk.Entry(window)
med_name_entry.pack()

tk.Label(window, text="Intervali:").pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

time_unit = tk.StringVar(value="minuta")
tk.OptionMenu(window, time_unit, "minuta", "ore").pack()

tk.Button(window, text="Shto ilaçin", command=add_medication).pack(pady=10)

tk.Label(window, text="Ilaçet").pack()
meds_list = tk.Listbox(window, width=50)
meds_list.pack(pady=10)


threading.Thread(target=update_display, daemon=True).start()

window.mainloop()
