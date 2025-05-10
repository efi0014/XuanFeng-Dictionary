import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

# 新增：资源路径处理函数
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # 打包后的临时资源目录
    except AttributeError:
        base_path = os.path.abspath(".")  # 开发环境当前目录
    return os.path.join(base_path, relative_path)

# 主窗口
root = tk.Tk()
root.title("主窗口")
root.geometry("772x693")
root.resizable(True, True)

def open_new_window():
    root.withdraw()
    show_image_window()

# 创建按钮（修改路径）
image = Image.open(resource_path("1.png"))  # 使用resource_path
resized_image = image.resize((200, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)
btn = tk.Button(root, image=photo, command=open_new_window)
btn.place(relx=0.5, rely=0.5, anchor='center')

def show_image_window():
    new_win = tk.Toplevel()
    new_win.title("图片窗口")
    new_win.geometry("1400x1000")
    new_win.resizable(True, True)

    # 加载并填充窗口的图片（修改路径）
    bg_image = Image.open(resource_path("abcd.png"))  # 使用resource_path
    bg_resized = bg_image.resize((1400, 1000), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_resized)

    bg_label = tk.Label(new_win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ...（其余代码不变）

    # 变量定义
    x_var = tk.IntVar(value=0)
    x1_var = tk.IntVar()

    def update_x1(*args):
        x1_var.set(x_var.get() + 1)

    x_var.trace_add("write", update_x1)

    # 控件定义
    label_x = tk.Label(new_win, textvariable=x_var, font=("Arial", 20), bg="white")
    label_x1 = tk.Label(new_win, textvariable=x1_var, font=("Arial", 20), bg="white")

    btn_forward = tk.Button(new_win, text="前进", font=("Arial", 16))
    btn_back = tk.Button(new_win, text="悬锋人的字典里没有后退", font=("Arial", 16))

    # 动态调整位置的函数
    def update_positions(event=None):
        window_width = new_win.winfo_width()
        # 定义左右边距（可调整）
        left_margin = 50
        right_margin = 350
        label_left = 25
        label_right = window_width - 20  # 右侧标签距右20像素

        # 更新控件位置
        btn_forward.place(x=left_margin, y=900)
        btn_back.place(x=window_width - right_margin, y=900)
        label_x.place(x=label_left, y=908)
        label_x1.place(x=label_right, y=908)

    # 绑定窗口尺寸变化事件
    new_win.bind('<Configure>', update_positions)
    # 初始布局
    update_positions()

    # 按钮命令绑定
    btn_forward.config(command=lambda: x_var.set(x_var.get() + 1) if x_var.get() < 99 else None)
    btn_back.config(command=lambda: x_var.set(x_var.get() - 1) if x_var.get() > 0 else None)

root.mainloop()
