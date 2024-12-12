import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# إنشاء البيانات
data = {
    "Group": ["Real Estate", "Real Estate", "Gold", "Gold", "Cash", "Cash"],
    "Age": [35, 45, 40, 50, 25, 30],
    "Investment Amount (EGP)": [500000, 700000, 100000, 150000, 200000, 250000],
    "Expected Return (%)": [10, 12, 8, 7, 6, 5],
    "Risk Level": ["Low", "Low", "Medium", "Medium", "High", "High"]
}

df = pd.DataFrame(data)

# طباعة البيانات
print("Investment Data:")
print(df)

# تحليل بسيط
print("\nAverage Investment per Group:")
print(df.groupby("Group")["Investment Amount (EGP)"].mean())

# رسم بياني للإحصائيات
sns.barplot(x="Group", y="Investment Amount (EGP)", data=df, palette="viridis")
plt.title("Average Investment by Group")
plt.show()

# رسم مستوى المخاطر
sns.countplot(x="Group", hue="Risk Level", data=df, palette="coolwarm")
plt.title("Risk Levels by Group")
plt.show()
