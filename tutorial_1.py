# "Solutions" to the Data36 tutorial I gave the new recruits.

import pandas as pd
import numpy as np

print("Zoo File")
print(pd.read_csv("zoo.csv"))
print("Tutorial Read File")
print(pd.read_csv("test_folder/pandas_tutorial_read.csv", delimiter=';'))
article_read = pd.read_csv("test_folder/pandas_tutorial_read.csv", delimiter=';', names=['my_datetime', 'event', 'country', 'user_id','source', 'topic'])
print("Head")
print(article_read.head())
print("Tail")
print(article_read.tail())
print("Random Sampling")
print(article_read.sample(10))
print("Column Selection")
print(article_read[['country', 'user_id']])
print("Getting a Series")
print(article_read.user_id)
print(article_read['country'])
print("Filtering based on Data Values")
print(article_read[article_read.source == 'SEO'])
print("Combining Functions")
print(article_read.head()[['country', 'user_id']])
print("Test Yourself")
article_read_filtered = article_read[article_read.country == 'country_2']
article_read_condensed = article_read_filtered[['user_id', 'country', 'topic']]
print(article_read_condensed.head())

# PART 2

zoo = pd.read_csv('zoo.csv', delimiter=',')
print("Counting in One Col")
print(zoo[['animal']].count())
print("Summing in One Col")
print(zoo.water_need.sum())
print("Min")
print(zoo.water_need.min())
print("Max")
print(zoo.water_need.max())
print("Mean")
print(zoo.water_need.mean())
print("Median")
print(zoo.water_need.median())
print("Grouping")
print(zoo.groupby('animal').water_need.mean())
print("Test Yourself: Maximum Source Frequency Count")
print(article_read.groupby('source').count().event.max())
print("Test Yourself: Most Frequent Topic & Source Combo")
article_read_c2 = article_read[article_read.country == 'country_2']
print(article_read_c2.groupby(['topic', 'source']).count().event)#add in .max for the number, but this doesn't allow you to see the name

# PART 3

zoo_eats = pd.DataFrame([['elephant', 'vegetables'], ['tiger', 'meat'], ['kangaroo', 'vegetables'], ['zebra', 'vegetables'], ['giraffe', 'vegetables']], columns=['animal', 'food'])
zoo_full = zoo_eats.merge(zoo, how='right', left_on='animal', right_on='animal').fillna("Unknown")
print(zoo_full)
zoo_full = zoo_full.sort_values(by=['animal', 'water_need'], ascending=False)
zoo_full = zoo_full.reset_index(drop = True)
print(zoo_full)
print("TEst Yourself: Task I")
blog_buy = ""
print(article_read)
print(blog_buy)
#article_stuff = pd.merge(article_read, blog_buy, left_on='user_id', right_on='user_id')
#print(article_stuff)
