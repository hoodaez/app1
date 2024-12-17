from collections import deque

# 1. خوارزمية البحث في العرض أولاً (BFS)
def bfs(graph, start):
    visited = set()  # مجموعة لتتبع العقد التي تم زيارتها
    queue = deque([start])  # قائمة انتظار لحفظ العقد التي سيتم زيارتها

    while queue:
        vertex = queue.popleft()  # إزالة العنصر الأول من قائمة الانتظار
        if vertex not in visited:
            visited.add(vertex)  # إضافة العقدة إلى مجموعة العقد التي تمت زيارتها
            print(f"BFS: Visiting {vertex}")  # طباعة العقدة التي تتم زيارتها
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)  # إضافة الجيران الذين لم تتم زيارتهم بعد

    return visited

# 2. خوارزمية البحث في العمق أولاً (DFS) باستخدام التكرار (Recursion)
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()  # مجموعة لتتبع العقد التي تم زيارتها

    visited.add(start)  # إضافة العقدة الحالية إلى مجموعة العقد التي تمت زيارتها
    print(f"DFS (Recursive): Visiting {start}")  # طباعة العقدة التي تتم زيارتها

    for neighbor in graph[start]:  # زيارة الجيران
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)  # استدعاء دالة DFS بشكل تكراري للجيران غير الذين تم زيارتهم

    return visited

# 3. خوارزمية البحث في العمق أولاً (DFS) باستخدام المكدس (Stack)
def dfs_stack(graph, start):
    visited = set()  # مجموعة لتتبع العقد التي تم زيارتها
    stack = [start]  # مكدس لاحتواء العقد التي سيتم زيارتها

    while stack:
        vertex = stack.pop()  # استخراج العقدة الأخيرة من المكدس
        if vertex not in visited:
            visited.add(vertex)  # إضافة العقدة إلى مجموعة العقد التي تمت زيارتها
            print(f"DFS (Stack): Visiting {vertex}")  # طباعة العقدة التي تتم زيارتها
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)  # إضافة الجيران غير الذين تم زيارتهم

    return visited


# تعريف الرسم البياني (Graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# اختبار BFS و DFS:
print("1. BFS Traversal:")
bfs_result = bfs(graph, 'A')
print("Visited nodes:", bfs_result)  # سيتم طباعة جميع العقد التي تمت زيارتها
print("\n")

print("2. DFS Traversal (Using Recursion):")
dfs_recursive_result = dfs_recursive(graph, 'A')
print("Visited nodes:", dfs_recursive_result)  # سيتم طباعة جميع العقد التي تمت زيارتها
print("\n")

print("3. DFS Traversal (Using Stack):")
dfs_stack_result = dfs_stack(graph, 'A')
print("Visited nodes:", dfs_stack_result)  # سيتم طباعة جميع العقد التي تمت زيارتها
