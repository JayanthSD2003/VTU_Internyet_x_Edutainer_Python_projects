import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # XAMPP default
        database='company'
    )

def fetch_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT empID, empName, empDept FROM employees")
        rows = cursor.fetchall()
        
        for item in tree.get_children():
            tree.delete(item)
        
        for row in rows:
            tree.insert("", "end", values=row)
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Fetch Error: {err}")

def add_employee():
    emp_name = name_entry.get().strip()
    emp_dept = dept_entry.get().strip()
    
    if not emp_name or not emp_dept:
        messagebox.showwarning("Input Error", "Fill both fields.")
        return
    
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (empName, empDept) VALUES (%s, %s)", (emp_name, emp_dept))
        conn.commit()
        cursor.close()
        conn.close()
        
        messagebox.showinfo("Success", "Employee added!")
        name_entry.delete(0, tk.END)
        dept_entry.delete(0, tk.END)
        fetch_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Add Error: {err}")

def delete_employee():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection", "Select a row to delete.")
        return
    
    emp_id = tree.item(selected)['values'][0]
    if messagebox.askyesno("Confirm", f"Delete employee ID {emp_id}?"):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE empID = %s", (emp_id,))
            conn.commit()
            cursor.close()
            conn.close()
            
            messagebox.showinfo("Success", "Employee deleted!")
            fetch_data()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Delete Error: {err}")

def on_tree_select(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected)['values']
        id_entry.delete(0, tk.END)
        id_entry.insert(0, values[0])
        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])
        dept_entry.delete(0, tk.END)
        dept_entry.insert(0, values[2])

def update_employee():
    emp_id = id_entry.get().strip()
    emp_name = name_entry.get().strip()
    emp_dept = dept_entry.get().strip()
    
    if not all([emp_id, emp_name, emp_dept]):
        messagebox.showwarning("Input Error", "Fill all fields.")
        return
    
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET empName=%s, empDept=%s WHERE empID=%s", 
                      (emp_name, emp_dept, emp_id))
        conn.commit()
        cursor.close()
        conn.close()
        
        messagebox.showinfo("Success", "Employee updated!")
        clear_entries()
        fetch_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Update Error: {err}")

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Employee Manager - Full CRUD")
root.geometry("700x600")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Emp ID:").grid(row=0, column=0, padx=5)
id_entry = tk.Entry(input_frame, width=10)
id_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Emp Name:").grid(row=0, column=2, padx=5)
name_entry = tk.Entry(input_frame, width=25)
name_entry.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Emp Dept:").grid(row=0, column=4, padx=5)
dept_entry = tk.Entry(input_frame, width=20)
dept_entry.grid(row=0, column=5, padx=5)

# Buttons frame
btn_frame = tk.Frame(input_frame)
btn_frame.grid(row=0, column=6, padx=10)

tk.Button(btn_frame, text="Add", command=add_employee, bg="lightgreen", width=8).pack(pady=2)
tk.Button(btn_frame, text="Update", command=update_employee, bg="lightyellow", width=8).pack(pady=2)
tk.Button(btn_frame, text="Clear", command=clear_entries, bg="lightgray", width=8).pack(pady=2)

# Treeview
columns = ("empID", "empName", "empDept")
tree = ttk.Treeview(root, columns=columns, show="headings", height=18)
tree.heading("empID", text="Emp ID")
tree.heading("empName", text="Emp Name")
tree.heading("empDept", text="Emp Dept")
tree.column("empID", width=80)
tree.column("empName", width=300)
tree.column("empDept", width=200)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(pady=10, side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Buttons below tree
lower_btn_frame = tk.Frame(root)
lower_btn_frame.pack(pady=10)

tk.Button(lower_btn_frame, text="Refresh", command=fetch_data, bg="lightblue").pack(side="left", padx=5)
tk.Button(lower_btn_frame, text="Delete Selected", command=delete_employee, bg="orange").pack(side="left", padx=5)

# Bind selection to populate fields
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Initial load
fetch_data()

root.mainloop()
