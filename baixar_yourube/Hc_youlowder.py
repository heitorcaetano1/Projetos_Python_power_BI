#ferramentas
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widegets ():
    link_label = Label(root,text="YouTube link: ",
                       bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root,width=55,
                          textvariable= video_link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Descrição: ",
                              bg="#E8D579")

    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)

    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    download_B = Button(root, text="Download",
                        command=Download,
                        width=20,
                        bg="#05E8E0")
    download_B.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)
def Browse():

    download_Diretory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    download_Path.set(download_Diretory)

def Download():
    Youtube_link = video_link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.first()

    videoStream.download(download_Folder)

    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOAD AND SAVED IN\n" + download_Folder)

root = tk.Tk()

root.geometry("600x120")
root.resizable(False, False)
root.title("YOU_Louder")
root.config(background="#000000")

video_link = StringVar()
download_Path = StringVar()

Widegets()

root.mainloop()