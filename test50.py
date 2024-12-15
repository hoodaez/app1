import requests  # استيراد مكتبة requests لإجراء طلبات HTTP
import pandas as pd  # استيراد مكتبة pandas للتحليل والتعامل مع البيانات
import asyncio  # استيراد مكتبة asyncio لإدارة البرمجة غير المتزامنة
import aiohttp  # استيراد مكتبة aiohttp لإجراء طلبات HTTP غير متزامنة
from concurrent.futures import ThreadPoolExecutor  # استيراد ThreadPoolExecutor لإدارة المهام المتوازية

# تعريف فئة WeatherAPI للحصول على بيانات الطقس من API OpenWeather
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key  # تخزين مفتاح API
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"  # تحديد الرابط الأساسي للـ API

    def fetch_weather(self, city):
        """إحضار بيانات الطقس لمدينة واحدة."""
        params = {  # المعلمات المرسلة مع الطلب
            'q': city,  # اسم المدينة
            'appid': self.api_key,  # مفتاح API
            'units': 'metric'  # الوحدة المستخدمة لدرجة الحرارة (مئوية)
        }
        response = requests.get(self.base_url, params=params)  # إرسال طلب GET للـ API
        if response.status_code == 200:  # إذا كانت استجابة الطلب ناجحة (رمز الحالة 200)
            return response.json()  # إرجاع البيانات بتنسيق JSON
        else:
            return {"error": response.status_code, "message": response.text}  # في حالة وجود خطأ، إرجاع التفاصيل

# تعريف فئة WeatherProcessor لمعالجة البيانات وتحويلها إلى DataFrame
class WeatherProcessor:
    @staticmethod
    def process_weather_data(weather_data):
        """استخراج البيانات المهمة وتحويلها إلى DataFrame."""
        records = []  # قائمة لتخزين البيانات المعالجة
        for data in weather_data:  # المرور عبر جميع بيانات الطقس
            if "error" not in data:  # التأكد من أنه لا يوجد خطأ في البيانات
                records.append({
                    "City": data['name'],  # اسم المدينة
                    "Temperature": data['main']['temp'],  # درجة الحرارة بالمئوية
                    "Humidity": data['main']['humidity'],  # نسبة الرطوبة
                    "Weather": data['weather'][0]['description']  # وصف الطقس (مثلاً، سماء صافية)
                })
            else:
                print(f"Error fetching data: {data['message']}")  # طباعة رسالة الخطأ في حال حدوث مشكلة
        return pd.DataFrame(records)  # إرجاع البيانات في صورة DataFrame

# تعريف دالة غير متزامنة لجلب بيانات الطقس لمدينة واحدة
async def fetch_weather_async(session, url, params):
    """إحضار بيانات الطقس لمدينة واحدة بشكل غير متزامن."""
    async with session.get(url, params=params) as response:  # استخدام طلب GET غير متزامن
        return await response.json()  # إرجاع البيانات بتنسيق JSON

# تعريف دالة غير متزامنة لجلب بيانات الطقس لعدة مدن في نفس الوقت
async def fetch_all_weather(api_key, cities):
    """إحضار بيانات الطقس لعدة مدن بشكل متزامن."""
    tasks = []  # قائمة لتخزين المهام غير المتزامنة
    base_url = "http://api.openweathermap.org/data/2.5/weather"  # الرابط الأساسي للـ API
    async with aiohttp.ClientSession() as session:  # إنشاء جلسة غير متزامنة
        for city in cities:  # المرور عبر جميع المدن
            params = {
                'q': city,  # اسم المدينة
                'appid': api_key,  # مفتاح API
                'units': 'metric'  # وحدة قياس درجة الحرارة
            }
            tasks.append(fetch_weather_async(session, base_url, params))  # إضافة المهمة إلى القائمة
        return await asyncio.gather(*tasks)  # انتظار جميع المهام لتكتمل وإرجاع النتائج

# تعريف الدالة الرئيسية لتنفيذ البرنامج
def main():
    # تهيئة مفتاح API
    api_key = "your_openweather_api_key"  # ضع مفتاح API الخاص بك هنا
    cities = ["Cairo", "London", "New York", "Tokyo", "Dubai", "Paris"]  # قائمة المدن التي سيتم جلب بيانات الطقس لها

    # جلب البيانات بشكل متزامن باستخدام asyncio
    print("Fetching weather data...")  # طباعة رسالة لبدء جلب البيانات
    weather_data = asyncio.run(fetch_all_weather(api_key, cities))  # تشغيل الدالة غير المتزامنة لجلب البيانات لجميع المدن

    # معالجة البيانات وتحليلها
    print("Processing weather data...")  # طباعة رسالة لبدء معالجة البيانات
    processor = WeatherProcessor()  # إنشاء كائن من فئة WeatherProcessor
    df = processor.process_weather_data(weather_data)  # معالجة البيانات وتحويلها إلى DataFrame

    # عرض البيانات المعالجة
    print("\nWeather Data:")  # طباعة عنوان للبيانات
    print(df)  # عرض البيانات في شكل DataFrame

    # حفظ البيانات في ملف CSV
    df.to_csv("weather_data.csv", index=False)  # حفظ البيانات في ملف CSV بدون عمود الفهرس
    print("\nData saved to 'weather_data.csv'!")  # طباعة رسالة تؤكد حفظ البيانات في الملف

# تنفيذ الدالة الرئيسية إذا تم تشغيل السكربت بشكل مباشر
if __name__ == "__main__":
    main()  # استدعاء الدالة الرئيسية لبدء تنفيذ البرنامج
