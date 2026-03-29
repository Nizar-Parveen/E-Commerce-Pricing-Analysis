import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_pricing_uncleaned.csv")

# Fill competitor prices if one missing
df['Competitor_A_Price'] = df['Competitor_A_Price'].fillna(df['Competitor_B_Price'])
df['Competitor_B_Price'] = df['Competitor_B_Price'].fillna(df['Competitor_A_Price'])

# Create competitor average
df['Competitor_Avg_Price'] = df[['Competitor_A_Price','Competitor_B_Price']].mean(axis=1)

# ❗ Delete rows where both were blank
df = df.dropna(subset=['Competitor_Avg_Price'])

# Fill Our price using market average
df['Our_Price'] = df['Our_Price'].fillna(df['Competitor_Avg_Price'])

# Fill rating
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# Fix date
df['Last_Updated'] = pd.to_datetime(df['Last_Updated'], errors='coerce')

# Price difference
df['Price_Difference'] = df['Our_Price'] - df['Competitor_Avg_Price']

# Pricing logic
def pricing_status(diff):
    if diff > 100:
        return "Overpriced"
    elif diff < -100:
        return "Underpriced"
    else:
        return "Competitive"

df['Pricing_Status'] = df['Price_Difference'].apply(pricing_status)

# Summary
print("\nPricing Summary:\n")
print(df['Pricing_Status'].value_counts())

# Show final data
print("\nFinal Cleaned Dataset:\n")
print(df.head())

# Save cleaned data
df.to_csv("ecommerce_pricing_cleaned.csv", index=False)

# --------------------
# Chart 1: Pricing Status Count
# --------------------
status_counts = df['Pricing_Status'].value_counts()

plt.figure(figsize=(6,4))
status_counts.plot(kind='bar')
plt.title("Pricing Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Products")
plt.show()

# --------------------
# Chart 2: Our Price vs Market Avg
# --------------------
avg_prices = [
    df['Our_Price'].mean(),
    df['Competitor_Avg_Price'].mean()
]

labels = ['Our Price', 'Market Avg']

plt.figure(figsize=(5,4))
plt.bar(labels, avg_prices)
plt.title("Our Price vs Market Average")
plt.show()

# --------------------
# Chart 3: Top Overpriced Products
# --------------------

overpriced = df[df['Pricing_Status']=="Overpriced"] \
              .sort_values(by='Price_Difference', ascending=False) \
              .head(10)


plt.figure(figsize=(6,4))
plt.barh(overpriced['Product_Name'], overpriced['Price_Difference'])
plt.title("Top Overpriced Products")
plt.xlabel("Price Difference")
plt.show()
