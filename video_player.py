import tkinter as tk

import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideolist
from update import UpdateVideo

# TTK
    

import ttkbootstrap as ttk
 
#___________functions for buttons clicked status_____________#
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))
    radio_var.set(None)

def create_video_clicked():
    status_lbl.configure(text="Create Video button was clicked!")
    CreateVideolist(tk.Toplevel(window))
    radio_var.set(None)
    
def update_videos_clicked():
    status_lbl.configure(text="Update Videos button was clicked!")
    UpdateVideo(tk.Toplevel(window))
    radio_var.set(None)

#___________ window configuration_____________#
window = ttk.Window(themename="solar")
window.geometry("750x200")
window.title("Video Player")

radio_var = tk.StringVar(value=None)
fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Check Videos",variable=radio_var, command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Create Video List",variable=radio_var,command=create_video_clicked)#, command=create_video_list_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Update Videos",variable=radio_var,command=update_videos_clicked)#, command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
