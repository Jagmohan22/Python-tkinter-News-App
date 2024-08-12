import csv
import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
from tkinter import messagebox
class NewsApp:
  
  def __init__(self):
    self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=fbc3602059e94456b4ba9ccd4d58c09f').json()
    self.load_gui()
    self.load_news_item(0)
  def load_gui(self):
    self.root=Tk()
    self.root.title("UPPD")
    self.root.geometry('350x600')
    self.root.resizable(0,0)
    self.root.configure(background='black') 
  def clear(self):
    for i in self.root.pack_slaves():
      i.destroy()
  def load_news_item(self,index):
    
    self.clear()
    try:
      img_url = self.data['articles'][index]['urlToImage']
      raw_data = urlopen(img_url).read()
      im = Image.open(io.BytesIO(raw_data)).resize((350,250))
      photo = ImageTk.PhotoImage(im)
    except:
      img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
      raw_data = urlopen(img_url).read()
      im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
      photo = ImageTk.PhotoImage(im)
      
    label = Label(self.root,image=photo)
    label.pack()
    
    
    heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
    heading.pack(pady=(10,20))
    heading.config(font=('verdana',15))
    
    details = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=350,justify='center')
    details.pack(pady=(2,20))
    details.config(font=('verdana',12))
    
    frame = Frame(self.root,bg='black')
    frame.pack(expand=True,fill=BOTH)
    
    if(index != 0):
        Prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index-1))
        Prev.pack(side=LEFT)
    
    Read = Button(frame,text='Readmore',width=16,height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
    Read.pack(side=LEFT)
    
    if index!=len(self.data['articles']) - 1:
        next = Button(frame,text='Next',width=16,height=3,command=lambda :self.load_news_item(index+1))
        next.pack(side=LEFT)
    
    
    self.root.mainloop()
    
  def open_link(self,url):
    webbrowser.open(url)
  
def handle_login():
    email = email_input.get()
    password = pass_input.get()
    
    
    email = email_input.get()
    password = pass_input.get()

    
    with open('user_data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == email and row[2] == password:
                messagebox.showinfo("Success", "Successfully logged in")
                login_window.destroy()
                news_app = NewsApp()
                return
        messagebox.showerror("Login failed", "Invalid email or password")
    

        

def on_email_click(event):
    if email_input.get() == "Enter Email":
        email_input.delete(0, END)
        email_input.config(fg='black')

def on_pass_click(event):
    if pass_input.get() == "Enter Password":
        pass_input.delete(0, END)
        pass_input.config(fg='black')
        pass_input.config(show='*')
        

class SignUpPage:
    def __init__(self, parent):
        self.parent = parent
        self.sign_up_window = Toplevel(parent)
        self.sign_up_window.title("Sign Up")
        self.sign_up_window.geometry('350x600')
        self.sign_up_window.configure(background="black")
        
        text_label = Label(self.sign_up_window, text="Sign UP", fg="white", bg="black")
        text_label.pack()
        text_label.config(font=("verdana",24))
        
        

        self.username_label = Label(self.sign_up_window, text="Username", fg="white", bg="black")
        self.username_label.pack(pady=(20,5))
        self.username_label.config(font=("verdana",12))
        self.username_input = Entry(self.sign_up_window, width=50)
        self.username_input.pack(ipady=6, pady=(10,30))
        
        self.email_label = Label(self.sign_up_window, text="Email", fg="white", bg="black")
        self.email_label.pack(pady=(20,5))
        self.email_label.config(font=("verdana",12))
        self.email_input = Entry(self.sign_up_window, width=50)
        self.email_input.pack(ipady=6, pady=(1,15))
        
        self.pass_label = Label(self.sign_up_window, text="Password", fg="white", bg="black")
        self.pass_label.pack(pady=(20,5))
        self.pass_label.config(font=("verdana",12))
        self.pass_input = Entry(self.sign_up_window, width=50)
        self.pass_input.pack(ipady=6, pady=(1,15))
        
        self.sign_up_btn = Button(self.sign_up_window, text="Sign Up", bg='white', fg='black', width=15, height=2, command=self.handle_signup)
        self.sign_up_btn.pack(pady=(10,20))
        self.sign_up_btn.config(font=("verdana",9))
        self.otp = None

    def handle_signup(self):
        
        username = self.username_input.get()
        email = self.email_input.get()
        password = self.pass_input.get()

        
        with open('user_data.csv', mode='a', newline='') as file:
          writer = csv.writer(file)
          writer.writerow([username, email, password])

        messagebox.showinfo("Success", "Account created successfully!")
        self.sign_up_window.destroy()

def handle_signup():
    sign_up_page = SignUpPage(login_window)

  

login_window = Tk()
login_window.title("UPPD Login")
login_window.geometry('350x600')
login_window.configure(background="black")

img = Image.open("imageS3.png")
resized_img = img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(login_window, image=img)
img_label.pack(pady=(10,10))

text_label = Label(login_window, text="UPPD", fg="white", bg="black")
text_label.pack()
text_label.config(font=("verdana",24))

text1_label = Label(login_window, text="Uttar Purab Paschim Dakshin", fg="white", bg="black")
text1_label.pack()
text1_label.config(font=("verdana",14))



email_input = Entry(login_window, width=50, fg='grey')
email_input.pack(ipady=6, pady=(6, 15))
email_input.insert(0, 'Enter Email')
email_input.bind("<FocusIn>", on_email_click)



pass_input = Entry(login_window, width=50, fg='grey')
pass_input.pack(ipady=6, pady=(4, 15))
pass_input.insert(0, 'Enter Password')
pass_input.bind("<FocusIn>", on_pass_click)

login_btn = Button(login_window, text="Login Here", bg='white', fg='black', width=15, height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",9))

singUp_btn=Button(login_window, text="Sign Up Here", bg='white', fg='black', width=15, height=2,command=handle_signup)
singUp_btn.pack(pady=(10,20))
singUp_btn.config(font=("verdana",9))

text2_label = Label(login_window, text="UPPD: Your instant news fix, at your fingertips.", fg="white", bg="black")
text2_label.pack()
text2_label.config(font=("verdana",11))

text1_labe3 = Label(login_window,text="Your shortcut to the latest headlines.\n Stay informed with quick news updates.\n Get curated stories in a glance with UPPD.\n Your go-to app for bite-sized news.", fg="white", bg="black")
text1_labe3.pack()
text1_labe3.config(font=("verdana",10))
login_window.mainloop()
