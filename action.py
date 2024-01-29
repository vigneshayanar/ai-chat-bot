import text_to_speech
import speech_to_text
import datetime
import weather
import webbrowser

def actions():
    text_to_speech.text_to_speech("what is your name sir")
    name=speech_to_text.speech_text()
    text_to_speech.text_to_speech(f"hello {name}")
    text_to_speech.text_to_speech("ask me anything")
    user_data=speech_to_text.speech_text()
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return"My name is virtual assistant"

    elif "hello" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech(f"hey,{name} , how i can help you")
        return f"hey,{name} , how i can help you"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech(f"good morning {name}")
        return f"good morning {name}"

    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        time=(str)(current_time)+"hour:",(str)(current_time.mintue)+" minte"
        text_to_speech.text_to_speech(time)
        return time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in  user_data:
        webbrowser.open("https://www.youtube.com/watch?v=ZdMZ40GSVmc&list=RDMMZdMZ40GSVmc&start_radio=1")
        return "https://www.youtube.com/watch?v=ZdMZ40GSVmc&list=RDMMZdMZ40GSVmc&start_radio=1"

    elif "youtube" in user_data:
        webbrowser.open("http://youtube.com/")
        return "http://youtube.com/"

    elif "weather" in user_data:
        weather.weather_current()
        return weather.weather_current()

    else:
        text_to_speech.text_to_speech(" i am understand what your speaking")
        return " i am understand what your speaking"

actions()