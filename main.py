import speech_recognition as sr
import os
import webbrowser
import requests
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import datetime
import numpy as np
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""

def chat(query):
    global chatStr
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
    chatStr += f"User: {query}\n Jarvis: "
    completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": f"{chatStr}"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)
    try:
        speaker.Speak(completion.choices[0].message.content)
        chatStr += f"{completion.choices[0].message.content}\n"
        return completion.choices[0].message.content
    except:
        print("An exception occurred")


def ai(prompt):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
    text = f"AI response for Prompt: {prompt} \n *************************\n\n"
    completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": f"{prompt}"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)
    try:
        # print(completion.choices[0].message.content)
        text += completion.choices[0].message.content
    except:
        print("An exception occurred")
    if not os.path.exists("AI"):
        os.mkdir("AI")    
    with open(f"AI/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


# Function to fetch news for a specific country
news_api_key = os.getenv("NEWS_API_KEY")
def get_news(country_code="us"):
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_api_key}"
    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data['status'] != "ok":
            speaker.Speak(f"Sorry, I couldn't fetch news for {country_code.upper()}.")
            return
        # Fetch the top headlines
        articles = news_data['articles']
        if not articles:
            speaker.Speak(f"No news articles found for {country_code.upper()}.")
            return
        # Read out the top 5 headlines
        speaker.Speak(f"Here are the top news headlines for {country_code.upper()}:")
        for i, article in enumerate(articles[:5]):  # Get only top 5 headlines
            speaker.Speak(f"Headline {i + 1}: {article['title']}")
    except Exception as e:
        speaker.Speak("There was an issue fetching the news.")
        print(f"Error: {e}")

# Function to take the country name or code from the user's voice command
def get_country_code(query):
    # Map common country names to their ISO country codes
    country_codes = {
        "united states": "us",
        "india": "in",
        "united kingdom": "gb",
        "canada": "ca",
        "australia": "au",
        "germany": "de",
        "france": "fr",
        # Add more countries as needed
    }

    # Try to find a matching country name in the user's query
    for country_name, code in country_codes.items():
        if country_name in query.lower():
            return code
    # If no country found, return default (US)
    return "us"


# Function to get weather information
weather_api_key = os.getenv("WEATHER_API_KEY")
def get_weather(city="Dehradun"):
    url = f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no'   
    try:
        response = requests.get(url)
        weather_data = response.json()

        if 'error' in weather_data:
            speaker.Speak(f"Sorry, I couldn't find weather information for {city}.")
            return

        # Extract weather information
        current = weather_data['current']
        temp = current['temp_c']
        condition = current['condition']['text']
        humidity = current['humidity']
        wind_speed = current['wind_kph']
        
        # Speak the weather information
        speaker.Speak(f"The weather in {city} is currently {condition} with a temperature of {temp} degrees Celsius. "
                      f"The humidity is {humidity}% and the wind speed is {wind_speed} kilometers per hour.")
    except Exception as e:
        speaker.Speak("There was an issue fetching the weather.")
        print(f"Error: {e}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"



if __name__ == '__main__':
    print('PyCharm')
    s = "Hello I am Jarvis AI"
    speaker.Speak(s)
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        musicPath = "C:/Users/HP/Music/"
        songs = [["Dandelions", f"{musicPath}dandelions_11.mp3"], ["Bandana", f"{musicPath}Bandana_12.mp3"],
                 ["Under the influence", f"{musicPath}Under-The-Influence_64"]]
        for song in songs:
            if f"Play {song[0]}".lower() in query.lower():
                speaker.Speak(f"Playing {song[0]} sir...")
                os.startfile(song[1])
                
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Sir time is {hour} hour {min} minutes")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "news" in query.lower():
            country_code = get_country_code(query)
            get_news(country_code)

        elif "weather" in query.lower():
            # Optional: Extract the city from the user's command
            if "in" in query.lower():
                city = query.split("in")[-1].strip()  # Extract the city name
                get_weather(city)
            else:
                get_weather()

        elif "Jarvis Quit".lower() in query.lower():
            speaker.Speak("Goodbye")
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
