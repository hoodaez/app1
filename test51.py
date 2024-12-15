# استيراد المكتبات اللازمة
import pandas as pd  # مكتبة pandas لتحليل البيانات وإدارتها في شكل جداول DataFrame
from sklearn.model_selection import train_test_split  # لتقسيم البيانات إلى تدريب واختبار
from sklearn.ensemble import RandomForestClassifier  # خوارزمية الغابات العشوائية لإنشاء نموذج التعلم الآلي
from sklearn.metrics import accuracy_score, classification_report  # لتقييم دقة النموذج وإنتاج تقرير التصنيف
from sklearn.preprocessing import StandardScaler  # لتوحيد البيانات وجعلها أكثر دقة في النماذج
import matplotlib.pyplot as plt  # مكتبة لرسم الرسوم البيانية
import seaborn as sns  # مكتبة لرسم الرسوم البيانية المتقدمة والتصورات

# تحميل البيانات
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"  # رابط تحميل بيانات مجموعة إيريس
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']  # أسماء الأعمدة
data = pd.read_csv(url, header=None, names=column_names)  # قراءة البيانات من الرابط وتحديد الأعمدة

# عرض أول 5 صفوف من البيانات
print(data.head())  # عرض أول 5 صفوف من البيانات للتأكد من التحميل بشكل صحيح

# استكشاف البيانات
print("\nMissing values:")  # طباعة جملة لمعرفة ما إذا كانت هناك قيم مفقودة
print(data.isnull().sum())  # حساب عدد القيم المفقودة في كل عمود

# تحويل الأعمدة النصية إلى قيم رقمية (Encoding)
data['class'] = data['class'].astype('category').cat.codes  # تحويل العمود النصي 'class' إلى قيم رقمية

# فصل الميزات عن الهدف
X = data.drop('class', axis=1)  # حذف العمود 'class' للحصول على الميزات X (الخصائص)
y = data['class']  # تحديد العمود 'class' كهدف y (الذي نريد التنبؤ به)

# تقسيم البيانات إلى تدريب واختبار (80% للتدريب، 20% للاختبار)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # تقسيم البيانات إلى تدريب واختبار

# مقياس البيانات (توحيد القيم لجعل النماذج أكثر دقة)
scaler = StandardScaler()  # إنشاء كائن لتوحيد البيانات
X_train = scaler.fit_transform(X_train)  # توحيد بيانات التدريب
X_test = scaler.transform(X_test)  # توحيد بيانات الاختبار باستخدام نفس معايير التدريب

# بناء نموذج Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)  # إنشاء نموذج Random Forest مع 100 شجرة قرار
model.fit(X_train, y_train)  # تدريب النموذج باستخدام بيانات التدريب

# التنبؤ بالنتائج
y_pred = model.predict(X_test)  # استخدام النموذج للتنبؤ بالقيم في بيانات الاختبار

# تقييم النموذج
print("\nAccuracy Score:")  # طباعة جملة لتوضيح النتيجة
print(accuracy_score(y_test, y_pred))  # حساب دقة النموذج (نسبة التنبؤات الصحيحة)

# تقرير التصنيف
print("\nClassification Report:")  # طباعة جملة لتوضيح تقرير التصنيف
print(classification_report(y_test, y_pred))  # عرض تقرير التصنيف الذي يشمل الدقة، الاسترجاع، F1-score لكل فئة

# رسم مصفوفة الارتباك (Confusion Matrix)
from sklearn.metrics import confusion_matrix  # استيراد دالة حساب مصفوفة الارتباك
cm = confusion_matrix(y_test, y_pred)  # حساب مصفوفة الارتباك بناءً على النتائج الحقيقية والمُتنبأة

# رسم مصفوفة الارتباك
plt.figure(figsize=(6, 6))  # تحديد حجم الشكل الذي سيتم رسمه
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Setosa', 'Versicolor', 'Virginica'], yticklabels=['Setosa', 'Versicolor', 'Virginica'])  # رسم المصفوفة مع التسمية التوضيحية لكل خلية
plt.title("Confusion Matrix")  # إضافة عنوان للرسم البياني
plt.xlabel("Predicted")  # تسمية المحور الأفقي (التنبؤات)
plt.ylabel("Actual")  # تسمية المحور الرأسي (القيم الحقيقية)
plt.show()  # عرض الرسم البياني
