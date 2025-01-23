# Local Explorer Application

## Description
Local Explorer is a Flask-based web application that integrates weather data fetching, location services, and activity suggestions. The application provides the following key features:

1. User authentication with a login interface.
2. Real-time weather data retrieval using the OpenWeatherMap API.
3. A chatbot interface for interaction.
4. Integration with a map using Leaflet.js.
5. Activity recommendations based on user preferences and weather conditions.

## Features

### Login Interface
- Users can log in with their credentials (username and password).
- After a successful login, users are redirected to the main interface.

### Weather Information
- Utilizes the OpenWeatherMap API to fetch and display real-time weather data based on the user's location.
- Displays temperature, weather description, wind speed, humidity, and pressure.

### Map Integration
- Displays a map centered at a default location.
- Uses Leaflet.js to show OpenStreetMap tiles and markers.

### Chatbot
- Provides a simple chatbot interface for user interaction.
- User messages are displayed along with a response area.

### Activity Selection
- Allows users to choose activities based on weather conditions.
- Activities include hiking, reading indoors, swimming, and going to the cinema.
- Selected activities are displayed in a summary.

## Technologies Used

### Frontend
- HTML5
- CSS3 (with Bootstrap for styling)
- Leaflet.js for map integration
- Font Awesome for icons

### Backend
- Flask (Python)
- OpenWeatherMap API for weather data

## Installation

### Prerequisites
- Python 3.x
- Flask
- A valid OpenWeatherMap API key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/local-explorer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd local-explorer
   ```
3. Install required Python packages:
   ```bash
   pip install flask requests
   ```
4. Set your OpenWeatherMap API key in the Python script (`app.py`):
   ```python
   API_KEY = "your_api_key_here"
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
6. Open your browser and go to `http://127.0.0.1:5001/` to access the application.

## File Structure
```
local-explorer/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── app.py
└── README.md
```

## API Integration
- **Endpoint:** `http://api.openweathermap.org/data/2.5/weather`
- **Method:** GET
- **Parameters:**
  - `lat`: Latitude of the user's location.
  - `lon`: Longitude of the user's location.
  - `appid`: OpenWeatherMap API key.
  - `units`: Metric system for temperature (e.g., Celsius).

## How to Use

1. **Login:** Enter your username and password to access the application.
2. **Fetch Weather:** Click "Get Weather" to retrieve weather data for your current location.
3. **Map:** View your location and surrounding areas on the map.
4. **Chatbot:** Use the chatbot interface for interaction.
5. **Activities:** Select activities based on the weather and submit your preferences.

## Screenshots

<img width="958" alt="Image" src="https://github.com/user-attachments/assets/4820c5fd-96eb-4014-843c-b0bb60fef569" />
<img width="959" alt="Image" src="https://github.com/user-attachments/assets/82a5515a-bdc7-44f3-918c-2b92b87a8da6" />
<img width="680" alt="Image" src="https://github.com/user-attachments/assets/24e6d1c9-75ab-4f58-bbc7-5490d10c0f14" />

<img width="958" alt="Image" src="https://github.com/user-attachments/assets/86460ea5-4709-4150-9b09-7d62bbc05c8d" />
<img width="958" alt="Image" src="https://github.com/user-attachments/assets/38d94442-3d91-4cce-9c94-d430e3129e34" />
<img width="680" alt="Image" src="https://github.com/user-attachments/assets/24e6d1c9-75ab-4f58-bbc7-5490d10c0f14" />
<img width="701" alt="Image" src="https://github.com/user-attachments/assets/2eac3204-8941-4eda-b8f1-7a8434e5b085" />
<img width="680" alt="Image" src="https://github.com/user-attachments/assets/24e6d1c9-75ab-4f58-bbc7-5490d10c0f14" />
<img width="959" alt="Image" src="https://github.com/user-attachments/assets/1f774293-ca29-4eed-8b6e-882c9b1f250f" />



  

## Known Issues
- Limited chatbot functionality (future updates may include AI integration).
- No database for user management (passwords are not stored).

## Future Enhancements
- Add a database for user authentication.
- Enhance chatbot functionality with AI/ML integration.
- Provide weather-based activity suggestions automatically.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any issues or feature requests, feel free to contact the project maintainer at `hasnahatti70@gmail.com`.


