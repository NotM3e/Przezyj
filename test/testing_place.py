import tkinter as tk
import time

class ScrollingInfoBar:
    def __init__(self, root, text, width=400, height=30, scroll_speed=2):
        self.root = root
        self.width = width
        self.height = height
        self.scroll_speed = scroll_speed

        self.canvas = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()

        self.text_id = self.canvas.create_text(0, height // 2, anchor=tk.W, text=text, font=("Arial", 12), fill="black")
        self.text_width = self.canvas.bbox(self.text_id)[2] - self.canvas.bbox(self.text_id)[0]

        self.start_scroll()

    def start_scroll(self):
        self.canvas.coords(self.text_id, self.width, self.height // 2)
        self.scroll_text()

    def scroll_text(self):
        x, y = self.canvas.coords(self.text_id)
        if x + self.text_width > 0:
            self.canvas.move(self.text_id, -self.scroll_speed, 0)
            self.root.after(10, self.scroll_text)
        else:
            self.start_scroll()

root = tk.Tk()
root.geometry("500x100")

scrolling_bar = ScrollingInfoBar(root, text="To jest pasek informacyjny przesuwający tekst z lewej do prawej.")
root.mainloop()
