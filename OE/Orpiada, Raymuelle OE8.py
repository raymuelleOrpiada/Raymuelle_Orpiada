import tkinter as tk

window = tk.Tk()
window.title(f"Task Management") 
window.geometry("400x300") 

counter = 1
def iprint_mo_to():
    global counter
    usr_input = task_input.get()
    print(f"{counter}. {usr_input}")
    counter += 1
    
button_print = tk.Button(window, text = "Add Task", command = iprint_mo_to)
button_print.grid(row = 0, column = 1, padx = 20, pady = 20)

task_input = tk.Entry(window)
task_input.grid(row = 0, column = 0, padx = 40)

window.mainloop()