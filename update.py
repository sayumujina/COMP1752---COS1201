from tkinter import *
from tkinter import messagebox
import tkinter as tk

from library_item import LibraryItem
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content) 

def errorID():
    messagebox.showwarning(name="Invlid ID", message="Please enter a valid ID")

class UpdatedVideoDetails(): 
    def __init__(self, name=None, director=None, rating=None):
            self.name = name
            self.director = director
            self.rating = rating

class UpdateVideo():
    def __init__(self,window):
        window.geometry("1200x680")
        window.minsize(1200,680)
        window.maxsize(1200,680)
        window.title("Update Videos")
        self.videoplaylist=[]

        listall_button= Button(window, text="List All Videos",command = self.listall)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
            
        self.video_box = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.video_box.grid(row=1, column=0, padx=10, pady=10)
                
        self.Video_ID = Label(window,text="Enter Video ID")
        self.Video_ID.grid(row=2, column=0, padx=10, pady=10)
                
        self.ID_input = Entry(window, width=3)
        self.ID_input.grid(row=2, column=1, padx=10, pady=10, sticky='E')

        self.label_rating = Label(window, text="Enter New Rating:")
        self.label_rating.grid(row=4, column=0, padx=10, pady=10)

        self.rating_input = Entry(window, width=3)
        self.rating_input.grid(row=4, column=1, padx=10, pady=10, sticky='E')
            
        self.check_video = Button(window,text="Check Video",command = self.displayinfo)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
            
        self.Videoinfo_box = tkst.ScrolledText(window, width=38, height=12, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, padx=10, pady=10)

        self.update_button = Button(window, text="Update", command=self.displayupdate)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)
    
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)

    def displayupdate(self):
        key = self.ID_input.get()
        new_rating = self.rating_input.get()
        if new_rating is not None:
            rating = new_rating
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            name = lib.get_name(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)

    def displayinfo(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)
           
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    UpdateVideo (window)
    window.mainloop()