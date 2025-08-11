# 📌 Task 5 - Data Analysis on CSV Files
# Objective: Analyze sales data using Pandas

# 1️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV with encoding fix & clean column names
file_path = r"D:\ELEVATE LABS\TASK 5\sales_data_sample.csv"
df = pd.read_csv(file_path, encoding="latin1")
df.columns = df.columns.str.strip()  # Remove extra spaces

print("✅ Columns in CSV:", list(df.columns))

# 2️⃣ Auto-detect required columns
product_col = None
sales_col = None
month_col = None

for col in df.columns:
    if "product" in col.lower():
        product_col = col
    if "sale" in col.lower():
        sales_col = col
    if "month" in col.lower():
        month_col = col

if not product_col or not sales_col:
    raise ValueError("❌ Could not find Product/Sales columns in CSV.")

print(f"📦 Product column: {product_col}")
print(f"💰 Sales column: {sales_col}")
if month_col:
    print(f"📆 Month column: {month_col}")
else:
    print("⚠ No Month column found, skipping month-based analysis.")

# 3️⃣ Explore the Data
print("📄 Data Info:")
print(df.info())

print("\n📊 Summary Statistics:")
print(df.describe())

print("\n❓ Missing Values:")
print(df.isnull().sum())

# 4️⃣ Group and Summarize Data
sales_by_product = df.groupby(product_col)[sales_col].sum()
print("\n💰 Total Sales by Product:")
print(sales_by_product)

if month_col:
    sales_by_month = df.groupby(month_col)[sales_col].sum()
    print("\n📆 Total Sales by Month:")
    print(sales_by_month)

# 5️⃣ Visualization
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (8, 5)

# Bar chart - Sales by Product
sales_by_product.plot(kind='bar', color='skyblue', title='Total Sales by Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Line chart - Sales by Month (if month column exists)
if month_col:
    sales_by_month.plot(kind='line', marker='o', color='green', title='Sales Trend Over Months')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.show()

# 6️⃣ Insights
print("🔍 Insights:")
print(f"📌 Top Selling Product: {sales_by_product.idxmax()} with {sales_by_product.max()} sales")
if month_col:
    print(f"📌 Highest Sales Month: {sales_by_month.idxmax()} with {sales_by_month.max()} sales")
