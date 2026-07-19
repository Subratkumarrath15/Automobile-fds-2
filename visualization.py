import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Read Dataset
df = pd.read_csv("Automobile_data.csv")

# Create graphs folder if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# Replace '?' with NaN
df = df.replace('?', pd.NA)

# Convert required columns to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
df["engine-size"] = pd.to_numeric(df["engine-size"], errors="coerce")

# -------------------------------
# 1. Fuel Type Bar Chart
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="fuel-type", data=df)
plt.title("Fuel Type Distribution")
plt.savefig("graphs/fuel_type_bar.png")
plt.close()

# -------------------------------
# 2. Body Style Pie Chart
# -------------------------------
plt.figure(figsize=(6,6))
df["body-style"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Body Style Distribution")
plt.savefig("graphs/body_style_pie.png")
plt.close()

# -------------------------------
# 3. Price Histogram
# -------------------------------
plt.figure(figsize=(7,5))
plt.hist(df["price"].dropna(), bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("graphs/price_histogram.png")
plt.close()

# -------------------------------
# 4. Engine Size vs Price
# -------------------------------
plt.figure(figsize=(7,5))
plt.scatter(df["engine-size"], df["price"])
plt.title("Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.savefig("graphs/engine_vs_price.png")
plt.close()

# -------------------------------
# 5. Average Price by Cylinders
# -------------------------------
avg_price = df.groupby("num-of-cylinders")["price"].mean()

plt.figure(figsize=(8,5))
avg_price.plot(marker='o')
plt.title("Average Price by Number of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Average Price")
plt.grid(True)
plt.savefig("graphs/avg_price_cylinders.png")
plt.close()

# -------------------------------
# 6. Horsepower Box Plot
# -------------------------------
plt.figure(figsize=(6,5))
sns.boxplot(y=df["horsepower"])
plt.title("Horsepower Distribution")
plt.savefig("graphs/horsepower_boxplot.png")
plt.close()

print("========================================")
print("All graphs generated successfully!")
print("Saved inside 'graphs' folder.")
print("========================================")