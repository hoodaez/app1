# 1. الترتيبات (Permutations) باستخدام Backtracking
# الهدف: إيجاد جميع الترتيبات الممكنة للأرقام في قائمة.

def permutations(nums, start=0):
    if start == len(nums):  # إذا وصلنا إلى نهاية القائمة
        print(nums)  # طباعة الترتيب الحالي
        return
    
    for i in range(start, len(nums)):  # تكرار عبر جميع الأرقام
        # تبادل الأرقام
        nums[start], nums[i] = nums[i], nums[start]
        permutations(nums, start + 1)  # استدعاء الدالة بشكل تكراري
        # التراجع عن التبادل (Backtrack)
        nums[start], nums[i] = nums[i], nums[start]

print("1. Permutations of [1, 2, 3]:")
permutations([1, 2, 3])  # سيطبع جميع الترتيبات الممكنة للقائمة

print("\n")

# 2. مشكلة N-Queens باستخدام Backtracking
# الهدف: وضع N ملكات على لوحة شطرنج بحيث لا تهاجم أي ملكة الأخرى.
# الشروط: الملكات لا يمكن أن تكون في نفس الصف، العمود، أو القطر.

def is_safe(board, row, col, n):
    for i in range(row):  # التحقق من العمود
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:  # إذا وضعنا جميع الملكات
        print_board(board, n)
        return

    for col in range(n):  # محاولة وضع الملكة في كل عمود
        if is_safe(board, row, col, n):  # إذا كان وضع الملكة آمنًا
            board[row] = col  # وضع الملكة في المكان الحالي
            solve_n_queens(board, row + 1, n)  # التكرار لوضع الملكة التالية
            board[row] = -1  # التراجع عن وضع الملكة (Backtrack)

def print_board(board, n):
    for i in range(n):
        row = ['Q' if x == board[i] else '.' for x in range(n)]
        print(' '.join(row))
    print("\n")

print("2. Solving the N-Queens problem for N=4:")
n = 4
board = [-1] * n  # تمثيل لوحة الشطرنج
solve_n_queens(board, 0, n)  # حل المشكلة مع N = 4

print("\n")

# 3. مشكلة مجموع العناصر (Subset Sum Problem) باستخدام Backtracking
# الهدف: إيجاد جميع المجموعات الفرعية التي تعطي مجموعًا معينًا.

def subset_sum(nums, target, current_set, index):
    if sum(current_set) == target:  # إذا وصلنا إلى المجموع المطلوب
        print(current_set)  # طباعة المجموعة الفرعية
        return
    if index == len(nums):  # إذا استعرضنا جميع الأرقام
        return

    # إضافة العنصر الحالي إلى المجموعة الفرعية
    subset_sum(nums, target, current_set + [nums[index]], index + 1)

    # التراجع عن إضافة العنصر الحالي (Backtrack)
    subset_sum(nums, target, current_set, index + 1)

print("3. Subset sum with target 5 from [1, 2, 3, 4]:")
subset_sum([1, 2, 3, 4], 5, [], 0)  # إيجاد المجموعات الفرعية التي تعطي مجموع 5
