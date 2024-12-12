import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# توليد بيانات مبيعات عشوائية
np.random.seed(42)
num_sales = 1000

data = {
    "Product Category": np.random.choice(["Electronics", "Clothing", "Furniture"], size=num_sales, p=[0.4, 0.4, 0.2]),
    "Customer Age": np.random.randint(18, 60, size=num_sales),
    "Purchase Amount (EGP)": np.random.randint(50, 5000, size=num_sales),
    "Date": pd.date_range(start="2023-01-01", periods=num_sales, freq="H").strftime('%Y-%m-%d'),
}

df = pd.DataFrame(data)

# إضافة عمود "اليوم" للتحليل
df["Day"] = pd.to_datetime(df["Date"]).dt.day_name()

# طباعة أول خمس صفوف للتأكد
print(df.head())

# تحليل البيانات
print("\nAverage Purchase Amount by Product Category:")
print(df.groupby("Product Category")["Purchase Amount (EGP)"].mean())

print("\nSales Distribution by Day:")
print(df["Day"].value_counts())

# رسم بياني 1: متوسط الإنفاق حسب الفئة
plt.figure(figsize=(10, 6))
sns.barplot(x="Product Category", y="Purchase Amount (EGP)", data=df, palette="viridis")
plt.title("Average Purchase Amount by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Purchase Amount (EGP)")
plt.show()

# رسم بياني 2: توزيع المبيعات حسب الأيام
plt.figure(figsize=(10, 6))
sns.countplot(x="Day", data=df, order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], palette="coolwarm")
plt.title("Sales Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Number of Sales")
plt.show()

# رسم بياني 3: العلاقة بين عمر العميل والمبلغ المصروف
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Customer Age", y="Purchase Amount (EGP)", hue="Product Category", data=df, palette="Set2")
plt.title("Customer Age vs Purchase Amount by Product Category")
plt.xlabel("Customer Age")
plt.ylabel("Purchase Amount (EGP)")
plt.legend(title="Product Category")
plt.show()


