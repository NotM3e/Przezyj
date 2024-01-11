import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
import random

class Game():
    def __init__(self, root, play):
    # Root etc.
        self.root = root
        self.play = play
        self.root.title("Przeżyj!")
        self.root.configure(bg="#fff")
        self.root.minsize(270, 215)
        self.root.maxsize(650, 465)
        self.root.resizable(False, False)

        self.font_h1 = ("Arabic Transparent", 30)
        self.font_h2 = ("Arabic Transparent", 17)
        self.font_h3 = ("Arabic Transparent", 13)
        self.font_p1 = ("Arabic Transparent", 11)
        self.font_p2 = ("Arabic Transparent", 9)

        self.color_first = "#FFF"
        self.color_second = "#E9E9E9"
        self.color_third = "#DAD0D0"
        self.color_fourth = "#FFBBBB"
        self.color_fifth = "#DDDDBC"
        self.color_sixth = "#BBFFBD"

        self.create_start_gui()
        self.show_start_gui()

    def create_start_gui(self):
    # Main tab::
        self.start_frame = tk.Frame(self.root, bg=self.color_first)
        self.start_label = tk.Label(self.start_frame, text="Przeżyj!", font=self.font_h1, bg=self.color_first, height=2)
        self.start_button1 = tk.Button(self.start_frame, text="Informacje", font=self.font_p1, bg=self.color_second, width=15, command=lambda:
                                       [self.hide_frame(self.start_frame), self.info_frame.pack(fill=tk.BOTH, expand=True)])
        self.start_button2 = tk.Button(self.start_frame, text="Zacznij nową grę!", font=self.font_p1, bg=self.color_second, width=15, command=lambda:
                                       [self.hide_frame(self.start_frame), self.new_game()])
        self.start_button3 = tk.Button(self.start_frame, text="Wczytaj grę!", font=self.font_p1, bg=self.color_second, width=15, command=lambda:
                                       [self.hide_frame(self.start_frame), self.load_frame1.pack(fill=tk.BOTH, expand=True)])

    # Info tab:
        self.info_frame = tk.Frame(self.root, bg=self.color_first)
        self.info_label1 = tk.Label(self.info_frame, text="Informacje", font=self.font_h2, bg=self.color_first)
        self.info_label2 = tk.Label(self.info_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis ultrices dui. Nullam ac enim sed lectus egestas pharetra in sit amet neque. Aenean a pulvinar tortor, at pellentesque est. Etiam euismod ut massa non hendrerit. Donec eget nulla vitae tellus rutrum vestibulum auctor ac orci. Duis maximus ligula at erat varius porttitor. Nam magna erat, porttitor non nulla et, euismod placerat arcu. Fusce eu cursus dui, non laoreet tellus. Phasellus tincidunt nisi interdum diam ultricies iaculis. Vestibulum at porta purus.", font=self.font_p1, bg=self.color_first)
        self.info_button = tk.Button(self.info_frame, text="Wróć", font=self.font_p1, bg=self.color_second, width=15, command=lambda:
                                     [self.hide_frame(self.info_frame), self.start_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True)])
        self.info_frame.pack(fill=tk.BOTH, expand=True)
        self.info_label1.pack(pady=5)
        self.info_label2.pack(pady=5, fill="x")
        self.info_button.pack(ipady=2)

        self.info_frame.pack_forget()
        self.info_label2.bind("<Configure>", self.set_label_wrap)

    # Load save tab:
        self.load_frame1 = tk.Frame(self.root, bg=self.color_first)
        self.load_label1 = tk.Label(self.load_frame1, text="Zapisy", font=self.font_h2, bg=self.color_first)
        self.load_listbox = tk.Listbox(self.load_frame1, selectmode=tk.SINGLE, width=50, height=5)
        self.load_button1 = tk.Button(self.load_frame1, text="Wczytaj", font=self.font_p1, bg=self.color_second, width=15, command=self.load_save)
        self.load_button2 = tk.Button(self.load_frame1, text="Usuń", font=self.font_p1, bg=self.color_second, width=15, command=self.delate_save)
        self.load_button3 = tk.Button(self.load_frame1, text="Wróć", font=self.font_p1, bg=self.color_second, width=15, command=lambda:
                                     [self.hide_frame(self.load_frame1), self.start_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True), self.load_label2.config(text="")])
        self.load_frame2 = tk.Frame(self.load_frame1, bg=self.color_first)
        self.load_label2 = tk.Label(self.load_frame2, text="", font=self.font_p2, bg=self.color_first, wraplength=270)
        
        self.load_frame1.pack(fill=tk.BOTH, expand=True)
        self.load_label1.pack(pady=5)
        self.load_listbox.pack(padx=5, pady=5)
        self.load_button1.pack(ipady=2)
        self.load_button2.pack(ipady=2, pady=5)
        self.load_button3.pack(ipady=2)
        self.load_frame2.pack(fill=tk.BOTH, expand=True)
        self.load_label2.pack(pady=5, side=tk.LEFT)

        self.load_button1.bind("<Button-2>", self.create_save) # TEMP

        # Quest icon:
        self.question_icon = tk.PhotoImage(file="data/questionmark.png")
        self.question_canvas = tk.Canvas(self.load_frame2, width=32, height=32, bg=self.color_first, bd=0, highlightthickness=0)
        self.question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        self.question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości"))

        self.load_frame1.pack_forget()

    def show_start_gui(self):
        self.start_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True)
        self.start_label.pack()
        self.start_button1.pack(ipady=3)
        self.start_button2.pack(ipady=3, pady=5)
        self.start_button3.pack(ipady=3)

    def show_info_message(self, title, message):
        messagebox.showinfo(title, message)

    def set_label_wrap(self, event):
        wraplength = event.width-1
        event.widget.configure(wraplength=wraplength)

    def hide_frame(self, frame):
        frame.pack_forget()

    def question(self, quest, prev_func, next_func):
        self.new_game_frame = tk.Frame(self.root, bg=self.color_first)
        self.new_game_label1 = tk.Label(self.new_game_frame, text=quest, font=self.font_h3, bg=self.color_first, wraplength=350)
        self.new_game_frame1 = tk.Frame(self.new_game_frame, bg=self.color_first)
        self.new_game_button1 = tk.Button(self.new_game_frame1, text="Nie", font=self.font_p1, bg=self.color_second, width=8, command=lambda:
                                          [self.hide_frame(self.new_game_frame), prev_func()])
        self.new_game_button2 = tk.Button(self.new_game_frame1, text="Tak", font=self.font_p1, bg=self.color_second, width=8, command=lambda:
                                          [self.hide_frame(self.new_game_frame), next_func()])

        self.new_game_frame.pack(expand=True)
        self.new_game_label1.pack(pady=20)
        self.new_game_frame1.pack(expand=True)
        self.new_game_button1.pack(side=tk.LEFT, padx=5, ipady=4)
        self.new_game_button2.pack(side=tk.LEFT, padx=5, ipady=4)

    def new_game(self):
        self.question("Czy napewno chcesz rozpocząć nową grę?", self.show_start_gui, self.create_statistics)

    def create_statistics(self):
    # Statistics on the world in the game:
        print("TEST")
        self.stats = {
            "day": 0,
            "money": round(random.uniform(9.90, 21.90), 2),
            "work": 0,
            "intelligence": 10,
            "strength": 10,
            "stamina": 10
        }

    # Manipulation of the game's chances:
        self.manipulation = {
            "luck": 10,
        }

    # Player needs in the game:
        self.player_needs = {         # max 100 for each
            "thirst": 100,
            "hunger": 100,
            "fatigue": 100
        }
        # UPDATE Create save.txt in data/saves/
        self.create_save(None) # TEMP None


        # self.create_maingame()

    def create_save(self, event): # TEMP None
        today = date.today()
        time_now = datetime.now()
        save_title = "save_title"
        current_date = today.strftime("%d/%m/%Y")
        current_time = time_now.strftime("%H:%M:%S")
        test = f"{save_title} - {current_date} {current_time}"
        self.load_listbox.insert(tk.END, test)

    def load_save(self):
        selected_index = self.load_listbox.curselection()

        if not selected_index:
            self.load_label2.config(text="Wybierz zapis do wczytania")
            return

        self.load_label2.config(text="Wczytywanie.")
    def delate_save(self):
        selected_index = self.load_listbox.curselection()

        if not selected_index:
            self.load_label2.config(text="Wybierz zapis do usunięcia")
            return
        
        # Remove the selected item from the listbox
        self.load_listbox.delete(selected_index)
        self.load_label2.config(text="Usunięto zapis")

    def create_maingame(self):
        self.mg_button1 = tk.Button(self.root, text="Następny dzień", command=self.next_day)
        self.mg_button1.pack()

    def next_day(self):
        self.stats["day"] += 1
        print(f"day = {self.stats['day']}")


root = tk.Tk()
play = True
game = Game(root, play)
root.mainloop()