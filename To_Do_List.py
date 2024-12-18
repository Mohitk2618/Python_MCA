import tkinter as tk

# Add task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Delete task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
task_entry = tk.Entry(root, width=30)
task_entry.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=30, height=10)
task_listbox.pack(padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Run the main loop
root.mainloop()