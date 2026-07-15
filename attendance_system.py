############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
from tkinter import PhotoImage
import tkinter.simpledialog as tsd

from PIL import Image, ImageTk
import cv2, os
import csv
import numpy as np
import pandas as pd
import datetime
import time

######################## MODERN UI FRONT-END ########################

from tkinter import ttk

window = tk.Tk()
window.title("AI Face Recognition Attendance System")
window.geometry("1350x720")
window.configure(bg="#0f172a")  # Dark blue background

style = ttk.Style()
style.theme_use("clam")

# ------------------ HEADER ------------------
header = tk.Frame(window, bg="#020617", height=80)
header.pack(fill="x")

title = tk.Label(
    header,
    text="AI Face Recognition Attendance System",
    bg="#020617",
    fg="white",
    font=("Segoe UI", 26, "bold")
)
title.pack(side="left", padx=30)

date_label = tk.Label(
    header,
    text=f"{day}-{mont[month]}-{year}",
    bg="#020617",
    fg="#38bdf8",
    font=("Segoe UI", 14, "bold")
)
date_label.pack(side="right", padx=20)

clock = tk.Label(
    header,
    bg="#020617",
    fg="#22c55e",
    font=("Segoe UI", 14, "bold")
)
clock.pack(side="right", padx=10)
tick()

# ------------------ MAIN BODY ------------------
main = tk.Frame(window, bg="#0f172a")
main.pack(fill="both", expand=True, padx=20, pady=20)

# ------------------ LEFT CARD (Attendance) ------------------
left_card = tk.Frame(main, bg="#1e293b", bd=0)
left_card.place(relx=0.02, rely=0.02, relwidth=0.45, relheight=0.92)

tk.Label(
    left_card,
    text="📋 Attendance Panel",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

trackImg = tk.Button(
    left_card,
    text="🎥 Take Attendance",
    command=TrackImages,
    bg="#22c55e",
    fg="black",
    font=("Segoe UI", 13, "bold"),
    width=20
)
trackImg.pack(pady=10)

# Treeview
tv = ttk.Treeview(left_card, columns=("name", "date", "time"), height=14)
tv.heading("#0", text="ID")
tv.heading("name", text="Name")
tv.heading("date", text="Date")
tv.heading("time", text="Time")

tv.column("#0", width=80)
tv.column("name", width=150)
tv.column("date", width=120)
tv.column("time", width=120)

tv.pack(pady=20, padx=15, fill="x")

# Scrollbar
scroll = ttk.Scrollbar(left_card, orient="vertical", command=tv.yview)
tv.configure(yscrollcommand=scroll.set)
scroll.place(relx=0.96, rely=0.24, relheight=0.45)

quit_btn = tk.Button(
    left_card,
    text="❌ Exit",
    command=window.destroy,
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=20
)
quit_btn.pack(pady=20)

# ------------------ RIGHT CARD (Registration) ------------------
right_card = tk.Frame(main, bg="#1e293b", bd=0)
right_card.place(relx=0.50, rely=0.02, relwidth=0.48, relheight=0.92)

tk.Label(
    right_card,
    text="🧑 New Registration",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

tk.Label(right_card, text="Student ID", bg="#1e293b", fg="white", font=("Segoe UI", 12)).pack()
txt = ttk.Entry(right_card, width=30)
txt.pack(pady=5)

tk.Label(right_card, text="Student Name", bg="#1e293b", fg="white", font=("Segoe UI", 12)).pack()
txt2 = ttk.Entry(right_card, width=30)
txt2.pack(pady=5)

takeImg = tk.Button(
    right_card,
    text="📸 Take Images",
    command=TakeImages,
    bg="#38bdf8",
    fg="black",
    font=("Segoe UI", 13, "bold"),
    width=25
)
takeImg.pack(pady=15)

trainImg = tk.Button(
    right_card,
    text="💾 Save Profile",
    command=psw,
    bg="#a855f7",
    fg="white",
    font=("Segoe UI", 13, "bold"),
    width=25
)
trainImg.pack(pady=10)

message1 = tk.Label(
    right_card,
    text="1) Take Images  →  2) Save Profile",
    bg="#1e293b",
    fg="#22c55e",
    font=("Segoe UI", 11, "bold")
)
message1.pack(pady=10)

message = tk.Label(
    right_card,
    text="",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 11)
)
message.pack()

######################## END MODERN UI ########################
