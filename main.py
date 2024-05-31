from datetime import datetime
import tkinter as tk
from tkinter import *
from sqlite3 import Error
from tkinter import ttk
from tkinter import ttk, messagebox
from Admin import *
from PIL import Image, ImageTk
import sqlite3
import random
import string
import hashlib
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
import time
from tkinter import simpledialog, messagebox

def convert_to_sha256(data):
    sha256_hash = hashlib.sha256()    
    sha256_hash.update(data.encode('utf-8'))    
    return sha256_hash.hexdigest()

class WelcomeScreen:
    def GetUserName(self):
        return self.UName.get()
    def save_Info(self):
        UUB = self.UName.get()
        if self.UName.get() == self.placeholder_text and self.Entry2.get() == self.placeholder_text2 and self.Entry4.get() == self.placeholder_text4:
            tk.messagebox.showinfo("Warning!!","Enter Data before Sign Up plz!!")
        else:
            try:
                 UserName = self.UName.get()
                 Passwordbb = self.Entry2.get()
                 Email = self.Entry4.get()
                 Password = convert_to_sha256(Passwordbb)
                 con = sqlite3.connect('IS_Project.db')
                 cursor = con.cursor()            
                 cursor.execute("Insert into login(UserName,U_or_A,Email,Password) values(?,'U',?,?)",
                           (UserName,Email,Password))
                 con.commit()
                 con.close()
                 messagebox.showinfo("Congrats!!","Your Data has been Saved!!\nYou can login now!!")
            except sqlite3.Error as e:
                tk.messagebox.showinfo ("Warning!!","Username or Email Already in use please choose another one!!")
    
    
    def check_MainInfo(self):
        if self.UName.get() == self.placeholder_text or self.Entry2.get() == self.placeholder_text2:
            tk.messagebox.showinfo("Warning!!", "Enter Username and Password before Login please!!")
            return False
        else:
            try:
                UserName = self.UName.get()
                Passwordbb = self.Entry2.get()
                Password = convert_to_sha256(Passwordbb)
                con = sqlite3.connect('IS_Project.db')
                cursor = con.cursor()
                cursor.execute("SELECT * FROM login WHERE UserName=? AND Password=? And U_or_A = 'U' ", (UserName, Password))
                result = cursor.fetchone()
                con.close()
                if result:
                    tk.messagebox.showinfo("Success!!", "Login Successful!!")
                    return True
                else:
                    tk.messagebox.showinfo("Failed!!", "Invalid Username or Password!!")
                    return False
            except sqlite3.Error as e:
                tk.messagebox.showinfo("Error!!", "An error occurred while trying to login: {}".format(e))
                return False

    def GeneratePassword(self):
        length = 8
        chars = string.ascii_letters
        chars += string.digits
        randompass = ''.join([random.choice(chars) for i in range(length)])
        self.Entry2.delete(0,tk.END)
        self.Entry2.insert(0,randompass)

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
        logo_image = Image.open("C:/Users/RAZI/Desktop/IS Project/management.png").convert("RGBA") 
        resized_logo = logo_image.resize((100, 100))
        self.logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label = tk.Label(window, image=self.logo, background="#ffffff")
        self.logo_label.place(relx=0.25, rely=0.18, height=90 ,width=90)

        logo_image1 = Image.open("C:/Users/RAZI/Desktop/IS Project/management.png").convert("RGBA") 
        resized_logo1 = logo_image.resize((100, 100))
        self.logo1 = ImageTk.PhotoImage(resized_logo1)
        self.logo1_label = tk.Label(window, image=self.logo, background="#00264a")
        self.logo1_label.place(relx=0.6, rely=0.18, height=90 ,width=90)
        
        # Button
        self.Button1 = tk.Button(self.Canvas1, activebackground="#ececec",
                                 activeforeground="#000000", background="#ffffff", disabledforeground="#a3a3a3",
                                 foreground="#000000", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''USER''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.25, rely=0.35, height=24, width=90)

        self.Button2 = tk.Button(self.Canvas1, command=self.selectAdmin, activebackground="#ececec",
                                 activeforeground="#000000", background="#00406c", disabledforeground="#a3a3a3",
                                 foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
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
                               text='''ENTER USERNAME : ''')
        self.Label2.place(relx=0.2, rely=0.45, height=21, width=140)

        self.UName = tk.Entry(window, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                              foreground="#000000")
        self.UName.place(relx=0.5, rely=0.45, height=21, relwidth=0.264)
         #Place Holder
        self.placeholder_text = "Enter UserName..."
        self.UName.insert(0, self.placeholder_text)
        self.UName.bind("<FocusIn>", self.on_entry_click)
        self.UName.bind("<FocusOut>", self.on_entry_leave)
        self.UName.place(relx=0.5, rely=0.45, height=21, relwidth=0.264)


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
                                 text='''Generate''',command=self.GeneratePassword)
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
                                 text='''LOGIN''',command=self.LoginPage)
        self.Button1.place(relx=0.2, rely=0.7, height=41, width=130)  # Adjust the relx, rely, height, and width as needed
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        #signup
        self.Button2 = tk.Button(window,
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''SIGNUP''',command=self.save_Info)
        self.Button2.place(relx=0.5, rely=0.7, height=41, width=130)  # Adjust the relx, rely, height, and width as needed
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")

        #Disclaimer
        self.Label10 = tk.Label(window, background="#00406c" , disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 8", foreground="#ffffff",
                               text='''*Disclaimer!!! You must remember your password. ''')
        self.Label10.place(relx=0.03, rely=0.85, height=17, width=300)

        self.Label11 = tk.Label(window, background="#00406c" , disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 8", foreground="#ffffff",
                               text='''*We Recommend you to use generated password.''')
        self.Label11.place(relx=0.03, rely=0.91, height=17, width=300)

        #Feild1
    def on_entry_click(self, event):
        if self.UName.get() == self.placeholder_text:
            self.UName.delete(0, tk.END)
            self.UName.config(foreground='Black')

    def on_entry_leave(self, event):
        if self.UName.get() == '':
            self.UName.insert(0, self.placeholder_text)
            self.UName.config(foreground='gray')
    
    #feild2
    def on_entry_click2(self, event):
        if self.Entry2.get() == self.placeholder_text2:
            self.Entry2.delete(0, tk.END)
            self.Entry2.config(foreground='Black')

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



    def selectAdmin(self):
        self.window.withdraw()
        Admin(tk.Toplevel()) # type: ignore

    def LoginPage(self):
        if self.check_MainInfo() == True:
            self.window.withdraw()
            CheckBackPageInfo(tk.Toplevel()) # type: ignore

    
    def BackPage(self):
        if self.check_MainInfo() == True:
            self.window.withdraw()

class CheckBackPageInfo:
    def __init__(self, window):
        self.window = window

        self.window_width = 1000
        self.window_height = 350
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Information")
        self.window.minsize(1000, 350)
        self.window.maxsize(1000, 350)

        # # Load the background image
        bg_image = Image.open("C:/Users/RR/Desktop/IS Project/background_image.png")
        resized_image = bg_image.resize((self.window_width, self.window_height))
        self.resized_bg_image = ImageTk.PhotoImage(resized_image)

        # Create canvas
        self.Canvas1 = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.Canvas1.pack()

        # Display background image
        self.Canvas1.create_image(0, 0, anchor=tk.NW, image=self.resized_bg_image)

        self.frame = tk.Frame(self.Canvas1, background="",height=600)  # Create the frame on the canvas
        self.frame.pack()

        self.create_widgets()  # Call create_widgets after creating frame

        # Add account button
        self.Button2 = tk.Button(window,
                                 command=self.gotoadd,   
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''Add Account''')
        self.Button2.place(relx=0.85, rely=0.01, height=21, width=100)
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")


        #Back Button
        self.Buttonback = tk.Button(window,  
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0",
                                 pady="0",
                                 text='''Back''', command=self.BackPage)
        self.Buttonback.place(relx=0.85, rely=0.88, height=25, width=100)
        self.Buttonback.configure(font="-family {Segoe UI} -size 10 -weight bold")

        #Instructions
        
        self.Label8 = tk.Label(window, background=None , disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 8", foreground="#000000",
                               text='''*Please click the password you need to decrypt. ''')
        self.Label8.place(relx=0.02, rely=0.85, height=18, width=250)

        self.Label9 = tk.Label(window, background=None , disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 8", foreground="#000000",
                               text='''*If you need to add accoun click on add account button.''')
        self.Label9.place(relx=0.02, rely=0.9, height=18, width=300)

    def BackPage(self):
        self.window.withdraw()
        WelcomeScreen(tk.Toplevel())


    

    def create_widgets(self):
        self.account_id_label = tk.Label(self.frame, text="User Accounts Info", background="#00406c", foreground="#ffffff")
        self.account_id_label.pack(pady=5)

        # Database Connections
        conn = sqlite3.connect('IS_Project.db')
        cursor = conn.cursor()

        # Query to select data from a table
        cursor.execute("SELECT * FROM user_show")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        # Close the database connection
        conn.close()

        # Create a Treeview widget inside the frame
        tree_frame = tk.Frame(self.frame)
        tree_frame.pack(expand=True, fill='both', pady=10, padx=10)

        tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

        # Define headings and columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=int(self.window_width/len(columns)))

        # Insert data into the Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Add a vertical scrollbar to the Treeview
        vscrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=vscrollbar.set)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add a horizontal scrollbar to the Treeview
        hscrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=hscrollbar.set)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Pack the Treeview widget into the frame with expand and fill options
        tree.pack(expand=True, fill='both')

        # Pack the tree_frame to cover the whole page
        tree_frame.pack(expand=True, fill='both')

        self.tree = tree  # Make sure to assign tree to self.tree
        self.tree.bind("<<TreeviewSelect>>", self.on_row_click)

    def get_login_password(self, uname):
        # Connect to the SQLite database
        conn = sqlite3.connect('IS_Project.db')  # Replace 'IS_Project.db' with your actual database file path
        cursor = conn.cursor()

        # Execute the SELECT query to find the Account_Password for the specified username
        cursor.execute("SELECT Password FROM login WHERE UserName =?", (uname,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Close the connection
        conn.close()

        # Return the Account_Password if found, otherwise None
        return result[0] if result else None

    def fernet_decrypt(self, salt, password, encrypted_data):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=9999,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        # Encrypt the account password
        fkey = Fernet(key)
        try:
            fernetdecrypted_data = fkey.decrypt(encrypted_data)
            decrypted_data = fernetdecrypted_data.decode('utf-8')
            return decrypted_data
        except InvalidToken:
            return None

    def get_user_salt(self, uname):
        # Connect to the SQLite database
        conn = sqlite3.connect('IS_Project.db')  # Replace 'IS_Project.db' with your actual database file path
        cursor = conn.cursor()

        # Execute the SELECT query
        cursor.execute("SELECT User_Salt FROM user_details WHERE LoginUserName =?", (uname,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Close the connection
        conn.close()

        # Return the User_Salt if found, otherwise None
        return result[0] if result else None

    def on_row_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            # Extract the Account_Password from the selected row
            index_of_account_password_column = 3
            account_password = str(item['values'][index_of_account_password_column])
            # byteAcpass = account_password.encode()

            # Extract the User_Salt from the selected row
            index_of_username_column = 1
            uname = item['values'][index_of_username_column]
            salt =  self.get_user_salt(uname)
                        
            # Show password input dialog
            dialogpassword = simpledialog.askstring("Password", "Enter your Login password:", show='*')
            password = self.get_login_password(uname)
            shapass = convert_to_sha256(dialogpassword)

            BytePass = dialogpassword.encode()

            #Decryption:
            decryptedpass =  self.fernet_decrypt(salt,BytePass,account_password)
            

            if password == shapass:
                message = f"Password for this website is:\n{decryptedpass}"
                messagebox.showinfo("Decrypted Password!!", message)
            else:
                messagebox.showerror("Error", "Incorrect password!")


    def gotoadd(self):
        self.window.withdraw()
        AddAccount(tk.Toplevel())

                
class AddAccount:
    def __init__(self, window):
        self.window = window
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.title("Add Account")
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

        self.Label1 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#FFFFFF",
                               text='''ENTER YOUR INFORMATION''')
        self.Label1.place(relx=0.28, rely=0.08, height=31, width=250)

        # Entry 
        self.Label2 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''User Name : ''')
        self.Label2.place(relx=0.2, rely=0.2, height=21, width=140)

        self.Entry2 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry2.place(relx=0.5, rely=0.2, height=21, relwidth=0.264)
        self.Entry2.insert(0, welcome_screen.GetUserName())
        self.Entry2.config(state="disabled")

        # Username
        self.Label3 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''Account Username : ''')
        self.Label3.place(relx=0.2, rely=0.3, height=21, width=140)

        self.Entry3 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry3.place(relx=0.5, rely=0.3, height=21, relwidth=0.264)

        # Password
        self.Label4 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''Account Password : ''')
        self.Label4.place(relx=0.2, rely=0.4, height=21, width=140)

        self.Entry4 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry4.place(relx=0.5, rely=0.4, height=21, relwidth=0.264)

        # Email
        self.Label5 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''Site Name : ''')
        self.Label5.place(relx=0.2, rely=0.5, height=21, width=140)

        self.Entry5 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry5.place(relx=0.5, rely=0.5, height=21, relwidth=0.264)

        # URL
        self.Label6 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''URL : ''')
        self.Label6.place(relx=0.2, rely=0.6, height=21, width=140)

        self.Entry6 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry6.place(relx=0.5, rely=0.6, height=21, relwidth=0.264)

        # Description
        self.Label7 = tk.Label(self.Canvas1, background="#00406c", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 10 -weight bold", foreground="#ffffff",
                               text='''Description : ''')
        self.Label7.place(relx=0.2, rely=0.7, height=21, width=140)

        self.Entry7 = tk.Entry(self.Canvas1, background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="#000000")
        self.Entry7.place(relx=0.5, rely=0.7, height=21, relwidth=0.264)

        # Enter
        self.Button1 = tk.Button(self.Canvas1,
                                 activebackground="#ececec",
                                 background="#00406c",
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''ENTER''', command=self.AddInfo)
        self.Button1.place(relx=0.35, rely=0.8, height=41, width=130)  # Adjust the relx, rely, height, and width as needed
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")

        #Back Button
        self.Buttonback2 = tk.Button(window,  
                                 activebackground="#ececec",
                                 background="#00406c", 
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''Back''', command=self.backinfo)
        self.Buttonback2.place(relx=0.7, rely=0.9, height=25, width=100)
        self.Buttonback2.configure(font="-family {Segoe UI} -size 10 -weight bold")

    def backinfo(self):
        self.window.withdraw()
        CheckBackPageInfo(tk.Toplevel())

    def AddInfo(self):
        dialogpassword = simpledialog.askstring("Password", "Enter your Login password:", show='*')
        password = dialogpassword.encode()
        Uname = self.Entry2.get()
        AUname = self.Entry3.get()
        AccountPass = self.Entry4.get()
        APassde = AccountPass.encode()
        WebName = self.Entry5.get()
        url = self.Entry6.get()
        des = self.Entry7.get()

        # Generate a random salt
        salt = os.urandom(16)

        # Derive the key using PBKDF2HMAC
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=9999,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        # Encrypt the account password
        fkey = Fernet(key)
        APass = fkey.encrypt(APassde)

        # Connect to the SQLite database
        con = sqlite3.connect('IS_Project.db')

        try:
            with con:
                cursor = con.cursor()
                cursor.execute("SELECT MAX(ID) AS max_id FROM user_details")
                result = cursor.fetchone()

                if result and result[0] is not None:
                    max_id = result[0]
                    new_id = max_id + 1
                else:
                    new_id = 1

                # Insert the new account details into the database
                cursor.execute("INSERT INTO user_details (ID, LoginUserName, Account_Username, Account_Password, Website_Name, URL, Description, User_Salt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (new_id, Uname, AUname, APass, WebName, url, des, salt))

                con.commit()
                messagebox.showinfo("Success", "Account details saved successfully!")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()


    # def on_row_click(self, event):
    #     selected_item = self.tree.selection()
    #     if selected_item:
    #         item = self.tree.item(selected_item)
    #         decryptedpass = 'Wow!!'

    #         # Show password input dialog
    #         password = simpledialog.askstring("Password", "Enter your password:", show='*')
            
    #         if password:
    #             # You can add password verification here if needed

    #             # Show the messagebox with custom info
    #             message = f"Password for this website is:\n",decryptedpass
    #             messagebox.showinfo("Row Information", message)

        
if __name__ == "__main__":
    root = tk.Tk()
    welcome_screen = WelcomeScreen(root)
    root.mainloop()
