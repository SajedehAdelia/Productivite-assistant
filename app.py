from flask import Flask, render_template, request, session, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = "verysecretkey"

KEYWORDS = {
    "meeting": "Meeting scheduled",
    "gym": "Gym session",
    "study": "Study time",
    "work": "Work session",
    "call": "Call planned",
    "appointment": "Appointment set"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if 'planning' not in session:
        session['planning'] = []

    response = None

    if request.method == 'POST':
        user_input = request.form['user_input']


        time_match = re.search(r'\b(\d{1,2})(?:h|:)?(\d{0,2})?\s*(am|pm)?\b', user_input, re.IGNORECASE)
        task = user_input

        if time_match:
            hour = time_match.group(1)
            minute = time_match.group(2) if time_match.group(2) else "00"
            ampm = time_match.group(3)

            if ampm and ampm.lower() == 'pm' and int(hour) < 12:
                hour = str(int(hour) + 12)

            formatted_time = f"{hour.zfill(2)}:{minute.zfill(2)}"
            session['planning'].append({'time': formatted_time, 'task': task})
            session.modified = True
            response = f"Task added at {formatted_time}!"
        else:
            response = "Sorry, I couldn't find a time in your message."

    return render_template('index.html', response=response, planning=session['planning'])

def detect_tasks(text):
    results = []
    lower_text = text.lower()
    for keyword, action in KEYWORDS.items():
        if keyword in lower_text:
            results.append(action)
    if not results:
        results.append("No tasks detected. Try again!")
    return results

if __name__ == "__main__":
    app.run(debug=True)
