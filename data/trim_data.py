import pandas as pd

df = pd.read_csv("postings.csv")

# Select only the company name, title, and description columns
df = df[["company_name", "title", "description"]]

# Take a random sample of 10000 rows from the dataset
df = df.sample(n = 10000, random_state = 55)

# Save the CSV 
df.to_csv("postings_trimmed.csv", index = False)