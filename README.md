# E-Commerce-Pricing-Analysis
Analyze product pricing vs competitors (Excel + Python + Pandas + Matplotlib).

# 📊 E-Commerce Pricing Analysis

## 📌 Project Overview

This project analyzes product pricing in an e-commerce environment by comparing **our prices** with **competitor prices** to identify pricing gaps and optimize strategy.

The goal is to detect:

* Overpriced products (risk of losing customers)
* Underpriced products (opportunity to increase profit)
* Competitive products (correct pricing)

---

## 🛠 Tools & Technologies

* **Excel** (Data Cleaning, Pivot Tables, Dashboard)
* **Python** (Pandas, Matplotlib)
  
---

## 📂 Dataset

* Uncleaned real-world styled dataset with:

  * Missing values
  * Inconsistent pricing
  * Incomplete competitor data

---

## 🧹 Data Cleaning Process

### In Excel:

* Handled missing values using logical formulas
* Created **Competitor Average Price**
* Replaced missing `Our_Price` using market average
* Removed useless rows (no competitor data)
* Used **Paste Special → Values** for final clean dataset

### In Python (Pandas):

* Filled missing competitor prices
* Calculated competitor average
* Removed rows with no market price
* Converted data types (dates, numeric)
* Final cleaned dataset exported

---

## 📊 Analysis Performed

### 1. Price Comparison

* Calculated **Price Difference**:

  ```
  Price_Difference = Our_Price - Competitor_Avg_Price
  ```

### 2. Pricing Classification

* Overpriced → Price higher than market
* Underpriced → Price lower than market
* Competitive → Close to market price

---

## 📈 Dashboard (Excel)

Created interactive dashboard using:

* Pivot Tables
* Pie Chart (Pricing Status Distribution)
* Bar Chart (Top Overpriced Products)
* Category-wise Pricing Analysis
* KPI Cards:

  * Total Products
  * Overpriced Count
  * Underpriced Count
  * Competitive Count

---

## 📊 Python Visualization

Generated charts using Matplotlib:

* Pricing Status Distribution
* Our Price vs Market Average
* Top 10 Overpriced Products

---

## 🎯 Key Insights

* Identified products priced significantly above competitors
* Found underpriced products with profit improvement potential
* Detected balanced (competitive) pricing segments

---

## 💡 Business Recommendations

* 🔻 Reduce prices for overpriced products
* 🔺 Increase prices slightly for underpriced products
* ⚖ Maintain pricing for competitive products

---

## 🚀 Outcome

* Built a complete pricing analysis system
* Performed real-world data cleaning
* Created dashboards and insights
* Developed pricing optimization strategy

---
