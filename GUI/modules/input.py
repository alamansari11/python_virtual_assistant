import speech_recognition as sr


class Input:
    def __init__(self):
        try:
            # here we are just initilizing the recognizer
            self.recognizer = sr.Recognizer()
            print(f"\nlistening...\n")
        except Exception as error:
            print(f"Listen_initialization_error: {error}")

    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.pause_threshold = 1
                # listen(source, timeout=None, phrase_time_limit=None, snowboy_configuration=None)
                self.audio = self.recognizer.listen(source, 0, 4)
                print("\nRecognizing...\n")
                self.query = self.recognizer.recognize_google(self.audio, language="en-in")
                print(f"You Said: {self.query}")
                return self.query
        except Exception as error:
            print(f"Listen_listen_error: {error}")

# for testing --------------------------

#
# Listen = Listen()
# Listen.listen()
