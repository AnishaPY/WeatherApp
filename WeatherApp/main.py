from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import requests

def data_get():
    city = city_name.get()
    api_key = "f8c21eb7e0c1adea91b757e4dd13ac77"
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    l2.config(text=data["weather"][0]["main"])
    l4.config(text=data["weather"][0]["description"])
    l6.config(text=str(int(data["main"]["temp"] - 273.15)))
    l8.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x500")

# Correct image path
bg_image = Image.open("image/weather.jpg") 
bg_image = bg_image.resize((500, 500), Image.Resampling.LANCZOS)  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(win, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_name = Label(win, text="Welcome to Weather App", font=("Times New Roman", 20, "bold"))
title_name.place(x=25, y=50, height=40, width=450)

city_name = StringVar()
places_in_nepal = [
    "Kathmandu", "Pokhara", "Biratnagar", "Lalitpur", "Bhaktapur",
    "Birgunj", "Dharan", "Nepalgunj", "Butwal", "Hetauda",
    "Itahari", "Janakpur", "Chitwan", "Bharatpur", "Bhadrapur",
    "Gorkha", "Lumbini", "Tansen", "Dhulikhel", "Panauti",
    "Tulsipur", "Jumla", "Surkhet", "Dhangadhi", "Mahendranagar",
    "Ilam", "Panchthar", "Sindhuli", "Palpa", "Gulmi", "Baglung"
]
com = ttk.Combobox(win, values=places_in_nepal, font=("Times New Roman", 15), textvariable=city_name)
com.place(x=75, y=120, height=40, width=350)

l1 = Label(win, text="Weather Climate", font=("Times New Roman", 10, "bold"))
l1.place(x=90, y=270, height=30, width=150)

l2 = Label(win, text="", font=("Times New Roman", 10, "bold"))
l2.place(x=250, y=270, height=30, width=150)

l3 = Label(win, text="Weather Description", font=("Times New Roman", 10, "bold"))
l3.place(x=90, y=320, height=30, width=150)

l4 = Label(win, text="", font=("Times New Roman", 10, "bold"))
l4.place(x=250, y=320, height=30, width=150)

l5 = Label(win, text="Temperature", font=("Times New Roman", 10, "bold"))
l5.place(x=90, y=370, height=30, width=150)

l6 = Label(win, text="", font=("Times New Roman", 10, "bold"))
l6.place(x=250, y=370, height=30, width=150)

l7 = Label(win, text="Pressure", font=("Times New Roman", 10, "bold"))
l7.place(x=90, y=420, height=30, width=150)

l8 = Label(win, text="", font=("Times New Roman", 10, "bold"))
l8.place(x=250, y=420, height=30, width=150)

but = Button(win, text="Check", font=("Times New Roman", 15, "bold"), command=data_get)
but.place(x=180, y=190, height=30, width=150)

win.mainloop()
