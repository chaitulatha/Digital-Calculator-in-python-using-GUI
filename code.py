import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.set(result)
        except:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.StringVar()
entry_field = tk.Entry(root, textvar=entry, font="Arial 20")
entry_field.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']

]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", height=2, width=5)
        button.pack(side="left", padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
