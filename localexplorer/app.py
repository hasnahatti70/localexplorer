from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Remplacez par votre clé API OpenWeatherMap
API_KEY = "a64270e39c4f757d19d4a09e789581a5"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    # Appeler l'API OpenWeatherMap
    weather_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_info = {
            "location": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"],
            "wind_speed": weather_data["wind"]["speed"],
            "humidity": weather_data["main"]["humidity"],
            "pressure": weather_data["main"]["pressure"],
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
