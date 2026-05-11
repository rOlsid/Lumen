import tkinter as tk
from tkinter import messagebox
import time

class Ilac:
    def __init__(self, emri, intervali_ore):
        self.emri = emri
        self.intervali_sekonda = intervali_ore * 3600
        self.koha_fillestare = time.time()
        self.koha_tjeter_doz = self.koha_fillestare + self.intervali_sekonda

class DispenserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dispenser i Ilaçeve për të Verbër")
        self.root.geometry("600x450")
        self.ilacet = []

        # Titulli
        self.label_titull = tk.Label(root, text="Dispenser i Ilaçeve", font=("Helvetica", 18, "bold"), fg="blue")
        self.label_titull.pack(pady=10)

        # Emri i ilaçit
        tk.Label(root, text="Emri i Ilaçit:", font=("Helvetica", 14)).pack()
        self.entry_emri = tk.Entry(root, font=("Helvetica", 14))
        self.entry_emri.pack(pady=5)

        # Intervali në orë
        tk.Label(root, text="Intervali (në orë):", font=("Helvetica", 14)).pack()
        self.entry_intervali = tk.Entry(root, font=("Helvetica", 14))
        self.entry_intervali.pack(pady=5)

        # Butoni për shtim
        self.button_shto = tk.Button(root, text="Shto Ilaçin", font=("Helvetica", 14), command=self.shto_ilacin)
        self.button_shto.pack(pady=10)

        # Lista e ilaçeve të shtuar
        self.label_lista = tk.Label(root, text="Ilaçet aktive:", font=("Helvetica", 14, "bold"))
        self.label_lista.pack(pady=5)
        self.lista_ilaceve = tk.Listbox(root, font=("Helvetica", 12), width=50)
        self.lista_ilaceve.pack(pady=5)

        # Fillon kontrollin e dozave
        self.root.after(1000, self.kontrollo_dozat)

    def shto_ilacin(self):
        emri = self.entry_emri.get()
        try:
            intervali = int(self.entry_intervali.get())
            if emri and intervali > 0:
                ilaci = Ilac(emri, intervali)
                self.ilacet.append(ilaci)
                self.lista_ilaceve.insert(tk.END, f"{emri} - Doza tjetër në {intervali} orë")
                self.entry_emri.delete(0, tk.END)
                self.entry_intervali.delete(0, tk.END)
            else:
                messagebox.showerror("Gabim", "Ju lutem vendosni emrin dhe kohën e saktë.")
        except ValueError:
            messagebox.showerror("Gabim", "Intervali duhet të jetë numër (në orë).")

    def kontrollo_dozat(self):
        koha_tani = time.time()
        for ilac in self.ilacet:
            if koha_tani >= ilac.koha_tjeter_doz:
                self.alert_kujtesa(ilac.emri)
                ilac.koha_fillestare = time.time()
                ilac.koha_tjeter_doz = ilac.koha_fillestare + ilac.intervali_sekonda
        self.root.after(60000, self.kontrollo_dozat)  # Kontroll çdo minutë

    def alert_kujtesa(self, emri_ilacit):
        messagebox.showinfo("Kujtesë!", f"Është koha për të marrë: {emri_ilacit}")

# Nisja e GUI
root = tk.Tk()
app = DispenserGUI(root)
root.mainloop()
