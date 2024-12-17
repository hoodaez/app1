import heapq  # مكتبة لتنفيذ قائمة الأولويات Priority Queue

# تعريف العقد والجيران (المصفوفة التمثيلية للخريطة)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

# تعريف دالة التقدير (Heuristic): المسافة التقديرية من كل عقدة إلى الهدف
heuristic = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 6, 'E': 1, 'F': 0
}

# خوارزمية A* للعثور على أقصر مسار
def a_star(graph, start, goal):
    # قائمة الأولويات (Priority Queue) للحفاظ على العقد المفتوحة
    open_list = []
    heapq.heappush(open_list, (0, start))  # إضافة البداية مع تكلفة 0

    # لتتبع المسار وأفضل تكلفة للعقدة
    came_from = {}
    g_score = {node: float('inf') for node in graph}  # جميع التكلفة الأولية لا نهائية
    g_score[start] = 0

    while open_list:
        # اختيار العقدة ذات التكلفة الأقل
        current_cost, current_node = heapq.heappop(open_list)

        # إذا وصلنا إلى الهدف، نقوم ببناء المسار
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]  # إرجاع المسار بالترتيب الصحيح

        # التحقق من الجيران
        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_score[current_node] + weight
            if tentative_g_score < g_score[neighbor]:
                # تحديث أفضل تكلفة
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None  # إذا لم يكن هناك مسار

# تجربة الخوارزمية
start_node = 'A'
goal_node = 'F'
shortest_path = a_star(graph, start_node, goal_node)

print(f"أقصر مسار من {start_node} إلى {goal_node}: {shortest_path}")
