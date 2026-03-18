# Python Tkinter GUI Application Suite

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/Library-Tkinter-orange.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-lightgrey.svg)
![Persistence](https://img.shields.io/badge/Storage-JSON%20%7C%20TXT-yellow.svg)

A collection of desktop applications developed to demonstrate **CRUD (Create, Read, Update, Delete)** operations, database integration, and local file persistence using Python's standard GUI library, Tkinter.

---

## 📂 Included Applications

### 1. Employee Management System (`GUIxMySQL(xampp).py`)
A professional-grade administrative tool designed to manage staff records via a MySQL backend.
* **Database Integration**: Connects to a local MySQL server (XAMPP default).
* **Dynamic Data Table**: Uses `ttk.Treeview` to display employee ID, Name, and Department.
* **Full CRUD**: Supports adding new records, updating existing entries via ID selection, and deleting specific rows.
* **Event Handling**: Features a selection bind that auto-populates input fields when a row is clicked.

### 2. Structured To-Do List (`ToDo_List_GUI_app(custom_tkinter).py`)
A task manager focused on data integrity and structured storage.
* **JSON Persistence**: Saves and loads tasks from `tasks.json`, preserving the list structure across sessions.
* **Safe Exit**: Includes a `WM_DELETE_WINDOW` protocol that prompts the user before quitting and performs a final save.
* **UI Feedback**: Utilizes colored buttons (Green for Add, Red for Delete) for intuitive navigation.

### 3. Lightweight To-Do List (`To-Do_List_GUI(tkinter)_Application.py`)
A simple, high-readability task tracker using flat-file storage.
* **TXT Storage**: Writes tasks to a simple `tasks.txt` file using line-breaks.
* **Visual Focus**: Features large "Times New Roman" headings for better accessibility.
* **Error Handling**: Includes `try-except` blocks to handle missing files and selection errors gracefully.

---

## 🛠️ Installation & Setup

### Prerequisites
1.  **Python 3.x** must be installed.
2.  **MySQL Connector**: Required for the Employee Manager. Install it via terminal:
    ```bash
    pip install mysql-connector-python
    ```
3.  **XAMPP**: To run the MySQL database locally.

### Database Configuration
Before running the Employee Manager, create the following structure in your MySQL admin (PHPMyAdmin):
```sql
CREATE DATABASE company;
USE company;

CREATE TABLE employees (
    empID INT AUTO_INCREMENT PRIMARY KEY,
    empName VARCHAR(100),
    empDept VARCHAR(100)
);
```
