import tkinter as tk
from tkinter import ttk
from datetime import datetime

def calculate():
    try:
        month = int(month_var.get())
        year = int(year_var.get())
        if not (1 <= month <= 12):
            result_var.set("เดือนต้องอยู่ระหว่าง 1-12")
            return
        A = month * 3
        B = year - month
        C = month * 2
        result_var.set(f"{A}{B}{C}")
    except ValueError:
        result_var.set("กรุณากรอกตัวเลขให้ถูกต้อง")

def reset_to_current():
    now = datetime.now()
    month_var.set(now.month)
    year_var.set(now.year)
    result_var.set("")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Game House Key Gen")
root.tk.call('tk', 'scaling', 2.0)
root.geometry("320x350")
root.resizable(False, False)

# กำหนดค่าปัจจุบัน
now = datetime.now()
month_var = tk.StringVar(value=now.month)
year_var = tk.StringVar(value=now.year)
result_var = tk.StringVar()

# ส่วนของอินพุต
ttk.Label(root, text="เดือน (1-12):", font=("Tahoma", 11)).pack(pady=(15, 0))
ttk.Entry(root, textvariable=month_var, justify="center", width=10).pack()

ttk.Label(root, text="ปี (ค.ศ.):", font=("Tahoma", 11)).pack(pady=(10, 0))
ttk.Entry(root, textvariable=year_var, justify="center", width=10).pack()

# ปุ่มคำนวณ
ttk.Button(root, text="คำนวณ", command=calculate).pack(pady=10)

# แสดงผลลัพธ์
ttk.Label(root, text="ผลลัพธ์:", font=("Tahoma", 11)).pack()
#ttk.Label(root, textvariable=result_var, font=("Consolas", 14, "bold"), foreground="blue").pack(pady=5)
tk.Entry(root, textvariable=result_var, state="readonly", relief="flat", bd=0, highlightthickness=0, font=("Consolas", 14, "bold"), justify="center", foreground="blue").pack(pady=10)

# ปุ่มรีเซ็ต
ttk.Button(root, text="รีเซ็ตกลับเป็นปัจจุบัน", command=reset_to_current).pack(pady=10)

root.mainloop()
