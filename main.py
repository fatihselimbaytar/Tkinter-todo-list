import tkinter as tk
from tkinter import messagebox

# ----------------- pencere -----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)

# ----------------- veri -----------------
tasks = []          # görev listesi
FILE_NAME = "tasks.txt"  # kayıt dosyası

# ----------------- fonksiyonlar -----------------
def save_tasks():
    # görevleri dosyaya kaydeder
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    # dosyadan görevleri yükler
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def refresh_listbox():
    # listbox'ı günceller
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{i}. {task}")

def add_task():
    # görev ekler
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Uyarı", "Görev boş olamaz")
        return
    tasks.append(task)
    task_entry.delete(0, tk.END)
    refresh_listbox()
    save_tasks()

def delete_task():
    # numaraya göre görev siler
    try:
        index = int(delete_entry.get()) - 1
        tasks.pop(index)
        delete_entry.delete(0, tk.END)
        refresh_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Uyarı", "Geçerli bir numara gir")

# ----------------- arayüz -----------------
tk.Label(root, text="Görev Ekle").pack(pady=5)

task_entry = tk.Entry(root)
task_entry.pack(fill="x", padx=10)

tk.Button(root, text="Ekle", command=add_task).pack(pady=5)

task_listbox = tk.Listbox(root, height=15)
task_listbox.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(root, text="Silmek istediğin görev numarası").pack(pady=5)

delete_entry = tk.Entry(root)
delete_entry.pack(fill="x", padx=10)

tk.Button(root, text="Sil", command=delete_task, bg="red", fg="white").pack(pady=10)

# ----------------- başlangıç -----------------
load_tasks()
refresh_listbox()

root.mainloop()
