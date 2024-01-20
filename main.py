import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import random
import os

class Game():
    def __init__(self, root, play):
    # Root etc.
        self.root = root
        self.play = play
        self.root.title("Przeżyj!")
        self.root.configure(bg="#fff")
        self.root.minsize(270, 215)
        self.root.maxsize(650, 465)
        # self.root.resizable(False, False) # TEMP

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

        self.root_main = tk.Frame(self.root, bg=self.color_1)
        self.root_main.pack(fill=tk.BOTH, expand=True)

        # self.create_statistics() # TEMP
# 
        self.create_start_gui() # TEMP
        self.show_start_gui()   # TEMP

    def create_start_gui(self):
    # Main tab::
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
                [self.hide_frame(self.start_frame), self.load_frame1.pack(padx=3, pady=2, fill=tk.BOTH, expand=True)])
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
        self.question_icon = tk.PhotoImage(file="data/img/questionmark.png")
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

    def show_info_message(self, title, message):
        messagebox.showinfo(title, message)

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
            "day": 0,
            "money": round(random.uniform(9.90, 21.90), 2),
            "work": 0,
            "intelligence": 10,
            "strength": 10,
            "stamina": 10,
            "luck": 10,
            "thirst": 100,
            "hunger": 100,
            "fatigue": 100,
            "water": 0,
            "baguette": 0,
            "creamery": 0,
            "newspaper": False
        }

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
            self.maingame_save_label2.config(text="Wpisz tytuł zapisu")
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
        self.maingame_save_label2.config(text=f"Zapisano save pod nazwą {save_title}")

    def selected_load_save(self):
        selected_index = self.load_listbox.curselection()
        if not selected_index:
            self.load_label2.config(text="Wybierz zapis do wczytania")
            return
        
        self.load_label2.config(text="Wczytywanie")
        filename = f"saves/save{selected_index[0] + 1}.txt"

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
                else:
                    try:
                        value = int(value_str)
                    except ValueError:
                        value = float(value_str)

                current_dict[key] = value

        print("Wczytano statystyki:")
        print("Stats:", self.stats)
        self.hide_frame(self.load_frame1)
        self.create_maingame()


    def selected_delate_save(self, listbox, command_log):
        selected_index = listbox.curselection()
        if not selected_index:
            command_log.config(text="Wybierz zapis do usunięcia")
            return
        
        command_log.config(text=f"Usunięto")
        filename = f"saves/save{selected_index[0] + 1}.txt"

        # Remove the selected item from the listbox
        self.load_listbox.delete(selected_index)
        os.remove(filename)
        command_log.config(text="Usunięto zapis")

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

        # Create of main elements
        self.maingame_frame3 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_frame4 = tk.Frame(self.maingame_frame3, bg=self.color_1)
        self.maingame_frame5 = tk.Frame(self.maingame_frame3, bg=self.color_1)
        self.maingame_frame6 = tk.Frame(self.maingame_frame3, bg=self.color_1)
        self.maingame_button1 = tk.Button(self.maingame_frame5, text="Następny dzień", font=self.font_p1, bg=self.color_2, width=15, command=self.next_day)
        self.maingame_button2 = tk.Button(self.maingame_frame5, text="Sklep", font=self.font_p1, bg=self.color_2, width=15)
        self.maingame_button3 = tk.Button(self.maingame_frame5, text="Praca", font=self.font_p1, bg=self.color_2, width=15)
        self.maingame_button4 = tk.Button(self.maingame_frame5, text="Statystyki", font=self.font_p1, bg=self.color_2, width=15)
        self.maingame_frame7 = tk.Frame(self.maingame_frame1, bg=self.color_1)
        self.maingame_label5 = tk.Label(self.maingame_frame7, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)

        # Create of needs elements
        self.maingame_frame4_1 = tk.Frame(self.maingame_frame4, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=2)
        self.maingame_frame4_1label = tk.Label(self.maingame_frame4_1, text="Potrzeby postaci:", font=self.font_p1, fg=self.color_7, bg=self.color_1, width=17)
        self.maingame_frame4_1frame = tk.Frame(self.maingame_frame4_1, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=1)

        # Create of equipment elements
        self.maingame_frame4_2 = tk.Frame(self.maingame_frame6, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=2)
        self.maingame_frame4_2label = tk.Label(self.maingame_frame4_2, text="Ekwipunek postaci:", font=self.font_p1, fg=self.color_7, bg=self.color_1, width=17)
        self.maingame_frame4_2frame = tk.Frame(self.maingame_frame4_2, bg=self.color_1, highlightbackground=self.color_2, highlightthickness=1)

        # Visualisation of statistical elements
        self.maingame_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
        self.maingame_frame2.pack(fill="x", side=tk.TOP, anchor=tk.N, ipady=3, ipadx=3)
        self.maingame_stats_label1.grid(row=0, column=0, padx=5)
        self.maingame_stats_label2.grid(row=0, column=1, padx=5)
        self.maingame_stats_label3.grid(row=1, column=0, padx=5, ipady=3)
        self.maingame_stats_label4.grid(row=1, column=1, padx=5, ipady=3)

        # Visualisation of main elements
        self.maingame_frame3.pack(fill=tk.BOTH, expand=True)
        self.maingame_frame4.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.maingame_frame5.pack(expand=True, side=tk.LEFT, padx=30)
        self.maingame_frame6.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)
        self.maingame_button1.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button2.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button3.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_button4.pack(ipadx=5, ipady=4, pady=3)
        self.maingame_frame7.pack(fill=tk.BOTH, expand=True)
        self.maingame_label5.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        # Visualisation of needs elements
        self.maingame_frame4_1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame4_1label.pack()
        self.maingame_frame4_1frame.pack(fill=tk.BOTH, expand=True)

        # Visualisation of equipment elements
        self.maingame_frame4_2.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_frame4_2label.pack()
        self.maingame_frame4_2frame.pack(fill=tk.BOTH, expand=True)


        # Question icon
        self.maingame_question_canvas = tk.Canvas(self.maingame_frame7, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.maingame_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.maingame_question_canvas.pack(padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        # Binds
        self.maingame_question_canvas.bind("<Button-1>", lambda event:
                self.show_info_message("Tytuł", "Treść wiadomości"))    # TEMP konfiguracja wiadomości
        self.maingame_save_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame1),
                 self.maingame_save_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5), self.load_saves(self.maingame_save_listbox)])
        self.maingame_home_canvas.bind("<Button-1>", lambda event:
                [self.hide_frame(self.maingame_frame0),
                 self.question("Czy na pewno chcesz wrócić do menu głównego?", (lambda: self.maingame_frame0.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)), self.show_start_gui)])

    # Save tab:
        validate_cmd = (self.root.register(lambda new_text, max_chars=20: self.validate_input(new_text, max_chars)), '%P')

        self.maingame_save_frame1 = tk.Frame(self.maingame_frame0, bg=self.color_1)
        self.maingame_save_label1 = tk.Label(self.maingame_save_frame1, text="Zapisy gry", font=self.font_h2, fg=self.color_7, bg=self.color_1)
        self.maingame_save_listbox = tk.Listbox(self.maingame_save_frame1, selectmode=tk.SINGLE, width=55, height=5)
        self.maingame_save_entry1 = tk.Entry(self.maingame_save_frame1, validate="key", validatecommand=validate_cmd, width=40)
        self.maingame_save_button1 = tk.Button(self.maingame_save_frame1, text="Zapisz", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.save_game(), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button2 = tk.Button(self.maingame_save_frame1, text="Usuń", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.selected_delate_save(self.maingame_save_listbox, self.maingame_save_label2), self.load_saves(self.maingame_save_listbox)])
        self.maingame_save_button3 = tk.Button(self.maingame_save_frame1, text="Wróć", font=self.font_p1, bg=self.color_2, width=15, command=lambda:
                [self.hide_frame(self.maingame_save_frame1), self.maingame_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=2), self.maingame_save_label2.config(text="")])
        self.maingame_save_frame2 = tk.Frame(self.maingame_save_frame1, bg=self.color_1)
        self.maingame_save_label2 = tk.Label(self.maingame_save_frame2, text="", font=self.font_p2, fg=self.color_7, bg=self.color_1, wraplength=270)

        self.maingame_save_frame1.pack(fill=tk.BOTH, expand=True, padx=3, pady=5)
        self.maingame_save_label1.pack()
        self.maingame_save_listbox.pack(padx=5, pady=5)
        self.maingame_save_entry1.pack()
        self.maingame_save_button1.pack(ipady=5, pady=3)
        self.maingame_save_button2.pack(ipady=5, pady=3)
        self.maingame_save_button3.pack(ipady=5, pady=3)
        self.maingame_save_frame2.pack(fill=tk.BOTH, expand=True)
        self.maingame_save_label2.pack(pady=5, side=tk.LEFT, anchor=tk.SW)

        self.maingame_save_question_canvas = tk.Canvas(self.maingame_save_frame2, bg=self.color_1, bd=0, highlightthickness=0, width=32, height=32)
        self.maingame_save_question_canvas.create_image(16, 16, anchor=tk.CENTER, image=self.question_icon)
        self.maingame_save_question_canvas.pack(padx=5, side=tk.RIGHT, anchor=tk.SE)
        
        self.maingame_save_question_canvas.bind("<Button-1>", lambda event: self.show_info_message("Tytuł", "Treść wiadomości")) # TEMP konfiguracja wiadomości


        self.maingame_save_frame1.pack_forget()

    # Refresh of data in the game window, called when it changes
    def refresh_data(self):
        self.maingame_stats_label3.config(text=self.stats['day'])
        self.maingame_stats_label4.config(text=f"{self.stats['money']} PLN")

    def next_day(self):
        self.stats["day"] += 1
        print(f"day = {self.stats['day']}")
        self.refresh_data()


root = tk.Tk()
play = True
game = Game(root, play)
root.mainloop()