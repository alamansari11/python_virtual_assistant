import pyttsx3


class Output:
    def __init__(self):
        ''' 
        engine = text to speech engine
        voices will carry different types of voices available for the operating system
        we are setting the property to first voices
        and we are adjusting the rate of voice means how fast it speak 
        '''
        try:
            self.engine = pyttsx3.init("sapi5")
            self.voices = self.engine.getProperty('voices')
            self.engine.setProperty('voices', self.voices[0].id)
            self.engine.setProperty('rate', 170)
        except Exception as error:
            pass
            # print(f"speak_initialization_error: {error}")

    def speak(self, text):
        try:
            # print('\n')
            # print(f"Speaking: {text}")
            self.engine.say(text=text)
            self.engine.runAndWait()
            # print('\n')
        except Exception as error:
            pass
            # print(f"speak_say_error: {error}")

# for testing ---------------------------------
# Speak = Speak()
# Speak.say("hello how are you ")
