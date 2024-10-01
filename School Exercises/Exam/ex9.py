import tkinter as tk
def toggle_text():
    if label["text"] == "Clicke Me":
        label["text"] = "Button Clicked"
    else:
        label["text"] = "Click Me"

root = tk.Tk()
root.title("Toggle Text")

label = tk.Label(root,text="Click Me")
label.pack(pady=10)

button = tk.Button(root,text="Toggle",command=toggle_text())
label.pack(pady=10)

root.mainloop()