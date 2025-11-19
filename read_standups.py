import json

from daily_standup import str_to_date, SAVE_FILE


def load_previous_standups() -> list:
    if not SAVE_FILE.exists() or SAVE_FILE.stat().st_size == 0:
        return []
    else:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return data

if __name__ == "__main__":
    standups = load_previous_standups()
    for entry in standups:
        entry["date"] = str_to_date(entry["date"])
    for entry in standups:
        print(f"Date: {entry['date'].strftime('%d-%m-%Y')}")
        print(f"  Today: {entry['today']}")
        print(f"  Yesterday: {entry['yesterday']}")
        print(f"  Blockers: {entry['blockers']}")
        print(f"  Streak: {entry['streak']}")
        print()
