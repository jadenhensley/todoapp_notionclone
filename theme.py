import json

f = open('config/theme.json')

data = json.load(f)

user_preferences = dict()
user_preferences = data['colors']

f.close()

def getThemeConfig():
    return user_preferences