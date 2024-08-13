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

#___________GUI_____________#

class CheckVideos():
    def __init__(self, window):
        window.geometry("1140x600")
        window.minsize(1140, 600)
        window.maxsize(1140, 600)
        window.title("Check Videos")

        #___________video list interface_____________#
        self.list_txt = tkst.ScrolledText(window, width=60, height=9, wrap="none")
        self.list_txt.place(x=10, y=10)

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.place(x=13, y=228)

        #___________video search interface_____________#
        search_lbl = Label(window,text="Enter search term")
        search_lbl.place(x=10, y=290)
                
        self.search_input = Entry(window, width=22)
        self.search_input.place(x=230, y=295)

        self.search_button = Button(window, text="Search", command=self.search_clicked)
        self.search_button.place(x=500, y=290)

        #___________check video ID interface_____________#
        self.Video_ID = tk.Label(window, text="Enter video number")
        self.Video_ID.place(x=10, y=353)

        self.ID_input = tk.Entry(window, width=15)
        self.ID_input.place(x=245, y=358)

        self.check_video_button = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        self.check_video_button.place(x=438, y=350)

        #___________status label_____________#
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.place(x=900, y=10)

        #___________video box on the right_____________#
        self.video_txt = tk.Text(window, width=18, height=4, wrap="none")
        self.video_txt.place(x=620, y=290)

        self.list_videos_clicked() 

    #___________search function_____________#
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
                    id = LibraryItem['id']
                    name = lib.get_name(id)
                    director = lib.get_director(id)
                    rating = lib.get_rating(id)
                    play_count = lib.get_play_count(id)
                    item = f"{id} {name} - {director} - Rating: {rating} - Plays: {play_count} \n"
                    result_list.append((item))
                    break 
        
        result_list_text = ''.join(result_list)
        set_text(self.list_txt, result_list_text)

        if not term:
            error_msg = ("Please enter a valid search term")
            set_text(self.list_txt, error_msg)

        self.status_lbl.configure(text="Search button was clicked!")

    #___________commands for clicking their corresponding button_____________#
    def check_video_clicked(self):
        id = self.ID_input.get()
        name = lib.get_name(id)
        if name is not None:
            director = lib.get_director(id)
            rating = lib.get_rating(id)
            play_count = lib.get_play_count(id)
            video_details = f"{name}\n{director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, "Video not found")
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
