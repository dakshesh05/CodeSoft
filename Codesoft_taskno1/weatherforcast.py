from tkinter import Tk,Label,Entry,Button,UNDERLINE,StringVar
import requests

api_key = '4c7b099dca0216aae86174fb3b2104be'
api_url = "http://api.openweathermap.org/data/2.5/weather"

def pridict():
    location = valueEntry.get()
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        Label(text = "Temperature : ").grid(row = 3,column=1)
        Label(text = temperature,fg="red").grid(row = 3,column=2)
        
        Label(text = "humidity : ").grid(row = 4,column=1)
        Label(text = humidity,fg="red").grid(row = 4,column=2)
        
        Label(text = "description : ").grid(row = 5,column=1)
        Label(text = description,fg="red").grid(row = 5,column=2)
        
        Label(text = "wind_speed : ").grid(row = 6,column=1)
        Label(text = wind_speed,fg="red").grid(row = 6,column=2)
        Label(text = "These are the attributes that are being fetch.").grid(row = 7,column=1)        
    else:
        Label(text = "Something went Wrong. Please Try again!").grid(row = 7,column=1)
        
root = Tk()
root.geometry("480x360")
root.maxsize(500,400)
root.title("Weather Forcast")
Label(text = "Weather Forcast", fg = "red", font=("Times",20,"bold",UNDERLINE)
      ).grid(row=1,column=2)

Label(text = "Enter City / Zip Code : ",padx=5,pady=10,font=("times",13)).grid(row=2,column=1)

valueinput = StringVar()
valueEntry = Entry(root, textvariable=valueinput)
valueEntry.grid(row=2, column=2)

Button(text = "Pridict",command=pridict,bg="blue",fg="white",width=5).grid(row = 2,column=3)

root.mainloop()
