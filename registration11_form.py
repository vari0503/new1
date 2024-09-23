import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    email = entry_email.get()
    section = section_var.get()  # Get the selected section
    
    if not name or not age or not email:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    # Simulate saving the data (you can add database functionality here)
    messagebox.showinfo("Success", f"Registration successful for {name} in {section} section!")

    # Clear the fields after registration
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    gender_var.set("Male")
    section_var.set(section_options[0])  # Reset section selection

# Creating the main window
root = tk.Tk()
root.title("Registration Form")

# Creating labels and entry widgets
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=5)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=2, column=0, padx=10, pady=5)

gender_var = tk.StringVar(value="Male")
gender_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male.grid(row=2, column=1, padx=10, pady=5, sticky="w")

gender_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female.grid(row=2, column=1, padx=70, pady=5, sticky="w")

label_email = tk.Label(root, text="Email:")
label_email.grid(row=3, column=0, padx=10, pady=5)

entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Dropdown menu for section selection
label_section = tk.Label(root, text="Section:")
label_section.grid(row=4, column=0, padx=10, pady=5)

section_options = ["AIML", "AIDE", "CSE"]  # Section choices
section_var = tk.StringVar(value=section_options[0])
section_menu = tk.OptionMenu(root, section_var, *section_options)
section_menu.grid(row=4, column=1, padx=10, pady=5)

# Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
