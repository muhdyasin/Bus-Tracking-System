Got it 🚀 Here’s a clean and **GitHub-ready `README.md`** version of your instructions:

````markdown
# 🚌 Bus Tracking Flask App

A simple Flask-based bus tracking system using SQLite.  
It allows you to:
- View bus stops
- Add bus locations
- Fetch the latest bus location

---

## ⚡ How to Run Locally

### 1. Install Python
Make sure **Python 3.10+** is installed.

### 2. Open terminal and go to the project folder
```bash
cd path/to/Assignment
````

### 3. Create a virtual environment

```bash
python -m venv venv1
```

### 4. Activate the virtual environment

* On **Windows PowerShell**:

  ```bash
  .\venv1\Scripts\activate
  ```
* On **macOS/Linux**:

  ```bash
  source venv1/bin/activate
  ```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

(or manually install)

```bash
pip install flask flask_sqlalchemy
```

### 6. Run the Flask app

```bash
python app.py
```

### 7. Open in browser

The app will be available at:

```
http://127.0.0.1:5000/
```

---

## 🔗 API Endpoints

### 1. Get all stops

* Open in browser:

  ```
  http://127.0.0.1:5000/stops
  ```

### 2. Add a bus location (POST request)

Run this in **PowerShell** (with `venv1` activated):

```powershell
curl.exe -X POST http://127.0.0.1:5000/location -H "Content-Type: application/json" -d "{\"bus_id\":\"KL01AB1234\",\"lat\":11.0419,\"lon\":75.9279,\"timestamp\":\"2025-09-02T11:00:00\"}"
```

✅ Run this in a **separate terminal** while your Flask app is running.

### 3. Get the latest location of a bus

* Open in browser:

  ```
  http://127.0.0.1:5000/bus/KL01AB1234
  ```

---

## 📂 Project Structure

```
Assignment/
│-- app.py
│-- busStopData.json
│-- requirements.txt
│-- README.md

```

