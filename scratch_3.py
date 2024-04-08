from tkinter import *
import tkinter.messagebox

# main window
window = Tk()
window.title("To-Do List App")

background_image = PhotoImage(file=r"C:\Users\kazim\Downloads\TO DO LIST (1).png")

# label to display the image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# window title
window.option_add("*Font", "Helvetica 12 bold")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


center_window(window, 360, 600)

frame_task = Frame(window)
frame_task.pack(pady=(50, 10))

# listbox to display the tasks
listbox_task = Listbox(frame_task, bg="#C2A27F", fg="white", height=20, width=30, font=("Helvetica", 12),
                       selectbackground="gray")
listbox_task.pack(side=LEFT)

# scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Function to add tasks to the listbox


def add_task():
    task = entry_task.get()
    if task == "":
        tkinter.messagebox.showwarning(title="Warning!", message="Please Enter a Task")
    else:
        listbox_task.insert(END, task)
        entry_task.delete(0, END)

# Function to delete tasks from the listbox


def delete_task():
    task_index = listbox_task.curselection()
    if task_index:
        listbox_task.delete(task_index)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please Select a Task to Delete")

# Function to mark tasks as completed


def mark_completed():
    task_index = listbox_task.curselection()
    task = listbox_task.get(task_index)
    completed_task = task + " ✔"
    listbox_task.delete(task_index)
    listbox_task.insert(listbox_task.size(), completed_task)


def edit_task():
    task_index = listbox_task.curselection()
    if task_index:
        new_task = entry_task.get()
        listbox_task.delete(task_index)
        listbox_task.insert(task_index, new_task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please Select a Task to Edit")

# text entry field for adding tasks


entry_task = Entry(window, width=30, font=("Helvetica", 12))
entry_task.pack()

# Creating buttons for adding, deleting, and marking completed tasks

button_frame = Frame(window)
button_frame.pack(pady=(10, 20))

button_add = Button(button_frame, text="Add Task", command=add_task, bg="#C2A27F", fg="white")
button_add.pack(side=LEFT, padx=5)

button_delete = Button(button_frame, text="Delete Task", command=delete_task, bg="#C2A27F", fg="white")
button_delete.pack(side=LEFT, padx=5)

button_mark = Button(button_frame, text="Mark Completed", command=mark_completed, bg="#C2A27F", fg="white")
button_mark.pack(side=LEFT, padx=5)

edit_button_frame = Frame(window)
edit_button_frame.pack()

button_edit = Button(edit_button_frame, text="Edit Task", command=edit_task, bg="#C2A27F", fg="white")
button_edit.pack(pady=5)

window.mainloop()
