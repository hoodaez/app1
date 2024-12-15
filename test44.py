# استيراد المكتبات
import pandas as pd  # للتعامل مع البيانات
import numpy as np  # للعمليات الحسابية
import matplotlib.pyplot as plt  # لرسم البيانات


# إنشاء بيانات تجريبية لمصنع الملابس
data = {
    'Day': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-07'],
    'Produced Units': [100, 120, 110, 130, 125, 140, 135],  # عدد القطع المنتجة
    'Repairs': [5, 4, 6, 3, 5, 2, 4],  # عدد التصليحات
    'Defects': [2, 3, 1, 4, 2, 3, 1],  # عدد القطع التي بها درجات/عيوب
    'Dirt': [1, 2, 1, 2, 1, 3, 2]  # عدد القطع التي بها اتساخات
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# حساب الشغل السليم (عدد القطع المنتجة - التصليحات - العيوب - الاتساخات)
df['Good Work'] = df['Produced Units'] - (df['Repairs'] + df['Defects'] + df['Dirt'])

# حساب الإنتاج اليومي
df['Daily Production'] = df['Produced Units'] - (df['Repairs'] + df['Defects'] + df['Dirt'])

# حساب الإنتاج الأسبوعي
weekly_production = df['Daily Production'].sum()

# حساب الإنتاج الشهري (افتراض أن لدينا بيانات لكل يوم في الشهر)
monthly_production = df['Daily Production'].sum() * 4  # نفترض أن الشهر يحتوي على 4 أسابيع

# عرض البيانات بعد الحسابات
print("البيانات مع الحسابات:")
print(df)

# عرض الإنتاج اليومي
print("\nالإنتاج اليومي لكل يوم:")
print(df[['Day', 'Daily Production']])

# عرض الإنتاج الأسبوعي
print("\nالإنتاج الأسبوعي:", weekly_production)

# عرض الإنتاج الشهري
print("\nالإنتاج الشهري:", monthly_production)

# رسم بياني للإنتاج اليومي
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Daily Production'], marker='o', linestyle='-', color='b', label='الإنتاج اليومي')
plt.title('الإنتاج اليومي', fontsize=14)
plt.xlabel('اليوم', fontsize=12)
plt.ylabel('الإنتاج اليومي', fontsize=12)
plt.xticks(rotation=45)  # لتدوير التواريخ لتكون واضحة
plt.grid(True)
plt.legend()
plt.show()

# رسم بياني للإنتاج الأسبوعي (مجموع الإنتاج اليومي)
plt.figure(figsize=(10, 6))
plt.bar(['أسبوع واحد'], [weekly_production], color='g')
plt.title('الإنتاج الأسبوعي', fontsize=14)
plt.ylabel('الإنتاج الأسبوعي', fontsize=12)
plt.xticks(rotation=0)  # لتن��يف التواريخ للوضع على الصفح
plt.grid(True)
plt.show()

# رسم بياني للإنتاج الشهري (مجموع الإنتاج اليومي مضاعفًا لعدد الأسابيع في الشهر)
plt.figure(figsize=(10, 6))
plt.bar(['شهر واحد'], [monthly_production], color='r')
plt.title('الإنتاج الشهري', fontsize=14)
plt.xlabel('الشهر', fontsize=12)
plt.show()
