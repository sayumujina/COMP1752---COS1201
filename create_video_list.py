from tkinter import *
from tkinter import messagebox

import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
import csv

#MISC Functions
def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)
    
def add_text(text_area, content):
    text_area.insert(1.0, content + "\n")  
    
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
def errorDUP():
    messagebox.showinfo(title="Duplicate found", message="The video has already been added")
class CreateVideolist():
        def __init__(self,window):
            window.geometry("1080x510")
            window.title("Create Your Playlist")
            window.minsize(1080,510)
            window.maxsize(1080,510)
            self.videoplaylist=[]

            listall_button= Button(window, text="List All Videos",command = self.listall)
            listall_button.grid(row=0, column=0, padx=10, pady=10)
            
            self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
            self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.Video_ID = Label(window,text="Enter Video ID")
            self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
            
            self.ID_input = Entry(window, width=3)
            self.ID_input.grid(row=0, column=2, padx=8, pady=10)
            
            self.add_video = Button(window,text="Add Video",command=self.add_btn_clicked)
            self.add_video.grid(row=0, column=3, padx=8, pady=10)
            
            self.delete_list = Button(window,text="Clear list",command=self.clear_btn_clicked)
            self.delete_list.grid(row=0, column=4, padx=8, pady=10)
            
            self.playlist = tkst.ScrolledText(window, width=20, height=12, wrap="none")
            self.playlist.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)

            self.play_btn = Button(window,text="Play",command=self.play_btn_clicked)
            self.play_btn.grid(row=2, column=3, padx=8, pady=10)
            
            search_lbl = Label(window,text="Enter parameters")
            search_lbl.grid(row=2, column=0, padx=10, pady=10)
                    
            self.search_input = Entry(window, width=30)
            self.search_input.grid(row=2, column=1, padx=10, pady=10, sticky='E')

            self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
            self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

            self.search_button = Button(window, text="Search", command=self.search_clicked)
            self.search_button.grid(row=2, column=2, columnspan=5, sticky='W')

        # buttons
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

        def play_btn_clicked(self):
            id = self.ID_input.get()
            play_count = lib.get_play_count(id)
            
            play_count += 1

        def add_btn_clicked(self):
            key = self.ID_input.get()
            name = lib.get_name(key)
            x = key
            if x not in self.videoplaylist:
                self.videoplaylist.append(key)
                print (*self.videoplaylist)
                if name is not None:
                    addname=f"{name}"
                    add_text(self.playlist,addname)
                else:
                    errorID()
            elif x in self.videoplaylist:
                errorDUP()
                
        def clear_btn_clicked(self):
            self.playlist.delete("1.0", "end")
            self.videoplaylist.clear()
        
        def listall(self):
            showlist = lib.list_all()
            set_text(self.video_box,showlist)
        
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    CreateVideolist (window)
    window.mainloop()