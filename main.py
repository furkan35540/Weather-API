import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}"
    f"&appid={API_KEY}"
    f"&units=metric"
    f"&lang=en"
)

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    data = response.json()

    print("API Response:")
    print(data)

    if response.status_code == 200:
        print("\n===== WEATHER REPORT =====")
        print(f"📍 City: {data['name']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"🤔 Feels Like: {data['main']['feels_like']}°C")
        print(f"☁ Weather: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("\n❌ Error!")
        print(data.get("message", "Unknown error"))

except requests.exceptions.RequestException as e:
    print("Connection Error:", e)