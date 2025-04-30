from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "fc9fc5934247b98cecf1470c54a521f2"  # Replace with your actual API key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        return weather_result(city)
    return render_template("index.html")

@app.route("/weather/<city>")
def weather_result(city):
    base_url = "http://api.openweathermap.org/data/2.5/"
    units = "metric"

    # Current weather
    current_url = f"{base_url}weather?q={city}&appid={API_KEY}&units={units}"
    current_res = requests.get(current_url).json()

    # If the city is not found or any error occurs
    if current_res.get("cod") != 200:
        error_message = current_res.get("message", "City not found")
        return render_template("index.html", error=error_message)  # Pass the error message to index.html

    # Prepare weather data
    weather = {
        "city": current_res["name"],
        "country": current_res["sys"]["country"],
        "temp": f'{current_res["main"]["temp"]} °C',
        "feels": f'{current_res["main"]["feels_like"]} °C',
        "hum": f'{current_res["main"]["humidity"]} %',
        "press": f'{current_res["main"]["pressure"]} hPa',
        "wind": f'{current_res["wind"]["speed"]} m/s',
        "desc": current_res["weather"][0]["description"],
        "icon": current_res["weather"][0]["icon"],
        "sunrise": datetime.fromtimestamp(current_res["sys"]["sunrise"]).strftime("%H:%M"),
        "sunset": datetime.fromtimestamp(current_res["sys"]["sunset"]).strftime("%H:%M")
    }

    # 5-day / 3-hour forecast
    forecast_url = f"{base_url}forecast?q={city}&appid={API_KEY}&units={units}"
    forecast_res = requests.get(forecast_url).json()
    hourly = forecast_res["list"][:8]  # next 24 hours (3-hour intervals)

    # Temp trend (for chart)
    labels = [h["dt_txt"].split()[1][:5] for h in hourly]
    temps = [h["main"]["temp"] for h in hourly]

    # 5-day data (1 per day at 12:00)
    daily_data = []
    added_dates = set()
    for entry in forecast_res["list"]:
        date, time = entry["dt_txt"].split()
        if time == "12:00:00" and date not in added_dates:
            daily_data.append({
                "date": date,
                "icon": entry["weather"][0]["icon"],
                "max": round(entry["main"]["temp_max"]),
                "min": round(entry["main"]["temp_min"])
            })
            added_dates.add(date)

    return render_template("result.html",
                           weather=weather,
                           hourly=hourly,
                           daily_data=daily_data,
                           labels=labels,
                           temps=temps)

if __name__ == "__main__":
    app.run(debug=True)
