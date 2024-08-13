from tkinter import *
import math
import random
import smtplib
import pymysql as sql 

# Function to generate a 6-digit OTP
def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

# Function to send OTP via email
def send_otp(email_id, otp):
    message = f"{otp} is your OTP"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("skzaidu596@gmail.com", "vamf csxy rfdg gojv")
    server.sendmail("skzaidu596@gmail.com", email_id, message)
    server.quit()

# Function to handle the OTP generation and sending
def handle_otp():
    email = email_entry.get()
    otp = generate_otp()
    send_otp(email, otp)
    otp_label.config(text="OTP has been sent to your email!")
    otp_value.set(otp)  # Store the OTP to validate later

# Function to validate the OTP entered by the user
def validate_otp():
    entered_otp = otp_entry.get()
    if entered_otp == otp_value.get():
        otp_label.config(text="OTP Verified Successfully!")
    else:
        otp_label.config(text="Invalid OTP! Please try again.")

# Setting up the main Tkinter window
window = Tk()
window.title("SignUp")
window.geometry('950x500+300+200')  # Corrected 'x' to separate width and height
window.configure(bg="#fff")
window.resizable(False, False)

# Image path setup
img_path = 'D:\\my practice programs\\python\\TKINTER\\login.png'

try:
    img = PhotoImage(file=img_path)
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)
except TclError:
    print(f"Error: Unable to load image. Please check the file path and format.")

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='SignUp', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

### Username Field
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

### Email Field
def on_enter(e):
    email_entry.delete(0, 'end')

def on_leave(e):
    if email_entry.get() == '':
        email_entry.insert(0, 'Email')

email_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
email_entry.place(x=30, y=150)
email_entry.insert(0, 'Email')
email_entry.bind("<FocusIn>", on_enter)
email_entry.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

### OTP Field
def on_enter(e):
    otp_entry.delete(0, 'end')

def on_leave(e):
    if otp_entry.get() == '':
        otp_entry.insert(0, 'OTP')

otp_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
otp_entry.place(x=30, y=220)
otp_entry.insert(0, 'OTP')
otp_entry.bind("<FocusIn>", on_enter)
otp_entry.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# Button to Get OTP
otp_value = StringVar()  # To store the generated OTP
Button(frame, width=39, pady=7, text='Get OTP', bg='#57a1f8', fg='white', border=0, command=handle_otp).place(x=35, y=280)
otp_label = Label(frame, text='', fg='red', bg='white', font=('Microsoft Yahei UI Light', 9))
otp_label.place(x=90, y=310)

# Button to Validate OTP
Button (frame, width=39, pady=7, text='login', bg='#57a1f8', fg='white', border=0, command=validate_otp).place(x=35, y=340)

window.mainloop()

