from datetime import date
import sqlite3
import csv  

with open("data/mystats.csv", "r") as file:
    print("File opened successfully")  
    csv_reader = csv.DictReader(file)
    for row in csv_reader:

        print(row)

        calories = int(row['calories']) if row["calories"] else None
        weight = float(row['weight']) if row["weight"] else None
        sleep_hrs = float(row['sleep_hrs']) if row["sleep_hrs"] else None
        activity_mins = int(row['activity_mins']) if row["activity_mins"] else None
        mood = int(row['mood']) if row["mood"] else None
        screen_time = float(row['screen_time']) if row["screen_time"] else None

        if weight != None and (weight <= 0 ):
            print(f"Invalid weight value: {weight}. Weight value must be greater than 0.")

        if sleep_hrs != None and (sleep_hrs < 0 or sleep_hrs > 24):
            print(f"Invalid sleep hours value: {sleep_hrs}. Sleep hours value must be between 0 and 24.")

        if activity_mins != None and (activity_mins < 0 or activity_mins > 1440):
            print(f"Invalid activity minutes value: {activity_mins}. Activity value must be between 0 and 1440 minutes.")

        if mood != None and (mood < 1 or mood> 5):
            print(f"Invalid mood rating: {mood}. Mood rating must be between 1 and 5.")

        if screen_time != None and (screen_time < 0 or screen_time > 24):
            print(f"Invalid screen time value: {screen_time}. Screen time value must be between 0 and 24.")



        



                        

        print(type(date))

conn = sqlite3.connect('mylog.db')

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
      mood INTEGER
      screen_time REAL
    )
""")

conn.close()
