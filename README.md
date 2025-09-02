How to Run the Bus Tracking Flask App Locally

1. Install Python
   Make sure Python 3.10+ is installed on your system.

2. Open terminal and go to the project folder
   
3. Create a virtual environment
   python -m venv venv1

4. Activate the virtual environment
   - On Windows PowerShell:
     .\venv1\Scripts\activate

   - On macOS/Linux:
     source venv1/bin/activate

5. Install dependencies
   pip install flask flask_sqlalchemy

6. Run the Flask app
   python app.py

7. Open in browser
   The app will be available at:
   http://127.0.0.1:5000/


API Testing

1. Get all stops
   Open in browser or use curl:
   http://127.0.0.1:5000/stops

2. Add a bus location (POST request)
   Run this in PowerShell:
   curl.exe -X POST http://127.0.0.1:5000/location -H "Content-Type: application/json" -d "{\"bus_id\":\"KL01AB1234\",\"lat\":11.0419,\"lon\":75.9279,\"timestamp\":\"2025-09-02T11:00:00\"}"
   Should run the above command in a separate terminal using the same virtual environment.

3. Get the latest location of a bus
   http://127.0.0.1:5000/bus/KL01AB1234
