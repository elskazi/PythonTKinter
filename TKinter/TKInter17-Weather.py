#pip install requests
#pip install ttkthemes

from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = "bcb339fb2806c606ec2a19c8b12f4053"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}



root = ThemedTk(theme="arc")
root.title("Запрос погоды")
root.geometry("500x400+400+150")
root.resizable(0,0)
root.iconbitmap("ico.ico")

def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        description = weather['weather'][0]['description']
        sunrise_time = weather['sys']['sunrise']
        sunset_time = weather['sys']['sunset']
        sunrise_time_struct = time.localtime(sunrise_time)
        sunset_time_struct = time.localtime(sunset_time)
        sunrise = time.strftime("%H:%M:%S", sunrise_time_struct )
        sunset = time.strftime("%H:%M:%S", sunset_time_struct)
        #print("OK")
        return f"Местоположение: {city}, {country} \n" \
               f"Температура: {temp} C \n" \
               f"Атм. давление: {pressure} гПА\n" \
               f"Влажность: {humidity} %\n" \
               f"Скорость вветра: {wind} м/с\n" \
               f"Погодные условия: {description}\n" \
               f"Восход: {sunrise} \n" \
               f"Закат: {sunset} "
    except:
        return "Ошибка получения данных... \n" \
               "это может быть связано с тем \n" \
               "что не верно ввели город или \n" \
               "данные просто не доступны"




def get_weather(event=""):
    if not entry.get():
        messagebox.showwarning("Ошибка", "Введите запрос в формате city,country_code" )
    else:
        params = {
            "appid": API_KEY,
            "q": entry.get(),
            "units": "metric",
            "lang": "ru",
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        #print(weather)
        label['text'] = print_weather(weather)

def city_go(text):
    entry.delete(0, 300)
    entry.insert(0, text)
    get_weather()
#def city_go2():
#    entry.delete(0, 300)
#    entry.insert(0, btr_city2["text"])
#    get_weather()

city_ru = ["Санкт-Петербург", "Москва", "Сочи", "Ростов-на-Дону", "Казань", "Самара", "Воркута"]
column_m = 0
for c in city_ru:
    btr_city = ttk.Button(root, text=c,
                          style="btnCity.TButton",
                          command=lambda text=c: city_go(text), ).grid(row=0, column=column_m)
    column_m+=1

#btr_city = ttk.Button(root, text="Санкт-Петербург", style="btnCity.TButton", command = city_go)
#btr_city.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.1, anchor="n")

#btr_city2 = ttk.Button(root, text="Москва", style="btnCity.TButton", command = city_go2)
#btr_city2.place(relx=0.3, rely=0, relwidth=0.2, relheight=0.1, anchor="n")

#btn_city3 = ttk.Button(root)
#btn_city3.grid()

style = ttk.Style()
style.configure("TLabel", padding=5, font="Arial 12")
style.configure("top.TLabel", font="Arial 8")
style.configure("btnCity.TButton", font="Arial 7", padding=4)


#top_frame
top_label = ttk.Label(root, text="Введите город, напиример 'Санкт-Петербург'", style="top.TLabel" )
top_label.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="n")
#top_frame
top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.1, anchor="n")

entry = ttk.Entry(top_frame,)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

#lower_frame
lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.9, relheight=0.6, anchor="n")

label = ttk.Label(lower_frame, anchor= "nw")
label.place(relwidth=1, relheight=1)

# Жмяк по Интеру забиндить
entry.bind("<Return>", get_weather)



root.mainloop()