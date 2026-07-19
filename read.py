import pandas as pd

# Read the dataset
df = pd.read_csv("Automobile_data.csv")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Display last 5 rows
print("\n========== LAST 5 ROWS ==========")
print(df.tail())

# Display shape
print("\n========== SHAPE OF DATASET ==========")
print(df.shape)

# Display column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Display data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Display missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Display summary statistics
print("\n========== SUMMARY STATISTICS ==========")
print(df.describe(include='all'))

# Display duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())