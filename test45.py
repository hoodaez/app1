# استيراد المكتبات اللازمة
import pandas as pd  # لتحليل البيانات وإدارتها
import numpy as np   # للعمليات الرياضية المتقدمة

# إنشاء بيانات افتراضية تمثل مبيعات يومية
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),  # تواريخ الأيام
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],   # أسماء المنتجات
    'Sales': [100, 200, 150, 120, 180, 170, 130, 190, 160, 110]      # مبيعات كل منتج
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# عرض البيانات الأولية
print("البيانات الأصلية:")
print(df)

# حساب متوسط المبيعات لكل منتج
average_sales = df.groupby('Product')['Sales'].mean()

# عرض متوسط المبيعات
print("\nمتوسط المبيعات لكل منتج:")
print(average_sales)

# إيجاد اليوم الذي حققت فيه المبيعات أعلى قيمة
max_sales_day = df.loc[df['Sales'].idxmax()]

# عرض اليوم ذو المبيعات الأعلى
print("\nاليوم الذي حقق أعلى مبيعات:")
print(max_sales_day)

# حساب إجمالي المبيعات
total_sales = df['Sales'].sum()

# عرض إجمالي المبيعات
print("\nإجمالي المبيعات:")
print(total_sales)
