# PYTHON program to convert Video File into Audio File


"""MoviePy is a Python module for video editing, which can be used for basic operations (like cuts, concatenations, title insertions), video compositing (a.k.a. non-linear editing), video processing, or to create advanced effects. It can read and write the most common video formats, including GIF."""

import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()                           # take file name from ur device as input
video = moviepy.editor.VideoFileClip(video)
audio = video.audio                                 # extracting audio from video

audio.write_audiofile("sampleV-T-A.mp3")            # New File would be named as "sampleV-T-A.mp3"
print("Video File Converted To Audio File : DONE !")
