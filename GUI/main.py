from kivy.config import Config
from kivy.core.window import Window
import random
import json
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from modules.input import Input
from modules.output import Output
from modules.task import Task
from kivy.core.clipboard import Clipboard

Config.set('graphics', 'resizable', 0)
# Config.set('graphics', 'borderless', 1)
Window.size = (400, 600)

with open('resources/intention.json', 'r') as intent_file:
    intent_dict = json.load(intent_file)['intention']


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 13


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 13


def change_screen(name):
    screen_manager.current = name


def bot_name():
    if screen_manager.get_screen('main').bot_name.text != "":
        screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
        screen_manager.current = "chats"


def change_chat_box_size(sentence):
    size = .77
    if len(sentence) < 6:
        size = .22
    elif len(sentence) < 11:
        size = .32
    elif len(sentence) < 16:
        size = .45
    elif len(sentence) < 21:
        size = .58
    elif len(sentence) < 26:
        size = .71
    return size


def check_for_code(command):
    list_code = ['program', 'code', 'python', 'c++', 'java', 'syntax']
    for i in command.split():
        print(i)
        if i in list_code:
            return True
    return False


class VirtualAssistant(MDApp):

    def build(self):
        self.open_ai_flag = False
        self.response_data = None
        self.query = None
        self.task = Task()

        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("chats.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager

    def basic_functions(self, response):
        if "time" == response:
            return self.task.time()
        elif "date" == response:
            return self.task.date()
        elif "screenshot" == response:
            Task().screenshot()
            return "Screenshot taken"
        elif "location" == response:
            return self.task.location()

    def speak_after_some_time(self, dt):
        print(check_for_code(self.query))
        if self.open_ai_flag and check_for_code(self.query):
            Output().speak('The answer is copied to your clipboard')
            Clipboard.copy(self.response_data)
        else:
            Output().speak(self.response_data)
        if "quit" in self.query.split():
            exit()

    def response(self, *args):
        for i in intent_dict:
            pattern = i['pattern']
            response = i['response']
            if self.query in pattern:
                if len(response) == 1:
                    return self.basic_functions(response[0])
                elif len(response) > 1:
                    return random.choice(response)
        print(self.query.split())
        if "google" in self.query.split():
            self.task.google(self.query)
            return "here is your search result"
        try:
            self.open_ai_flag = True
            return self.task.open_ai(self.query)
        except Exception as error:
            print(error)
            return "Sorry I can't help you with that at the moment"

    def send(self):
        global open_ai_flag
        self.query = Input().listen()
        # print(self.query)
        if self.query is not None:
            self.query = self.query.lower()
            size = change_chat_box_size(self.query)
            try:
                screen_manager.get_screen('chats').chat_list.add_widget(
                    Command(text=self.query, size_hint_x=size, halign="left"))
                self.response_data = str(self.response())
                size = change_chat_box_size(self.response_data)
                screen_manager.get_screen('chats').chat_list.add_widget(
                    Response(text=self.response_data, size_hint_x=size, halign="left"))
                Clock.schedule_once(self.speak_after_some_time, 3)
            except Exception as error:
                print(f"send_function_chat_add_error:{error}")


if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf", fn_bold="Poppins-SemiBold.ttf")

    try:
        VirtualAssistant().run()
    except Exception as e:
        print(f'Application error: {e}')
