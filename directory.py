import os
import pandas as pd

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# Check if the movies.csv file exists in the directory
if "movies.csv" in os.listdir():
    print("movies.csv found!")
    # Load the data from the CSV file into a pandas dataframe
    movies_df = pd.read_csv("movies.csv")
    print("Loaded data from movies.csv")
else:
    print("movies.csv not found!")
