# Challenges for the political group and their solutions.

import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy

path = 'student.sqlite'
engine = sqlalchemy.create_engine('sqlite:///' + path)

residents_table = pd.read_sql('Residents', engine)
# note to self: test out "parse_dates" stuff later!

print(residents_table.head())

print("Average Voter Engagement Score: " + str(np.mean(residents_table['voter_engagement_score'])))
print("Max Voter Engagement Score: " + str(np.max(residents_table['voter_engagement_score'])))
print("Min Voter Engagement Score: " + str(np.min(residents_table['voter_engagement_score'])))

# meh way to do it
print("number of people below 30")
new_table = residents_table[residents_table['age'] < 30]
print(np.size(new_table['resident_id']))
print("number of people 30 or above")
other_new_table = residents_table[residents_table['age'] >= 30]
print(np.size(new_table['resident_id']))

# c00l way to do it
residents_table["Below 30"] = residents_table['age'] < 30
residents_table["Mean VES"] = residents_table["voter_engagement_score"]
residents_table["Min VES"] = residents_table["voter_engagement_score"]
residents_table["Max VES"] = residents_table["voter_engagement_score"]
residents_table["Number of Residents"] = None
residents_table_grouped = residents_table.groupby("Below 30").agg({"Number of Residents": np.size, "Mean VES": np.mean, "Min VES": np.min, "Max VES": np.max})
print(residents_table_grouped)

# CHALLENGE I: read sql table using necessary library imports and print out the first 5 lines. feel free to reference the sample.py file and data36 tutorial for this.

# CHALLENGE II: print out average, minimum, and maximum voter engagement score.

# CHALLENGE III: print out the number of residents below 30 and the number of residents above 30

# CHALLENGE IV: combine challenges II and III -- print out average, min, and max in voters below 30 and above 30.

# CHALLENGE V: add other statistics factors like median. explore numpy's library documentation and the data36 tutorials for this.

# CHALLENGE VI: Sort the table by voter engagement score and print the first 5 rows.

# CHALLENGE VII: Write any of the new tables you have created to a file called practiceday1.csv (You'll have to create this file within your project first)
