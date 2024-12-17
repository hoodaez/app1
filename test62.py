# 1. حساب العامل (Factorial) باستخدام التكرار
# العامل هو حاصل ضرب جميع الأعداد من 1 إلى n.
def factorial(n):
    if n == 0 or n == 1:  # حالة الإيقاف: إذا كانت القيمة 0 أو 1
        return 1
    else:
        return n * factorial(n - 1)  # استدعاء الدالة نفسها مع (n-1)

print("1. Factorial of 5:")
print(factorial(5))  # الناتج يجب أن يكون 120

print("\n")

# 2. حساب الأعداد في سلسلة فيبوناتشي (Fibonacci) باستخدام التكرار
# الأعداد في سلسلة فيبوناتشي هي: 0, 1, 1, 2, 3, 5, 8, 13, ...
# يتم حساب كل عدد عن طريق جمع العددين السابقين.
def fibonacci(n):
    if n <= 1:  # حالة الإيقاف: إذا كانت n 0 أو 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # استدعاء الدالة نفسها مع (n-1) و (n-2)

print("2. Fibonacci number at position 6:")
print(fibonacci(6))  # الناتج يجب أن يكون 8

print("\n")

# 3. طباعة الأرقام من 1 إلى n باستخدام التكرار
# في هذه الدالة، نطبع الأرقام من 1 إلى n باستخدام التكرار.
def print_numbers(n):
    if n == 0:  # حالة الإيقاف: إذا كانت n 0
        return
    print_numbers(n - 1)  # استدعاء الدالة نفسها مع (n-1)
    print(n)  # طباعة العدد الحالي

print("3. Printing numbers from 1 to 5:")
print_numbers(5)  # سيتم طباعة الأرقام من 1 إلى 5

print("\n")

# 4. حساب مجموع الأعداد من 1 إلى n باستخدام التكرار
# نقوم بحساب مجموع الأعداد من 1 إلى n باستخدام التكرار.
def sum_numbers(n):
    if n == 0:  # حالة الإيقاف: إذا كانت n 0
        return 0
    else:
        return n + sum_numbers(n - 1)  # استدعاء الدالة نفسها مع (n-1)

print("4. Sum of numbers from 1 to 5:")
print(sum_numbers(5))  # الناتج يجب أن يكون 15

print("\n")

# 5. عكس السلسلة النصية باستخدام التكرار
# نقوم بعكس السلسلة النصية باستخدام التكرار.
def reverse_string(s):
    if len(s) == 0:  # حالة الإيقاف: إذا كانت السلسلة فارغة
        return s
    else:
        return reverse_string(s[1:]) + s[0]  # استدعاء الدالة مع السلسلة بدون أول حرف

print("5. Reversed string of 'hello':")
print(reverse_string("hello"))  # الناتج يجب أن يكون "olleh"

print("\n")

# 6. إيجاد أكبر عدد في قائمة باستخدام التكرار
# نقوم بإيجاد أكبر عدد في القائمة باستخدام التكرار.
def find_max(nums):
    if len(nums) == 1:  # حالة الإيقاف: إذا كانت القائمة تحتوي على عنصر واحد فقط
        return nums[0]
    else:
        max_of_rest = find_max(nums[1:])  # استدعاء الدالة مع باقي القائمة
        return max(nums[0], max_of_rest)  # إرجاع أكبر عدد بين العنصر الأول وباقي القائمة

print("6. Maximum number in the list [1, 3, 2, 7, 5]:")
print(find_max([1, 3, 2, 7, 5]))  # الناتج يجب أن يكون 7

print("\n")

# 7. حساب القيم الزوجية في القائمة باستخدام التكرار
# نقوم بحساب القيم الزوجية في القائمة باستخدام التكرار.
def count_even(nums):
    if len(nums) == 0:  # حالة الإيقاف: إذا كانت القائمة فارغة
        return 0
    else:
        # إذا كان العنصر الأول زوجيًا نعده
        if nums[0] % 2 == 0:
            return 1 + count_even(nums[1:])  # إضافة 1 للعناصر الزوجية
        else:
            return count_even(nums[1:])  # استدعاء الدالة مع باقي العناصر

print("7. Counting even numbers in the list [1, 2, 3, 4, 5, 6]:")
print(count_even([1, 2, 3, 4, 5, 6]))  # الناتج يجب أن يكون 3
