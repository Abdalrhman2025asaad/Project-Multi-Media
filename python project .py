import tkinter as tk
from tkinter import messagebox
import yt_dlp
import vlc
import sys
import os


# Redirect VLC logs to a file to avoid excessive terminal output
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")

# Turn off verbose logging in VLC
os.environ["PYTHON_VLC_VERBOSE"] = "0"

def play_media(format_type):
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", " Request the user to input a valid video URL!")
        return

    try:
# Configuration options for yt-dlp
        ydl_opts = {"quiet": True, "format": format_type}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info["url"]
            play_stream(stream_url)
    except Exception as e:
        messagebox.showerror("Error", f" Something went wrong, an error has occurred: {e}")

def play_stream(stream_url):
    try:
        # Create VLC instance
        instance = vlc.Instance("--quiet", "Option to hide video title display during playback")
        player = instance.media_player_new()
        media = instance.media_new(stream_url)
        player.set_media(media)
        
# Set the audio volume level to 100% (maximum)
        player.audio_set_volume(100)
        
# Start video playback
        player.play()
        
# The confirmation message has been intentionally removed for clarity
# Displays an information message when the media starts playing with sound
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while trying to play: {e}")

# Initialize the GUI
root = tk.Tk()
root.title("Media Player")

tk.Label(root, text="insert the video URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Play High quality ", command=lambda: play_media("best")).pack(pady=5)
tk.Button(root, text="Play Low quality", command=lambda: play_media("worst")).pack(pady=5)
tk.Button(root, text="Play Audio ", command=lambda: play_media("bestaudio")).pack(pady=5)

root.mainloop()