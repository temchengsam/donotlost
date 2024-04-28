import os
import random
import tkinter as tk
from tkinter import messagebox

# 遊戲選項
choices = ["剪刀", "石头", "布"]

# 判斷遊戲結果的邏輯
def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (
        (user_choice == "剪刀" and computer_choice == "布") or
        (user_choice == "石头" and computer_choice == "剪刀") or
        (user_choice == "布" and computer_choice == "石头")
    ):
        return "你贏了！"
    else:
        return "你輸了"

# 建立主窗口
root = tk.Tk()
root.title("剪刀石頭布")
root.geometry("400x300")  # 設定窗口大小
root.configure(bg="#f0f0f0")  # 設定背景色

# 生成結果標籤
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
result_label.pack(pady=20)

# 定義按鈕點擊事件
def on_choice_click(user_choice):
    computer_choice = random.choice(choices)
    result = check_winner(user_choice, computer_choice)

    # 更新結果標籤
    result_label.config(
        text=f"你選了：{user_choice}\n電腦選了：{computer_choice}\n結果：{result}",
        fg="black",
    )

    # 如果結果是用戶輸了，彈出一個提示框
    if result == "你輸了":
        messagebox.showinfo("遊戲結果", "很遺憾，你輸了。再試一次吧！")

# 添加按鈕框架
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=20)

# 剪刀按鈕
scissors_btn = tk.Button(
    buttons_frame,
    text="剪刀",
    command=lambda: on_choice_click("剪刀"),
    font=("Arial", 14),
    width=10,
    bg="#d3d3d3",
    fg="black",
)
scissors_btn.pack(side=tk.LEFT, padx=10)

# 石頭按鈕
rock_btn = tk.Button(
    buttons_frame,
    text="石头",
    command=lambda: on_choice_click("石头"),
    font=("Arial", 14),
    width=10,
    bg="#d3d3d3",
    fg="black",
)
rock_btn.pack(side=tk.LEFT, padx=10)

# 布按鈕
paper_btn = tk.Button(
    buttons_frame,
    text="布",
    command=lambda: on_choice_click("布"),
    font=("Arial", 14),
    width=10,
    bg="#d3d3d3",
    fg="black",
)
paper_btn.pack(side=tk.LEFT, padx=10)

# 啟動主程序
root.mainloop()