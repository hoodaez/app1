# 1. حساب الأعداد في سلسلة فيبوناتشي (Fibonacci) باستخدام البرمجة الديناميكية
# نستخدم Memoization لتخزين الحسابات المتكررة.

# Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:  # إذا كانت النتيجة موجودة مسبقًا في الميمو
        return memo[n]
    if n <= 1:  # حالة الإيقاف
        return n
    # تخزين النتيجة في الميمو لتجنب الحساب المتكرر
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("1. Fibonacci (Memoization) for 6:")
print(fibonacci_memo(6))  # الناتج يجب أن يكون 8

print("\n")

# 2. حساب العامل (Factorial) باستخدام البرمجة الديناميكية
# نستخدم Tabulation لتخزين الحسابات في جدول.

# Tabulation
def factorial_tabulation(n):
    dp = [1] * (n + 1)  # جدول لتخزين العوامل
    for i in range(2, n + 1):  # بدءًا من 2 لأن العامل لـ 1 هو 1 بالفعل
        dp[i] = dp[i - 1] * i  # تخزين العامل
    return dp[n]

print("2. Factorial (Tabulation) for 5:")
print(factorial_tabulation(5))  # الناتج يجب أن يكون 120

print("\n")

# 3. مشكلة السلة (Knapsack Problem) باستخدام البرمجة الديناميكية
# الهدف: إيجاد أقصى قيمة يمكن أخذها مع الحفاظ على الوزن.

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # جدول لحفظ القيم المؤقتة
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])  # اختيار بين تضمين أو عدم تضمين العنصر
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5

print("3. Knapsack Problem:")
print(knapsack(weights, values, capacity))  # الناتج يجب أن يكون 220

print("\n")

# 4. إيجاد أطول سلسلة فرعية مشتركة (Longest Common Subsequence) باستخدام البرمجة الديناميكية
# الهدف: إيجاد أطول سلسلة فرعية مشتركة بين سلسلتين.

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # جدول لحفظ القيم المؤقتة
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # إذا كانت الأحرف متطابقة
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # أخذ القيمة الأعظم بين السطر والعمود
    return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"

print("4. Longest Common Subsequence (LCS) between AGGTAB and GXTXAYB:")
print(lcs(X, Y))  # الناتج يجب أن يكون 4

