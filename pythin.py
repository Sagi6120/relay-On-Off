from flask import Flask, render_template
import RPi.GPIO as GPIO

# GPIO Setup
GPIO.setmode(GPIO.BCM)
relay_pin = 17  # Set your relay pin number
GPIO.setup(relay_pin, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turn_on', methods=['POST'])
def turn_on():
    GPIO.output(relay_pin, GPIO.HIGH)
    return '', 204  # No content

@app.route('/turn_off', methods=['POST'])
def turn_off():
    GPIO.output(relay_pin, GPIO.LOW)
    return '', 204  # No content

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)  # Listen on all interfaces
    except KeyboardInterrupt:
        print("Server interrupted")
    finally:
        GPIO.cleanup()
