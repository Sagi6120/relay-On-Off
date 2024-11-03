from flask import Flask, request, jsonify
from flask_cors import CORS
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
relay_pin = 17  # Replace with your GPIO pin number
GPIO.setup(relay_pin, GPIO.OUT)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/relay', methods=['POST'])
def control_relay():
    data = request.json
    action = data.get('action')
    
    if action == "on_akm":
        GPIO.output(relay_pin, GPIO.HIGH)
        return jsonify({"status": "Relay set to AKM"}), 200
    elif action == "on_nio":
        GPIO.output(relay_pin, GPIO.LOW)
        return jsonify({"status": "Relay set to NIO"}), 200
    else:
        return jsonify({"error": "Invalid action"}), 400

@app.route('/status', methods=['GET'])
def relay_status():
    state = GPIO.input(relay_pin)
    return jsonify({"relay_status": "AKM" if state else "NIO"})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
