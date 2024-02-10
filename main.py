import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime
import random
import os

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

        self.color_1 = "#1E2F4F"
        self.color_2 = "#CACACA"    # Gray
        self.color_3 = "#35426D"
        self.color_4 = "#FFBBBB"    # red
        self.color_5 = "#DDDDBC"    # Yellow
        self.color_6 = "#BBFFBD"    # Green
        self.color_7 = "#FFFFFF"    # White
        self.color_8 = "#1F2C44"    # Shadow border

        self.style = ttk.Style()
        self.question_icon = tk.PhotoImage(file="data/img/questionmark.png")

        self.root_main = tk.Frame(self.root, bg=self.color_1)
        self.root_main.pack(fill=tk.BOTH, expand=True)
        self.last_save = []
        self.root_second_opened = 0

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

        self.start_button1 = tk.Button(self.start_frame, text="Informacje", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.info_frame.pack(padx=3, pady=10, fill=tk.BOTH, expand=True)])
        self.start_button2 = tk.Button(self.start_frame, text="Zacznij nową grę!", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.new_game()])
        self.start_button3 = tk.Button(self.start_frame, text="Wczytaj grę!", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.start_frame), self.load_saves(self.load_listbox), self.load_frame1.pack(padx=3, pady=2, fill=tk.BOTH, expand=True)])
        self.start_button4 = tk.Button(self.start_frame, text="Osiągnięcia", font=self.font_p1, bg=self.color_2, width=15)

    # Info tab:
        self.info_frame = tk.Frame(self.root_main, bg=self.color_1)
        self.info_label1 = tk.Label(self.info_frame, text="Informacje", font=self.font_h2, fg=self.color_7, bg=self.color_1)
        self.info_label2 = tk.Label(self.info_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis ultrices dui. Nullam ac enim sed lectus egestas pharetra in sit amet neque. Aenean a pulvinar tortor, at pellentesque est. Etiam euismod ut massa non hendrerit. Donec eget nulla vitae tellus rutrum vestibulum auctor ac orci. Duis maximus ligula at erat varius porttitor. Nam magna erat, porttitor non nulla et, euismod placerat arcu. Fusce eu cursus dui, non laoreet tellus. Phasellus tincidunt nisi interdum diam ultricies iaculis. Vestibulum at porta purus.", font=self.font_p1, fg=self.color_7, bg=self.color_1, wraplength=630) # TEMP dodać informacje
        self.info_button = tk.Button(self.info_frame, text="Wróć", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.info_frame), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])

        self.info_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.info_label1.pack(pady=5)
        self.info_label2.pack(padx=3, pady=5, fill="x")
        self.info_button.pack(ipady=2)

        self.info_frame.pack_forget()
        # self.info_label2.bind("<Configure>", self.set_label_wrap)

    # Load save tab:
        self.load_frame1 = tk.Frame(self.root_main, bg=self.color_1)
        self.load_label1 = tk.Label(self.load_frame1, text="Wczytaj grę", font=self.font_h2, fg=self.color_7, bg=self.color_1)
        self.load_listbox = tk.Listbox(self.load_frame1, selectmode=tk.SINGLE, width=55, height=5)
        self.load_button1 = tk.Button(self.load_frame1, text="Wczytaj", font=self.font_p1, bg=self.color_2, width=15, command=self.selected_load_save)
        self.load_button2 = tk.Button(self.load_frame1, text="Usuń", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                self.selected_delate_save(self.load_listbox, self.load_label2))
        self.load_button3 = tk.Button(self.load_frame1, text="Wróć", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.load_frame1), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.load_label2.config(text="")])
        self.load_frame2 = tk.Frame(self.load_frame1, bg=self.color_1)
        self.load_label2 = tk.Label(self.load_frame2, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)
        
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
        
        self.load_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości

        self.load_frame1.pack_forget()
        self.load_saves(self.load_listbox)

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

    def new_game(self):
        self.question("Czy napewno chcesz rozpocząć nową grę?", self.show_start_gui, self.create_statistics)
        
    def question(self, quest, prev_func, next_func):
        self.question_frame = tk.Frame(self.root_main, bg=self.color_1)
        self.question_label1 = tk.Label(self.question_frame, text=quest, font=self.font_h3, fg=self.color_7, bg=self.color_1, wraplength=450)
        self.question_frame1 = tk.Frame(self.question_frame, bg=self.color_1)
        self.question_button1 = tk.Button(self.question_frame1, text="Nie", font=self.font_p1, bg=self.color_2, width=8, command=lambda:
                [self.hide_frame(self.question_frame), prev_func()])
        self.question_button2 = tk.Button(self.question_frame1, text="Tak", font=self.font_p1, bg=self.color_2, width=8, command=lambda:
                [self.hide_frame(self.question_frame), next_func()])

        self.question_frame.pack(padx=3, pady=10, expand=True)
        self.question_label1.pack(pady=20)
        self.question_frame1.pack(expand=True)
        self.question_button1.pack(side=tk.LEFT, padx=5, ipady=4)
        self.question_button2.pack(side=tk.LEFT, padx=5, ipady=4)

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
            "scratch card": 2,
            "lastpayment": 0,
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
        self.maingame_frame2 = tk.Frame(self.maingame_frame1, bg=self.color_3, highlightbackground=self.color_8, highlightthickness=2)
        self.maingame_stats_label1 = tk.Label(self.maingame_frame2, text="Dzień", font=self.font_p2i, fg=self.color_2, bg=self.color_3)
        self.maingame_stats_label2 = tk.Label(self.maingame_frame2, text="Pieniądze", font=self.font_p2i, fg=self.color_2, bg=self.color_3)
        self.maingame_stats_label3 = tk.Label(self.maingame_frame2, text=self.stats['day'], font=self.font_p1b, fg=self.color_7, bg=self.color_3)
        self.maingame_stats_label4 = tk.Label(self.maingame_frame2, text=f"{self.stats['money']} PLN", font=self.font_p1b, fg=self.color_7, bg=self.color_3)

        # Configure grid columns
        self.maingame_frame2.grid_columnconfigure(0, weight=1)
        self.maingame_frame2.grid_columnconfigure(1, weight=2)
        self.maingame_frame2.grid_columnconfigure(2, weight=0)
        self.maingame_frame2.grid_columnconfigure(4, weight=0)
        self.maingame_frame2.grid_columnconfigure(6, weight=0)

        # Create images
        self.maingame_debug_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_3, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_debug_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_debug_icon)
        self.maingame_save_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_3, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_save_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_save_icon)
        self.maingame_home_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_3, bd=0, highlightthickness=0, width=48, height=52)
        self.maingame_home_canvas.create_image(24, 27, anchor=tk.CENTER, image=self.maingame_home_icon)
        self.maingame_settings_canvas = tk.Canvas(self.maingame_frame2, bg=self.color_3, bd=0, highlightthickness=0, width=48, height=52)
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
        self.maingame_button1 = tk.Button(self.maingame_frame6, text="Następny dzień", font=self.font_p1, bg=self.color_2, width=15, command=self.next_day)
        self.maingame_button2 = tk.Button(self.maingame_frame6, text="Sklep", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.create_root_second(1)])
        self.maingame_button3 = tk.Button(self.maingame_frame6, text="Praca", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.create_root_second(2)])
        self.maingame_button4 = tk.Button(self.maingame_frame6, text="Statystyki", font=self.font_p1, bg=self.color_2, width=15)
        self.maingame_frame8 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_label5 = tk.Label(self.maingame_frame8, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)

        # Create of needs elements
        self.maingame_frame5_1 = tk.Frame(self.maingame_frame5, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=2)
        self.maingame_frame5_1label = tk.Label(self.maingame_frame5_1, text="Potrzeby postaci:", font=self.font_p1, fg=self.color_7, bg=self.color_1, width=17)
        self.maingame_frame5_1frame1 = tk.Frame(self.maingame_frame5_1, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=1)
        self.maingame_frame5_1frame2 = tk.Frame(self.maingame_frame5_1frame1, bg=self.color_1)
        self.maingame_frame5_1_label1 = tk.Label(self.maingame_frame5_1frame2, text="Pragnienie", font=self.font_p2i, fg=self.color_2, bg=self.color_1)
        self.maingame_frame5_1_progressbar1 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)
        self.maingame_frame5_1_label2 = tk.Label(self.maingame_frame5_1frame2, text="Głód", font=self.font_p2i, fg=self.color_2, bg=self.color_1)
        self.maingame_frame5_1_progressbar2 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)
        self.maingame_frame5_1_label3 = tk.Label(self.maingame_frame5_1frame2, text="Zmęczenie", font=self.font_p2i, fg=self.color_2, bg=self.color_1)
        self.maingame_frame5_1_progressbar3 = ttk.Progressbar(self.maingame_frame5_1frame2, orient="horizontal", mode="determinate", length=120, maximum=100)

        # Configure grid columns
        self.maingame_frame5_1frame2.grid_columnconfigure(0, weight=1)
        self.maingame_frame5_1frame2.grid_rowconfigure(0, weight=0)

        # Create of equipment elements
        self.maingame_frame5_2 = tk.Frame(self.maingame_frame7, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=2)
        self.maingame_frame5_2label = tk.Label(self.maingame_frame5_2, text="Ekwipunek postaci:", font=self.font_p1, fg=self.color_7, bg=self.color_1, width=17)
        self.maingame_frame5_2frame1 = tk.Frame(self.maingame_frame5_2, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=1)
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
                print(self.stats['duty'])])
        self.maingame_question_canvas.bind("<Button-1>", lambda event:
                self.show_info_message("Tytuł", "Treść wiadomości"))    # TEMP konfiguracja wiadomości
        self.maingame_save_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame1),
                 self.maingame_save_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.load_saves(self.maingame_save_listbox)])
        self.maingame_home_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame0),
                 self.question("Czy na pewno chcesz wrócić do menu głównego?", (lambda: self.maingame_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)), self.show_start_gui)])

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

        # Names for jobs:
        self.jobs_names = [
            "Bezrobotny",
            "Pakowacz na magazynie",
            "Magazynier",
            "Operator wózka widłowego",
            "Kierownik magazynu"
        ]

        self.product_day = self.stats['day'] - 1

        self.refresh_stats()
        self.refresh_data()

    # Save tab:
        validate_cmd = (self.root.register(lambda new_text, max_chars=20: self.validate_input(new_text, max_chars)), '%P')

        self.maingame_save_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_save_label1 = tk.Label(self.maingame_save_frame1, text="Zapisy gry", font=self.font_h2, fg=self.color_7, bg=self.color_1)
        self.maingame_save_listbox = tk.Listbox(self.maingame_save_frame1, selectmode=tk.SINGLE, width=55, height=5)
        self.maingame_save_label2 = tk.Label(self.maingame_save_frame1, text="Wpisz nazwe zapisu:", font=self.font_p2i, fg=self.color_7, bg=self.color_1)
        self.maingame_save_entry1 = tk.Entry(self.maingame_save_frame1, validate="key", validatecommand=validate_cmd, width=40)
        self.maingame_save_button1 = tk.Button(self.maingame_save_frame1, text="Zapisz", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.save_game(), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button2 = tk.Button(self.maingame_save_frame1, text="Usuń", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.selected_delate_save(self.maingame_save_listbox, self.maingame_save_label3), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button3 = tk.Button(self.maingame_save_frame1, text="Wróć", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.hide_frame(self.maingame_save_frame1), self.maingame_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=2), self.maingame_save_label3.config(text="")])
        self.maingame_save_frame2 = tk.Frame(self.maingame_save_frame1, bg=self.color_1)
        self.maingame_save_label3 = tk.Label(self.maingame_save_frame2, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)

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
        
        self.maingame_save_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości


        self.maingame_save_frame1.pack_forget()

    # Death tab:
        self.maingame_death_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_death_frame2 = tk.Frame(self.maingame_death_frame1, bg=self.color_1)
        self.maingame_death_frame2frame1 = tk.Frame(self.maingame_death_frame2, bg=self.color_3, highlightbackground=self.color_8, highlightthickness=2)
        self.maingame_death_frame2label1 = tk.Label(self.maingame_death_frame2frame1, text="Przyczyna śmierci:", font=self.font_h2, fg=self.color_7, bg=self.color_3)
        self.maingame_death_frame2label2 = tk.Label(self.maingame_death_frame2frame1, text="{death_reason}", font=self.font_p2, fg=self.color_2, bg=self.color_3)

        self.maingame_death_frame3 = tk.Frame(self.maingame_death_frame1, bg=self.color_1)
        self.maingame_death_frame4 = tk.Frame(self.maingame_death_frame3, bg=self.color_1)
        self.maingame_death_frame4frame1 = tk.Frame(self.maingame_death_frame4, bg=self.color_1)
        self.maingame_death_frame4_frame1 = tk.Frame(self.maingame_death_frame4frame1, bg=self.color_8, highlightbackground=self.color_3, highlightthickness=1)
        self.maingame_death_frame4_frame1_label1 = tk.Label(self.maingame_death_frame4_frame1, text="Dzień:", font=self.font_p2i, fg=self.color_2, bg=self.color_8, width=12)
        self.maingame_death_frame4_frame1_label2 = tk.Label(self.maingame_death_frame4_frame1, text=self.stats['day'], font=self.font_p1, fg=self.color_7, bg=self.color_8)
        self.maingame_death_frame4_frame2 = tk.Frame(self.maingame_death_frame4frame1, bg=self.color_8, highlightbackground=self.color_3, highlightthickness=1)
        self.maingame_death_frame4_frame2_label1 = tk.Label(self.maingame_death_frame4_frame2, text="Pieniędzy:", font=self.font_p2i, fg=self.color_2, bg=self.color_8, width=12)
        self.maingame_death_frame4_frame2_label2 = tk.Label(self.maingame_death_frame4_frame2, text=self.stats['money'], font=self.font_p1, fg=self.color_7, bg=self.color_8)
        self.maingame_death_frame4frame2 = tk.Frame(self.maingame_death_frame4, bg=self.color_1)

        self.maingame_death_frame3_button1 = tk.Button(self.maingame_death_frame3, text="Statystyki", font=self.font_p1, bg=self.color_2, width=15)
        self.maingame_death_frame3_button2 = tk.Button(self.maingame_death_frame3, text="Dalej", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.maingame_frame0, self.maingame_death_frame1), self.start_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.maingame_death_frame5 = tk.Frame(self.maingame_death_frame3, bg=self.color_1)
        self.maingame_death_frame5_label1 = tk.Label(self.maingame_death_frame5, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=370)

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
                
        self.maingame_death_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości

        self.maingame_death_frame1.pack_forget()

    def refresh_stats(self):
        self.products_amounts = {
            "water": 5,
            "baguette": 5,
            "creamery": 2,
            "newspaper": 1,
            "scratch card": 5
        }

    # Refresh of data in the game window, called when it changes
    def refresh_data(self, stats=True, needs=True):
        if stats:
            self.stats['money'] = round(self.stats['money'], 2)
            self.maingame_stats_label3.config(text=self.stats['day'])
            self.maingame_stats_label4.config(text=f"{self.stats['money']} PLN")

        if needs:
            self.maingame_frame5_1_progressbar1["value"] = self.stats['thirst']
            self.maingame_frame5_1_progressbar2["value"] = self.stats['hunger']
            self.maingame_frame5_1_progressbar3["value"] = self.stats['fatigue']

    def create_item_frames(self):
        # Lista przedmiotów do wyświetlenia
        items_to_display = ['water', 'baguette', 'creamery', 'scratch card']

        row_frame = None  # Inicjalizacja zmiennej przechowującej bieżący rząd

        for item in items_to_display:
            quantity = self.stats.get(item, 0)  # Pobierz ilość, jeśli przedmiot nie istnieje, przyjmij 0

            if quantity > 0:
                # Sprawdź, czy istnieje rząd, jeśli nie, utwórz nowy
                if row_frame is None or len(row_frame.winfo_children()) >= 2:
                    row_frame = tk.Frame(self.maingame_frame5_2frame2, bg=self.color_1)
                    row_frame.pack(side=tk.TOP, pady=5)

                # Ramka dla każdego przedmiotu
                item_frame = tk.Frame(row_frame, bg=self.color_2, bd=0)
                item_frame.pack(side=tk.LEFT, padx=2)

                # Funkcja obsługująca kliknięcie na ramkę przedmiotu
                click_handler = lambda event, item=item: self.use_item(item)
                item_frame.bind("<Button-1>", click_handler)

                # Nazwa przedmiotu
                item_label = tk.Label(item_frame, text=item, font=self.font_p2i, bg=self.color_2, width=10)
                item_label.pack()

                # Zdjęcie przedmiotu (zakładam, że masz pliki obrazów o nazwach "water.jpg", "baguette.jpg", itd.)
                image_path = f"data/img/{item}.jpg"
                item_image = Image.open(image_path)
                item_image = item_image.resize((32, 32), Image.LANCZOS)
                item_photo = ImageTk.PhotoImage(item_image)

                item_image_label = tk.Label(item_frame, image=item_photo)
                item_image_label.image = item_photo
                item_image_label.bind("<Button-1>", click_handler)
                item_image_label.pack()

                # Ilość przedmiotu
                quantity_label = tk.Label(item_frame, text=f"Ilość: {quantity}", font=self.font_p2i, bg=self.color_2)
                quantity_label.pack()

    def use_item(self, item):
        # Funkcja wywoływana po użyciu przedmiotu
        quantity = self.stats.get(item, 0)

        if quantity > 0:
            # Użycie przedmiotu (tu możesz dodać logikę związaną z efektem użycia)
            print(f"Użyto przedmiotu: {item}")

            if item in self.ranges_hunger:
                min_range, max_range = self.ranges_hunger[item]
                random_value = random.randint(min_range, max_range)
                self.stats['hunger'] += random_value
            if item in self.ranges_water:
                min_range, max_range = self.ranges_water[item]
                random_value = random.randint(min_range, max_range)
                self.stats['thirst'] += random_value
            if item in self.ranges_fatigue:
                min_range, max_range = self.ranges_fatigue[item]
                random_value = random.randint(min_range, max_range)
                self.stats['fatigue'] += random_value

            # Zmniejszenie ilości przedmiotu
            self.stats[item] -= 1

            # Jeżeli ilość spadła do 0, usuń przedmiot z listy
            if self.stats[item] == 0:
                self.stats[item] = 0

            # Zaktualizuj widok
            self.update_item_frames(self.maingame_frame5_2frame2, self.create_item_frames)
            self.death_detector()
            self.refresh_data(False)
            

    def update_item_frames(self, frame, func = None):
        # Usuń stare ramki
        for widget in frame.winfo_children():
            widget.destroy()

        # Wygeneruj na nowo ramki przedmiotów
        if func:
            func()

    def set_needs_event(self, key, text2):
        self.maingame_label5.config(text=f"Dzień {self.stats['day']}: {text2}")
        self.stats[key] = 20

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

        if choice == 1:
            self.second_products()
            self.store_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        if choice == 2:
            self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        
        if self.root_second_opened == 0:
            self.root_second_opened = choice

    def components_root_second(self):
        self.rootsec_main = tk.Frame(self.root_second, bg=self.color_1)
        self.rootsec_main.pack(fill=tk.BOTH, expand=True)

    # Store widnow:

        self.store_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.store_label1 = tk.Label(self.store_frame0, text="Sklep", font=self.font_h2, fg=self.color_7, bg=self.color_1, width=25)
        self.store_frame1 = tk.Frame(self.store_frame0, bg=self.color_1)

        self.store_frame2 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_frame3 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_button1 = tk.Button(self.store_frame3, text="Dobry uczynek", font=self.font_p1, bg=self.color_2, width=14)
        self.store_button2 = tk.Button(self.store_frame3, text="Zamknij", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.root_x()])
        self.store_frame4 = tk.Frame(self.store_frame0, bg=self.color_1)
        self.store_label6 = tk.Label(self.store_frame4, text="Aby zakupić produkt, wybierz lewym przyciskiem myszy na zdjęcie", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=370)

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

        self.store_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości

    # Work window:
    
        # Work tab:
        if self.stats['duty']:
            self.duty_message2 = "Weź wolne"
        else:
            self.duty_message2 = "Idź do pracy"
        if self.stats['work'] == 0:
            self.duty_message1 = "Żebraj"
        else:
            self.duty_message1 = "Odbierz wypłatę"
        
        self.work_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.work_label1 = tk.Label(self.work_frame0, text="Praca", font=self.font_h2, fg=self.color_7, bg=self.color_1, width=25)
        self.work_frame1 = tk.Frame(self.work_frame0, bg=self.color_1)
        self.work_frame2 = tk.Frame(self.work_frame0, bg=self.color_1)
        self.work_button1 = tk.Button(self.work_frame2, text="Znajdź pracę", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.hide_frame(self.work_frame0), self.work_find_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.work_button2 = tk.Button(self.work_frame2, text="Umiejętności", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.wip(self.work_label2)])
        self.work_button3 = tk.Button(self.work_frame2, text=self.duty_message1, font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.wip(self.work_label2)])
        self.work_button4 = tk.Button(self.work_frame2, text=self.duty_message2, font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.duty_toggle(True, self.work_button4, self.work_label2)])
        self.work_button5 = tk.Button(self.work_frame2, text="Zamknij", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.root_x()])
        self.work_frame3 = tk.Frame(self.work_frame0, bg=self.color_1)
        self.work_label2 = tk.Label(self.work_frame3, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)

        self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.work_label1.pack(pady=5)
        self.work_frame1.pack(fill=tk.BOTH, expand=True, ipady=10)
        self.work_frame2.pack(fill=tk.BOTH, expand=True)
        self.work_button1.pack(ipady=2, pady=3)
        self.work_button2.pack(ipady=2, pady=3)
        self.work_button3.pack(ipady=2, pady=3)
        self.work_button4.pack(ipady=2, pady=3)
        self.work_button5.pack(ipady=2, pady=3)
        self.work_frame3.pack(fill=tk.BOTH, expand=True)
        self.work_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.work_question_canvas = tk.Canvas(self.work_frame3, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.work_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.work_question_canvas.pack(pady=5, padx=5, side=tk.RIGHT, anchor=tk.SE)

        self.work_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości

        # Find work tab:
        self.work_find_frame0 = tk.Frame(self.rootsec_main, bg=self.color_1)
        self.work_find_label1 = tk.Label(self.work_find_frame0, text="Aplikuj do pracy", font=self.font_h2, fg=self.color_7, bg=self.color_1, width=25)
        self.work_find_frame1 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_frame2 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_button1 = tk.Button(self.work_find_frame2, text="Bezrobotny", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.apply_job(0, self.work_find_label2), self.duty_toggle(False, self.work_button4)])
        self.work_find_button2 = tk.Button(self.work_find_frame2, text="Magazynier", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.apply_job(1, self.work_find_label2), self.duty_toggle(False)])
        self.work_find_button3 = tk.Button(self.work_find_frame2, text="Wróć", font=self.font_p1, bg=self.color_2, width=14, command=lambda:
                [self.hide_frame(self.work_find_frame0), self.work_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)])
        self.work_find_frame3 = tk.Frame(self.work_find_frame0, bg=self.color_1)
        self.work_find_label2 = tk.Label(self.work_find_frame3, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)


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
        self.work_find_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości

        self.work_find_frame0.pack_forget()

    def second_products(self):
        # New prices every day
        if not self.root_second_opened == 1 or not self.product_day == self.stats['day']:
            self.update_item_frames(self.store_frame1)
            self.create_second_products(self.store_frame1)
            

    def second_products_price(self):
        if self.product_day == self.stats['day']:
            return

        self.product_day = self.stats['day']

        self.current_prices = {
            "water": 5,
            "baguette": 5,
            "creamery": 5,
            "newspaper": 5,
            "scratch card": 5
        }

        for item in self.products_amounts.keys():
            current_price = self.products_prices.get(item, [])
            current_price = random.choice(current_price)
            self.current_prices[item] = current_price
            print(f"{item}: {current_price}")

    def create_second_products(self, frame):
        self.second_products_price()
        for item in self.products_amounts.keys():

            item_frame = tk.Frame(frame, bg=self.color_3, highlightbackground=self.color_8, highlightthickness=2)

            click_handler = lambda event, item=item: self.buy_item(item)

            item_label = tk.Label(item_frame, text=item, font=self.font_p2i, fg=self.color_7, bg=self.color_3, width=10)

            image_path = f"data/img/{item}.jpg"
            item_image = Image.open(image_path)
            item_image = item_image.resize((32, 32), Image.LANCZOS)
            item_photo = ImageTk.PhotoImage(item_image)

            item_image_label = tk.Label(item_frame, image=item_photo)
            item_image_label.image = item_photo

            current_price = self.current_prices.get(item)
            quantity_label = tk.Label(item_frame, text=f"{current_price} pln", font=self.font_p2i, fg=self.color_2, bg=self.color_3)

            item_label.pack()
            item_image_label.pack()
            quantity_label.pack()
            item_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2)

            item_image_label.bind("<Button-1>", click_handler)
            item_frame.bind("<Button-1>", click_handler)

    def buy_item(self, item):
        quantity = self.products_amounts.get(item, 0)
        price = self.current_prices.get(item, 0)

        if not quantity > 0:
            item = self.capitalize_first_letter(item)
            self.store_label6.config(text=f"{item} się skończył, wróć jutro.")
            return
        if self.stats['money'] < price:
            self.store_label6.config(text=f"Nie stać Cię, na {item}.")
            return

        self.stats['money'] -= price
        self.products_amounts[item] -= 1
        self.stats[item] += 1
        self.update_item_frames(self.maingame_frame5_2frame2, self.create_item_frames)
        self.refresh_data(True, False)
        
        self.store_label6.config(text=f"Kupiłeś {item}")

        print(f"Kupiono: {item} {price}")

    def wip(self, label):
        label.config(text="Work In Progress")

    def duty_toggle(self, change = True, button = None, label = None):
        if self.stats['work'] == 0 and label:
            label.config(text="Chcesz wziąść wolne, gdy jesteś bezrobotny?")
            return
        if self.stats['duty']:
            if change: self.stats['duty'] = False
            else: self.stats['duty'] = False
            if label: label.config(text="Nie pójdziesz do pracy")
            if button and change: self.duty_message2 = "Idź do pracy"
        else:
            if change: self.stats['duty'] = True
            else: self.stats['duty'] = False
            if label: label.config(text="Pójdziesz do pracy")
            if button and change: self.duty_message2 = "Weź wolne"
            
        if self.stats['work'] == 0:
            self.duty_message1 = "Żebraj"
        else:
            self.duty_message1 = "Odbierz wypłatę"

        self.duty_buttons_refresh()

    def duty_buttons_refresh(self):
        self.work_button3.config(text=self.duty_message1)
        self.work_button4.config(text=self.duty_message2)


    def apply_job(self, choice, label):
        label.config(text="Przetwarzanie...")

        # Pobranie wymagań umiejętności dla wybranej pracy
        requirements = self.jobs_require_ranges.get(choice)
        
        if requirements:
            # Lista umiejętności, które gracz nie spełnia
            lacking_skills = [skill for skill, requirement in zip(["intelligence", "strength", "stamina"], requirements) if self.stats[skill] < requirement]
            
            if not lacking_skills:
                # Jeśli spełnia wymagania, ustaw pracę gracza na wartość choice
                self.stats['work'] = choice
                label.config(text=f"Pracujesz teraz jako: {self.jobs_names[choice]}")
            else:
                # Jeśli nie spełnia wymagań, wyświetl odpowiedni komunikat
                message = "Nie masz wystarczających umiejętności do tej pracy. Brakuje: " + ", ".join(lacking_skills)
                label.config(text=message)

    def death_detector(self):
        suspects = ['thirst', 'hunger']

        for key in suspects:
            value = self.stats[key]
            if value <= -20:
                print(f"{key} is below -20: {value}")
                self.dead_confirmed(key)
                
            if value >= 180:
                print(f"{key} is above 180: {value}")
                self.set_needs_event(key, "Pojechałeś do Rygi")

    def dead_confirmed(self, death_reason):
        self.stats['life'] = False
        self.stats['deathr'] = death_reason
        self.root_x()
        self.maingame_frame1.pack_forget()

        for filename in self.last_save:
            try:
                os.remove(filename)
                print(f"Plik {filename} został usunięty.")
            except OSError as e:
                print(f"Błąd podczas usuwania pliku: {e}")

        self.maingame_death_frame5_label1.config(text=f"Zapisy usunięte: {self.last_save}")
        self.maingame_death_frame2label2.config(text=self.stats['deathr'])
        self.maingame_death_frame4_frame1_label2.config(text=self.stats['day'])
        self.maingame_death_frame4_frame2_label2.config(text=self.stats['money'])
        self.maingame_death_frame1.pack(fill=tk.BOTH, expand=True)

    def calculate_fatigue_reduction(self):
        work_id = self.stats['work']
        return random.randint(*self.work_ranges_fatigue.get(work_id, (0, 0)))
    
    def calculate_payment_work(self):
        work_id = self.stats['work']
        return self.ranges_payment.get(work_id, 0)

    def next_day(self, needs=True):
        self.stats['day'] += 1
        a = 1       # TEMP boost from creamery B)
        if self.stats['duty']: self.stats['lastpayment'] += a
        print(f"day = {self.stats['day']}")

        # Needs reductions
        if needs and self.stats['duty'] == True:
            self.stats['thirst'] -= random.randint(30, 50)
            self.stats['hunger'] -= random.randint(25, 45)
            self.stats['fatigue'] -= self.calculate_fatigue_reduction()
        elif needs and not self.stats['duty']:
            self.stats['thirst'] -= random.randint(30, 45)
            self.stats['hunger'] -= random.randint(30, 45)
            self.stats['fatigue'] += random.randint(20, 40)

        # Giving payment
        if self.stats['lastpayment'] >= 5:
            self.stats['lastpayment'] = 0
            self.stats['money'] += self.calculate_payment_work()

        if self.root_second_opened == 1:
            self.second_products()
            self.store_label6.config(text="Aby zakupić produkt, wybierz lewym przyciskiem myszy na zdjęcie")

        self.refresh_stats()
        self.refresh_data()
        self.death_detector()



root = tk.Tk()
game = Game(root)
root.mainloop()