#GUI toolkit
import tkinter as tk
import http.client as httplib

import json

class WeatherGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.enter_city_label = tk.Label(self, text = "Enter City")
        #Creating the textbox for the user to enter their city
        self.city = tk.Entry(self)
        #Standard button to run the method get_weather
        self.enter_city_button = tk.Button(self, text = "Enter", command = self.get_weather)
        #Creating a message box that displays the information
        self.weather_information = tk.Message(self, text = "")

        self.enter_city_label.pack()
        self.city.pack()
        self.enter_city_button.pack()
        self.weather_information.pack()

    #TODO: Take the city and send a request to OpenWeather API.
    #Then need to parse the JSON file and take the relevant data.
    #Finally, I need to display the information
    def get_weather(self):
        connection = httplib.HTTPConnection("api.openweathermap.org")
        #TODO: read in the api key
        #api_key = 
        url = "/data/2.5/weather?q={0}&APPID={1}&units=metric".format(self.city.get(), api_key)
        connection.request("GET", url)
        response = connection.getresponse()

        #takes the response, decodes the bytes and then converts it into json
        json_file = json.loads(response.read().decode('utf-8'))

        #test
        print (json_file['name'])

        self.weather_information.configure(text = response.reason)


if __name__ == "__main__":
    top = tk.Tk()
    WeatherGUI(top).pack()
    top.mainloop()
