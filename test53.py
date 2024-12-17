# استيراد المكتبات اللازمة
import numpy as np  # مكتبة لمعالجة البيانات بشكل مصفوفات
import matplotlib.pyplot as plt  # مكتبة لرسم البيانات
from sklearn.model_selection import train_test_split  # لتقسيم البيانات
from sklearn.linear_model import LinearRegression  # نموذج الانحدار الخطي
from sklearn.metrics import mean_squared_error  # لتقييم النموذج

# إنشاء بيانات وهمية: المساحات (X) والأسعار (y)
# X هي مساحة المنزل بالأمتار المربعة
# y هي السعر المتوقع للمنازل
X = np.array([50, 60, 80, 100, 120, 150, 180]).reshape(-1, 1)  # إعادة تشكيل البيانات
y = np.array([100000, 120000, 160000, 200000, 240000, 300000, 360000])

# تقسيم البيانات إلى بيانات تدريب (70%) واختبار (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# إنشاء النموذج
model = LinearRegression()

# تدريب النموذج باستخدام بيانات التدريب
model.fit(X_train, y_train)

# استخدام النموذج لتوقع أسعار المنازل في بيانات الاختبار
y_pred = model.predict(X_test)

# حساب خطأ النموذج (MSE - متوسط مربع الخطأ)
mse = mean_squared_error(y_test, y_pred)

# عرض النتائج
print("المعامل (Coefficient):", model.coef_[0])  # قيمة الميل
print("التقاطع (Intercept):", model.intercept_)  # قيمة التقاطع مع المحور Y
print("متوسط مربع الخطأ (MSE):", mse)

# رسم البيانات
plt.scatter(X, y, color='blue', label='البيانات الأصلية')  # البيانات الأصلية
plt.plot(X, model.predict(X), color='red', label='خط الانحدار')  # خط النموذج
plt.xlabel('المساحة (m²)')
plt.ylabel('السعر ($)')
plt.legend()
plt.show()
