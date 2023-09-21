import tkinter as tk

def print_uppercase():
    entry_text = entry.get()
    uppercase_text = entry_text.upper()
    print("Uppercase Text:", uppercase_text)

# Create the main window
root = tk.Tk()
root.title("Tkinter Window with LabelFrame")

# Create a LabelFrame
label_frame = tk.LabelFrame(root, text="MyLabelFrame")
label_frame.pack(padx=100, pady=100)

# Create an Entry widget inside the LabelFrame
entry = tk.Entry(label_frame)
entry.pack()

# Create a button inside the LabelFrame to perform the action
button_inside = tk.Button(label_frame, text="Print Uppercase", command=print_uppercase)
button_inside.pack()

# Create a button below the LabelFrame (in the main window)
button_below = tk.Button(root, text="Button Below LabelFrame")
button_below.pack()

# Run the Tkinter main loop
root.mainloop()
