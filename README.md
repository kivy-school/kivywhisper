# KivyWhisper
## What is this?
This is a Kivy GUI for OpenAI's Whisper speech to text. Tested on Windows, but should work on Linux and Mac when packaged with PyInstaller. 

kivyschool links: 

https://kivyschool.com/blog/2024/07/12/kivy-whisper-part-1/

[![Watch the video](https://img.youtube.com/vi/2j4oQeDFVrs/maxresdefault.jpg)](https://www.youtube.com/embed/2j4oQeDFVrs)

## Why use it? 

The initial motivation for this repo is to have a GUI to manipulate Whisper. This is so that I can generate initial video to text files to put up transcripts on the kivyschool.com website. One good thing about this initial integration is that I can then switch models, make the GUI better, or even run this when I have no access to a terminal/cmd/powershell. Having complete control is really nice and being able to use Kivy to rapidly prototype a GUI is invaluable (this was built in 2 days discounting all the time I spent documenting it, total time was 6 days). Later on I still need to integrate multiprocessing to push blocking code onto a Python subprocess.

## What can you learn from this repo?

In this repo and associated youtube playlist, you will learn:

- How to integrate Kivy and OpenAI's Whisper automatic speech recognition system.
- How to deal with various Poetry bugs very easily (assuming you got the setup in the PREREQUISITE SETUP video of Pyenv + python-poetry)
- How to integrate machine learning/tensorflow Python packages with Kivy and package them with PyInstaller
- How to create and visualize Kivy app, then easily make it.
- How to use and manipulate Kivy's FileChooser widget on desktop.
- How to get and set data on various Kivy widgets.
- How to manipulate Kivy popups
- How to manipulate filepaths with Pathlib
- How to package a complex Kivy app with PyInstaller
- See firsthand how to create an app from concept to completion.
- See the app at various stages by running the various midpointX.py files


PREREQUISITE SETUP:

[![Watch the video](https://img.youtube.com/vi/qiIFJIqMHV0/maxresdefault.jpg)](https://www.youtube.com/embed/qiIFJIqMHV0)

## Rest of the playlist:

https://kivyschool.com/blog/2024/07/17/kivy-whisper-part-2/

https://kivyschool.com/blog/2024/07/19/kivy-whisper-part-3/

https://kivyschool.com/blog/2024/07/24/kivy-whisper-part-4/

https://kivyschool.com/blog/2024/07/26/kivy-whisper-part-5/

[![Watch the video](https://img.youtube.com/vi/vM4xBhjxF2E/maxresdefault.jpg)](https://www.youtube.com/embed/vM4xBhjxF2E)

[![Watch the video](https://img.youtube.com/vi/pMO68_QHHGo/maxresdefault.jpg)](https://www.youtube.com/embed/pMO68_QHHGo)

[![Watch the video](https://img.youtube.com/vi/9Z-8RYmOIns/maxresdefault.jpg)](https://www.youtube.com/embed/9Z-8RYmOIns)

[![Watch the video](https://img.youtube.com/vi/E5e3TIpz2zU/maxresdefault.jpg)](https://www.youtube.com/embed/E5e3TIpz2zU)
