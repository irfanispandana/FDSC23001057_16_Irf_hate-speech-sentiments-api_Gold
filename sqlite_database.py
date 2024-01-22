import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect('database/challenge_level_3.db')
cursor = conn.cursor()

conn.execute('''CREATE TABLE challenge(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tweet VARCHAR(255) NOT NULL,
    hs INTEGER NOT NULL,
    abusive INTEGER NOT NULL,
    hs_individual INTEGER NOT NULL,
    hs_group INTEGER NOT NULL,
    hs_religion INTEGER NOT NULL,
    hs_race INTEGER NOT NULL,
    hs_physical INTEGER NOT NULL,
    hs_gender INTEGER NOT NULL,
    hs_other INTEGER NOT NULL,
    hs_weak INTEGER NOT NULL,
    hs_moderate INTEGER NOT NULL,
    hs_strong INTEGER NOT NULL)
    ''')
conn.commit()
conn.close()

# Open the CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Insert each row into the table
    for row in reader:
        cursor.execute('''INSERT INTO challenge (tweet, hs, abusive, hs_individual, hs_group, hs_religion, hs_race, hs_physical, hs_gender, hs_other, hs_weak, hs_moderate, hs_strong)
                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', (row['Tweet'], row['HS'], row['Abusive'], row['HS_Individual'], row['HS_Group'], row['HS_Religion'], row['HS_Race'], row['HS_Physical'], row['HS_Gender'], row['HS_Other'], row['HS_Weak'], row['HS_Moderate'], row['HS_Strong']))

# Save the connection
conn.commit()
conn.close()

cursor.execute('SELECT * FROM challenge')
data = cursor.fetchall()
print(data)

cursor.execute('SELECT * FROM challenge_cleaned')
data = cursor.fetchall()
print(data)

cursor.execute('SELECT * FROM upload_and_download_csv_file')
data = cursor.fetchall()
print(data)

cursor.execute('SELECT * FROM challenge_cleaned_flask_swagger')
data = cursor.fetchall()
print(data)

## SHOW TABLE ##
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
data = cursor.fetchall()
print(data)

conn.close()