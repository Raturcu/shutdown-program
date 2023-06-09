import tkinter as tk
import tkinter.font as font
import os


root= tk.Tk();
root.title("Shutdown Program")

def Shutdown_Func():
    #if shutdown == 'shutdown' :
        #print("Shutdown !")
    os.system("shutdown /s /t 00");
def Restart_func():
    os.system("shutdown -r -t 00")    


canvas=tk.Canvas(root,height=300,width=500)
canvas.pack();

frame=tk.Frame(root,bg="#263D42")
frame.place(relwidth=.8,relheight=.8,relx=.1,rely=.1)


shutdown_button=tk.Button(frame,text="Shutdown Computer",height=1,width=30,bg="#ff2200",fg="#fff",command=Shutdown_Func)
shutdown_button_font=font.Font(size=20)
shutdown_button["font"]=shutdown_button_font
shutdown_button.pack()

restart_button=tk.Button(frame,text="Restart Computer",height=1,width=30,bg="#ff2200",fg="#fff",command=Restart_func)
restart_button_font=font.Font(size=20)
restart_button["font"]=restart_button_font
restart_button.pack()

root.mainloop()