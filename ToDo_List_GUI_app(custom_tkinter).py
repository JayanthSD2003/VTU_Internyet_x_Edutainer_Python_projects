import tkinter as tk
from tkinter import messagebox
import json # extra form edutainer internship task
import os # extra form edutainer internship task

tasks_file = 'tasks.json'

def load_tasks():
    if os.path.exists(tasks_file):
        try:
            with open(tasks_file, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks():
    with open(tasks_file, 'w') as f:
        json.dump(task_list, f)

def add_task():
    task = entry.get().strip()
    if task:
        task_list.append(task)
        update_listbox()
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        index = listbox.curselection()[0]
        del task_list[index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in task_list:
        listbox.insert(tk.END, task)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        tasks = list(listbox.get(0, tk.END))  # Convert tuple to list
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)  # Pretty print with indent
        root.destroy()

# Main window setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Load existing tasks
task_list = load_tasks()

# Listbox for tasks
listbox = tk.Listbox(root, height=15, width=50)
listbox.pack(pady=20)

update_listbox()

# Entry for new tasks
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)
entry.focus()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Selected", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
delete_btn.pack(side=tk.LEFT, padx=5)

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
