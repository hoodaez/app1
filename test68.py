# 1. ترتيب الفقاعة (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # تبديل العناصر
    return arr

# 2. ترتيب الإدراج (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # العنصر الذي سيتم إدراجه
        j = i - 1
        while j >= 0 and arr[j] > key:  # تحريك العناصر الأكبر من key إلى اليمين
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # إدراج العنصر في الموضع الصحيح
    return arr

# 3. ترتيب الاختيار (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:  # البحث عن العنصر الأصغر
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # تبديل العنصر الأصغر مع العنصر الحالي
    return arr

# 4. ترتيب الدمج (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # تقسيم المصفوفة إلى نصفين
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # ترتيب النصف الأيسر
        merge_sort(right_half)  # ترتيب النصف الأيمن

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):  # دمج النصفين
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):  # إضافة العناصر المتبقية من النصف الأيسر
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):  # إضافة العناصر المتبقية من النصف الأيمن
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# 5. ترتيب السريع (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # اختيار العنصر المحوري
    left = [x for x in arr if x < pivot]  # العناصر الأصغر من العنصر المحوري
    middle = [x for x in arr if x == pivot]  # العناصر التي تساوي العنصر المحوري
    right = [x for x in arr if x > pivot]  # العناصر الأكبر من العنصر المحوري
    return quick_sort(left) + middle + quick_sort(right)  # دمج الأجزاء المترتبة

# 6. ترتيب التوزيع (Radix Sort)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # افترض أن الأرقام في المصفوفة بين 0 و 9

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1  # زيادة العدد في المؤشر المناسب

    for i in range(1, 10):
        count[i] += count[i - 1]  # تحديث المصفوفة count بحيث تحتوي على الفهارس الصحيحة

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]  # وضع العنصر في الموضع الصحيح
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]  # نسخ العناصر المرتبة إلى المصفوفة الأصلية

def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# اختبار كل خوارزمية:
arr = [64, 34, 25, 12, 22, 11, 90]

# ترتيب الفقاعة:
print("1. Bubble Sort Result:")
print(bubble_sort(arr.copy()))  # استخدام نسخة من المصفوفة لتجنب التعديل عليها

# ترتيب الإدراج:
print("2. Insertion Sort Result:")
print(insertion_sort(arr.copy()))

# ترتيب الاختيار:
print("3. Selection Sort Result:")
print(selection_sort(arr.copy()))

# ترتيب الدمج:
print("4. Merge Sort Result:")
print(merge_sort(arr.copy()))

# ترتيب السريع:
print("5. Quick Sort Result:")
print(quick_sort(arr.copy()))

# ترتيب التوزيع:
print("6. Radix Sort Result:")
print(radix_sort(arr.copy()))
