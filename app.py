from flask import Flask, request, jsonify
from flask_cors import CORS
import RPi.GPIO as GPIO

# Set up GPIO for controlling the relay
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
relay_pin = 17  # Pin 17 is used here (adjust if needed)
GPIO.setup(relay_pin, GPIO.OUT)

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for all routes

@app.route('/relay', methods=['POST'])
def control_relay():
    """
    Endpoint to control the relay.
    Expects a JSON body with an "action" key, which can be "on_akm" or "on_nio".
    """
    data = request.json  # Parse JSON data from the request
    action = data.get('action')
    
    # Turn relay ON for "AKM" or OFF for "NIO" based on action
    if action == "on_akm":
        GPIO.output(relay_pin, GPIO.HIGH)  # Set relay to ON (High)
        return jsonify({"status": "Relay set to AKM"}), 200
    elif action == "on_nio":
        GPIO.output(relay_pin, GPIO.LOW)  # Set relay to OFF (Low)
        return jsonify({"status": "Relay set to NIO"}), 200
    else:
        return jsonify({"error": "Invalid action"}), 400  # Return error if action is invalid

@app.route('/status', methods=['GET'])
def relay_status():
    """
    Endpoint to get the current status of the relay.
    Returns "AKM" if relay is ON, "NIO" if relay is OFF.
    """
    state = GPIO.input(relay_pin)  # Get the current state of the relay
    return jsonify({"relay_status": "AKM" if state else "NIO"})

if __name__ == '__main__':
    try:
        # Run the Flask application on a specific IP address (192.168.19.100) and port 5000
        app.run(host='192.168.19.100', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO settings if interrupted
    finally:
        GPIO.cleanup()  # Ensure GPIO cleanup on exit
