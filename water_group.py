# Challenges for the water consumption group and their solutions.

import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy

path = 'student.sqlite'
engine = sqlalchemy.create_engine('sqlite:///' + path)

residents_table = pd.read_sql_table('Residents', engine)
# note to self: test out "parse_dates" stuff later!

print(residents_table.head())

print("Average Water Consumption: " + str(np.mean(residents_table['residential_gal_per_day'])))
print("Max Water Consumption: " + str(np.max(residents_table['residential_gal_per_day'])))
print("Min Water Consumption: " + str(np.min(residents_table['residential_gal_per_day'])))

# meh way to do it
print("number of people below 30")
new_table = residents_table[residents_table['age'] < 30]
print(np.size(new_table['resident_id']))
print("number of people 30 or above")
other_new_table = residents_table[residents_table['age'] >= 30]
print(np.size(new_table['resident_id']))

# c00l way to do it
residents_table["Below 30"] = residents_table['age'] < 30
residents_table["Mean WC"] = residents_table["residential_gal_per_day"]
residents_table["Min WC"] = residents_table["residential_gal_per_day"]
residents_table["Max WC"] = residents_table["residential_gal_per_day"]
residents_table["Number of Residents"] = None
residents_table_grouped = residents_table.groupby("Below 30").agg({"Number of Residents": np.size, "Mean WC": np.mean, "Min WC": np.min, "Max WC": np.max})
print(residents_table_grouped)

# CHALLENGE I: read sql table using necessary library imports and print out the first 5 lines. feel free to reference the data36 tutorial for this.

# CHALLENGE II: print out average, minimum, and maximum residential water consumption.

# CHALLENGE III: print out the number of residents below 30 and the number of residents above 30

# CHALLENGE IV: combine challenges II and III -- print out average, min, and max residential water consumption in residents below 30 and the number of residents above 30.
# (this is a flawed examination for many reasons but it's just an exercise intended to give you guys some practice)

# CHALLENGE V: add other statistics factors like median. explore numpy's library for this.

# CHALLENGE VI: Sort the table by water consumption and print out the first 5 lines.

# CHALLENGE VII: Write any of the new tables you have created to a file called practiceday1.csv (You'll have to create this file within your project first)
