import time
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

SAVE_NAME = "standup_data"
SAVE_FILE = Path(SAVE_NAME+".json")

def standup(date, streak):
    print(f"### Daily Standup {date} ###")
    print(f"Streak: {streak} ")

    yesterday = question_input("What did you do yesterday?")
    today = question_input("What will you do today?")
    blockers = question_input("What issues are blocking you?")

    save_standup(date, yesterday, today, blockers, streak)

    if streak == 1: # start of new streak
        print("Thanks for attending :)")
        print("See you tomorrow.")
    else:
        print("Thanks for attending :) ")
        print(f"You've attended {streak} standups in a row!")
        print("See you tomorrow.")

def save_standup(date, today, tomorrow, blockers, streak):

    if not SAVE_FILE.exists() or SAVE_FILE.stat().st_size == 0:
        data = []
    else:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

    standup = {
        "date": date.strftime("%d-%m-%Y"),
        "yesterday": today,
        "today": tomorrow,
        "blockers": blockers,
        "streak": streak,
    }

    with open(SAVE_FILE, "w") as f:
        data.append(standup)
        json.dump(data, f)
        
    print(f"saved to {os.path.abspath(SAVE_FILE)}")

def load_previous_standup() -> dict:
   
    if not SAVE_FILE.exists() or SAVE_FILE.stat().st_size == 0:
        return {"date": str_to_date("01-01-2000"), "streak": 0}
    else:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            # Get most recent entry
            if (isinstance(data, list)):
                data = data[-1]
            else:
                data = data
            # convert str date to date object
            data["date"] = str_to_date(data["date"])
            return data

def str_to_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y").date()

def question_input(text):
    print(text)
    print(":",end="")
    return input()

def date_today():
    return datetime.now().date()

def run():

    prev = load_previous_standup()
    prev_date = prev["date"]
    streak = prev["streak"]
    today = date_today()

    if (today == prev_date):
        print("Already stood up today.")
        return

    yesterday = today - timedelta(days=1)

    if (prev_date == yesterday):
        streak += 1
    else:
        streak = 1

    standup(today, streak)


if __name__ == "__main__":
    print("### DAILY STANDUP ###")
    run()