
# 🚌 Bus Tracking Flask App

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)  
A simple **Flask + SQLite** bus tracking system.  

This app allows you to:
- 📍 View bus stops  
- 🚌 Add bus locations  
- 📡 Fetch the latest location of a bus  

---

## ⚡ Getting Started

### 1️⃣ Install Python
Make sure **Python 3.10+** is installed:  
👉 [Download Python](https://www.python.org/downloads/)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/bus-tracking-app.git
cd bus-tracking-app
````

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv1
```

### 4️⃣ Activate Virtual Environment

* On **Windows PowerShell**:

  ```bash
  .\venv1\Scripts\activate
  ```
* On **macOS/Linux**:

  ```bash
  source venv1/bin/activate
  ```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(or manually)*

```bash
pip install flask flask_sqlalchemy
```

### 6️⃣ Run the App

```bash
python app.py
```

Server starts at:
👉 `http://127.0.0.1:5000/`

---

## 🔗 API Endpoints

### 📍 1. Get all stops

**GET** `/stops`

```url
http://127.0.0.1:5000/stops
```

---

### 🚌 2. Add a bus location

**POST** `/location`

Example (PowerShell):

```powershell
curl.exe -X POST http://127.0.0.1:5000/location -H "Content-Type: application/json" -d "{\"bus_id\":\"KL01AB1234\",\"lat\":11.0419,\"lon\":75.9279,\"timestamp\":\"2025-09-02T11:00:00\"}"
```

---

### 📡 3. Get latest bus location

**GET** `/bus/<bus_id>`
Example:

```url
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

---
