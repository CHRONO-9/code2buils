import random
import tkinter as tk

def draw_omikuji():
    results = ["🌟 大吉！最高の1日！", "✨ 中吉！いいことあるかも", "🍀 吉！コツコツいこう"]
    label_result.config(text=random.choice(results))

# ウィンドウの作成
root = tk.Tk()
root.title("おみくじアプリ v2")
root.geometry("320x200")

label_title = tk.Label(root, text="今日の運勢を占おう！", font=("sans-serif", 14, "bold"))
label_title.pack(pady=15)

btn = tk.Button(root, text="おみくじを引く", font=("sans-serif", 12), command=draw_omikuji)
btn.pack(pady=10)

label_result = tk.Label(root, text="（ボタンを押してね）", font=("sans-serif", 13), fg="blue")
label_result.pack(pady=15)

root.mainloop()
