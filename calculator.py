import tkinter as tk

def press(x):
    if x == "C":
        v.set("")
    elif x == "=":
        try:
            v.set(eval(v.get()))
        except Exception:
            v.set("Error")
    else:
        v.set(v.get() + x)

root = tk.Tk()
root.title("Calculator")
v = tk.StringVar()

tk.Entry(root, textvariable=v, font=20, justify="right").grid(
    row=0, column=0, columnspan=4, sticky="nsew"
)

buttons = "789/456*123-0.C+"
for i, b in enumerate(buttons):
    tk.Button(root, text=b, font=20, command=lambda x=b: press(x)).grid(
        row=i // 4 + 1, column=i % 4, sticky="nsew"
    )

tk.Button(root, text="=", font=20, command=lambda: press("=")).grid(
    row=5, column=0, columnspan=4, sticky="nsew"
)

root.mainloop()
