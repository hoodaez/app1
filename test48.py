# استيراد المكتبات اللازمة
import pandas as pd  # لتحليل البيانات
import numpy as np   # العمليات الرياضية
from sklearn.model_selection import train_test_split  # تقسيم البيانات
from sklearn.linear_model import LogisticRegression  # النموذج
from sklearn.metrics import accuracy_score, classification_report  # تقييم الأداء

# إنشاء بيانات افتراضية للعمليات
data = {
    'Transaction_Amount': [100, 1500, 200, 50, 3000, 10, 700, 4000, 20, 1000],
    'Transaction_Type': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],  # 0 للشرعية و1 للاحتيال
    'Account_Age': [5, 1, 3, 10, 0.5, 12, 4, 0.2, 15, 0.8],  # عمر الحساب بالسنوات
    'Is_Fraud': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1]  # الهدف (1 = احتيال، 0 = شرعي)
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# عرض البيانات
print("البيانات الأصلية:")
print(df)

# تقسيم البيانات إلى ميزات (X) وأهداف (y)
X = df[['Transaction_Amount', 'Transaction_Type', 'Account_Age']]
y = df['Is_Fraud']

# تقسيم البيانات إلى بيانات تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# إنشاء نموذج الانحدار اللوجستي
model = LogisticRegression()

# تدريب النموذج
model.fit(X_train, y_train)

# توقع النتائج للبيانات الاختبارية
y_pred = model.predict(X_test)

# تقييم النموذج
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# عرض النتائج
print("\nدقة النموذج:")
print(f"{accuracy * 100:.2f}%")
print("\nتقرير الأداء:")
print(report)

# اختبار نموذج على عملية جديدة
new_transaction = np.array([[500, 0, 2]])  # كمية: 500، نوع العملية: شرعية، عمر الحساب: سنتين
prediction = model.predict(new_transaction)

print("\nتوقع النموذج للعملية الجديدة:")
if prediction[0] == 1:
    print("احتيالية")
else:
    print("شرعية")
