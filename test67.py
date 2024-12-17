# 1. نافذة ثابتة الحجم (Fixed-size Sliding Window)
# الهدف: حساب مجموع الأرقام في نافذة ثابتة الحجم (على سبيل المثال، نافذة من 3 عناصر)
def fixed_size_window(arr, window_size):
    n = len(arr)
    if n < window_size:
        return []

    # حساب مجموع النافذة الأولى
    window_sum = sum(arr[:window_size])
    result = [window_sum]

    # التحرك عبر المصفوفة لتحديث مجموع النافذة
    for i in range(window_size, n):
        # إزاحة النافذة: أضف العنصر الجديد وأزل العنصر القديم
        window_sum += arr[i] - arr[i - window_size]
        result.append(window_sum)

    return result

# اختبار نافذة ثابتة الحجم
arr = [1, 2, 3, 4, 5, 6, 7]
window_size = 3
print("1. Fixed-size Sliding Window Result (Window Size = 3):")
print(fixed_size_window(arr, window_size))  # النتيجة: [6, 9, 12, 15, 18]

print("\n")

# 2. نافذة ثابتة الحجم لحساب الحد الأقصى (Maximum in Fixed-size Sliding Window)
# الهدف: إيجاد الحد الأقصى في كل نافذة ثابتة الحجم
from collections import deque

def max_in_fixed_window(arr, window_size):
    n = len(arr)
    if n < window_size:
        return []

    dq = deque()  # المكدس لاحتواء الأرقام المحتملة
    result = []

    # المرور عبر العناصر في المصفوفة
    for i in range(n):
        # إزالة العناصر التي خرجت من النطاق
        if dq and dq[0] < i - window_size + 1:
            dq.popleft()

        # إزالة العناصر الأصغر من العنصر الحالي من المكدس
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        # إضافة الحد الأقصى عندما يتم استيفاء النافذة
        if i >= window_size - 1:
            result.append(arr[dq[0]])

    return result

# اختبار نافذة ثابتة الحجم لحساب الحد الأقصى
print("2. Maximum in Fixed-size Sliding Window Result (Window Size = 3):")
print(max_in_fixed_window(arr, window_size))  # النتيجة: [3, 4, 5, 6, 7]

print("\n")

# 3. نافذة قابلة للتمدد (Variable-size Sliding Window)
# الهدف: إيجاد أكبر مجموع لنافذة متغيرة الحجم بحيث لا يتجاوز المجموع الحد المعطى
def variable_size_window(arr, limit):
    n = len(arr)
    window_sum = 0
    left = 0
    max_sum = 0

    # التحرك عبر المصفوفة
    for right in range(n):
        window_sum += arr[right]

        # إذا تجاوز المجموع الحد، نقوم بتقليص النافذة من اليسار
        while window_sum > limit:
            window_sum -= arr[left]
            left += 1

        # تحديث أكبر مجموع
        max_sum = max(max_sum, window_sum)

    return max_sum

# اختبار نافذة قابلة للتمدد
limit = 10
print("3. Variable-size Sliding Window Result (Max Sum <= 10):")
print(variable_size_window(arr, limit))  # النتيجة: 10 (نافية [1, 2, 3, 4])

