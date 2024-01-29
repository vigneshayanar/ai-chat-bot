#https://www.google.com/search?q=weather+chennai
import webbrowser
import speech_to_text
import text_to_speech

def weather_current():
    text_to_speech.text_to_speech("what is your name of city")
    city=user_data=speech_to_text.speech_text()
    webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
