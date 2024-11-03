from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
relay_pin = 17  # Replace with your GPIO pin number
GPIO.setup(relay_pin, GPIO.OUT)

app = Flask(__name__)

@app.route('/relay', methods=['POST'])
def control_relay():
    data = request.json
    action = data.get('action')
    
    if action == "on":
        GPIO.output(relay_pin, GPIO.HIGH)
        return jsonify({"status": "Relay turned ON"}), 200
    elif action == "off":
        GPIO.output(relay_pin, GPIO.LOW)
        return jsonify({"status": "Relay turned OFF"}), 200
    else:
        return jsonify({"error": "Invalid action"}), 400

@app.route('/status', methods=['GET'])
def relay_status():
    state = GPIO.input(relay_pin)
    return jsonify({"relay_status": "ON" if state else "OFF"})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
