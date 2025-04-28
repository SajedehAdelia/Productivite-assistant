from flask import Flask, render_template, request, jsonify
from datetime import datetime
import dateparser

app = Flask(__name__)

tasks = {}

def parse_task_date(user_input):
    """Parse the user's input to detect a specific date, like 'tomorrow' or '2025-05-05'."""
    parsed_date = dateparser.parse(user_input)
    if parsed_date:
        return parsed_date.date()
    return datetime.now().date()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/process_task', methods=['POST'])
def process_task():
    user_message = request.json.get('message', '')
    print(f"Received message: {user_message}")

    intents = {
        'meeting': ['meeting', 'appointment', 'conference', 'meet'],
        'call': ['call', 'phone', 'teleconference', 'ring'],
        'gym': ['gym', 'workout', 'exercise', 'fitness'],
        'reminder': ['remind', 'reminder', 'remember'],
    }

    detected_intent = None
    for intent, keywords in intents.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', user_message, re.IGNORECASE):
                detected_intent = intent
                break
        if detected_intent:
            break

    # Date and time extraction
    date_time = dateparser.parse(user_message)

    if detected_intent:
        response_message = f"Got it! I'll set a {detected_intent}."
        if date_time:
            response_message += f" Scheduled for {date_time.strftime('%A, %B %d at %I:%M %p')}."
    else:
        response_message = "Sorry, I didn't understand the task. Could you rephrase?"

    return jsonify({'response': response_message})
if __name__ == "__main__":
    app.run(debug=True)