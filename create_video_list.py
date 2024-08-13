from tkinter import *
from tkinter import messagebox

import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
import csv

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)
    
def add_text(text_area, content):
    text_area.insert(1.0, content + "\n")  
    
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
def errorDUP():
    messagebox.showinfo(title="Duplicate found", message="The video has already been added")

#___________GUI_____________#
class CreateVideolist():
        #___________window size_____________#
        def __init__(self,window):
            window.geometry("1140x580")
            window.title("Create Your Playlist")
            window.minsize(1140,580)
            window.maxsize(1140,580)
            self.videoplaylist=[]

            #___________video list interface_____________#
            self.list_txt = tkst.ScrolledText(window, width=60, height=9, wrap="none")
            self.list_txt.place(x=10, y=10)

            list_videos_btn= tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
            list_videos_btn.place(x=13, y=228)

            #___________video search interface_____________#
            self.search_input = Entry(window, width=21)
            self.search_input.place(x=230, y=295)
        
            search_lbl = Label(window,text="Enter search term")
            search_lbl.place(x=10, y=290)
                    
            self.search_button = Button(window, text="Search", command=self.search_clicked)
            self.search_button.place(x=485, y=290)
            
            #___________check video ID interface_____________#
            self.Video_ID = Label(window,text="Enter video number")
            self.Video_ID.place(x=10, y=353)
            
            self.ID_input = Entry(window, width=17)
            self.ID_input.place(x=245, y=358)
            
            #___________add, delete and play the playlist_____________#
            self.add_video = Button(window,text="Add Video",command=self.add_btn_clicked)
            self.add_video.place(x=449, y=350)
            
            self.delete_list = Button(window,text="Clear list",command=self.clear_btn_clicked)
            self.delete_list.place(x=466, y=410)
            
            self.play_count_increment = Text(window, width=3, height=1, wrap="none")
            self.play_count_increment.place(x=450, y=470)

            #___________playlist box_____________#
            self.playlist = tkst.ScrolledText(window, width=18, height=9, wrap="none")
            self.playlist.place(x=598, y=290)

            self.play_btn = Button(window,text="Play",command=self.play_btn_clicked)
            self.play_btn.place(x=515, y=470)

            #___________status label_____________#
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
        def play_btn_clicked(self):
            id = self.ID_input.get()
            lib.increment_play_count(id)
            play_count1 = lib.get_play_count(id)
            set_text(self.play_count_increment, play_count1)
            self.status_lbl.configure(text="Play button was clicked!")

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
            self.status_lbl.configure(text="Add video button was clicked!")
                
        def clear_btn_clicked(self):
            self.playlist.delete("1.0", "end")
            self.videoplaylist.clear()
            set_text(self.play_count_increment, '0')
            self.status_lbl.configure(text="Clear list button was clicked!")

        def list_videos_clicked(self):
            video_list = lib.list_all()
            set_text(self.list_txt, video_list)
            self.status_lbl.configure(text="List Videos button was clicked!")
        
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    CreateVideolist (window)
    window.mainloop()
