# دالة لحساب مجموع الأرقام الزوجية
def sum_of_even_numbers(numbers):
    total = 0  # متغير لتخزين مجموع الأرقام الزوجية
    
    # المرور عبر كل عنصر في القائمة
    for num in numbers:
        if num % 2 == 0:  # التحقق إذا كان الرقم زوجيًا
            total += num  # إضافة الرقم الزوجي إلى المجموع
    
    return total  # إرجاع المجموع النهائي

# مثال للاستخدام
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# استدعاء دالة حساب مجموع الأرقام الزوجية
result = sum_of_even_numbers(numbers)

# طباعة النتيجة
print("مجموع الأرقام الزوجية في القائمة:", result)



# دالة لإيجاد أكبر رقم في القائمة
def find_largest_number(numbers):
    largest = numbers[0]  # نبدأ بأول رقم في القائمة كأكبر رقم
    
    # المرور عبر جميع الأرقام في القائمة
    for num in numbers:
        if num > largest:  # إذا كان الرقم الحالي أكبر من أكبر رقم موجود
            largest = num  # تحديث أكبر رقم
    
    return largest  # إرجاع أكبر رقم

# مثال للاستخدام
numbers = [12, 45, 67, 23, 89, 34]

# استدعاء الدالة للعثور على أكبر رقم
largest = find_largest_number(numbers)

# طباعة النتيجة
print("أكبر رقم في القائمة هو:", largest)


def find_all_number(numbers,target):
    total = 0
    for i in numbers:
        if i == target:
            total +=1
    return total

result = find_all_number([1,2,3,4,5,6,7,8,9,10] , 5)

print("عدد الأرقام المطلوبة هو:",result)














