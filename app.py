from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

KEYWORDS = {
    "meeting": "Meeting scheduled",
    "gym": "Gym session",
    "study": "Study time",
    "work": "Work session",
    "call": "Call planned",
    "appointment": "Appointment set"
}

tasks = {}

def get_month_days(month, year):
    """Return a list of days for a given month and year."""
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month + 1, 1) - timedelta(days=1)
    
    days = []
    for day in range(1, last_day.day + 1):
        date = datetime(year, month, day)
        days.append(date)
    
    return days

@app.route("/", methods=["GET", "POST"])
def index():
    today = datetime.now().date()

    if request.method == "POST":
        user_input = request.form["user_input"]
        task_time = request.form.get("time", "12:00")  
        task_date = today  

        for keyword, description in KEYWORDS.items():
            if keyword in user_input.lower():
                task_description = f"{description} at {task_time}"
                
                tasks.setdefault(task_date, []).append(task_description)
                
                response = f"Task added: {task_description} on {task_date.strftime('%Y-%m-%d')}"
                break
        else:
            response = "No recognized task found."

        return render_template("index.html", response=response, tasks=tasks, month_days=get_month_days(today.month, today.year), today=today)

    return render_template("index.html", tasks=tasks, month_days=get_month_days(today.month, today.year), today=today)


if __name__ == "__main__":
    app.run(debug=True)
