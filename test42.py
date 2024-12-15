# استيراد المكتبات
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# إنشاء بيانات تجريبية
data = {
    'Age': [25, 34, 22, 45, 33, 27],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Previous Purchase': ['T-Shirt', 'Dress', 'Jeans', 'Blouse', 'Jacket', 'Skirt'],
    'Recommended Product': ['Hoodie', 'Skirt', 'Jacket', 'Cardigan', 'Sweater', 'Blouse']
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# ترميز الأعمدة النصية إلى أرقام
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])
df['Previous Purchase'] = encoder.fit_transform(df['Previous Purchase'])
df['Recommended Product'] = encoder.fit_transform(df['Recommended Product'])

# عرض البيانات بعد الترميز
print("\nالبيانات بعد الترميز:")
print(df)

# فصل البيانات إلى ميزات (Features) ونتائج (Labels)
X = df[['Age', 'Gender', 'Previous Purchase']]  # الميزات
y = df['Recommended Product']  # النتيجة المستهدفة

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء نموذج KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)  # تدريب النموذج

# اختبار النموذج
y_pred = model.predict(X_test)

# تقييم النموذج
accuracy = accuracy_score(y_test, y_pred)
print("\nدقة النموذج:", accuracy)

# استخدام النموذج لتقديم توصية جديدة
new_data = [[30, 1, 2]]  # العمر: 30، الجنس: أنثى، المنتج السابق: Jeans
recommendation = model.predict(new_data)
print("\nالتوصية للبيانات الجديدة:", encoder.inverse_transform(recommendation))

