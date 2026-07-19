import pandas as pd
from scipy.spatial.distance import pdist, squareform

# Read dataset
df = pd.read_csv("Automobile_data.csv")

print("========== NOMINAL DISSIMILARITY ==========\n")

# Nominal Attributes
nominal = df[['fuel-type', 'aspiration']]

# Convert categories into numbers
nominal = nominal.astype('category').apply(lambda x: x.cat.codes)

# Dissimilarity Matrix
nominal_distance = squareform(pdist(nominal, metric='hamming'))

print(nominal_distance)

print("\n========== NUMERIC DISSIMILARITY ==========\n")

# Numeric Attributes
numeric = df[['engine-size', 'horsepower']]

# Replace '?' with NaN
numeric = numeric.replace('?', pd.NA)

# Convert to numeric
numeric = numeric.apply(pd.to_numeric)

# Remove missing values
numeric = numeric.dropna()

# Euclidean Distance
numeric_distance = squareform(pdist(numeric, metric='euclidean'))

print(numeric_distance)