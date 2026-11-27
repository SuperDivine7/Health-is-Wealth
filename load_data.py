# Import necessary libraries
import sqlite3
import csv 
from pprint import pprint

# Connect to SQLite
conn = sqlite3.connect('mylog.db')

# Create a cursor object
import os
print(os.path.abspath("mylog.db"))

cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_stats 
    ( date TEXT PRIMARY KEY,
      time TEXT,
      calories INTEGER,
      weight REAL,
      sleep_hrs REAL,
      activity_mins INTEGER,
      mood INTEGER,
      screen_time REAL
    )
""")

cursor.execute("PRAGMA table_info(daily_stats)")
print(cursor.fetchall())

# Read CSV and validate data

with open("data/mystats.csv", "r") as file:
    print("File opened successfully")  
    csv_reader = csv.DictReader(file)

    # Loop through each row in the CSV file
    for row in csv_reader:

        #Print each row neatly with newline between dates
        pprint(row, sort_dicts=False)
        print()

        date = row['date']
        time = row['time'] if row["time"] else None
        calories = int(row['calories']) if row["calories"] else None
        weight = float(row['weight']) if row["weight"] else None
        sleep_hrs = float(row['sleep_hrs']) if row["sleep_hrs"] else None
        activity_mins = int(row['activity_mins']) if row["activity_mins"] else None
        mood = int(row['mood']) if row["mood"] else None
        screen_time = float(row['screen_time']) if row["screen_time"] else None

        if weight != None and (weight <= 0 ):
            print(f"Invalid weight value: {weight}. Weight value must be greater than 0.")
            weight = None

        if sleep_hrs != None and (sleep_hrs < 0 or sleep_hrs > 24):
            print(f"Invalid sleep hours value: {sleep_hrs}. Sleep hours value must be between 0 and 24.")
            sleep_hrs = None

        if activity_mins != None and (activity_mins < 0 or activity_mins > 1440):
            print(f"Invalid activity minutes value: {activity_mins}. Activity value must be between 0 and 1440 minutes.")
            activity_mins = None

        if mood != None and (mood < 1 or mood> 5):
            print(f"Invalid mood rating: {mood}. Mood rating must be between 1 and 5.")
            mood = None

        if screen_time != None and (screen_time < 0 or screen_time > 24):
            print(f"Invalid screen time value: {screen_time}. Screen time value must be between 0 and 24.")
            screen_time = None

    # Insert data into the database
        cursor.execute("""
            INSERT OR REPLACE INTO daily_stats (date, time, calories, weight, sleep_hrs, activity_mins, mood, screen_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (date, time, calories, weight, sleep_hrs, activity_mins, mood, screen_time))

conn.commit()

cursor.execute("SELECT COUNT(*) FROM daily_stats")
print("Total records:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM daily_stats") 
records = cursor.fetchall()

for record in records:
    print(record)

conn.close()
