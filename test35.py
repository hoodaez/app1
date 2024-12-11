import tkinter as tk
from tkinter import messagebox
import math

def click(button_text):
    if button_text == "=":
        try:
            expression = entry.get()
            expression = expression.replace("π", str(math.pi))
            expression = expression.replace("e", str(math.e))
            expression = expression.replace("^", "**")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# وظائف الدوال المتقدمة
def advanced_function(func):
    try:
        expression = entry.get()
        if func == "√":
            result = math.sqrt(float(expression))
        elif func == "log":
            result = math.log(float(expression))
        elif func == "sin":
            result = math.sin(math.radians(float(expression)))
        elif func == "cos":
            result = math.cos(math.radians(float(expression)))
        elif func == "tan":
            result = math.tan(math.radians(float(expression)))
        else:
            result = "Error"
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# إنشاء نافذة التطبيق
app = tk.Tk()
app.title("Touchscreen Calculator")
app.geometry("400x600")
app.configure(bg="#2e3f4f")

# إدخال النصوص
entry = tk.Entry(app, width=18, font=("Arial", 24), bd=10, insertwidth=2, justify="right", bg="#f5f5f5")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# أزرار الآلة الحاسبة
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "sin", "cos", "tan", "√",
    "π", "e", "log", "^"
]

row_val = 1
col_val = 0

for button in buttons:
    if button in ["sin", "cos", "tan", "√", "log"]:
        tk.Button(
            app, text=button, padx=20, pady=20, font=("Arial", 14), bg="#82caff", fg="#000", relief="raised", command=lambda b=button: advanced_function(b)
        ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(
            app, text=button, padx=20, pady=20, font=("Arial", 14), bg="#d1e7dd", fg="#000", relief="raised", command=lambda b=button: click(b)
        ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# تكبير الأزرار تلقائيًا
for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for j in range(4):
    app.grid_columnconfigure(j, weight=1)

# تشغيل التطبيق
app.mainloop()