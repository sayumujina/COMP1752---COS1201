import tkinter as tk

import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideolist
from update import UpdateVideo
from ttkbootstrap import Style
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
window.geometry("850x180")
window.title("Video Player")
style=Style(theme='minty')
radio_var = tk.StringVar(value=None)
fonts.configure()

def night_switch():
    if theme_toggle.get() == 1:
        style.theme_use("solar")
    else:
        style.theme_use("minty")

theme_toggle = tk.IntVar()

toggle= ttk.Checkbutton(bootstyle='success,round-toggle',text='Night mode',variable=theme_toggle,command=night_switch)
toggle.place(x=650, y=10)

header_lbl = ttk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.place(x=20, y=10)

check_videos_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Check Videos",variable=radio_var, command=check_videos_clicked)
check_videos_btn.place(x=20, y=60)

create_video_list_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Create Video List",variable=radio_var,command=create_video_clicked)
create_video_list_btn.place(x=210, y=60)

update_videos_btn = ttk.Radiobutton(window,bootstyle="info toolbutton outline", text="Update Videos",variable=radio_var,command=update_videos_clicked)
update_videos_btn.place(x=435, y=60)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.place(x=200, y=120)

window.mainloop()
