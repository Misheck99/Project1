#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:34:40 2024

@author: avntrainee
"""
#import pandas 

import pandas as pd

# Load the data
movie_data = pd.read_csv('movie_dataset.csv')

# Display movie data
print(movie_data)

# Inspect the dataset
movie_data.info()

# Describe the data
print(movie_data.describe())

# Check missing values
missing_values = movie_data.isnull().sum()
print("Missing values:\n", missing_values)

# Drop data with missing values
df = movie_data.dropna(axis=0)

# Check if missing values remain after dropping
print("Missing values after dropping:\n", df.isnull().sum())

# Top 5 highest-rated movies
top_rated = df.sort_values(by='Rating', ascending=False).head(5)
print("Top 5 highest-rated movies:\n", top_rated[['Title', 'Rating', 'Year']])

# Calculate average revenue
if 'Revenue (Millions)' in df.columns:
    average_revenue = df['Revenue (Millions)'].mean()
    print(f"The average revenue of all movies is: {average_revenue} million dollars")
else:
    print("Revenue (Millions) column not found!")

# Filter movies between 2015 and 2017
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate average revenue for filtered movies
if 'Revenue (Millions)' in filtered_movies.columns:
    average_revenue_2015_2017 = filtered_movies['Revenue (Millions)'].mean()
    print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_2017} million dollars")
else:
    print("Revenue (Millions) column not found!")

# Filter movies released in 2016 and count them
movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print(f"\nNumber of movies released in 2016: {num_movies_2016}")

# Filter movies with a rating of at least 8.0 and count them
highly_rated_movies = df[df['Rating'] >= 8.0]
num_rated_movies = len(highly_rated_movies)
print(f"\nNumber of movies with a rating of at least 8.0: {num_rated_movies}")

# Movies directed by Christopher Nolan
movies_Nolan = df[df['Director'] == 'Christopher Nolan']
print("\nChristopher Nolan's movies:\n", movies_Nolan)
print(f"Number of movies directed by Christopher Nolan: {len(movies_Nolan)}")

# Average rating per year
average_rating_per_year = df.groupby("Year")["Rating"].mean()
print("\nAverage rating per year:\n", average_rating_per_year)

# Filter movies released in 2006 and count them
movies_2006 = df[df["Year"] == 2006]
num_movies_2006 = len(movies_2006)
print(f"\nNumber of movies released in 2006: {num_movies_2006}")

# Double-check movies released in 2016
print("\nMovies released in 2016:\n", movies_2016)
































