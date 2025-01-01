import geopandas as gpd
import matplotlib.pyplot as plt

# تحميل خريطة العالم
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# قائمة الدول العربية
arab_countries = [
    "Algeria", "Bahrain", "Comoros", "Djibouti", "Egypt", "Iraq", "Jordan", "Kuwait", "Lebanon", "Libya", 
    "Mauritania", "Morocco", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Somalia", "Sudan", "Syria", 
    "Tunisia", "United Arab Emirates", "Yemen"
]

# تصفية البيانات لتشمل الدول العربية فقط
arab_map = world[world['name'].isin(arab_countries)]

# إعداد الرسم
fig, ax = plt.subplots(figsize=(10, 10))
arab_map.plot(ax=ax, color='lightblue', edgecolor='black')

# إضافة العناوين
ax.set_title('خريطة الوطن العربي', fontsize=16)
ax.set_xlabel('خط الطول')
ax.set_ylabel('خط العرض')

# عرض الخريطة
plt.show()
