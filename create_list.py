from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

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
class CreatePlaylist():
        def __init__(self,window):
            window.geometry("850x350")
            window.title("Create Your Playlist")
            self.videoplaylist=[]
            #GUI
            listall_button= Button(window, text="List All Videos",command = self.listall)
            listall_button.grid(row=0, column=0, padx=10, pady=10)
            
            self.video_box = tkst.ScrolledText(window, width=48, height=12, wrap="none")
            self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.Video_ID = Label(window,text="Enter Video ID")
            self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
            
            self.ID_input = Entry(window, width=3)
            self.ID_input.grid(row=0, column=2, padx=8, pady=10)
            
            self.add_video = Button(window,text="Add Video",command=self.add_btn_clicked)
            self.add_video.grid(row=0, column=3, padx=8, pady=10)
            
            self.delete_list = Button(window,text="Clear list",command=self.clear_btn_clicked)
            self.delete_list.grid(row=0, column=4, padx=8, pady=10)
            
            self.playlist = tkst.ScrolledText(window, width=38, height=12, wrap="none")
            self.playlist.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
            
        #Button Functions
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
    CreatePlaylist (window)
    window.mainloop()