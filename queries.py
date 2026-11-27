# Import libraries
import sqlite3
import csv 

# Connect to SQLite
conn = sqlite3.connect('mylog.db')

# Create a cursor object
import os
print(os.path.abspath("mylog.db"))

cursor = conn.cursor()

cursor.execute("SELECT AVG(sleep_hrs) FROM daily_stats")
print("On average you sleep for", cursor.fetchone()[0], "hours per day.")