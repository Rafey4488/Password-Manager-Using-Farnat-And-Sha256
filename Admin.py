from datetime import datetime
import tkinter as tk
from tkinter import *
from sqlite3 import Error
from tkinter import ttk
from tkinter import ttk, messagebox
from main import *
#from customer1 import *
from PIL import Image, ImageTk

class Admin:
    def __init__(self, window):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Welcome")
        self.window.minsize(500, 600)
        self.window.maxsize(500, 600)

        # Load the image file
        bg_image = Image.open("C:/Users/RR/Desktop/IS Project/background_image.png")

        # Resize the image to fit the window size
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)


        #logo
        logo_image = Image.open("C:/Users/RR/Desktop/IS Project/management.png").convert("RGBA") 
        resized_logo = logo_image.resize((100, 100))
        self.logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label = tk.Label(window, image=self.logo, background="#00264a")
        self.logo_label.place(relx=0.25, rely=0.18, height=90 ,width=90)

        logo_image1 = Image.open("C:/Users/RR/Desktop/IS Project/management.png").convert("RGBA") 
        resized_logo1 = logo_image.resize((100, 100))
        self.logo1 = ImageTk.PhotoImage(resized_logo1)
        self.logo1_label = tk.Label(window, image=self.logo, background="#ffffff")
        self.logo1_label.place(relx=0.6, rely=0.18, height=90 ,width=90)
        
        # Button
        self.Button1 = tk.Button(self.Canvas1, command=self.selectMain ,activebackground="#ececec",
                                 activeforeground="#000000", background="#00264a", disabledforeground="#a3a3a3",
                                 foreground="#ffffff", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''USER''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.25, rely=0.35, height=24, width=90)

        self.Button2 = tk.Button(self.Canvas1, activebackground="#ececec",
                                 activeforeground="#000000", background="#ffffff", disabledforeground="#a3a3a3",
                                 foreground="#000000", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''ADMIN''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.6, rely=0.35, height=24, width=87)

        self.Label1 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#FFFFFF",
                               text='''PLEASE SELECT YOUR ROLE''')
        self.Label1.place(relx=0.28, rely=0.08, height=31, width=250)





         #Entry 
        self.Label2 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER NAME : ''')
        self.Label2.place(relx=0.2, rely=0.45, height=21, width=140)

        self.Entry1 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry1.place(relx=0.5, rely=0.45, height=21, relwidth=0.264)
         #Place Holder
        self.placeholder_text = "Enter Name..."
        self.Entry1.insert(0, self.placeholder_text)
        self.Entry1.bind("<FocusIn>", self.on_entry_click)
        self.Entry1.bind("<FocusOut>", self.on_entry_leave)
        self.Entry1.place(relx=0.5, rely=0.45, height=21, relwidth=0.264)



        self.Label3 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER PASSWORD : ''')
        self.Label3.place(relx=0.2, rely=0.52, height=21, width=140)

        self.Entry2 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry2.place(relx=0.5, rely=0.52, height=21, relwidth=0.264)

        #Generate Password
        self.Button2 = tk.Button(window,  
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''Generate''')
        self.Button2.place(relx=0.79, rely=0.52, height=21, width=80)
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")

         #Place Holder
        self.placeholder_text2 = "Enter Password..."
        self.Entry2.insert(0, self.placeholder_text2)
        self.Entry2.bind("<FocusIn>", self.on_entry_click2)
        self.Entry2.bind("<FocusOut>", self.on_entry_leave2)
        self.Entry2.place(relx=0.5, rely=0.52, height=20, relwidth=0.264)

        #Email
        self.Label4 = tk.Label(window, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''ENTER EMAIL : ''')
        self.Label4.place(relx=0.2, rely=0.59, height=21, width=140)

        self.Entry4 = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.Entry4.place(relx=0.5, rely=0.59, height=21, relwidth=0.264)

         #Place Holder
        self.placeholder_text4 = "Enter Email..."
        self.Entry4.insert(0, self.placeholder_text4)
        self.Entry4.bind("<FocusIn>", self.on_entry_click4)
        self.Entry4.bind("<FocusOut>", self.on_entry_leave4)
        self.Entry4.place(relx=0.5, rely=0.59, height=21, relwidth=0.264)

        #login
        self.Button1 = tk.Button(window, 
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''LOGIN''')
        self.Button1.place(relx=0.35, rely=0.7, height=41, width=130)  # Adjust the relx, rely, height, and width as needed
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        # #signup
        # self.Button2 = tk.Button(window, 
        #                          activebackground="#ececec",
        #                          background="#00406c", 
        #                          foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
        #                          highlightcolor="black", pady="0",
        #                          text='''SIGNUP''')
        # self.Button2.place(relx=0.5, rely=0.7, height=41, width=130)  # Adjust the relx, rely, height, and width as needed
        # self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")


        #Feild1
    def on_entry_click(self, event):
        if self.Entry1.get() == self.placeholder_text:
            self.Entry1.delete(0, tk.END)
            self.Entry1.config(foreground='Black')

    def on_entry_leave(self, event):
        if self.Entry1.get() == '':
            self.Entry1.insert(0, self.placeholder_text)
            self.Entry1.config(foreground='gray')
    
    #feild2
    def on_entry_click2(self, event):
        if self.Entry2.get() == self.placeholder_text2:
            self.Entry2.delete(0, tk.END)
            self.Entry2.config(foreground='Black', show='x')

    def on_entry_leave2(self, event):
        if self.Entry2.get() == '':
            self.Entry2.insert(0, self.placeholder_text2)
            self.Entry2.config(foreground='gray', show='')
    
    #feild4
    def on_entry_click4(self, event):
        if self.Entry4.get() == self.placeholder_text4:
            self.Entry4.delete(0, tk.END)
            self.Entry4.config(foreground='Black')

    def on_entry_leave4(self, event):
        if self.Entry4.get() == '':
            self.Entry4.insert(0, self.placeholder_text4)
            self.Entry4.config(foreground='gray')

    def selectMain(self):
        self.window.withdraw()
        WelcomeScreen(tk.Toplevel())




# if __name__ == "__main__":
#     root = tk.Tk()
#     welcome_screen = WelcomeScreen(root)
#     root.mainloop()
