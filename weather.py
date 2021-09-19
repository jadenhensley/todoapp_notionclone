import time
import requests, json
# different formatted unicode symbols for terminal output
from formats import u_checkbox_empty, u_checkbox_full, u_moon, u_sun, u_clouds, u_umbrella

current_time = time.localtime()

f = open('config/api_tokens.json')

data = json.load(f)

cityid = str()
cityid = data['weatherdata']['cityid']
api_key = str()
api_key = data['weatherdata']['api_key']

f.close()

def Month():
    if current_time.tm_mon == 1:
        return "January"
    elif current_time.tm_mon == 2:
        return "February"
    elif current_time.tm_mon == 3:
        return "March"
    elif current_time.tm_mon == 4:
        return "April"
    elif current_time.tm_mon == 5:
        return "May"
    elif current_time.tm_mon == 6:
        return "June"
    elif current_time.tm_mon == 7:
        return "July"
    elif current_time.tm_mon == 8:
        return "August"
    elif current_time.tm_mon == 9:
        return "September"
    elif current_time.tm_mon == 10:
        return "October"
    elif current_time.tm_mon == 11:
        return "November"
    elif current_time.tm_mon == 12:
        return "December"


def AM_or_PM():
    return f"AM  {u_sun}" if current_time.tm_hour < 12 else f"PM  {u_moon}"
    # todo: make the moon / sun symbol more specific to PM hours
    # todo: add symbols for degree temperature

def TimeOfDay():
    """
    0: is morning
    1: is evening
    2: is night time
    """
    if current_time.tm_hour <= 10:
        return 0
    elif current_time.tm_hour >= 20:
        return 2
    else: # is in between 10 and 12 (this is awkward to read)
        return 1

def getWeekDay():
    if current_time.tm_wday == 0:
        return "Monday"
    elif current_time.tm_wday == 1:
        return "Tuesday"
    elif current_time.tm_wday == 2:
        return "Wednesday"
    elif current_time.tm_wday == 3:
        return "Thursday"
    elif current_time.tm_wday == 4:
        return "Friday"
    elif current_time.tm_wday == 5:
        return "Saturday"
    elif current_time.tm_wday == 6:
        return "Sunday"

def getLocalTime():
    if current_time.tm_min < 10:
        has_zero = "0"+str(current_time.tm_min)
        return f"{current_time.tm_hour % 12}:{has_zero}:{current_time.tm_sec} {AM_or_PM()}\n{Month()} {current_time.tm_mday}, {current_time.tm_year}"
    else:
        return f"{current_time.tm_hour % 12}:{current_time.tm_min}:{current_time.tm_sec} {AM_or_PM()}\n{Month()} {current_time.tm_mday}, {current_time.tm_year}"



def getLocalWeather():
    completeURL = f'https://api.openweathermap.org/data/2.5/weather?id={cityid}&appid={api_key}'
    response = requests.get(completeURL)
    data = response.json()
    return str(int(data["main"]["temp"] * (9/5) - 459.67)) + " degrees fahrenheit"
    # TO DO: Get not only the temperature, but also weather (cloudy, rainy, etc.) and print expected symbol
    # also print humidity, sunrise, sunset for fun.