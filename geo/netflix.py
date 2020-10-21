from time import sleep
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
rows, columns = df.shape
for i in range(0, 100):
    movie = dict(df.iloc[i])
    title, rating = movie['title'], movie['rating']
    print(title, rating)