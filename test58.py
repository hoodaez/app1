import random

# 1. استخدام حلقة for للطباعة من 1 إلى 5
print("1. Loop with 'for' from 1 to 5:")
for i in range(1, 6):  # range(1, 6) يعني الأعداد من 1 إلى 5
    print(i)  # نقوم بطباعة قيمة i في كل مرة من الحلقة

print("\n")

# 2. استخدام حلقة while للطباعة من 1 إلى 5
print("2. Loop with 'while' from 1 to 5:")
i = 1
while i <= 5:  # الشرط: إذا كانت قيمة i أقل من أو تساوي 5
    print(i)  # نقوم بطباعة i في كل مرة من الحلقة
    i += 1  # بعد كل تكرار، نقوم بزيادة قيمة i بمقدار 1

print("\n")

# 3. استخدام حلقة for مع قائمة
print("3. Loop with 'for' over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # نقوم بطباعة العنصر الحالي

print("\n")

# 4. استخدام حلقة while مع شرط التوقف
print("4. Loop with 'while' based on a condition:")
i = 1
while i % 2 != 0:  # البحث عن أول عدد زوجي
    i += 1  # زيادة i حتى يصبح عددًا زوجيًا
print(f"The first even number is {i}")  # طباعة أول عدد زوجي

print("\n")

# 5. استخدام حلقة for مع القيم العشوائية
print("5. Loop with 'for' generating random numbers:")
for _ in range(5):  # نكرر 5 مرات
    print(random.randint(1, 100))  # توليد وطباعة رقم عشوائي بين 1 و 100

print("\n")

# 6. استخدام حلقة for مع شرط التصفية (الأعداد الزوجية)
print("6. Loop with 'for' and filtering even numbers:")
for i in range(1, 11):  # نمر عبر الأعداد من 1 إلى 10
    if i % 2 == 0:  # إذا كان العدد زوجيًا
        print(i)  # نقوم بطباعة العدد الزوجي

print("\n")

# 7. استخدام break للخروج من الحلقة
print("7. Using 'break' to exit the loop:")
for i in range(1, 11):
    if i == 6:  # إذا كانت قيمة i تساوي 6
        print("Found 6, breaking out of the loop.")  # نطبع رسالة
        break  # نخرج من الحلقة عندما نجد العدد 6
    print(i)  # نطبع i

print("\n")

# 8. استخدام continue لتخطي تكرار معين
print("8. Using 'continue' to skip a specific iteration:")
for i in range(1, 11):
    if i == 6:  # إذا كانت قيمة i تساوي 6
        print("Skipping 6.")
        continue  # ننتقل مباشرة للتكرار التالي دون تنفيذ بقية الكود
    print(i)  # نطبع i

