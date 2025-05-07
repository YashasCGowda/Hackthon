AI-Powered Carbon Footprint Tracker
A web application to calculate, track, and visualize your carbon footprint, with AI-generated suggestions to reduce emissions. The project uses Flask for the backend, MongoDB for data storage, and a React-based frontend for the user interface.
Table of Contents

Overview
Features
Project Structure
Prerequisites
Setup Instructions
Usage
Testing
Troubleshooting
Contributing
License

Overview
The AI-Powered Carbon Footprint Tracker allows users to input their weekly transportation, energy usage, and diet habits to calculate their annual carbon footprint. The application provides a breakdown of emissions, comparisons to U.S. and global averages, visualizations (pie and line charts), and personalized suggestions to reduce emissions. The backend is built with Flask and MongoDB, while the frontend uses React, Tailwind CSS, and Chart.js for a responsive and interactive UI.
Features

Carbon Footprint Calculation: Estimates annual CO2 emissions based on transportation (miles driven, fuel type), energy usage (kWh), and diet (meat-heavy, moderate, vegetarian, vegan).
Data Storage: Stores user entries in MongoDB for historical tracking.
Visualizations: Displays emission breakdowns (pie chart) and trends over time (line chart) using Chart.js.
AI Suggestions: Provides personalized suggestions to reduce emissions, powered by a similarity-based algorithm using suggestions_data.json.
Responsive UI: Built with React and Tailwind CSS, with light/dark mode and color theme options (blue, green, purple).
Backend API: Flask RESTful API endpoints for calculating (/api/calculate) and retrieving historical data (/api/history).

Project Structure
CARBON_FOOTPRINT_PROJECT/
├── backend/
│   ├── climatiq_api.py         # Placeholder for Climatiq API integration
│   ├── fetch_db.py             # API endpoint to fetch historical data from MongoDB
│   ├── insert_db.py            # API endpoint to insert new entries into MongoDB
│   ├── main.py                 # Flask application entry point
│   ├── model.py                # Basic suggestion prediction logic
│   ├── test_db.py              # Test script for MongoDB insertion
│   ├── test_utils.py           # Unit tests for utility functions
│   └── utils.py                # Utility functions (e.g., input validation, config loading)
├── frontend/
│   ├── index.html              # Main React-based frontend UI
│   └── suggestions_data.json   # Training data for AI suggestion generation
├── .env                        # Environment variables (e.g., MONGO_URI)
├── .gitignore                  # Git ignore file to exclude sensitive data
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

Prerequisites

Python 3.8+: Required for the Flask backend.
MongoDB: Local installation or a cloud service (e.g., MongoDB Atlas).
Git: To clone and manage the repository.
Web Browser: To access the frontend (served by Flask).
Internet Connection: For CDN dependencies (React, Tailwind CSS, Chart.js).

Setup Instructions

Clone the Repository:
git clone https://github.com/yourusername/CARBON_FOOTPRINT_PROJECT.git
cd CARBON_FOOTPRINT_PROJECT


Install MongoDB:

Local Installation: Download and install MongoDB from mongodb.com. Start the MongoDB server:mongod


Cloud Service: Use MongoDB Atlas (create a free cluster at mongodb.com/cloud/atlas).


Set Up a Virtual Environment:
python -m venv venv


Activate the virtual environment:
Windows:venv\Scripts\activate


macOS/Linux:source venv/bin/activate






Install Dependencies:
pip install -r requirements.txt


Configure Environment Variables:

Create a .env file in the root directory:touch .env


Add your MongoDB URI:MONGO_URI=mongodb://localhost:27017/


For MongoDB Atlas, use your cluster URI:MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority






Run the Flask Server:
cd backend
python main.py


The server will run at http://localhost:5000.



Usage

Access the Application:

Open your browser and go to http://localhost:5000.
You’ll see the "AI-Powered Carbon Footprint Tracker" interface.


Input Your Data:

Fill out the form with:
Week number
College (e.g., College A, B, or C)
Weekly transportation (miles driven)
Fuel type (gasoline, diesel, electric)
Monthly electricity usage (kWh)
Diet type (meat-heavy, moderate, vegetarian, vegan)


Click Calculate Footprint.


View Results:

See your estimated annual carbon footprint (in metric tons of CO2).
View a breakdown of emissions (transport, energy, diet).
Compare your footprint to U.S. and global averages.
Read AI-generated suggestions to reduce emissions.


Visualize Data:

Click View Visualization to see:
A pie chart of your emission breakdown for a selected week.
A line chart showing your footprint trend over weeks.


Select a week from the dropdown to update the charts.


Customize the UI:

Toggle between light and dark modes using the Dark Mode button.
Change the color theme (blue, green, purple, none) using the dropdown.



Testing

Unit Tests:
Test utility functions:cd backend
python test_utils.py




Database Tests:
Test MongoDB insertion (ensure MongoDB is running):python test_db.py


This inserts test data into the entries collection.



Troubleshooting

"Failed to load necessary data":

Cause: Flask server or MongoDB isn’t running.
Fix:
Ensure the Flask server is running: cd backend && python main.py.
Ensure MongoDB is running: mongod.
Check the browser console (F12 → Console) for specific errors.
Test endpoints with Postman:
GET http://localhost:5000/api/history (should return [] or a list).
GET http://localhost:5000/suggestions_data.json (should return JSON).






MongoDB Connection Errors:

Cause: Incorrect MONGO_URI or MongoDB not running.
Fix:
Verify MONGO_URI in .env.
Ensure MongoDB is running (mongod for local, or check MongoDB Atlas cluster status).
Test connection: mongo "mongodb://localhost:27017/".




CORS Issues:

Cause: Frontend and backend on different ports.
Fix: The Flask server (main.py) includes CORS support. Ensure you access the app via http://localhost:5000.


Port Conflicts:

Cause: Port 5000 is in use.
Fix: Edit main.py to use a different port (e.g., 5001) and update index.html fetch URLs:app.run(debug=False, host='0.0.0.0', port=5001)





Contributing

Fork the repository.
Create a new branch:git checkout -b feature/your-feature-name


Make your changes and commit:git add .
git commit -m "Add your feature"


Push to your fork:git push origin feature/your-feature-name


Open a pull request on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for details.
