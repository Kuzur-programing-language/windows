# kuzur_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

class KuzurGUI:
    def __init__(self, root):
        self.root = root
        root.title("KuzurLang Launcher")
        root.geometry("700x500")

        tk.Label(root, text="KuzurLang Launcher", font=("Arial", 24)).pack(pady=10)

        tk.Button(root, text="Open .kz File", command=self.open_file, width=30, height=2).pack(pady=5)
        tk.Button(root, text="Run Snake Game", command=self.run_snake, width=30, height=2).pack(pady=5)
        tk.Button(root, text="Run Calculator", command=self.run_calc, width=30, height=2).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit, width=30, height=2).pack(pady=5)

        self.text = tk.Text(root, height=15)
        self.text.pack(pady=10, fill=tk.BOTH, expand=True)

    def run_kuzur(self, file):
        # Run kuzur.exe with the selected .kz file
        exe_path = os.path.join(os.path.dirname(sys.argv[0]), "kuzur.exe")
        if not os.path.exists(exe_path):
            messagebox.showerror("Error", "kuzur.exe not found!")
            return

        try:
            cmd = [exe_path, file]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out, err = proc.communicate()
            if out: self.text.insert(tk.END, out + "\n")
            if err: self.text.insert(tk.END, err + "\n")
        except Exception as e:
            self.text.insert(tk.END, f"Error: {e}\n")

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("KuzurLang files","*.kz")])
        if file:
            self.run_kuzur(file)

    def run_snake(self):
        snake_file = os.path.join("examples","snake.kz")
        if os.path.exists(snake_file):
            self.run_kuzur(snake_file)
        else:
            messagebox.showerror("Error", "snake.kz not found!")

    def run_calc(self):
        calc_file = os.path.join("examples","calc.kz")
        if os.path.exists(calc_file):
            self.run_kuzur(calc_file)
        else:
            messagebox.showerror("Error", "calc.kz not found!")

if __name__=="__main__":
    root = tk.Tk()
    gui = KuzurGUI(root)
    root.mainloop()
