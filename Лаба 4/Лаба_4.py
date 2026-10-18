import math
import tkinter as tk
from tkinter import filedialog

W = 600
H = 600
canvas = None


def put(x, y, color):
    canvas.create_line(x, y, x + 1, y, fill=color)


def circ_equation(x0, y0, r, color):
    for x in range(r + 1):
        y = round(math.sqrt(r * r - x * x))
        put(x0 + x, y0 + y, color)
        put(x0 + x, y0 - y, color)
        put(x0 - x, y0 + y, color)
        put(x0 - x, y0 - y, color)
        put(x0 + y, y0 + x, color)
        put(x0 + y, y0 - x, color)
        put(x0 - y, y0 + x, color)
        put(x0 - y, y0 - x, color)


def circ_param(x0, y0, r, color):
    tau = 0.0
    dtau = 1.0 / r
    while tau <= 2 * math.pi + dtau:
        x = round(r * math.cos(tau))
        y = round(r * math.sin(tau))
        put(x0 + x, y0 + y, color)
        tau = tau + dtau


def circ_brez(x0, y0, r, color):
    def put8(px, py):
        put(x0 + px, y0 + py, color)
        put(x0 + px, y0 - py, color)
        put(x0 - px, y0 + py, color)
        put(x0 - px, y0 - py, color)
        put(x0 + py, y0 + px, color)
        put(x0 + py, y0 - px, color)
        put(x0 - py, y0 + px, color)
        put(x0 - py, y0 - px, color)

    x = 0
    y = r
    delta = 2 - 2 * r
    while x <= y:
        put8(x, y)
        d1 = 2 * (delta + y) - 1
        d2 = 2 * (delta - x) - 1
        if delta < 0 and d1 <= 0:
            x = x + 1
            delta = delta + 2 * x + 1
        elif delta > 0 and d2 > 0:
            y = y - 1
            delta = delta - 2 * y + 1
        else:
            x = x + 1
            y = y - 1
            delta = delta + 2 * (x - y)


def circ_builtin(x0, y0, r, color):
    canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline=color)


def arc_param(x0, y0, r, ang1, ang2, color):
    a1 = math.radians(ang1)
    a2 = math.radians(ang2)
    dtau = 1.0 / r
    tau = a1
    while tau <= a2 + dtau:
        x = round(r * math.cos(tau))
        y = round(r * math.sin(tau))
        put(x0 + x, y0 + y, color)
        tau = tau + dtau


def create():
    canvas.delete("all")
    R = int(entry_r.get())
    cx = int(entry_cx.get())
    cy = int(entry_cy.get())

    circ_equation(cx, cy, R, "red")
    circ_param(cx, cy, R - 6, "green")
    circ_brez(cx, cy, R - 12, "blue")
    circ_builtin(cx, cy, R - 18, "gray")

    s = R / math.sqrt(3)
    x1, y1 = cx, cy - round(s)
    x2, y2 = cx - R // 2, cy + round(s / 2)
    x3, y3 = cx + R // 2, cy + round(s / 2)

    circ_brez(x1, y1, R, "black")
    circ_brez(x2, y2, R, "black")
    circ_brez(x3, y3, R, "black")

    arc_param(x1, y1, R, 30, 150, "black")
    arc_param(x2, y2, R, -90, 30, "black")
    arc_param(x3, y3, R, 150, 270, "black")


def save():
    path = filedialog.asksaveasfilename(defaultextension=".ps",
                                        filetypes=[("PostScript", "*.ps")])
    if path:
        canvas.postscript(file=path)


root = tk.Tk()
root.title("ЛР 4 вариант 6")

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="R:").pack(side=tk.LEFT)
entry_r = tk.Entry(frame, width=5)
entry_r.insert(0, "120")
entry_r.pack(side=tk.LEFT, padx=3)

tk.Label(frame, text="cx:").pack(side=tk.LEFT)
entry_cx = tk.Entry(frame, width=5)
entry_cx.insert(0, "300")
entry_cx.pack(side=tk.LEFT, padx=3)

tk.Label(frame, text="cy:").pack(side=tk.LEFT)
entry_cy = tk.Entry(frame, width=5)
entry_cy.insert(0, "300")
entry_cy.pack(side=tk.LEFT, padx=3)

tk.Button(frame, text="Создать", command=create).pack(side=tk.LEFT, padx=10)
tk.Button(frame, text="Сохранить", command=save).pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack(pady=5)

root.mainloop()