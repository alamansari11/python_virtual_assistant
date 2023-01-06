import requests
import wikipedia
import pyautogui
import random
import pywhatkit
import datetime
import geocoder
import openai
import webbrowser
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup
from newsapi import NewsApiClient


class Task:

    def __init__(self):
        self.shopping_list_data = []
        pass

    def open_ai(self, prompt):
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(response.choices[0]['text'])
        return response.choices[0]['text']

    def time(self):
        try:
            time = datetime.datetime.now().strftime("%H:%M")
            return time
        except Exception as error:
            pass
            # print(f"task_time_error:{error}")

    def date(self):
        try:
            date = datetime.date.today()
            # print("Today date is: ", date)
            # Speak().say(date)
            return date
        except Exception as error:
            pass
            # print(f"task_date_error:{error}")

    def location(self):
        try:
            g = geocoder.ip('me')
            state = g.state
            city = g.city
            current_location = f"You are current location is {state} state and {city} city"
            print(current_location)
            return current_location
            # importing modules
            # from geopy.geocoders import Nominatim
            # # calling the nominatim tool
            # geoLoc = Nominatim(user_agent="GetLoc")
            # latitude,longitude,altitude = loc.position
            # locname = geoLoc.reverse(f"{latitude}, {longitude}")
            # # printing the address/location name
            # return locname.address
        except Exception as error:
            pass
            # print(f"task_location_error:{error}")

    def google(self, query):
        try:
            query = query.lower()
            query_filter = str(query).replace("google ", "").replace("google search ", "").replace("search", "")
            pywhatkit.search(query_filter)
            # Speak().say("here is your search result")
        except Exception as error:
            pass
            # print(f"task_google_search_error:{error}")

    def screenshot(self):
        try:
            import os
            import random
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Desktop')
            # now = str(datetime.datetime.now())
            screenshot_name = str(random.random())
            screenshot_name = screenshot_name.replace('0.', '')
            pyautogui.screenshot(desktop + "\\" + screenshot_name + ".png")
        except Exception as error:
            pass
            # print(f"task_screenshot_error:{error}")
    #
    def week_day(self):
        try:
            day = datetime.datetime.today().weekday() + 1
            week_days = {1: 'Monday', 2: 'Tuesday',
                         3: 'Wednesday', 4: 'Thursday',
                         5: 'Friday', 6: 'Saturday',
                         7: 'Sunday'}
            return week_days[day]
        except Exception as error:
            pass
            # print(f"Task_week_days_error:{error}")

    def weather_report(self):
        try:
            g = geocoder.ip('me')
            city = g.city
            # creating url and requests instance
            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content
            # getting raw data
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            # formatting data
            data = str.split('\n')
            time = data[0]
            sky = data[1]
            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text
            # getting other required data
            pos = strd.find('Wind')
            other_data = strd[pos:]
            # printing all data
            # print("Temperature is", temp)
            # print("Time: ", time)
            # print("Sky Description: ", sky)
            # print(other_data)
            return temp + " " + sky

        except Exception as error:
            pass
            # print(f"task_weather_report_error:{error}")

    def shopping_list(self, command):
        try:
            new_item = command.replace('add ', '').replace('list', '').replace('remove ', '').replace('delete ', '') \
                .replace('to ', '').replace('my ', '').replace('shopping ', '').replace('from ', '')
            print(new_item)
            if 'add' in command:
                self.shopping_list_data.append(new_item)
            elif 'remove' in command or 'delete' in command:
                self.shopping_list_data.remove(new_item)
            return ','.join(self.shopping_list_data)
        except Exception as error:
            pass
            # print(f"task_shopping_list_error:{error}")

    def youtube(self, query):
        try:
            # query = query.lower()
            query_filter = str(query).replace("play ", "").replace("youtube search ", "").replace("on ", "").replace(
                "youtube ", "")
            # # pywhatkit.search(query_filter)
            # webbrowser.open("www.youtube.com")
            # # Speak().say("here is your search result")
            results = YoutubeSearch(query_filter, max_results=2).to_dict()
            print(results)
            # webbrowser.open(results[0]['thumbnails'][0])
            webbrowser.open("www.youtube.com/watch?v=" + results[0]['id'])
        except Exception as error:
            pass
            # print(f"task_youtube_search_error:{error}")

    def news(self, query):
        try:
            newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
            query_filter = str(query).replace("news ", "").replace("latest ", "").replace("about ","")
            topic = query_filter
            data = newsapi.get_top_headlines(
                q=topic, language="en", page_size=2)
            newsData = data["articles"]
            final_news = []
            for y in newsData:
                final_news.append(y["description"])
            final = ("\n".join(final_news))
            return final
        except Exception as error:
            pass
            # print(f"task_news_error:{error}")

# obj = Task()
# obj.news('science')
# #
