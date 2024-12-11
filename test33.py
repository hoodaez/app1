import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل البيانات
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
data = pd.read_csv(url)

print(data.head())

# عد الأنواع في العمود species
species_count = data['species'].value_counts()
print("\nCounter of species:\n", species_count)

# إعداد الشكل
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# رسم الرسم الصندوقي
sns.boxplot(x='species', y='sepal_length', data=data, palette="Set2")

plt.title("التوزيع حسب النوع")
plt.xlabel("النوع")
plt.ylabel("طول الكأس (sepal length)")

# عرض الرسم
plt.show()

# إنشاء تقرير Excel
report_file = 'iris_report.xlsx'
data.describe().to_excel(report_file)

print("The report is saved as", report_file)
