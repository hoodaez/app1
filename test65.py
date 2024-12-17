# 1. خوارزمية الفرز باستخدام دمج (Merge Sort) - مثال على تقسيم وغزو
def merge_sort(arr):
    # إذا كانت القائمة تحتوي على عنصر واحد أو أقل، لا حاجة للفرز
    if len(arr) <= 1:
        return arr

    # تقسيم القائمة إلى نصفين
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # قسمنا النصف الأول
    right_half = merge_sort(arr[mid:])  # قسمنا النصف الثاني

    # دمج النصفين بعد ترتيبهم
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # دمج القوائم بالترتيب
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # إضافة العناصر المتبقية
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# اختبار Merge Sort
arr = [38, 27, 43, 3, 9, 82, 10]
print("1. Merge Sort Result:")
print(merge_sort(arr))  # النتيجة يجب أن تكون [3, 9, 10, 27, 38, 43, 82]

print("\n")

# 2. خوارزمية البحث الثنائي (Binary Search) - مثال آخر على تقسيم وغزو
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # وجدنا العنصر
        elif arr[mid] < target:
            left = mid + 1  # البحث في النصف الأيمن
        else:
            right = mid - 1  # البحث في النصف الأيسر
    return -1  # العنصر غير موجود

# اختبار Binary Search
sorted_arr = [3, 9, 10, 27, 38, 43, 82]
target_value = 27
print("2. Binary Search Result:")
print(binary_search(sorted_arr, target_value))  # النتيجة يجب أن تكون 3 (المؤشر الذي يحتوي على 27)

print("\n")

# 3. خوارزمية البحث العميق أولاً (DFS) في الرسم البياني
# هذه الخوارزمية تستخدم "تقسيم وغزو" على الرسم البياني (الشجرة).
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # تعيين مجموعة لتتبع العقد التي تم زيارتها
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # نغزو العقدة المجاورة باستخدام DFS

    return visited

# اختبار DFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("3. DFS Result:")
print(dfs(graph, 'A'))  # النتيجة ستكون العقد التي تم زيارتها (مجموعات تم زيارتها)

print("\n")

# 4. خوارزمية البحث في العرض (BFS) - مثال آخر على تقسيم وغزو
from collections import deque

def bfs(graph, start):
    visited = set()  # لتتبع العقد التي تم زيارتها
    queue = deque([start])  # قائمة انتظار لحفظ العقد التي سيتم زيارتها

    while queue:
        vertex = queue.popleft()  # إزالة العنصر الأول من القائمة
        if vertex not in visited:
            visited.add(vertex)  # إضافة العقدة إلى مجموعة الزيارات
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return visited

# اختبار BFS
print("4. BFS Result:")
print(bfs(graph, 'A'))  # النتيجة ستكون العقد التي تم زيارتها في البحث في العرض

print("\n")

# 5. خوارزمية كراسكال (Kruskal's Algorithm) - مثال آخر على تقسيم وغزو لتقليل الوزن في الرسم البياني
# الهدف من كراسكال هو إيجاد الشجرة المولدة الأدنى في الرسم البياني.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # استخدام الاستدعاء العكسي (recursion)
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # دمج الأشجار إذا كان الجذرين مختلفين
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# خوارزمية كراسكال للبحث عن الشجرة المولدة الأدنى
def kruskal(n, edges):
    edges = sorted(edges, key=lambda edge: edge[2])  # ترتيب الحواف حسب الوزن
    ds = DisjointSet(n)
    mst = []  # الشجرة المولدة الأدنى

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # إذا كانت العقدتين ليستا في نفس المجموعة
            mst.append((u, v, weight))
            ds.union(u, v)

    return mst

# اختبار Kruskal's Algorithm
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4  # عدد العقد
print("5. Kruskal's Algorithm Result (Minimum Spanning Tree):")
print(kruskal(n, edges))  # النتيجة ستكون الحواف المكونة للشجرة المولدة الأدنى

