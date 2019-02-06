#GUI toolkit
import tkinter as tk
import http.client as httplib

import json

class WeatherGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.enter_city_label = tk.Label(self, text="Enter City")
        #Creating the textbox for the user to enter their city
        self.city = tk.Entry(self)
        #Standard button to run the method get_weather
        self.enter_city_button = tk.Button(self, text="Enter", command = self.get_weather)
        #Creating a message box that displays the information
        self.weather_information = tk.Message(self, textvariable = "")

        self.enter_city_label.pack(side="top", fill="x", pady=2)
        self.city.pack(side="top", fill="x", padx=50 ,pady=2)
        self.enter_city_button.pack(side="top", pady=2)
        self.weather_information.pack(side="top", fill="both", expand=True, anchor="center")

    def get_weather(self):
        connection = httplib.HTTPConnection("api.openweathermap.org")
        #reads in the api key
        api_key = open("apikey.txt", "r").read()
        url = "/data/2.5/weather?q={0}&APPID={1}&units=metric".format(self.city.get(), api_key)
        connection.request("GET", url)
        response = connection.getresponse()

        #takes the response, decodes the bytes and then converts it into json
        json_file = json.loads(response.read().decode('utf-8'))

        #TODO: Improve formatting
        #TODO: Add an image based on the weather forecast
        information = '''
Place:          {0}
Weather:        {1}
Temperature:    {2}°
Wind speed:     {3}
Cloud coverage: {4}%
                '''.format(json_file['name'], 
                    json_file['weather'][0]['main'], 
                    json_file['main']['temp'], 
                    json_file['wind']['speed'], 
                    json_file['clouds']['all'])

        self.weather_information.configure(text=information)

if __name__ == "__main__":
    top = tk.Tk()
    WeatherGUI(top).pack(fill = "both", expand = True)
    top.title("What's the Weather?")
    top.resizable(width=False, height=False)
    #top.geometry('300x250')
    top.mainloop()
