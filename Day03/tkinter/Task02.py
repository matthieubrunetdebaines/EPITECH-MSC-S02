import tkinter as tk

def print_uppercase():
    entry_text = entry.get()
    uppercase_text = entry_text.upper()
    print("Uppercase Text:", uppercase_text)

# Create the main window
root = tk.Tk()
root.title("Tkinter Window with LabelFrame")

# create a canvas
canvas= tk.Canvas(root)
canvas.pack(fill="both", expand="yes")

# load img as a pic
background_image = tk.PhotoImage(file="bg_f2g.gif")

# config canvas to use img as bg
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas.image = background_image

# Calculate the center coordinates of the canvas
canvas_width = canvas.winfo_reqwidth()
canvas_height = canvas.winfo_reqheight()
center_x = canvas_width / 2
center_y = canvas_height / 2

# Create a LabelFrame
label_frame = tk.LabelFrame(root, text="MyLabelFrame", bd=0, background="White")
label_frame.place(relx=0, rely=0, anchor="center", x=center_x, y=center_y)

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
