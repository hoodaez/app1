# استيراد المكتبات
import pandas as pd  # للتعامل مع البيانات
from sklearn.model_selection import train_test_split  # لتقسيم البيانات
from sklearn.neighbors import KNeighborsClassifier  # نموذج KNN
from sklearn.preprocessing import LabelEncoder  # لتحويل النصوص إلى أرقام

# إنشاء بيانات تجريبية (إذا لم يكن لديك ملف بيانات جاهز)
data = {
    'Book Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F'],
    'Genre': ['Fiction', 'Non-Fiction', 'Science', 'Fiction', 'Science', 'Non-Fiction'],
    'User Rating': [5, 4, 5, 3, 4, 3],
    'Recommendation': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# عرض البيانات الأولية
print("البيانات الأولية:")
print(df)

# ترميز الأعمدة النصية إلى أرقام باستخدام LabelEncoder
encoder = LabelEncoder()
df['Genre'] = encoder.fit_transform(df['Genre'])  # تحويل عمود النوع
df['Recommendation'] = encoder.fit_transform(df['Recommendation'])  # تحويل عمود التوصيات

# عرض البيانات بعد الترميز
print("\nالبيانات بعد الترميز:")
print(df)

# فصل البيانات إلى ميزات (Features) ونتائج (Labels)
X = df[['Genre', 'User Rating']]  # الأعمدة المستخدمة كميزات
y = df['Recommendation']  # العمود المستهدف (التوصيات)

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء نموذج KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)  # تدريب النموذج

# اختبار النموذج على بيانات جديدة
new_data = [[0, 5]]  # النوع: Fiction (0)، التقييم: 5
recommendation = model.predict(new_data)

# عرض التوصية بناءً على البيانات الجديدة
print("\nالتوصية للكتاب الجديد:", "Yes" if recommendation[0] == 1 else "No")
