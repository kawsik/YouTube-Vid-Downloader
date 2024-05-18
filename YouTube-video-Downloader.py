import pytube 
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_yt_video(url,save_path):
    try: 
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path = save_path)
        print("Video downloaded sucessfully")

    except Exception as e:
        print(e)

def open_dialog_box():
    folder = filedialog.askdirectory()
    if folder:
        print(f"{folder} is selected.")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the Youtube video url : ")
    save_dir = open_dialog_box()

    if save_dir:
        print("started to download") 
        download_yt_video(video_url,save_dir)

    else:
        print("Invalid Saved Location")  
