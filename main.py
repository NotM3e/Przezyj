import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime
import random
import os
import time

class Game():
    def __init__(self, root):
    # Root etc.
        self.root = root
        self.root.title("Przeżyj!")
        self.root.configure(bg="#fff")
        self.root.minsize(270, 215)
        self.root.maxsize(650, 465)
        self.root.resizable(False, False) # TEMP

        self.font_h1 = ("Segoe UI Black", 30)
        self.font_h2 = ("Segoe UI Semibold", 17)
        self.font_h3 = ("Microsoft YaHei", 13)
        self.font_p1 = ("Microsoft YaHei", 12)
        self.font_p1b = ("Microsoft YaHei", 12, "bold")
        self.font_p2 = ("Microsoft YaHei", 9)
        self.font_p2i = ("Arabic Transparent", 9, "italic")

        self.color_1 = "#1E2F4F"    # Main backgorund
        self.color_2 = "#35426D"    # Lighter main
        self.color_3 = "#1F2C44"    # Shadow border
        self.color_4 = "#FFFFFF"    # White
        self.color_5 = "#CACACA"    # Gray

        self.color_11 = "#FFBBBB"   # red
        self.color_12 = "#DDDDBC"   # Yellow
        self.color_13 = "#BBFFBD"   # Green

        self.question_icon = tk.PhotoImage(file="data/img/questionmark.png")

        self.root_main = tk.Frame(self.root, bg=self.color_1)
        self.root_main.pack(fill=tk.BOTH, expand=True)
        self.last_save = []
        self.root_second_opened = 0
        self.root_third_opened = False

        # self.create_statistics() # TEMP

        self.create_start_gui() # TEMP
        self.show_start_gui()   # TEMP

    def create_start_gui(self):
    # Main tab:
        self.start_frame = tk.Frame(self.root_main, bg=self.color_1)

        self.start_logo_icon = tk.PhotoImage(file="data/img/przezyj.png")
        self.start_logo_canvas = tk.Canvas(self.start_frame, bg=self.color_1, bd=0, highlightthickness=0, width=418, height=190)
        self.start_logo_canvas.create_image(209, 95, anchor=tk.CENTER, image=self.start_logo_icon)
        self.start_logo_canvas.pack(anchor=tk.CENTER)

        self.start_button1 = tk.Button(self.start_frame, text="Informacje", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.info_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True)])
        self.start_button2 = tk.Button(self.start_frame, text="Zacznij nową grę!", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.new_game()])
        self.start_button3 = tk.Button(self.start_frame, text="Wczytaj grę!", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.load_saves(self.load_listbox), self.load_frame1.pack(padx=3, pady=2, fill=tk.BOTH, expand=True)])
        self.start_button4 = tk.Button(self.start_frame, text="Osiągnięcia", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.achiv_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True)])

    # Info tab:
        self.info_frame = tk.Frame(self.root_main, bg=self.color_1)
        self.info_label1 = tk.Label(self.info_frame, text="Informacje", font=self.font_h2, fg=self.color_4, bg=self.color_1)
        self.info_label2 = tk.Label(self.info_frame, text="Przeżywaj jak najwięcej dni! Osiągaj cele, wykonuj interaktywne zadania, dbaj o postać, rozwijaj wiedzę. Zapisuj swój postęp, korzystaj z punktów informacyjnych, gdy się zagubisz. Uważaj na losowe zdarzenia! Utrzymaj się jak najdłużej przy życiu!", font=self.font_p1, fg=self.color_4, bg=self.color_1, wraplength=630)
        self.info_button = tk.Button(self.info_frame, text="Wróć", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.info_frame), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])

        self.info_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.info_label1.pack(pady=5)
        self.info_label2.pack(padx=3, pady=5, fill="x")
        self.info_button.pack(ipady=2, pady=4)

        self.info_frame.pack_forget()
        # self.info_label2.bind("<Configure>", self.set_label_wrap)

    # Load save tab:
        self.load_frame1 = tk.Frame(self.root_main, bg=self.color_1)
        self.load_label1 = tk.Label(self.load_frame1, text="Wczytaj grę", font=self.font_h2, fg=self.color_4, bg=self.color_1)
        self.load_listbox = tk.Listbox(self.load_frame1, selectmode=tk.SINGLE, width=55, height=5)
        self.load_button1 = tk.Button(self.load_frame1, text="Wczytaj", font=self.font_p1, bg=self.color_5, width=15, command=self.selected_load_save)
        self.load_button2 = tk.Button(self.load_frame1, text="Usuń", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                self.selected_delate_save(self.load_listbox, self.load_label2))
        self.load_button3 = tk.Button(self.load_frame1, text="Wróć", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.load_frame1), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.load_label2.config(text="")])
        self.load_frame2 = tk.Frame(self.load_frame1, bg=self.color_1)
        self.load_label2 = tk.Label(self.load_frame2, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=270)
        
        self.load_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.load_label1.pack(pady=5)
        self.load_listbox.pack(padx=5, pady=5)
        self.load_button1.pack(ipady=2)
        self.load_button2.pack(ipady=2, pady=5)
        self.load_button3.pack(ipady=2)
        self.load_frame2.pack(fill=tk.BOTH, expand=True)
        self.load_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        # Question icon
        self.load_question_canvas = tk.Canvas(self.load_frame2, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.load_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.load_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        self.load_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Wczytywanie!", "Wczytaj swoją przygodę! W każdym momencie możesz załadować swój postęp, jednak pamiętaj, że w przypadku śmierci wszystkie zapisane dane związane z tą sesją zostaną usunięte. Graj ostrożnie i korzystaj z tej możliwości mądrze!")) # TEMP usuwanie save kiedyś zmienić

        self.load_frame1.pack_forget()
        self.load_saves(self.load_listbox)

    # Achievements tab:
        self.achiv_frame = tk.Frame(self.root_main, bg=self.color_1)
        self.achiv_label1 = tk.Label(self.achiv_frame, text="Osiągnięcia", font=self.font_h2, fg=self.color_4, bg=self.color_1)
        self.achiv_label2 = tk.Label(self.achiv_frame, text="Work in progress", font=self.font_p2, fg=self.color_4, bg=self.color_1)
        self.achiv_button = tk.Button(self.achiv_frame, text="Wróć", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.achiv_frame), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])

        self.achiv_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.achiv_label1.pack(pady=5)
        self.achiv_label2.pack(padx=3, pady=5, fill="x")
        self.achiv_button.pack(ipady=2, pady=4)

        self.achiv_frame.pack_forget()

    def show_start_gui(self):
        self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.start_button1.pack(ipadx=11, ipady=5, pady=4)
        self.start_button2.pack(ipadx=11, ipady=5, pady=4)
        self.start_button3.pack(ipadx=11, ipady=5, pady=4)
        self.start_button4.pack(ipadx=11, ipady=5, pady=4)

        self.last_save = []
        self.root_x()
        print(self.last_save)

    def show_info_message(self, title, message):
        messagebox.showinfo(title, message)

    def capitalize_first_letter(self, text):
        return text[0].upper() + text[1:]

    def set_label_wrap(self, event):
        wraplength = event.width-12
        event.widget.configure(wraplength=wraplength)

    def hide_frame(self, *frames):
        for frame in frames:
            frame.pack_forget()

    def intermediary(self, label, value, next_func = None, arg = None):
        label.config(text=value)
        if next_func:
            next_func(arg)

    def id_name_job(self, id):
        jobs = {
            0: ("Bezrobotny", "brak"),
            1: ("Magazyn", "Pakowacz"),
            2: ("Magazyn", "Magazynier"),
            3: ("Magazyn", "Operator wózka widłowego"),
            4: ("Magazyn", "Kierownik magazynu")
        }
        if id in jobs:
            return jobs[id]
        else:
            return "NULL", "NULL"

    def new_game(self):
        self.question(self.root_main, "Czy napewno chcesz rozpocząć nową grę?", self.show_start_gui, self.create_statistics)
        
    def question(self, frame, quest, prev_func, next_func):
        self.question_frame = tk.Frame(frame, bg=self.color_1)
        self.question_label1 = tk.Label(self.question_frame, text=quest, font=self.font_h3, fg=self.color_4, bg=self.color_1, wraplength=450)
        self.question_frame1 = tk.Frame(self.question_frame, bg=self.color_1)
        self.question_button1 = tk.Button(self.question_frame1, text="Nie", font=self.font_p1, bg=self.color_5, width=8, command=lambda:
                [self.hide_frame(self.question_frame), prev_func()])
        self.question_button2 = tk.Button(self.question_frame1, text="Tak", font=self.font_p1, bg=self.color_5, width=8, command=lambda:
                [self.hide_frame(self.question_frame), next_func()])

        self.question_frame.pack(padx=3, pady=10, expand=True)
        self.question_label1.pack(pady=20)
        self.question_frame1.pack(expand=True)
        self.question_button1.pack(padx=5, ipady=4, side=tk.LEFT)
        self.question_button2.pack(padx=5, ipady=4, side=tk.LEFT)

    def small_question(self, frame, quest, next_func, *arg):
        print("small_question")
        label = self.find_label(frame)
        if label:
            label.config(text="")
        
        self.s_question_frame = tk.Frame(frame, bg=self.color_1)
        self.s_question_label1 = tk.Label(self.s_question_frame, text=quest, font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=450)
        self.s_question_frame1 = tk.Frame(self.s_question_frame, bg=self.color_1)
        self.s_question_button1 = tk.Button(self.s_question_frame1, text="Nie", font=self.font_p2, bg=self.color_5, width=5, command=lambda:
                [self.hide_frame(self.s_question_frame)])
        self.s_question_button2 = tk.Button(self.s_question_frame1, text="Tak", font=self.font_p2, bg=self.color_5, width=5, command=lambda:
                [self.hide_frame(self.s_question_frame), next_func(*arg)])

        self.s_question_frame.pack(expand=True)
        self.s_question_label1.pack(pady=2)
        self.s_question_frame1.pack(expand=True)
        self.s_question_button1.pack(padx=5, side=tk.LEFT)
        self.s_question_button2.pack(padx=5, side=tk.LEFT)

    def find_label(self, frame):
        for child in frame.winfo_children():  # Iteracja przez dzieci ramki
            if isinstance(child, tk.Label):  # Sprawdzenie czy dziecko jest etykietą
                return child  # Zwrócenie etykiety, jeśli zostanie znaleziona
        return None  # Zwrócenie None, jeśli nie znajdziemy etykiety

    def create_statistics(self):
    # Statistics on the world in the game:
        self.stats = {
            "life": True,
            "day": 0,
            "money": round(random.uniform(9.90, 21.90), 2),
            "work": 0,
            "duty": False,
            "intelligence": 10,
            "strength": 10,
            "stamina": 10,
            "luck": 10,
            "thirst": 100,
            "hunger": 99,
            "fatigue": 98,
            "water": 5,
            "baguette": 3,
            "creamery": 1,
            "newspaper": False,
            "scratch card": 0,
            "lastpayment": 0,
            "internship": 0,
            "deathr": "???"
        }

        self.last_save = []
        self.create_maingame()


# Saving game:

    # Loading saves at start program or called when player want refresh listbox
    def load_saves(self, listbox):
        # Delating current info from listbox
        listbox.delete(0, tk.END)
        
        # Loading records into the Listbox
        file_list = sorted(os.listdir("saves"))
        for fil in file_list:
            with open(f"saves/{fil}", "r") as file:
                label = file.readline().strip()
                listbox.insert(tk.END, label)
    
    def save_game(self):
        save_title = self.maingame_save_entry1.get()
        if not save_title:
            self.maingame_save_label3.config(text="Wpisz tytuł zapisu")
            return
        
        n = 1
        while os.path.exists(f"saves/save{n}.txt"):
            n += 1

        save_filename = f"saves/save{n}.txt"
        with open(save_filename, "w") as file:
            # Zapisywanie etykiety
            now = datetime.datetime.now()
            label = f"{save_title} - {now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
            file.write(label + "\n")

            # Zapisywanie statystyk
            stats_str = "\n".join([f"{key}: {value}" for key, value in self.stats.items()])
            file.write(stats_str + "\n")

        # Dodawanie zapisu do listboxa
        self.maingame_save_listbox.insert(tk.END, label)
        self.maingame_save_label3.config(text=f"Zapisano save pod nazwą {save_title}")
        self.last_save.append(save_filename)
        print(self.last_save)

    def selected_load_save(self, index = None):
        if not index:
            selected_index = self.load_listbox.curselection()
            if not selected_index:
                self.load_label2.config(text="Wybierz zapis do wczytania")
                return
            else:
                selected_index = selected_index[0]
        else:
            selected_index = index

        self.load_label2.config(text="Wczytywanie")
        filename = f"saves/save{selected_index + 1}.txt"

        if not os.path.exists(filename):
            self.selected_load_save(selected_index + 1)
            return

        # Wczytywanie gry z pliku
        with open(filename, "r") as file:
            # Wczytywanie etykiety
            label = file.readline().strip()
            print(label)

            # Wczytywanie statystyk
            self.stats = {}

            current_dict = self.stats

            for line in file:
                line = line.strip()
                key, value_str = map(str.strip, line.split(": "))

                if value_str.lower() == "true" or value_str.lower() == "false":
                    value = value_str.lower() == "true"

                elif value_str.isdigit():
                    value = int(value_str)

                elif value_str.replace('.', '', 1).isdigit():
                    value = float(value_str)

                else:
                    value = value_str

                current_dict[key] = value

        print("Wczytano statystyki:")
        print("Stats:", self.stats)
        self.hide_frame(self.load_frame1)
        self.create_maingame()
        self.load_label2.config(text="")

        self.last_save.append(filename)
        print(self.last_save)

    def selected_delate_save(self, listbox, command_log, index = None):
        if not index:
            selected_index = listbox.curselection()
            if not selected_index:
                command_log.config(text="Wybierz zapis do usunięcia")
                return
            else:
                selected_index = selected_index[0]
        else:
            selected_index = index

        filename = f"saves/save{selected_index + 1}.txt"

        if not os.path.exists(filename):
            self.selected_delate_save(listbox, command_log, selected_index + 1)

        listbox.delete(selected_index)
        os.remove(filename)
        command_log.config(text="Usunięto zapis")

        if filename in self.last_save:
            self.last_save.remove(filename)
            print(self.last_save)
        else:
            print("selected_delate_save - self.last_save - ERROR")

    def validate_input(self, new_text, max_chars):
        # Sprawdź, czy nowy tekst nie przekracza maksymalnej liczby znaków
        return len(new_text) <= max_chars


# Main game:

    def create_maingame(self):
    # Main tab:
        # Loading images
        self.maingame_debug_icon = tk.PhotoImage(file="data/img/debug1.png")
        self.maingame_save_icon = tk.PhotoImage(file="data/img/save1.png")
        self.maingame_home_icon = tk.PhotoImage(file="data/img/home1.png")
        self.maingame_settings_icon = tk.PhotoImage(file="data/img/settings1.png")

        # Create of statistical elements
        self.maingame_frame0 = tk.Frame(self.root_main, bg=self.color_1)
        self.maingame_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_frame2 = tk.Frame(self.maingame_frame1, bg=self.color_2, highlightbackground=self.color_3, highlightthickness=2)
        self.maingame_stats_label1 = tk.Label(self.maingame_frame2, text="Dzień", font=self.font_p2i, fg=self.color_5, bg=self.color_2)
        self.maingame_stats_label2 = tk.Label(self.maingame_frame2, text="Pieniądze", font=self.font_p2i, fg=self.color_5, bg=self.color_2)
        self.maingame_stats_label3 = tk.Label(self.maingame_frame2, text=self.stats["day"], font=self.font_p1b, fg=self.color_4, bg=self.color_2)
        self.maingame_stats_label4 = tk.Label(self.maingame_frame2, text=f"{self.stats["money"]} PLN", font=self.font_p1b, fg=self.color_4, bg=self.color_2)

        # Configure grid columns
        self.maingame_frame2.grid_columnconfigure(0, weight=1)
        self.maingame_frame2.grid_columnconfigure(1, weight=2)
        self.maingame_frame2.grid_columnconfigure(2, weight=0)
        self.maingame_frame2.grid_columnconfigure(4, weight=0)
        self.maingame_frame2.grid_columnconfigure(6, weight=0)

        # Create images
        self.maingame_debug_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_2, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_debug_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_debug_icon)
        self.maingame_save_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_2, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_save_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_save_icon)
        self.maingame_home_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_2, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_home_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_home_icon)
        self.maingame_settings_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_2, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_settings_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_settings_icon)

        # Visualisation of images
        self.maingame_debug_canvas.grid(row=0, column=2, rowspan=2, columnspan=2, padx=5)
        self.maingame_save_canvas.grid(row=0, column=4, rowspan=2, columnspan=2, padx=5)
        self.maingame_home_canvas.grid(row=0, column=6, rowspan=2, columnspan=2, padx=5)
        self.maingame_settings_canvas.grid(row=0, column=8, rowspan=2, columnspan=2, padx=5)

        # Creating a moving label
        self.maingame_frame3 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_frame3_canvas = tk.Canvas(self.maingame_frame3, width=594, height=22, bg=self.color_1, highlightthickness=0)
        self.maingame_text_id = self.maingame_frame3_canvas.create_text(0, 22 // 2, anchor=tk.W, text="", font=("Arial", 12), fill="white")
        self.maingame_text_width = self.maingame_frame3_canvas.bbox(self.maingame_text_id)[2] - self.maingame_frame3_canvas.bbox(self.maingame_text_id)[0]

        # Create of main elements
        self.maingame_frame4 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_frame5 = tk.Frame(self.maingame_frame4, bg=self.color_1)
        self.maingame_frame6 = tk.Frame(self.maingame_frame4, bg=self.color_1)
        self.maingame_frame7 = tk.Frame(self.maingame_frame4, bg=self.color_1)
        self.maingame_button1 = tk.Button(self.maingame_frame6, text="Następny dzień", font=self.font_p1, bg=self.color_5, width=15, command=self.next_day)
        self.maingame_button2 = tk.Button(self.maingame_frame6, text="Sklep", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.create_root_second(1)])
        self.maingame_button3 = tk.Button(self.maingame_frame6, text="Praca", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.create_root_second(2)])
        self.maingame_button4 = tk.Button(self.maingame_frame6, text="Statystyki", font=self.font_p1, bg=self.color_5, width=15)
        self.maingame_frame8 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_label5 = tk.Label(self.maingame_frame8, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=550)

        # Create of needs elements
        self.maingame_frame5_1 = tk.Frame(self.maingame_frame5, bg=self.color_1, highlightbackground=self.color_5, highlightthickness=2)
        self.maingame_frame5_1label = tk.Label(self.maingame_frame5_1, text="Potrzeby postaci:", font=self.font_p1, fg=self.color_4, bg=self.color_1, width=17)
        self.maingame_frame5_1frame1 = tk.Frame(self.maingame_frame5_1, bg=self.color_1, highlightbackground=self.color_5, highlightthickness=1)
        self.maingame_frame5_1frame2 = tk.Frame(self.maingame_frame5_1frame1, bg=self.color_1)
        self.maingame_frame5_1_label1 = tk.Label(self.maingame_frame5_1frame2, text="Pragnienie", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.maingame_frame5_1_progressbar1 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)
        self.maingame_frame5_1_label2 = tk.Label(self.maingame_frame5_1frame2, text="Głód", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.maingame_frame5_1_progressbar2 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)
        self.maingame_frame5_1_label3 = tk.Label(self.maingame_frame5_1frame2, text="Zmęczenie", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.maingame_frame5_1_progressbar3 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)

        # Configure grid columns
        self.maingame_frame5_1frame2.grid_columnconfigure(0, weight=1)
        self.maingame_frame5_1frame2.grid_rowconfigure(0, weight=0)

        # Create of equipment elements
        self.maingame_frame5_2 = tk.Frame(self.maingame_frame7, bg=self.color_1, highlightbackground=self.color_5, highlightthickness=2)
        self.maingame_frame5_2label = tk.Label(self.maingame_frame5_2, text="Ekwipunek postaci:", font=self.font_p1, fg=self.color_4, bg=self.color_1, width=17)
        self.maingame_frame5_2frame1 = tk.Frame(self.maingame_frame5_2, bg=self.color_1, highlightbackground=self.color_5, highlightthickness=1)
        self.maingame_frame5_2frame2 = tk.Frame(self.maingame_frame5_2frame1, bg=self.color_1)
        self.create_item_frames()

        # Visualisation of statistical elements
        self.maingame_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
        self.maingame_frame2.pack(fill="x", side=tk.TOP, anchor=tk.N, ipady=3, ipadx=3)
        self.maingame_stats_label1.grid(row=0, column=0, padx=5)
        self.maingame_stats_label2.grid(row=0, column=1, padx=5)
        self.maingame_stats_label3.grid(row=1, column=0, padx=5, ipady=3)
        self.maingame_stats_label4.grid(row=1, column=1, padx=5, ipady=3)

        # Visualisation a moving label
        self.maingame_frame3.pack(fill="x")
        self.maingame_frame3_canvas.pack()

        # Visualisation of main elements
        self.maingame_frame4.pack(fill=tk.BOTH, expand=True)
        self.maingame_frame5.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.maingame_frame6.pack(expand=True, side=tk.LEFT, padx=30)
        self.maingame_frame7.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)
        self.maingame_button1.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button2.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button3.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button4.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_frame8.pack(fill=tk.BOTH, expand=True)
        self.maingame_label5.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        # Visualisation of needs elements
        self.maingame_frame5_1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame5_1label.pack()
        self.maingame_frame5_1frame1.pack(fill=tk.BOTH, expand=True)
        self.maingame_frame5_1frame2.pack(expand=True)
        self.maingame_frame5_1_label1.grid(row=0, column=0)
        self.maingame_frame5_1_progressbar1.grid(row=1, column=0)
        self.maingame_frame5_1_label2.grid(row=2, column=0)
        self.maingame_frame5_1_progressbar2.grid(row=3, column=0)
        self.maingame_frame5_1_label3.grid(row=4, column=0)
        self.maingame_frame5_1_progressbar3.grid(row=5, column=0)

        # Visualisation of equipment elements
        self.maingame_frame5_2.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame5_2label.pack()
        self.maingame_frame5_2frame1.pack(fill=tk.BOTH, expand=True)
        self.maingame_frame5_2frame2.pack(expand=True)

        # Question icon
        self.maingame_question_canvas = tk.Canvas(self.maingame_frame8, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.maingame_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.maingame_question_canvas.pack(padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        # Binds
        self.maingame_debug_canvas.bind("<Button-1>", lambda event: [
                self.pre_work(self.stats["work"]), print(self.stats["internship"])])
        self.maingame_debug_canvas.bind("<Button-2>", lambda event: [
                self.increase_stats(["intelligence","strength", "stamina"], 10), print(self.stats), self.pre_work(2)])
        self.maingame_question_canvas.bind("<Button-1>", lambda event:
                self.show_info_message("Informacja!", "W głównej części gry masz możliwość przechodzenia do następnego dnia, kontynuując swoją przygodę, zapewniania swoich podstawowych potrzeb, takich jak jedzenie, picie i odpoczynek, sprawdzania swoich statystyk, aby monitorować postęp, przechodzenia do różnych miejsc, takich jak praca czy sklep, aby wykonywać zadania lub kupować potrzebne przedmioty, oraz sprawdzania swojego ekwipunku, zarządzania przedmiotami i dostosowywania ich do zmieniających się sytuacji."))
        self.maingame_save_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame1),
                 self.maingame_save_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.load_saves(self.maingame_save_listbox)])
        self.maingame_home_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame0),
                 self.question(self.root_main, "Czy na pewno chcesz wrócić do menu głównego?", (lambda: self.maingame_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)), self.show_start_gui)])

        # Payments ranges:
        self.ranges_payment = {
            0: 10,
            1: 20,
            2: 30,
            3: 40,
            4: 55
        }
        
        # Items needs ranges:
        self.ranges_water = {
            "water": (35, 50),
            "creamery": (5, 10)
        }
        self.ranges_hunger = {
            "baguette": (35, 55),
            "creamery": (20, 30)
        }
        self.ranges_fatigue = {
            "creamery": (5, 10)
        }

        # Work ranges fatigue:
        self.work_ranges_fatigue = {
            0: (0, 0),      # Bezrobotny
            1: (16, 22),    # Pakowacz na magazynie
            2: (17, 25),    # Magazynier
            3: (16, 20),    # Operator wózka widłowego
            4: (15, 19)     # Kierownik magazynu
        }

        # Products prices:
        self.products_prices = {
            "water": [1.19, 1.49, 1.69, 1.75, 1.79, 1.85, 1.89, 1.95, 1.99, 2.09, 2.19],
            "baguette": [2.99, 3.29, 3.35, 3.39, 3.45, 3.49, 3.55, 3.59, 3.65, 3.69, 3.75, 3.79, 3.89, 3.99],
            "creamery": [5.99, 6.99, 7.29, 7.39, 7.59, 7.69, 7.79, 7.89, 7.99, 8.19, 8.29, 8.39, 8.99],
            "newspaper": [5.99, 6.49, 6.55, 6.59, 6.69, 6.79, 6.99],
            "scratch card": [5.00]
        }
        
        # Skills requirements for job:
        # id: (intelligence, strength, stamina)
        self.jobs_require_ranges = {
            0: (5, 5, 5),       # Bezrobotny
            1: (10, 10, 10),    # Pakowacz na magazynie
            2: (15, 20, 20),    # Magazynier
            3: (20, 25, 20),    # Operator wózka widłowego
            4: (45, 25, 20)     # Kierownik magazynu
        }

        self.last_begging = self.stats["day"] - 1
        self.product_day = self.stats["day"] - 1

        self.refresh_stats()
        self.refresh_data()

    # Save tab:
        validate_cmd = (self.root.register(lambda new_text, max_chars=20: self.validate_input(new_text, max_chars)), '%P')

        self.maingame_save_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_save_label1 = tk.Label(self.maingame_save_frame1, text="Zapisy gry", font=self.font_h2, fg=self.color_4, bg=self.color_1)
        self.maingame_save_listbox = tk.Listbox(self.maingame_save_frame1, selectmode=tk.SINGLE, width=55, height=5)
        self.maingame_save_label2 = tk.Label(self.maingame_save_frame1, text="Wpisz nazwe zapisu:", font=self.font_p2i, fg=self.color_4, bg=self.color_1)
        self.maingame_save_entry1 = tk.Entry(self.maingame_save_frame1, validate="key", validatecommand=validate_cmd, width=40)
        self.maingame_save_button1 = tk.Button(self.maingame_save_frame1, text="Zapisz", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.save_game(), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button2 = tk.Button(self.maingame_save_frame1, text="Usuń", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.selected_delate_save(self.maingame_save_listbox, self.maingame_save_label3), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button3 = tk.Button(self.maingame_save_frame1, text="Wróć", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.hide_frame(self.maingame_save_frame1), self.maingame_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=2), self.maingame_save_label3.config(text="")])
        self.maingame_save_frame2 = tk.Frame(self.maingame_save_frame1, bg=self.color_1)
        self.maingame_save_label3 = tk.Label(self.maingame_save_frame2, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=270)

        self.maingame_save_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_save_label1.pack()
        self.maingame_save_listbox.pack(padx=5, pady=5)
        self.maingame_save_label2.pack()
        self.maingame_save_entry1.pack(pady=3)
        self.maingame_save_button1.pack(ipady=5, pady=3)
        self.maingame_save_button2.pack(ipady=5, pady=3)
        self.maingame_save_button3.pack(ipady=5, pady=3)
        self.maingame_save_frame2.pack(fill=tk.BOTH, expand=True)
        self.maingame_save_label3.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.maingame_save_question_canvas = tk.Canvas(self.maingame_save_frame2, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.maingame_save_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.maingame_save_question_canvas.pack(padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        self.maingame_save_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Zapisywanie!", "Zapisz swoją przygodę! W każdym momencie możesz zachować swój postęp, jednak pamiętaj, że w przypadku wszystkie zapisane dane związane z tą sesją zostaną usunięte. Graj ostrożnie i korzystaj z tej możliwości mądrze!")) # TEMP usuwanie save kiedyś zmienić


        self.maingame_save_frame1.pack_forget()

    # Death tab:
        self.maingame_death_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_death_frame2 = tk.Frame(self.maingame_death_frame1, bg=self.color_1)
        self.maingame_death_frame2frame1 = tk.Frame(self.maingame_death_frame2, bg=self.color_2, highlightbackground=self.color_3, highlightthickness=2)
        self.maingame_death_frame2label1 = tk.Label(self.maingame_death_frame2frame1, text="Przyczyna śmierci:", font=self.font_h2, fg=self.color_4, bg=self.color_2)
        self.maingame_death_frame2label2 = tk.Label(self.maingame_death_frame2frame1, text="{death_reason}", font=self.font_p2, fg=self.color_5, bg=self.color_2)

        self.maingame_death_frame3 = tk.Frame(self.maingame_death_frame1, bg=self.color_1)
        self.maingame_death_frame4 = tk.Frame(self.maingame_death_frame3, bg=self.color_1)
        self.maingame_death_frame4frame1 = tk.Frame(self.maingame_death_frame4, bg=self.color_1)
        self.maingame_death_frame4_frame1 = tk.Frame(self.maingame_death_frame4frame1, bg=self.color_3, highlightbackground=self.color_2, highlightthickness=1)
        self.maingame_death_frame4_frame1_label1 = tk.Label(self.maingame_death_frame4_frame1, text="Dzień:", font=self.font_p2i, fg=self.color_5, bg=self.color_3, width=12)
        self.maingame_death_frame4_frame1_label2 = tk.Label(self.maingame_death_frame4_frame1, text=self.stats["day"], font=self.font_p1, fg=self.color_4, bg=self.color_3)
        self.maingame_death_frame4_frame2 = tk.Frame(self.maingame_death_frame4frame1, bg=self.color_3, highlightbackground=self.color_2, highlightthickness=1)
        self.maingame_death_frame4_frame2_label1 = tk.Label(self.maingame_death_frame4_frame2, text="Pieniędzy:", font=self.font_p2i, fg=self.color_5, bg=self.color_3, width=12)
        self.maingame_death_frame4_frame2_label2 = tk.Label(self.maingame_death_frame4_frame2, text=self.stats["money"], font=self.font_p1, fg=self.color_4, bg=self.color_3)
        self.maingame_death_frame4frame2 = tk.Frame(self.maingame_death_frame4, bg=self.color_1)

        self.maingame_death_frame3_button1 = tk.Button(self.maingame_death_frame3, text="Statystyki", font=self.font_p1, bg=self.color_5, width=15)
        self.maingame_death_frame3_button2 = tk.Button(self.maingame_death_frame3, text="Dalej", font=self.font_p1, bg=self.color_5, width=15, command=lambda:
                [self.hide_frame(self.maingame_frame0, self.maingame_death_frame1), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.maingame_death_frame5 = tk.Frame(self.maingame_death_frame3, bg=self.color_1)
        self.maingame_death_frame5_label1 = tk.Label(self.maingame_death_frame5, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=370)

        self.maingame_death_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_death_frame2.pack(fill="x", side=tk.TOP)
        self.maingame_death_frame2frame1.pack(ipady=5, ipadx=20)
        self.maingame_death_frame2label1.pack(pady=3)
        self.maingame_death_frame2label2.pack()

        self.maingame_death_frame3.pack(fill=tk.BOTH, expand=True)
        self.maingame_death_frame4.pack(padx=5,pady=10)
        self.maingame_death_frame4frame1.pack(fill=tk.BOTH)
        self.maingame_death_frame4frame2.pack(fill=tk.BOTH)
        self.maingame_death_frame4_frame1.pack(padx=7, pady=10, side=tk.LEFT)
        self.maingame_death_frame4_frame1_label1.grid(row=0, column=0)
        self.maingame_death_frame4_frame1_label2.grid(row=1, column=0)
        self.maingame_death_frame4_frame2.pack(padx=7, pady=10, side=tk.LEFT)
        self.maingame_death_frame4_frame2_label1.grid(row=0, column=1)
        self.maingame_death_frame4_frame2_label2.grid(row=1, column=1)

        self.maingame_death_frame3_button1.pack(ipady=5, pady=3)
        self.maingame_death_frame3_button2.pack(ipady=5, pady=3)
        self.maingame_death_frame5.pack(fill=tk.BOTH, expand=True)
        self.maingame_death_frame5_label1.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.maingame_death_question_canvas = tk.Canvas(self.maingame_death_frame5, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.maingame_death_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.maingame_death_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)
                
        self.maingame_death_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Śmierć", "Po śmierci, wszystkie zapisane dane związane z bieżącą sesją zostaną nieodwracalnie usunięte.")) # TEMP konfiguracja wiadomości

        self.maingame_death_frame1.pack_forget()

    def refresh_stats(self):
        self.products_amounts = {
            "water": 5,
            "baguette": 5,
            "creamery": 2,
            "newspaper": 1,
            "scratch card": 10
        }

    # Refresh of data in the game window, called when it changes
    def refresh_data(self, stats=True, needs=True, skills=False):
        if stats:
            self.stats["money"] = round(self.stats["money"], 2)
            self.maingame_stats_label3.config(text=self.stats["day"])
            self.maingame_stats_label4.config(text=f"{self.stats["money"]} PLN")

        if needs:
            self.adjust_progressbar(self.maingame_frame5_1_progressbar1, self.stats["thirst"])
            self.adjust_progressbar(self.maingame_frame5_1_progressbar2, self.stats["hunger"])
            self.adjust_progressbar(self.maingame_frame5_1_progressbar3, self.stats["fatigue"])
        
        if skills:
            self.adjust_progressbar(self.work_skills_progressbar1, self.stats["intelligence"])
            self.adjust_progressbar(self.work_skills_progressbar2, self.stats["strength"])
            self.adjust_progressbar(self.work_skills_progressbar3, self.stats["stamina"])
            if self.stats["duty"]:
                self.work_skills_label5_a.config(text="☑")
            else: 
                self.work_skills_label5_a.config(text="❎")

    def adjust_progressbar(self, progressbar, target_value):
        prev_value = progressbar["value"]
        print(f"{prev_value} to: {target_value}")
        if not prev_value == target_value:
            while progressbar["value"] > target_value:
                progressbar["value"] -= 1
                progressbar.update()
                time.sleep(0.005)
            while progressbar["value"] < target_value:
                progressbar["value"] += 1
                progressbar.update()
                time.sleep(0.001)


    def create_item_frames(self):
        # Lista przedmiotów do wyświetlenia
        items_to_display = ["water", "baguette", "creamery"]

        row_frame = None  # Inicjalizacja zmiennej przechowującej bieżący rząd

        for item in items_to_display:
            quantity = self.stats.get(item, 0)  # Pobierz ilość, jeśli przedmiot nie istnieje, przyjmij 0

            if quantity > 0:
                # Sprawdź, czy istnieje rząd, jeśli nie, utwórz nowy
                if row_frame is None or len(row_frame.winfo_children()) >= 2:
                    row_frame = tk.Frame(self.maingame_frame5_2frame2, bg=self.color_1)
                    row_frame.pack(side=tk.TOP, pady=5)

                # Ramka dla każdego przedmiotu
                item_frame = tk.Frame(row_frame, bg=self.color_5, bd=0)
                item_frame.pack(side=tk.LEFT, padx=2)

                # Funkcja obsługująca kliknięcie na ramkę przedmiotu
                click_handler = lambda event, item=item: self.use_item(item)
                item_frame.bind("<Button-1>", click_handler)

                # Nazwa przedmiotu
                item_label = tk.Label(item_frame, text=item, font=self.font_p2i, bg=self.color_5, width=10)
                item_label.pack()

                image_path = f"data/img/{item}.png"
                item_image = Image.open(image_path)
                item_image = item_image.resize((32, 32), Image.LANCZOS)
                item_photo = ImageTk.PhotoImage(item_image)

                item_image_label = tk.Label(item_frame, image=item_photo, bg=self.color_5)
                item_image_label.image = item_photo
                item_image_label.bind("<Button-1>", click_handler)
                item_image_label.pack()

                # Ilość przedmiotu
                quantity_label = tk.Label(item_frame, text=f"Ilość: {quantity}", font=self.font_p2i, bg=self.color_5)
                quantity_label.pack()

    def use_item(self, item, refresh = True):
        # Funkcja wywoływana po użyciu przedmiotu
        quantity = self.stats.get(item, 0)
        
        events = {
            # "newspaper": lambda: self.create_root_thrid(), # TEMP GAZETA
            "scratch card": lambda: self.pre_thrid(item)
        }

        if quantity > 0:
            # Użycie przedmiotu (tu możesz dodać logikę związaną z efektem użycia)
            print(f"Użyto przedmiotu: {item}")

            if item in self.ranges_hunger:
                min_range, max_range = self.ranges_hunger[item]
                random_value = random.randint(min_range, max_range)
                self.stats["hunger"] += random_value
            if item in self.ranges_water:
                min_range, max_range = self.ranges_water[item]
                random_value = random.randint(min_range, max_range)
                self.stats["thirst"] += random_value
            if item in self.ranges_fatigue:
                min_range, max_range = self.ranges_fatigue[item]
                random_value = random.randint(min_range, max_range)
                self.stats["fatigue"] += random_value
            if item in events:
                events[item]()


            # Zmniejszenie ilości przedmiotu
            self.stats[item] -= 1

            # Jeżeli ilość spadła do 0, usuń przedmiot z listy
            if self.stats[item] == 0:
                self.stats[item] = 0

            # Zaktualizuj widok
            if refresh:
                self.update_item_frames(self.maingame_frame5_2frame2, self.create_item_frames)
                self.refresh_data(False)
            self.death_detector()

    def update_item_frames(self, frame, func = None):
        # Usuń stare ramki
        for widget in frame.winfo_children():
            widget.destroy()

        # Wygeneruj na nowo ramki przedmiotów
        if func:
            func()

    def set_needs_event(self, key, config2, text2, value):
        if config2 and text2:
            config2.config(text=f"Dzień {self.stats["day"]}: {text2}")
        self.stats[key] = value

    def root_x(self):
        if self.root_second_opened:
            self.root_second_opened = 0
            self.root_second.destroy()

    def create_root_second(self, choice):
        if self.root_second_opened == 0:
            self.root_second = tk.Toplevel()
            self.root_second.title("Przeżyj!")
            self.root_second.resizable(False, False) # TEMP
            self.components_root_second()

        self.root_second.protocol("WM_DELETE_WINDOW", self.root_x)
        

        self.store_frame0.pack_forget()
        self.work_frame0.pack_forget()
        self.work_find_frame0.pack_forget()
        self.work_skills_frame0.pack_forget()

        if choice == 1:
            self.second_products()
            self.store_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        if choice == 2:
            self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.root_second_opened = choice

    def components_root_second(self):
        self.rootsec_main = tk.Frame(self.root_second, bg=self.color_1)
        self.rootsec_main.pack(fill=tk.BOTH, expand=True)

    # Store widnow:

        self.store_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.store_label1 = tk.Label(self.store_frame0, text="Sklep", font=self.font_h2, fg=self.color_4, bg=self.color_1, width=25)
        self.store_frame1 = tk.Frame(self.store_frame0, bg=self.color_1)

        self.store_frame2 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_frame3 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_button1 = tk.Button(self.store_frame3, text="Dobry uczynek", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                self.wip(self.store_label6))
        self.store_button2 = tk.Button(self.store_frame3, text="Zamknij", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.root_x()])
        self.store_frame4 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_label6 = tk.Label(self.store_frame4, text="Aby zakupić produkt, wybierz lewym przyciskiem myszy na zdjęcie", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=370)

        self.store_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.store_label1.pack(pady=5)
        self.store_frame1.pack(fill=tk.BOTH, expand=True)

        self.store_frame2.pack(fill=tk.BOTH, expand=True, ipady=10)
        self.store_frame3.pack(fill=tk.BOTH, expand=True)
        self.store_button1.pack(ipady=2, pady=3)
        self.store_button2.pack(ipady=2, pady=3)
        self.store_frame4.pack(fill=tk.BOTH, expand=True)
        self.store_label6.pack(pady=5, side=tk.LEFT, anchor=tk.SW)


        self.store_question_canvas = tk.Canvas(self.store_frame4, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.store_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.store_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)

        self.store_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Sklep!", "W sklepie możesz zakupić produkty niezbędne do życia, jak również przedmioty rozrywkowe, takie jak zdrapki czy gazety. Ceny produktów zmieniają się codziennie, a towary są dostępne w ograniczonej ilości, dlatego dobrze jest być czujnym i dokonywać zakupów z rozwagą.")) # TEMP konfiguracja wiadomości

    # Work window:
    
        # Work tab:
        
            # Variables:
        self.duty_command1 = lambda: self.intermediary(self.work_label2, "", self.jobless_begging)
        self.duty_command2 = lambda: self.intermediary(self.work_label2, "", self.wip, self.work_label2)
        if self.stats["duty"]:
            self.duty_message2 = "Weź wolne"
        else:
            self.duty_message2 = "Idź do pracy"
        if self.stats["work"] == 0:
            self.duty_message1 = "Żebraj"
        else:
            self.duty_message1 = "Odbierz wypłatę"
        
            # Frames:
        self.work_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)

        self.work_frame1 = tk.Frame(self.work_frame0, bg=self.color_2, highlightbackground=self.color_3, highlightthickness=2)
        self.work_stats_label1 = tk.Label(self.work_frame1, text="Praca", font=self.font_p2i, fg=self.color_5, bg=self.color_2)
        self.work_stats_label2 = tk.Label(self.work_frame1, text="Stanowisko", font=self.font_p2i, fg=self.color_5, bg=self.color_2)
        self.work_stats_label3 = tk.Label(self.work_frame1, text="loading", font=self.font_p1b, fg=self.color_4, bg=self.color_2)
        self.work_stats_label4 = tk.Label(self.work_frame1, text="loading", font=self.font_p1b, fg=self.color_4, bg=self.color_2)

        self.work_frame2 = tk.Frame(self.work_frame0, bg=self.color_1, width=400)
        self.work_frame3 = tk.Frame(self.work_frame0, bg=self.color_1)
        self.work_button1 = tk.Button(self.work_frame3, text="Znajdź pracę", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.intermediary(self.work_label2, "", self.hide_frame, self.work_frame0), self.work_find_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.work_button2 = tk.Button(self.work_frame3, text="Umiejętności", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.intermediary(self.work_label2, "", self.hide_frame, self.work_frame0), self.work_skills_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.refresh_data(False, False, True)])  # TEMP umiejętności
        self.work_button3 = tk.Button(self.work_frame3, text=self.duty_message1, font=self.font_p1, bg=self.color_5, width=14, command=self.duty_command1)  # TEMP self.wip
        self.work_button4 = tk.Button(self.work_frame3, text=self.duty_message2, font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.duty_toggle(True, self.work_button4, self.work_label2)])
        self.work_button5 = tk.Button(self.work_frame3, text="Zamknij", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.root_x()])
        self.work_frame4 = tk.Frame(self.work_frame0, bg=self.color_1)
        self.work_label2 = tk.Label(self.work_frame4, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=270)

            # Placements a frames:
        self.work_frame1.grid_columnconfigure(0, weight=1)
        self.work_frame1.grid_columnconfigure(1, weight=1)

        self.work_frame1.pack(fill="x", side=tk.TOP, anchor=tk.N, ipady=3, ipadx=3)
        self.work_stats_label1.grid(row=0, column=0, padx=5)
        self.work_stats_label2.grid(row=0, column=1, padx=5)
        self.work_stats_label3.grid(row=1, column=0, padx=5, ipady=3)
        self.work_stats_label4.grid(row=1, column=1, padx=5, ipady=3)


        self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.work_frame2.pack(fill=tk.BOTH, expand=True, ipady=10)
        self.work_frame3.pack(fill=tk.BOTH, expand=True)
        self.work_button1.pack(ipady=2, pady=3)
        self.work_button2.pack(ipady=2, pady=3)
        self.work_button3.pack(ipady=2, pady=3)
        self.work_button4.pack(ipady=2, pady=3)
        self.work_button5.pack(ipady=2, pady=3)
        self.work_frame4.pack(fill=tk.BOTH, expand=True)
        self.work_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.work_question_canvas = tk.Canvas(self.work_frame4, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.work_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.work_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)

            # Binds:
        self.work_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Praca!", "W oknie pracy możesz podjąć zatrudnienie. Pamiętaj, że nie wszędzie z niskimi umiejętnościami się dostaniesz, a szef nie awansuje cię, jeśli nie wykonujesz pracy perfekcyjnie. Gdy nie masz pracy, raz dziennie możesz żebrać, zdobywając pieniądze i czasem jakieś przedmioty. Wypłatę możesz odebrać co piąty dzień pracy, co wiąże się z interaktywnym zadaniem do wykonania! Należy pamiętać, że jeśli poprosisz szefa o wcześniejszą wypłatę, otrzymasz mniejsze wynagrodzenie. Wykonanie interaktywnego zadania dodaje bonus do wypłaty oraz zwiększa szanse na awans.")) # TEMP konfiguracja wiadomości

        self.work_stats_refresh(self.stats["work"])

        # Find work tab:
        self.work_find_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.work_find_label1 = tk.Label(self.work_find_frame0, text="Aplikuj do pracy", font=self.font_h2, fg=self.color_4, bg=self.color_1, width=25)
        self.work_find_frame1 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_frame2 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_button1 = tk.Button(self.work_find_frame2, text="Bezrobotny", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.small_question(self.work_find_frame3, "Czy napewno chcesz zostać bezrobotnym?", self.apply_job, 0, self.work_find_label2), self.duty_toggle(False, self.work_button4)])
        self.work_find_button2 = tk.Button(self.work_find_frame2, text="Magazynier", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.small_question(self.work_find_frame3, "Czy napewno chcesz się zatrudnić jako magazynier?", self.apply_job, 1, self.work_find_label2), self.duty_toggle(False)])
        self.work_find_button3 = tk.Button(self.work_find_frame2, text="Wróć", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.hide_frame(self.work_find_frame0), self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.work_find_frame3 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_label2 = tk.Label(self.work_find_frame3, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=270)


        self.work_find_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.work_find_label1.pack(pady=5)
        self.work_find_frame1.pack(fill=tk.BOTH, expand=True, ipady=10)
        self.work_find_frame2.pack(fill=tk.BOTH, expand=True)
        self.work_find_button1.pack(ipady=2, pady=3)
        self.work_find_button2.pack(ipady=2, pady=3)
        self.work_find_button3.pack(ipady=2, pady=3)
        self.work_find_frame3.pack(fill=tk.BOTH, expand=True)
        self.work_find_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.work_find_question_canvas = tk.Canvas(self.work_find_frame3, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.work_find_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.work_find_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)
        self.work_find_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Aplikuj do pracy!", "W oknie aplikowania do pracy pamiętaj, że niektóre stanowiska wymagają większych umiejętności niż tylko pisanie i czytanie. Dlatego z czasem konieczne będzie podjęcie dodatkowej nauki, aby zdobyć wymagane kwalifikacje i awansować w karierze.")) # TEMP konfiguracja wiadomości

        self.work_find_frame0.pack_forget()
        
        # Skills work tab:
        self.work_skills_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.work_skills_label1 = tk.Label(self.work_skills_frame0, text="Twoje umiejętności☑❎", font=self.font_h2, fg=self.color_4, bg=self.color_1, width=25)

        self.work_skills_frame1 = tk.Frame(self.work_skills_frame0, bg=self.color_1)
        self.work_skills_label2 = tk.Label(self.work_skills_frame1, text="Inteligencja", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_progressbar1 = ttk.Progressbar(self.work_skills_frame1, orient="horizontal", mode="determinate", length=100, maximum=100)
        self.work_skills_label3 = tk.Label(self.work_skills_frame1, text="Siła", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_progressbar2 = ttk.Progressbar(self.work_skills_frame1, orient="horizontal", mode="determinate", length=100, maximum=100)
        self.work_skills_label4 = tk.Label(self.work_skills_frame1, text="Stamina", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_empty1 = tk.Label(self.work_skills_frame1, text="", bg=self.color_1)
        self.work_skills_progressbar3 = ttk.Progressbar(self.work_skills_frame1, orient="horizontal", mode="determinate", length=100, maximum=100)
        self.work_skills_label5 = tk.Label(self.work_skills_frame1, text="Prawo jazdy?", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_label5_a = tk.Label(self.work_skills_frame1, text="❎", font=self.font_p1b, fg=self.color_5, bg=self.color_1)
        self.work_skills_label6 = tk.Label(self.work_skills_frame1, text="Kurs zarządzania?", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_label6_a = tk.Label(self.work_skills_frame1, text="❎", font=self.font_p1b, fg=self.color_5, bg=self.color_1)
        self.work_skills_label7 = tk.Label(self.work_skills_frame1, text="WIP", font=self.font_p2i, fg=self.color_5, bg=self.color_1)
        self.work_skills_label7_a = tk.Label(self.work_skills_frame1, text="❎", font=self.font_p1b, fg=self.color_5, bg=self.color_1)
        self.work_skills_empty2 = tk.Label(self.work_skills_frame1, text="", bg=self.color_1)

        self.work_skills_button1 = tk.Button(self.work_skills_frame0, text="Wróć", font=self.font_p1, bg=self.color_5, width=14, command=lambda:
                [self.hide_frame(self.work_skills_frame0), self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        
        self.work_skills_frame2 = tk.Frame(self.work_skills_frame0, bg=self.color_1)
        self.work_skills_label8 = tk.Label(self.work_skills_frame2, text="", font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=270)

        self.work_skills_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.work_skills_label1.pack(pady=5)

        self.work_skills_frame1.pack(fill=tk.BOTH, expand=True)
        self.work_skills_label2.grid(row=0, column=0)
        self.work_skills_progressbar1.grid(row=1, column=0, padx=10)
        self.work_skills_label3.grid(row=0, column=1)
        self.work_skills_progressbar2.grid(row=1, column=1, padx=10)
        self.work_skills_label4.grid(row=0, column=2)
        self.work_skills_progressbar3.grid(row=1, column=2, padx=10)
        self.work_skills_empty1.grid(row=2, column=0, columnspan=3)

        self.work_skills_label5.grid(row=3, column=0)
        self.work_skills_label5_a.grid(row=4, column=0)
        self.work_skills_label6.grid(row=3, column=1)
        self.work_skills_label6_a.grid(row=4, column=1)
        self.work_skills_label7.grid(row=3, column=2)
        self.work_skills_label7_a.grid(row=4, column=2)
        self.work_skills_empty2.grid(row=5, column=0, columnspan=3)
        
        self.work_skills_button1.pack(ipady=2)
        self.work_skills_frame2.pack(fill=tk.BOTH, expand=True)
        self.work_skills_label8.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.work_skills_question_canvas = tk.Canvas(self.work_skills_frame2, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.work_skills_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.work_skills_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)
        self.work_skills_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("WIP!", "WIP")) # TEMP konfiguracja wiadomości

        self.work_skills_label2.bind("<Button-1>", lambda event: self.increase_stats(["intelligence"], 1, True))
        self.work_skills_progressbar1.bind("<Button-1>", lambda event: self.increase_stats(["intelligence"], 1, True))
        self.work_skills_label3.bind("<Button-1>", lambda event: self.increase_stats(["strength"], 1, True))
        self.work_skills_progressbar2.bind("<Button-1>", lambda event: self.increase_stats(["strength"], 1, True))
        self.work_skills_label4.bind("<Button-1>", lambda event: self.increase_stats(["stamina"], 1, True))
        self.work_skills_progressbar3.bind("<Button-1>", lambda event: self.increase_stats(["stamina"], 1, True))

        for i in range(3):
            self.work_skills_frame1.grid_columnconfigure(i, weight=1)


        self.work_skills_frame0.pack_forget()

    def second_products(self):
        # New prices every day
        if not self.root_second_opened == 1 or not self.product_day == self.stats["day"]:
            self.update_item_frames(self.store_frame1)
            self.create_second_products(self.store_frame1)
            

    # To generate new prices for each products in shop, without any arguments:
    def second_products_price(self):
        # It returns nothing if the product_day is the same as today's so that prices can be generated once a day.
        if self.product_day == self.stats["day"]:
            return

        self.product_day = self.stats["day"]

        # Temporary prices, about to be generated
        self.current_prices = {
            "water": 5,
            "baguette": 5,
            "creamery": 5,
            "newspaper": 5,
            "scratch card": 5
        }

        # For each names keys, generate new prices
        for item in self.products_amounts.keys():
            current_price = self.products_prices.get(item, [])
            current_price = random.choice(current_price)
            self.current_prices[item] = current_price
            print(f"{item}: {current_price}")

    def create_second_products(self, frame):
        self.second_products_price()
        for item in self.products_amounts.keys():

            item_frame = tk.Frame(frame, bg=self.color_2, highlightbackground=self.color_3, highlightthickness=2)

            click_handler = lambda event, item=item: self.buy_item(item)

            item_label = tk.Label(item_frame, text=item, font=self.font_p2i, fg=self.color_4, bg=self.color_2, width=10)

            image_path = f"data/img/{item}.png"
            item_image = Image.open(image_path)
            item_image = item_image.resize((64, 64), Image.LANCZOS)
            item_photo = ImageTk.PhotoImage(item_image)

            item_image_label = tk.Label(item_frame, image=item_photo, bg=self.color_2)
            item_image_label.image = item_photo

            current_price = self.current_prices.get(item)
            quantity_label = tk.Label(item_frame, text=f"{current_price} pln", font=self.font_p2i, fg=self.color_5, bg=self.color_2)

            item_label.pack()
            item_image_label.pack()
            quantity_label.pack()
            item_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2)

            item_image_label.bind("<Button-1>", click_handler)
            item_frame.bind("<Button-1>", click_handler)

    def buy_item(self, item):
        quantity = self.products_amounts.get(item, 0)
        price = self.current_prices.get(item, 0)
        auto_use = ["newspaper", "scratch card"]

        if not quantity > 0:
            item = self.capitalize_first_letter(item)
            self.store_label6.config(text=f"{item} się skończył, wróć jutro.")
            return
        if self.stats["money"] < price:
            self.store_label6.config(text=f"Nie stać Cię, na {item}.")
            return

        self.stats["money"] -= price
        self.products_amounts[item] -= 1
        self.stats[item] += 1
        if not item in auto_use:
            self.update_item_frames(self.maingame_frame5_2frame2, self.create_item_frames)
        self.refresh_data(True, False)
        
        self.store_label6.config(text=f"Kupiłeś {item}")

        print(f"Kupiono: {item} {price}")
        
        # Automatic use of an item if it is on the list 
        if item in auto_use:
            self.use_item(item, False)

    def wip(self, label):
        label.config(text="Work In Progress")

    def increase_stats(self, stats, value, minus_fatigue = None):
        for stat in stats:
            self.stats[stat] += value
        if minus_fatigue:
            self.stats["fatigue"] -= random.randint(7,13)
            self.refresh_data(False, True, True)
            self.death_detector()

    def duty_toggle(self, change = True, button = None, label = None):
        if self.stats["work"] == 0 and label:
            label.config(text="Chcesz wziąść wolne, gdy jesteś bezrobotny?")
            return
        if self.stats["duty"]:
            if change: self.stats["duty"] = False
            else: self.stats["duty"] = False
            if label: label.config(text="Nie pójdziesz do pracy")
            if button and change: self.duty_message2 = "Idź do pracy"
        else:
            if change: self.stats["duty"] = True
            else: self.stats["duty"] = False
            if label: label.config(text="Pójdziesz do pracy")
            if button and change: self.duty_message2 = "Weź wolne"
            
        if self.stats["work"] == 0:
            self.duty_message1 = "Żebraj"
        else:
            self.duty_message1 = "Odbierz wypłatę"

        self.duty_buttons_refresh()

    def duty_buttons_refresh(self):
        self.work_button3.config(text=self.duty_message1)
        self.work_button4.config(text=self.duty_message2)

    def jobless_begging(self, event):
        if not self.stats["work"] == 0:
            quantity = round(self.stats["lastpayment"]/5 * self.calculate_payment_work(), 2)
            self.stats["money"] += quantity
            self.stats["lastpayment"] = 0
            self.work_label2.config(text=f"Odebrałeś {quantity} pln, ze swojej wypłaty!")
            self.refresh_data(True, False)
            return
        if self.last_begging == self.stats["day"]:
            self.work_label2.config(text="Możesz raz dziennie żebrać :v")
            return

        self.last_begging = self.stats["day"]
        begging = round(random.uniform(0.10, 3.50), 2)
        difficulty = random.randint(2, 8)
        self.stats["money"] += begging
        self.stats["fatigue"] -= difficulty
        self.refresh_data(True, True)
        self.work_label2.config(text=f"Zdobyłeś {begging} pln!")

    def work_stats_refresh(self, id):
        work, position = self.id_name_job(id)

        self.work_stats_label3.config(text=work)
        self.work_stats_label4.config(text=position)

    def calculate_promotion_chance(self):
        promotion_chances = {
            1: 15,
            2: 20,
            3: 50,
            4: 60,
            5: 70,
            6: 80,
            7: 100,
        }
        return promotion_chances.get(self.stats["internship"], 0)

    def try_promotion(self, skip = None):

        # When a player in a job that he has maxed
        not_for_promotion = [0, 4]
        if self.stats["work"] in not_for_promotion:
            return

        # Promotion ordered  
        if skip:
            self.work_promotion()
            return

        wylosowana = random.randint(1, 100)
        chance = self.calculate_promotion_chance()
        print(f"{wylosowana} and {chance}")
        
        if wylosowana <= chance:
            requirements = self.jobs_require_ranges.get(self.stats["work"] + 1)

            if requirements:
                # Lista umiejętności, które gracz nie spełnia
                lacking_skills = [skill for skill, requirement in zip(["intelligence", "strength", "stamina"], requirements) if self.stats[skill] < requirement]
                
                if not lacking_skills:
                    # Jeśli spełnia wymagania, ustaw pracę gracza na wartość choice
                    self.work_promotion()
                    self.work_stats_refresh(self.stats["work"])
                else:
                    # Jeśli nie spełnia wymagań, wyświetl odpowiedni komunikat
                    message = "Awans się nie udał, nie masz wystarczających umiejętności. Brakuje: " + ", ".join(lacking_skills)
                    self.maingame_label5.config(text=f"Dzień {self.stats["day"]}: {message}")

    def work_promotion(self):
        self.stats["work"] += 1
        self.stats["internship"] = 0
        work, position = self.id_name_job(self.stats["work"])
        self.maingame_label5.config(text=f"Dzień {self.stats["day"]}: Awansowałeś na stanowisko {position}")

    def apply_job(self, choice, label):
        # Names for jobs:
        jobs_names = [
            "Bezrobotny",
            "Pakowacz na magazynie",
            "Policjant?",
            "Stary",
            "Kierowniku złoty"
        ]
        label.config(text="Przetwarzanie...")

        # Pobranie wymagań umiejętności dla wybranej pracy
        requirements = self.jobs_require_ranges.get(choice)

        if requirements:
            # Lista umiejętności, które gracz nie spełnia
            lacking_skills = [skill for skill, requirement in zip(["intelligence", "strength", "stamina"], requirements) if self.stats[skill] < requirement]
            
            if not lacking_skills:
                # Jeśli spełnia wymagania, ustaw pracę gracza na wartość choice
                self.stats["work"] = choice
                label.config(text=f"Pracujesz teraz jako: {jobs_names[choice]}")
                self.work_stats_refresh(self.stats["work"])
            else:
                # Jeśli nie spełnia wymagań, wyświetl odpowiedni komunikat
                message = "Nie masz wystarczających umiejętności do tej pracy. Brakuje: " + ", ".join(lacking_skills)
                label.config(text=message)

    def emergency_from_work(self, id, content):
        self.intermediary(self.maingame_label5, f"Dzień {self.stats['day']}: {content}")
        self.end_work(False, id)

    def pre_work(self, id):
        work, position = self.id_name_job(id)
        print(f"pre_work({id}): {work} {position}")

        work_descriptions = [
            "NULL",
            "Twoim zadaniem jest klikanie lewym przyciskiem myszy na paczkę, aby ją spakować. Zakończ swoją zmianę, zdobywając bonus do wypłaty po spakowaniu 10 paczek!",
            "Twoim zadaniem jest dostarczenie paczek porozrzucanych po planszy w wyznaczoną strefę. Zakończ swoją zmianę, zdobywając bonus do wypłaty po odstawieniu 12 paczek!",
            "jazda od punktu do punktu paleciakiem",
            "klocki jak na human benchmark"
        ]
        
        self.minigame = MiniGame(self)

        self.minigame.root_third.title(f"{position}!")
        self.minigame.root_third.protocol("WM_DELETE_WINDOW", lambda: self.emergency_from_work(id, "Nie dostaniesz bonusu bo uciekłeś z pracy."))

        self.rootthrid_frame1 = tk.Frame(self.minigame.rootthrid_frame0, bg=self.color_1)
        self.rootthrid_label1 = tk.Label(self.rootthrid_frame1, text=f"{position}!", font=self.font_h2, fg=self.color_4, bg=self.color_1)
        self.rootthrid_label2 = tk.Label(self.rootthrid_frame1, text=work_descriptions[id], font=self.font_p2, fg=self.color_4, bg=self.color_1, wraplength=400)
        self.rootthrid_button1 = tk.Button(self.rootthrid_frame1, text="Dalej", font=self.font_p1, bg=self.color_5, width=12, command=lambda:
                self.work_next(self.rootthrid_frame2))
        self.rootthrid_frame2 = tk.Frame(self.minigame.rootthrid_frame0, bg=self.color_1)

        if id == 1:
            self.minigame.work_packing(self.rootthrid_frame2)
        if id == 2:
            self.minigame.work_moving_box(self.rootthrid_frame2)

        self.rootthrid_frame1.pack(fill=tk.BOTH, expand=True)
        self.rootthrid_label1.pack(pady=5)
        self.rootthrid_label2.pack(pady=5)
        self.rootthrid_button1.pack(pady=5)
        
    def work_next(self, frame):
        self.rootthrid_frame1.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def end_work(self, done, id):
        if done:
            self.stats["money"] += round(1.5 * self.calculate_payment_work(id), 2)
            self.try_promotion()
        else:
            self.stats["money"] += self.calculate_payment_work(id)
        self.refresh_data(True, False)

        self.minigame.activation()

        # Chance draw for promotion (from 2 internship 20%, up to 4 = 80%)
        self.stats["internship"] += 1

    def death_detector(self):
        suspects = ["thirst", "hunger", "fatigue"]
        thresholds_below = {
            "thirst": -20,
            "hunger": -20,
            "fatigue": -20
        }
        thresholds_above = {
            "fatigue": 180
        }
        events = {
            "thirst": lambda: self.dead_confirmed("thirst"),
            "hunger": lambda: self.dead_confirmed("hunger"),
            "fatigue": lambda: self.dead_confirmed("fatigue")
            }
        for key in suspects:
            value = self.stats[key]
            if value <= thresholds_below.get(key, float('-inf')):
                print(f"{key} is below {thresholds_below[key]}: {value}")
                events[key]()
                return True
            elif value >= 180 and key in ["thirst", "hunger"]:
                print(f"{key} is above 180: {value}")
                self.set_needs_event(key, self.maingame_label5, "Pojechałeś do Rygi", 20)
                return True
            elif value >= 180 and key in ["fatigue"]:
                print(f"{key} is above 180: {value}")
                self.set_needs_event("fatigue", None, None, 180)
                return True


    def dead_confirmed(self, death_reason):
        self.stats["life"] = False
        self.stats["deathr"] = death_reason
        self.root_x()
        if self.root_third_opened:
            self.root_third_opened = False
            self.minigame.root_third.destroy()
        self.maingame_frame1.pack_forget()

        for filename in self.last_save:
            try:
                os.remove(filename)
                print(f"Plik {filename} został usunięty.")
            except OSError as e:
                print(f"Błąd podczas usuwania pliku: {e}")

        self.maingame_death_frame5_label1.config(text=f"Zapisy usunięte: {self.last_save}")
        self.maingame_death_frame2label2.config(text=self.stats["deathr"])
        self.maingame_death_frame4_frame1_label2.config(text=self.stats["day"])
        self.maingame_death_frame4_frame2_label2.config(text=self.stats["money"])
        self.maingame_death_frame1.pack(fill=tk.BOTH, expand=True)

    def calculate_fatigue_reduction(self):
        work_id = self.stats["work"]
        return random.randint(*self.work_ranges_fatigue.get(work_id, (0, 0)))
    
    def calculate_payment_work(self, id = None):
        if not id:
            id = self.stats["work"]
        return self.ranges_payment.get(id, 0)

    def next_day(self, needs=True):
        self.stats["day"] += 1
        a = 1       # TEMP boost from creamery B)
        if self.stats["duty"]: self.stats["lastpayment"] += a
        print(f"day = {self.stats["day"]}")

        # Needs reductions
        if needs and self.stats["duty"] == True:
            self.stats["thirst"] -= random.randint(30, 50)
            self.stats["hunger"] -= random.randint(25, 45)
            self.stats["fatigue"] -= self.calculate_fatigue_reduction()
        elif needs and not self.stats["duty"]:
            self.stats["thirst"] -= random.randint(30, 45)
            self.stats["hunger"] -= random.randint(30, 45)
            self.stats["fatigue"] += random.randint(40, 50)

        # Refreshing shop products and command log
        if self.root_second_opened == 1:
            self.second_products()
            self.store_label6.config(text="Aby zakupić produkt, wybierz lewym przyciskiem myszy na zdjęcie")

        self.refresh_stats()
        self.refresh_data()
        if self.death_detector():
            return

        # Giving payment
        if self.stats["lastpayment"] >= 5:
            self.stats["lastpayment"] = 0
            self.pre_work(self.stats["work"])

    def pre_thrid(self, value):
        self.minigame = MiniGame(self)

        if value == "scratch card":
            self.minigame.scratch_card()

class MiniGame():
    def __init__(self, main):
        self.sync(main)
        if not self.main.root_third_opened:
            self.create_root_thrid()

    def sync(self, main):
        self.main = main

    def deactivation(self):
        # Disabling interaction with other windows
        self.main.root.attributes("-disabled", True)
        if not self.main.root_second_opened == 0:
            self.main.root_second.attributes("-disabled", True)

    def activation(self):
        # Disabling interaction with other windows
        self.main.root.attributes("-disabled", False)
        if not self.main.root_second_opened == 0:
            self.main.root_second.attributes("-disabled", False)
        self.main.root_third_opened = False
        self.root_third.destroy()

    # Scratch card system:
    def scratch_card(self):
        print("scratch_card()")
        self.rootthrid_frame2 = tk.Frame(self.rootthrid_frame0, bg=self.main.color_1)
        self.rootthrid_frame2.pack(fill=tk.BOTH, expand=True)
        self.sc_click_count = 0
        self.root_third.protocol("WM_DELETE_WINDOW", lambda: self.sc_get_result_text(True))

        self.sc_prizes = {
            1: ["Gratulacje! Wygrałeś 50 zł!", 50],
            2: ["Super! Nic nie wygrałeś", 0],
            3: ["Brawo! Wygrałeś 10 zł!", 10],
            4: ["Niesamowite! Wygrałeś 5 zł!", 5],
            5: ["Świetnie! Wygrałeś 2.5 zł!", 2.5],
            6: ["Fantastycznie! Wygrałeś 7 zł!", 7],
            7: ["Doskonale! Wygrałeś 9 zł!", 9],
            8: ["Wspaniale! Wygrałeś 20 zł!", 20],
            9: ["Rewelacyjnie! Wygrałeś 14 zł!", 14],
            10: ["Nie do wiary! Wygrałeś 11 zł!", 11],
            11: ["Niebywałe! Wygrałeś 200 zł!", 200]
        }

        self.sc_lose_texts = [
            "Niestety, nie wygrałeś nic tym razem.",
            "Spróbuj szczęścia ponownie!",
            "Może następnym razem będzie lepiej.",
            "Nie poddawaj się! Szansa na wygraną jest blisko.",
            "Trzymaj się! Warto próbować, nawet jeśli czasami przegrywasz.",
            "Zachowaj optymizm! Każda gra to szansa na sukces.",
            "Wygrana może być tylko kwestią czasu! Trzymaj się!",
            "Każdy hazardzista odchodzi przed wielką wygraną!"
        ]


        sc_image = Image.open("data/img/Pszemo_Money.png")
        sc_image = sc_image.resize((400, 400), Image.LANCZOS)
        self.sc_photo = ImageTk.PhotoImage(sc_image)

        self.sc_image_label = tk.Label(self.rootthrid_frame2, bg=self.main.color_1)
        self.sc_image_label.pack()

        self.sc_canvas = tk.Canvas(self.sc_image_label, width=400, height=400, bd=0, highlightthickness=0)
        self.sc_canvas.pack()

        # Umieść zdjęcie na kanwie
        self.sc_canvas.create_image(0, 0, anchor=tk.NW, image=self.sc_photo)

        # Umieść napis na zdjęciu
        self.sc_label1 = self.sc_canvas.create_text(200, 240, text="", width=280, font=self.main.font_p1, fill="black", justify=tk.CENTER)

        self.sc_label2 = tk.Label(self.rootthrid_frame2, text="Klikaj na zdrapkę, aby otworzyć!", font=self.main.font_p2, fg=self.main.color_4, bg=self.main.color_1, wraplength=270)
        self.sc_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.sc_canvas.bind("<Button-1>", self.sc_click_handler)
        
    def sc_click_handler(self, event):
        self.sc_click_count += 1
        if self.sc_click_count == 5:
            self.sc_canvas.itemconfig(self.sc_label1, text=self.sc_get_result_text())
        elif self.sc_click_count > 5:
            self.activation()

    def sc_get_result_text(self, handle = None):
        if random.random() < 0.2:
            prize_id = random.choice(list(self.sc_prizes.keys()))
            print(f"WYGRANA\n{prize_id}")
            prize_text, sc_prize_amount= self.sc_prizes[prize_id]
            self.sc_win(sc_prize_amount, handle)
            return f"{prize_text}"
        else:
            return random.choice(self.sc_lose_texts)

    def sc_win(self, value, skip = None):
        self.main.stats["money"] += value
        self.main.refresh_data(True, False)
        if skip:
            self.activation()

    def create_root_thrid(self):
        print("create_root_thrid()")
        self.deactivation()
        
        self.main.root_third_opened = True
        self.root_third = tk.Toplevel()
        self.root_third.resizable(False, False)
        
        self.rootthrid_main = tk.Frame(self.root_third, bg=self.main.color_1)
        self.rootthrid_frame0 = tk.Frame(self.rootthrid_main, bg=self.main.color_1)

        self.rootthrid_main.pack(fill=tk.BOTH, expand=True)
        self.rootthrid_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        
    # Box packing system:
    def work_packing(self, frame):
        self.work_job = 1
        self.rootthrid_frame2 = frame
        self.work_packing_images = [
            "data/img/pack1.png",
            "data/img/pack2.png",
            "data/img/pack3.png",
            "data/img/pack4.png",
            "data/img/pack5.png"
        ]
        self.work_packing_images = [tk.PhotoImage(file=file) for file in self.work_packing_images]
        self.work_packing_index = 0

        self.work_packing_frame1 = tk.Frame(self.rootthrid_frame2, bg=self.main.color_1, width=10, height=20)
        self.work_packing_label1 = tk.Label(self.rootthrid_frame2, text="Paczek spakowanych: 0/10", font=self.main.font_p1, fg=self.main.color_4, bg=self.main.color_1)
        self.work_packing_frame1.pack(side=tk.LEFT)
        self.work_packing_label1.pack(padx=10, pady=3)

        self.work_packing_canvas = tk.Canvas(self.rootthrid_frame2, bg=self.main.color_1, bd=0, highlightthickness=0, width=150, height=150)
        self.work_packing_canvas.pack()

        self.work_packing_update_image()
        
        self.work_packing_canvas.bind("<Button-1>", lambda event: self.work_packing_pack_box())
        self.work_packing_frame1.bind("<Button-2>", lambda event: self.work_end())
        
        self.packed_boxes = 0

    def work_packing_update_image(self):
        self.work_packing_photo = self.work_packing_images[self.work_packing_index]
        self.work_packing_canvas.delete("all")  # Usunięcie poprzedniego obrazu
        self.work_packing_canvas.create_image(75, 75, anchor=tk.CENTER, image=self.work_packing_photo)

    def work_packing_pack_box(self):
        self.work_packing_index += 1
        if self.work_packing_index >= len(self.work_packing_images):
            self.work_packing_index = 0
            self.packed_boxes += 1
            self.work_packing_label1.config(text=f"Paczek spakowanych: {self.packed_boxes}/10")

        if self.packed_boxes >= 10:
            self.work_end()
            return

        self.work_packing_update_image()

    # Moving box system:
    def work_moving_box(self, frame):
        self.work_job = 2
        self.rootthrid_frame2 = frame
        
        self.work_moving_box_frame1 = tk.Frame(self.rootthrid_frame2, bg=self.main.color_1, width=10, height=50)
        self.work_moving_box_label1 = tk.Label(self.rootthrid_frame2, text="Paczek dostarczonych: 0/12", font=self.main.font_p1, fg=self.main.color_4, bg=self.main.color_1)

        self.work_moving_box_frame1.pack(side=tk.LEFT)
        self.work_moving_box_label1.pack(padx=10, pady=3)

        self.work_moving_box_canvas = tk.Canvas(self.rootthrid_frame2, width=500, height=400, bg=self.main.color_3)
        self.work_moving_box_canvas.pack()

        self.work_moving_box_drag_count = 0

        self.work_moving_box_create_drop_zone()
        self.work_moving_box_create_random_package()

        self.work_moving_box_frame1.bind("<Button-2>", lambda event: self.work_end())

    def work_moving_box_create_drop_zone(self):
        self.zone_image = tk.PhotoImage(file="data/img/zone.png").subsample(2, 2)
        self.drop_zone = self.work_moving_box_canvas.create_image(random.randint(0, 380), random.randint(10, 270), anchor="nw", image=self.zone_image)

    def work_moving_box_create_random_package(self):
        self.package_image = tk.PhotoImage(file="data/img/pack.png").subsample(2, 2)
        self.package = self.work_moving_box_canvas.create_image(random.randint(0, 400), random.randint(0, 300), anchor="nw", image=self.package_image)
        self.work_moving_box_canvas.tag_bind(self.package, "<ButtonPress-1>", self.work_moving_box_on_drag_start)
        self.work_moving_box_canvas.tag_bind(self.package, "<B1-Motion>", self.work_moving_box_on_drag_motion)
        self.work_moving_box_canvas.tag_bind(self.package, "<ButtonRelease-1>", self.work_moving_box_on_drag_release)
        
    def work_moving_box_on_drag_start(self, event):
        self.drag_data = {'x': event.x, 'y': event.y}
        
    def work_moving_box_on_drag_motion(self, event):
        d_x = event.x - self.drag_data['x']
        d_y = event.y - self.drag_data['y']
        self.work_moving_box_canvas.move(self.package, d_x, d_y)
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y
        
    def work_moving_box_on_drag_release(self, event=None):
        package_coords = self.work_moving_box_canvas.coords(self.package)
        drop_zone_coords = self.work_moving_box_canvas.coords(self.drop_zone)
        print(package_coords)
        if (drop_zone_coords[0] - 5 <= package_coords[0] <= drop_zone_coords[0] + 35 and
            drop_zone_coords[1] - 5 <= package_coords[1] <= drop_zone_coords[1] + 35):
            self.work_moving_box_canvas.delete(self.package)
            self.work_moving_box_drag_count += 1
            # print(f"Odstawiłeś na ten moment: {self.work_moving_box_drag_count}")

            self.work_moving_box_label1.config(text = f"Paczek dostarczonych: {self.work_moving_box_drag_count}/12")
            if self.work_moving_box_drag_count >= 12:
                self.work_end()
                return
            self.work_moving_box_create_drop_zone()
            self.work_moving_box_create_random_package()
        elif (-90 >= package_coords[0] or package_coords[0] >= 495 or
              -90 >= package_coords[1] or package_coords[1] >= 395):
            self.main.emergency_from_work(self.work_job, "Nie dostaniesz bonusu bo wyrzuciłeś paczkę.")
    
    def work_end(self):
        self.main.end_work(True, self.work_job)
        
root = tk.Tk()
game = Game(root)
root.mainloop()