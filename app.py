from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BusStop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stopname = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class BusLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()
    if BusStop.query.count() == 0:  
        with open("busStopData.json", "r") as f:
            stops_data = json.load(f)
        
        for stop in stops_data["tirTOkuttp"][:5]:
            stop_obj = BusStop(
                stopname=stop["stopname"],
                latitude=stop["latitude"],
                longitude=stop["longitude"]
            )
            db.session.add(stop_obj)
        db.session.commit()


@app.route("/")
def home():
    return "Welcome to Evide"


@app.route("/stops", methods=["GET"])
def get_stops():
    stops = BusStop.query.all()
    return jsonify([
        {"stopname": s.stopname, "lat": s.latitude, "lon": s.longitude}
        for s in stops
    ])


@app.route("/location", methods=["POST"])
def update_location():
    data = request.get_json()
    required = {"bus_id", "lat", "lon", "timestamp"}
    if not data or not required.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_loc = BusLocation(
        bus_id=data["bus_id"],
        latitude=data["lat"],
        longitude=data["lon"],
        timestamp=data["timestamp"]
    )
    db.session.add(new_loc)
    db.session.commit()
    return jsonify({"message": "Location stored successfully"}), 201


@app.route("/bus/<bus_id>", methods=["GET"])
def get_bus(bus_id):
    loc = BusLocation.query.filter_by(bus_id=bus_id).order_by(BusLocation.id.desc()).first()
    if not loc:
        return jsonify({"error": "Bus not found"}), 404
    return jsonify({
        "bus_id": loc.bus_id,
        "lat": loc.latitude,
        "lon": loc.longitude,
        "timestamp": loc.timestamp
    })


if __name__ == "__main__":
    app.run(debug=True)
