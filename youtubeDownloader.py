from pytube import YouTube
from tkinter import*
window=Tk()
window.title("YOUTUBE VIDEO DOWNLOADER")
window.geometry("600x400")
window.iconbitmap("images/YouTube_23392.ico")
window.configure(bg="#d9faf1")

#top label
label1=Label(window,text="Paste your youtube link here",font="Tahoma 15",bg="#d9faf1",height=3,)
#type box
box=Entry(font="arial 20",bg="#c2bebe",width=25,)


#click button
b1=Button(window,text="Get Video",bg="#424141",fg="white",width=15,activebackground="red")

label1.pack()
box.pack()
b1.pack()

window.mainloop()

