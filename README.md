# Daily Standup
Scheduled CLI prompt for a daily standup including: What you did yesterday, What you plan to do today and what blockers you face.

Stores standups in a log. 

Keeps track of 'streak', number of days in a row you've attended the standup.

## Installation
download daily_standup.py

### Create Scheduled Task
#### On Windows
Edit run_standup.bat with the path to project directory and path to python.exe

Open Task Scheduler

create basic task

Set trigger to 09:00:00 every day

Start a program

Set Program/Script : run_standup.bat

Finish

## Usage
```python daily_standup.py```
to read the standups:
```python read_standups.py```
