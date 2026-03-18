import tkinter as tk
from tkinter import messagebox
#from tkinter import Button

# Add task to the listbox
def add_task():
    #print("testing add button")
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning - Input error", "Please enter a task!!!")
    print(f"You entered: {task}")

# Delete the selected task from the listbox    
def delete_task():
    #print("testing delete button")
    try:
        #print("testing delete button")
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)    
    except IndexError:
        messagebox.showwarning("Warning - Selection error", "Please select a task to delete!!!")

# Save tasks to file on closing the application        
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        tasks = listbox_tasks.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        root.destroy() 
        

root = tk.Tk()
root.title("To-Do List Application.")

label = tk.Label(root, text="Enter a task:", font=('Times New Roman', 26))
label.pack(pady=10)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command = add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", command = delete_task)
btn_delete.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
listbox_tasks.pack(pady=10)

# Load tasks from file if it exists
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
        print("tasks.txt file found, loading tasks...")
    for task in tasks:
        listbox_tasks.insert(tk.END, task)
except FileNotFoundError:
    pass

# Set-up closing event
root.protocol("WM_DELETE_WINDOW", on_closing)   

root.mainloop()
