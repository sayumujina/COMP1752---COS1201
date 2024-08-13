from tkinter import *
from tkinter import messagebox
from library_item import LibraryItem

import csv
import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content) 

def errorID():
    messagebox.showwarning(name="Invlid ID", message="Please enter a valid ID")

class UpdatedVideoDetails(): 
    def __init__(self, name=None, director=None, rating=None):
            self.name = name
            self.director = director
            self.rating = rating

#___________GUI_____________#
class UpdateVideo():
    def __init__(self,window):
        window.geometry("1200x680")
        window.minsize(1200,680)
        window.maxsize(1200,680)
        window.title("Update Videos")

        self.list_txt = tkst.ScrolledText(window, width=60, height=9, wrap="none")
        self.list_txt.place(x=10, y=10)

        list_videos_btn= Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.place(x=13, y=228)    

        self.video_txt = tk.Text(window, width=18, height=4, wrap="none")
        self.video_txt.place(x=620, y=290)

        self.check_video = Button(window,text="Check Video",command = self.check_videos_clicked)
        self.check_video.place(x=438, y=350)

        search_lbl = Label(window,text="Enter search term")
        search_lbl.place(x=10, y=290)

        self.search_input = Entry(window, width=22)
        self.search_input.place(x=230, y=295)

        self.search_button = Button(window, text="Search", command=self.search_clicked)
        self.search_button.place(x=500, y=290)
                
        self.Video_ID = Label(window,text="Enter video number")
        self.Video_ID.place(x=10, y=353)
                
        self.ID_input = Entry(window, width=15)
        self.ID_input.place(x=245, y=358)

        self.label_rating = Label(window, text="Enter new rating:")
        self.label_rating.place(x=10, y=416)

        self.rating_input = Entry(window, width=3)
        self.rating_input.place(x=210, y=421)

        self.update_button = Button(window, text="Update", command=self.displayupdate)
        self.update_button.place(x=260, y=416)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.place(x=900, y=10)

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

        term = self.search_input.get().lower()
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

    def listall(self):
        showlist = lib.list_all()
        set_text(self.check_video,showlist)
        
    #___________commands for clicking their corresponding button_____________#
    def displayupdate(self):
        key = self.ID_input.get()
        new_rating = int(self.rating_input.get())
        if new_rating is not None:
            lib.set_rating(key, new_rating)
            rating1 = lib.get_rating(key)
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            name = lib.get_name(key)
            info = f"{name}\n{director}\nRating: {rating1}\nPlays: {playcount}"
            set_text(self.video_txt,info)

    def check_videos_clicked(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            info = f"{name}\n{director}\nRating: {rating}\nPlays: {playcount}"
            set_text(self.video_txt,info)

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
           
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    UpdateVideo (window)
    window.mainloop()
