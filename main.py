from pytube import YouTube
from pytube import Playlist
import tkinter as tk 
from tkinter import filedialog
# tkinter is a basic 2D graphics library used to build graphical user interfaces
# we'll use it to make a simple visual user interface pop up for selecting the
# download folder


def download_video(url, save_path):
        # we're doing a "try and except" block because stuff
        # can go wrong when using this kind of API's
        try:
            yt = YouTube(url) # grabs an instance of the youtube video
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path = save_path) # writes the media stream to disk
            print("Video downloaded succesfully!")
        
        except Exception as e:
            print(e)

def open_file_dialog():
    # this will open the file dialogue where the user will pick
    # download directory
    folder = filedialog.askdirectory()
    if folder: # if the user selects a folder
        print (f"Selected folder: {folder}") # prints their selected folder
    
    return folder

if __name__ == "__main__":
    # Makes sure that you are directly running this Python
    # file before it executes anything that happens under this.
    # For example, if this file is reused by another file,
    # we don't want it to also run the code below.

    root = tk.Tk() # initializes the tk window 
    root.withdraw() # hides the tk window 

    video_url = input("Please enter the link of the YouTube video you wish to download:\n")
    save_dir = open_file_dialog()

    if save_dir: # Makes sure that the user selected a folder
        print("Downloading...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")