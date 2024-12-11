import sqlite3

# الاتصال بقاعدة البيانات
con = sqlite3.connect('test32.db')

# إنشاء مؤشر للعمل مع قاعدة البيانات
cursor = con.cursor()

# إضافة بيانات متعددة باستخدام executemany
movies = [
    ('Inception', 'Sci-Fi', 2010),
    ('Titanic', 'Romance', 1997),
    ('The Dark Knight', 'Action', 2008),
    ('Avatar', 'Sci-Fi', 2009),
    ('Gladiator', 'Action', 2000)
]
cursor.executemany("INSERT INTO movie (name, genre, year) VALUES (?, ?, ?)", movies)

# حفظ التغييرات
con.commit()

# إغلاق الاتصال
con.close()
