import tkinter as tk

def calculate_percentage():
    try:
        enter_amount = float(entry_amount.get())
        percent = float(entry_percent.get())
        result = (enter_amount * percent) / 100
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Percentage Calculator")

# Create and place the widgets
label_amount = tk.Label(root, text="Enter Amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

label_percent = tk.Label(root, text="Enter Percentage:")
label_percent.pack()

entry_percent = tk.Entry(root)
entry_percent.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate_percentage)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

# Run the application
root.mainloop()
