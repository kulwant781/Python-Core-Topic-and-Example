import time
import threading
from plyer import notification
from flask import Flask, render_template, request

app = Flask(__name__)

def drink_water_reminder(interval=3600):  # Default: Remind every 2 seconds
    while True:
        notification.notify(
            title="Drink Water Reminder 💧",
            message="Stay hydrated! Drink a glass of water now.",
            app_name="Water Reminder",
            timeout=10
        )
        time.sleep(interval)  # Wait before showing the next reminder

# Run the reminder function in a separate thread
reminder_thread = threading.Thread(target=drink_water_reminder, args=(3600,), daemon=True)
reminder_thread.start()

@app.route("/")
def home():
    return "Drink Water Reminder is Running!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
