import tkinter as tk
from tkinter import messagebox

class Game():
    def __init__(self, root, play):
        self.root = root
        self.play = play
        self.root.title("Przeżyj!")
        self.root.configure(bg="#fff")
        self.root.minsize(270, 170)
        self.root.maxsize(650, 265)

        self.load_frame = tk.Frame(self.root, bg="blue")
        self.load_label1 = tk.Label(self.load_frame, text="Wczytaj", font=("Courier New Baltic", 14), bg="blue")
        self.load_listbox = tk.Listbox(self.load_frame, selectmode=tk.SINGLE, width=50, height=5)
        self.load_button1 = tk.Button(self.load_frame, text="Wczytaj", font=("Courier New Baltic", 12), bg="green", width=15, command=self.load_game)
        self.load_button2 = tk.Button(self.load_frame, text="Wróć", font=("Courier New Baltic", 12), bg="green", width=15, command=lambda: [self.hide_frame(self.load_frame), self.start_frame.pack(fill=tk.BOTH, expand=True)])

        self.load_frame.pack(fill=tk.BOTH, expand=True)
        self.load_label1.pack(pady=5)
        self.load_listbox.pack()
        self.load_button1.pack(ipady=2, pady=5)
        self.load_button2.pack(ipady=2)

        # Dodanie ikony pytajnika w prawym dolnym rogu
        self.question_icon = tk.PhotoImage(file="questionmark.png")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.question_canvas = tk.Canvas(self.root, width=32, height=32, bg="#fff", bd=0, highlightthickness=0)
        self.question_canvas.create_image(screen_width - 16, screen_height - 16, anchor=tk.SE, image=self.question_icon)
        self.question_canvas.pack()

        # Powiązanie zdarzenia kliknięcia ikony pytajnika
        self.question_canvas.bind("<Button-1>", self.show_info_message)

    def show_info_message(self, event):
        # Wyświetlenie messagebox po kliknięciu ikony pytajnika
        messagebox.showinfo("Informacja", "To jest dodatkowa informacja!")

    def load_game(self):
        # Obsługa wczytywania gry
        print("Wczytywanie gry...")

    def hide_frame(self, frame):
        frame.pack_forget()

root = tk.Tk()
play = True
game = Game(root, play)

root.mainloop()
