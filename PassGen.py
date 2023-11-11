import tkinter as tk
import random
import string
root = tk.Tk()
root.geometry("555x444")



def generate_password1():
    password_length = int(passwordLength_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result = password
    generate_password_entry.insert(0, result)



def accept_password():
    accepted_password = generate_password_entry.get()
    username = name_entry.get()
    result_label.config(text=f"Username: {username}\nPassword: {accepted_password}")



def reset_password():
    generate_password_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    result_label.config(text="")




frame = tk.Frame(root, bg="gray")
frame.grid(row=0)
label1 = tk.Label(frame, text="Password Generator", fg="Blue", padx=50, pady=10, font=("Arial", 12, "underline"),
                  underline=0)
label1.grid()
enter_username = tk.Label(root, text="Enter User Name:")
enter_username.grid(row=1, column=0)

enter_passwordLength = tk.Label(root, text="Enter Password Length:")
enter_passwordLength.grid(row=2, column=0)

generate_password = tk.Label(root, text="Generated password:")
generate_password.grid(row=3, column=0)

username_value = tk.StringVar()
passwordLength_Value = tk.StringVar()


name_entry = tk.Entry(root, textvariable=username_value, borderwidth=3, relief="sunken")
passwordLength_entry = tk.Entry(root, textvariable=passwordLength_Value, borderwidth=3, relief="sunken")
generate_password_entry = tk.Entry(root, borderwidth=3, relief="sunken")

name_entry.grid(row=1, column=2)
passwordLength_entry.grid(row=2, column=2)
generate_password_entry.grid(row=3, column=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password1)
generate_button.grid(row=4, column=2)

accept_button = tk.Button(root, text="Accept", command=accept_password)
reset_button = tk.Button(root, text="Reset", command=reset_password)
accept_button.grid(row=5, column=2)
reset_button.grid(row=6, column=2)

result_label = tk.Label(root, text="")
result_label.grid(row=7, column=2)

root.mainloop()

      