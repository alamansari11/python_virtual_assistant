import wikipedia
import pyautogui
import random
import pywhatkit
import datetime
import geocoder
import openai
import webbrowser

class Task:

    def __init__(self):
        pass

    def open_ai(self,prompt):
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
        print(response.choices[0]['text'])
        return response.choices[0]['text']

    def time(self):
        try:
            time = datetime.datetime.now().strftime("%H:%M")
            return time
        except Exception as error:
            print(f"non_input_execution_time_error:{error}")

    def date(self):
        try:
            date = datetime.date.today()
            print("Today date is: ", date)
            # Speak().say(date)
            return date
        except Exception as error:
            print(f"non_input_execution_date_error:{error}")

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
            print(f"non_input_execution_location_error:{error}")

    # def wikipedia(self, query):
    #     try:
    #         query_filter = str(query).replace("who is ", "").replace("about ", "").replace("wikipedia ", "").replace(
    #             "what is ", "")
    #         result = wikipedia.summary(query_filter, sentences=2)
    #         print(result)
    #         # Speak().say(result)
    #         return result
    #     except Exception as error:
    #         print(f"input_execution_wikipedia_error:{error}")

    def google(self, query):
        try:
            query = query.lower()
            query_filter = str(query).replace("google ", "").replace("google search ", "").replace("search", "")
            pywhatkit.search(query_filter)
            # Speak().say("here is your search result")
        except Exception as error:
            print(f"input_execution_google_search_error:{error}")

    def screenshot(self):
        try:
            screenshot_name = datetime.datetime.now()
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'Screen-{screenshot_name}.png')
        except Exception as error:
            print(f"input_execution_screenshot_error:{error}")
