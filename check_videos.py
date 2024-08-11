from tkinter import *
from video_library import library
from library_item import LibraryItem

import tkinter as tk
import tkinter.scrolledtext as tkst

import csv
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        window.geometry("1100x600")
        window.minsize(1100, 600)
        window.maxsize(1100, 600)
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        search_lbl = Label(window,text="Enter parameters")
        search_lbl.grid(row=2, column=0, padx=10, pady=10)
                
        self.search_input = Entry(window, width=30)
        self.search_input.grid(row=2, column=1, padx=10, pady=10, sticky='E')

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.search_button = Button(window, text="Search", command=self.search_clicked)
        self.search_button.grid(row=2, column=3, columnspan=5, sticky='W')

        self.list_videos_clicked() 

    def search_clicked(self):
        library = []
        with open('info.csv') as csv_file:
            records = csv_file.readlines()
            csv_reader = csv.reader(csv_file, delimiter=',')
            for record in records:
                fields = record.strip().split(',')
                LibraryItem = {}
                LibraryItem['id'] = fields[0]
                LibraryItem['name'] = fields[1]
                LibraryItem['director'] = fields[2]
                LibraryItem['rating'] = fields[3]
                LibraryItem['play_count'] = fields[4]

                library.append(LibraryItem)

        term = self.search_input.get()
        result_list = []

        for LibraryItem in library:
            for val in LibraryItem.values():
                if isinstance(val, str) and term in val.lower(): # checks if val is a string before attempting to use the "in" operator. 
                    result_list.append(LibraryItem)
                    break 

        for LibraryItem in result_list:
            id = LibraryItem['id']
            name = lib.get_name(id)
            director = lib.get_director(id)
            rating = lib.get_rating(id)
            play_count = lib.get_play_count(id)
            video_details = f"{id} {name} - {director} - Rating: {rating} - Plays: {play_count}"
            set_text(self.list_txt, video_details)

        self.status_lbl.configure(text="Search button was clicked!")

    def check_video_clicked(self):
        id = self.input_txt.get()
        name = lib.get_name(id)
        if name is not None:
            director = lib.get_director(id)
            rating = lib.get_rating(id)
            play_count = lib.get_play_count(id)
            video_details = f"{name}\n{director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {id} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
