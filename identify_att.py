import pandas as pd

# Read the dataset
df = pd.read_csv("Automobile_data.csv")

print("========== ATTRIBUTE IDENTIFICATION ==========\n")

# Numeric Attributes
numeric_attributes = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Categorical Attributes
categorical_attributes = df.select_dtypes(include=['object']).columns.tolist()

print("Numeric Attributes:")
for i in numeric_attributes:
    print("-", i)

print("\nCategorical Attributes:")
for i in categorical_attributes:
    print("-", i)

# Binary Attributes
binary_attributes = []

for col in categorical_attributes:
    if df[col].nunique() == 2:
        binary_attributes.append(col)

print("\nBinary Attributes:")
for i in binary_attributes:
    print("-", i)

print("\nTotal Numeric Attributes :", len(numeric_attributes))
print("Total Categorical Attributes :", len(categorical_attributes))
print("Total Binary Attributes :", len(binary_attributes))