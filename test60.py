# 1. التكرار لحساب عامل العدد (Factorial)
# نقوم بحساب عامل العدد باستخدام التكرار
def factorial(n):
    # حالة الإيقاف: إذا كان n == 0 أو n == 1، نعيد 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # استدعاء دالة factorial لنفسها مع (n-1)

print("1. Factorial of 5:")
print(factorial(5))  # عامل العدد 5 هو 120

print("\n")

# 2. التكرار لحساب الأعداد في سلسلة فيبوناتشي
# سلسلة فيبوناتشي هي سلسلة من الأعداد حيث أن كل عدد هو مجموع العددين السابقين له.
def fibonacci(n):
    # حالة الإيقاف: إذا كانت n == 0 أو n == 1
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # استدعاء دالة fibonacci لنفسها مع (n-1) و (n-2)

print("2. Fibonacci sequence at position 6:")
print(fibonacci(6))  # العدد في الموقع السادس هو 8 (0, 1, 1, 2, 3, 5, 8)

print("\n")

# 3. التكرار لطباعة الأرقام من 1 إلى n
# نقوم باستخدام التكرار للطباعة من 1 إلى n
def print_numbers(n):
    # حالة الإيقاف: إذا كانت n == 0
    if n == 0:
        return
    print_numbers(n - 1)  # استدعاء الدالة مع (n-1)
    print(n)  # طباعة العدد الحالي

print("3. Printing numbers from 1 to 5:")
print_numbers(5)  # سيتم طباعة الأرقام من 1 إلى 5

print("\n")

# 4. التكرار لحساب مجموع الأعداد من 1 إلى n
# نقوم بحساب مجموع الأعداد من 1 إلى n باستخدام التكرار
def sum_numbers(n):
    # حالة الإيقاف: إذا كانت n == 0
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)  # استدعاء الدالة مع (n-1)

print("4. Sum of numbers from 1 to 5:")
print(sum_numbers(5))  # مجموع الأعداد من 1 إلى 5 هو 15

print("\n")

# 5. التكرار لعكس سلسلة نصية
# نقوم بعكس سلسلة نصية باستخدام التكرار
def reverse_string(s):
    # حالة الإيقاف: إذا كانت السلسلة فارغة
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]  # استدعاء الدالة مع السلسلة بدون أول حرف

print("5. Reversed string of 'hello':")
print(reverse_string("hello"))  # ستطبع 'olleh'

print("\n")

# 6. التكرار لإيجاد أكبر عدد في قائمة
# نقوم بإيجاد أكبر عدد في قائمة باستخدام التكرار
def find_max(nums):
    # حالة الإيقاف: إذا كانت القائمة تحتوي على عنصر واحد فقط
    if len(nums) == 1:
        return nums[0]
    else:
        # مقارنة العنصر الأول مع أكبر عدد في الجزء المتبقي من القائمة
        max_of_rest = find_max(nums[1:])
        if nums[0] > max_of_rest:
            return nums[0]
        else:
            return max_of_rest

print("6. Maximum number in the list [1, 3, 2, 7, 5]:")
print(find_max([1, 3, 2, 7, 5]))  # أكبر عدد في القائمة هو 7

print("\n")

# 7. التكرار لحساب القيم الزوجية في القائمة
# نقوم بحساب القيم الزوجية في قائمة باستخدام التكرار
def count_even(nums):
    # حالة الإيقاف: إذا كانت القائمة فارغة
    if len(nums) == 0:
        return 0
    else:
        # إذا كان العنصر الأول زوجيًا، نعده
        if nums[0] % 2 == 0:
            return 1 + count_even(nums[1:])
        else:
            return count_even(nums[1:])

print("7. Counting even numbers in the list [1, 2, 3, 4, 5, 6]:")
print(count_even([1, 2, 3, 4, 5, 6]))  # عدد الأعداد الزوجية في القائمة هو 3
