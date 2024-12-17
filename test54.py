# استيراد المكتبات
import tensorflow as tf  # مكتبة TensorFlow لبناء الشبكات العصبية
from tensorflow.keras.models import Sequential  # لإنشاء الشبكة العصبية كطبقات متسلسلة
from tensorflow.keras.layers import Dense, Flatten  # Dense للطبقات العادية، Flatten لتحويل البيانات
from tensorflow.keras.datasets import mnist  # قاعدة بيانات MNIST لتجربة البيانات الرقمية
from tensorflow.keras.utils import to_categorical  # لتحويل التصنيفات إلى صيغة One-Hot

# تحميل البيانات (سنستخدم MNIST كبيانات تجريبية)
# بيانات MNIST تحتوي على صور رقمية بالأبيض والأسود من 0 إلى 9
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# تطبيع البيانات: نقوم بقسمة القيم (0-255) إلى نطاق (0-1) لتسريع التدريب
X_train = X_train / 255.0
X_test = X_test / 255.0

# تحويل التصنيفات إلى صيغة One-Hot
y_train = to_categorical(y_train, 10)  # تحويل الأرقام 0-9 إلى صيغة التصنيف (10 فئات)
y_test = to_categorical(y_test, 10)

# إنشاء نموذج الشبكة العصبية
model = Sequential([
    Flatten(input_shape=(28, 28)),  # تحويل المصفوفة ثنائية الأبعاد (28x28) إلى مصفوفة مسطحة
    Dense(128, activation='relu'),  # طبقة مخفية بعدد 128 وحدة مع تفعيل ReLU
    Dense(64, activation='relu'),   # طبقة مخفية إضافية بعدد 64 وحدة
    Dense(10, activation='softmax') # طبقة الإخراج بـ 10 وحدات للتصنيفات (0-9)
])

# تجميع النموذج: تحديد وظيفة الخطأ والمحسن ومقاييس الأداء
model.compile(
    optimizer='adam',  # محسن Adam لتحسين الأوزان
    loss='categorical_crossentropy',  # دالة خطأ التصنيفات
    metrics=['accuracy']  # قياس الدقة أثناء التدريب
)

# تدريب النموذج
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# تقييم النموذج على بيانات الاختبار
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"الخسارة على بيانات الاختبار: {test_loss}")
print(f"الدقة على بيانات الاختبار: {test_accuracy}")

# توقع التصنيفات لصورة واحدة من بيانات الاختبار
predictions = model.predict(X_test[:1])
print("التوقع:", predictions.argmax())  # عرض التصنيف المتوقع
