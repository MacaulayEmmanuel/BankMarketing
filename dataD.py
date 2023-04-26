import sqlite3
from pathlib import Path

# Import pandas to work with data sets
import pandas as pd

# Create empty database
Path("bank.db").touch()

# Connect to database
conn = sqlite3.connect("bank.db")
c = conn.cursor()

# Create a table

'''
c.execute(
    """CREATE TABLE bank (
    age int, job text,
    marital text, education text,
    default_e text, balance int,
    housing text, loan text,
    contact text, day int,
    month text, duration int,
    campaign int, pdays text,
    previous int, poutcome text,
    deposit text
   );"""
)
'''
# Open csv file
bank = pd.read_csv("bank.csv")

# Add table to database
bank.to_sql("bank", conn, if_exists="append", index=False)


# Return one row from the 'bank' table
fetc = c.execute("""SELECT * FROM bank""").fetchone()
print(fetc)

