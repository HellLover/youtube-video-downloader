import tkinter
import customtkinter
from pytube import YouTube

# Functions
def download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        
        if video is not None:
            video.download()

        finishLabel.configure(text="Downloaded!", text_color="blue")
    except:
        finishLabel.configure(text="Invalid Video URL", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completed_of = bytes_downloaded / total_size * 100
    per = str(int(completed_of))
    p_percentage.configure(text=per + "%")
    p_percentage.update()

    progress_bar.set(float(completed_of) / 100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")
app.resizable(False, False)

# UI
title = customtkinter.CTkLabel(app, text="Enter a YouTube video link")
title.pack(pady=7, padx=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download_button = customtkinter.CTkButton(app, text="Download", command=download)
download_button.pack(padx=10, pady=10)

# Run the app
app.mainloop()
