import pandas as pd  # استيراد مكتبة pandas لتحليل البيانات

# إنشاء بيانات تجريبية داخل قاموس (Dictionary)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],  # أسماء الأشخاص
    'Age': [24, 27, 22, 32],  # أعمارهم
    'Salary': [50000, 60000, 45000, 80000]  # رواتبهم
}

# تحويل البيانات إلى DataFrame (هيكل جدولي يشبه Excel)
df = pd.DataFrame(data)

# عرض البيانات الأصلية
print("البيانات الأصلية:\n", df)

# تنظيف البيانات - إزالة الصفوف التي تحتوي على قيم فارغة (إذا كانت موجودة)
df_cleaned = df.dropna()

# إضافة عمود جديد يحسب الضرائب بنسبة 20% من الراتب
df_cleaned['Tax'] = df_cleaned['Salary'] * 0.2

# تصفية الأشخاص الذين يتقاضون رواتب أكبر من 50,000
high_salary = df_cleaned[df_cleaned['Salary'] > 50000]

# عرض البيانات بعد التصفية
print("\nالأشخاص برواتب عالية:\n", high_salary)
