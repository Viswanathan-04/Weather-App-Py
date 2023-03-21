from tkinter import *
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Weather App - AskPython.com")
city_value = StringVar()
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
def showWeather():
    url="https://www.google.com/search?q=chennai+weather"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)

city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack() 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()