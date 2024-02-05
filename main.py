from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x175")
window.title('Memphi$')




 
    
def userinput():
    global text_box_username , text_box_password
    label_username = ttk.Label(window, text="Username",font= ("Helvetica", 20))
    label_username.grid(column=1, row=2, padx=15, pady=10)
    text_box_username = Entry(window, width=20,font = ("Helvetica", 20))
    text_box_username.grid(column=2, row=2, padx=10, pady=10)
    label_password = ttk.Label(window, text="Password",font= ("Helvetica", 20))
    label_password.grid(column=1, row=3, padx=15, pady=10)
    text_box_password = Entry(window, width=20, font = ("Helvetica", 20))
    text_box_password.grid(column=2, row=3, padx=10, pady=10)
    button = ttk.Button(window, text="Create Account",  command=lambda: on_button_click(), width=20, padding=(20, 10))
    button.grid(column=2, row=4,padx=10, pady=10)
    username = text_box_username.get()
    password = text_box_password.get()
   




def on_button_click():
    global text_box_username , text_box_password
    username = text_box_username.get()
    password = text_box_password.get()
    
    if len(username) == 0  or len(password) == 0  or len(password) < 8 :
        print("Something wrong")
        window.destroy()
        window_error = Tk()
        window_error.geometry("700x200")
        window_error.title('Memphi$')
        label_notenough = ttk.Label(window_error, text="Please fill out all fields...\nThe password should be at least 8 characters long...\nPlease try again...", foreground = 'red', font= ("Helvetica", 20))
        label_notenough.grid(column=1, row=1, padx=15, pady=10) 
        window_error.after(3000, lambda: window_error.destroy())
    else:
        print("Account created")
        with open("database.txt", "a") as file:
            file.write(f"{username}|{password}\n")
        username = text_box_username.get()
        password = text_box_password.get()
        window.destroy()
        window_success = Tk()
        window_success.geometry("500x75")
        window_success.title('Memphi$')
        label_success = ttk.Label (window_success, text="Successfully registered!", foreground='green', font= ("Helvetica", 30))
        label_success.grid(column=1, row=1, padx=15, pady=10)
        window_success.after(3000, lambda: window_success.destroy())
        



userinput()
window.mainloop()

