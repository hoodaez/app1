# 1. تعريف عقدة الشجرة (Node)
class Node:
    def __init__(self, value):
        self.value = value  # القيمة التي تحتوي عليها العقدة
        self.left = None  # العقدة الفرعية اليسرى
        self.right = None  # العقدة الفرعية اليمنى

# 2. الشجرة الثنائية (Binary Tree)
class BinaryTree:
    def __init__(self):
        self.root = None  # الجذر هو None في البداية

    # 2.1 إضافة عقدة إلى الشجرة
    def insert(self, value):
        if self.root is None:  # إذا كانت الشجرة فارغة
            self.root = Node(value)  # تعيين الجذر
        else:
            self._insert(self.root, value)  # استدعاء دالة الإضافة بشكل تكراري

    def _insert(self, node, value):
        # إذا كانت القيمة أصغر من القيمة الحالية، نضيفها إلى اليسار
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        # إذا كانت القيمة أكبر أو تساوي، نضيفها إلى اليمين
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # 2.2 عرض الشجرة باستخدام البحث العرضي (In-order Traversal)
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)  # زيارة العقدة اليسرى
            print(node.value, end=" ")  # طباعة القيمة
            self.in_order_traversal(node.right)  # زيارة العقدة اليمنى

    # 2.3 عرض الشجرة باستخدام البحث المسبق (Pre-order Traversal)
    def pre_order_traversal(self, node):
        if node:
            print(node.value, end=" ")  # طباعة القيمة
            self.pre_order_traversal(node.left)  # زيارة العقدة اليسرى
            self.pre_order_traversal(node.right)  # زيارة العقدة اليمنى

    # 2.4 عرض الشجرة باستخدام البحث التالي (Post-order Traversal)
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)  # زيارة العقدة اليسرى
            self.post_order_traversal(node.right)  # زيارة العقدة اليمنى
            print(node.value, end=" ")  # طباعة القيمة

# 3. شجرة البحث الثنائية (Binary Search Tree - BST)
# تكون القيم الموجودة في الشجرة مرتبة بحيث أن جميع القيم في العقدة اليسرى أصغر من القيمة الرئيسية،
# وجميع القيم في العقدة اليمنى أكبر من القيمة الرئيسية.

class BinarySearchTree(BinaryTree):
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:  # إذا كانت الشجرة فارغة أو تم الوصول إلى عقدة فارغة
            return False
        if node.value == value:  # إذا كانت القيمة موجودة في العقدة الحالية
            return True
        elif value < node.value:  # إذا كانت القيمة أصغر من القيمة الحالية، نبحث في العقدة اليسرى
            return self._search(node.left, value)
        else:  # إذا كانت القيمة أكبر، نبحث في العقدة اليمنى
            return self._search(node.right, value)

    # 3.1 حذف عقدة من شجرة البحث الثنائية
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node  # إذا كانت العقدة فارغة، نعيدها كما هي
        if value < node.value:  # إذا كانت القيمة أصغر، نبحث في العقدة اليسرى
            node.left = self._delete(node.left, value)
        elif value > node.value:  # إذا كانت القيمة أكبر، نبحث في العقدة اليمنى
            node.right = self._delete(node.right, value)
        else:  # إذا كانت القيمة تساوي القيمة في العقدة الحالية
            if node.left is None:  # إذا كانت العقدة اليسرى فارغة
                return node.right  # نعيد العقدة اليمنى
            elif node.right is None:  # إذا كانت العقدة اليمنى فارغة
                return node.left  # نعيد العقدة اليسرى
            # إذا كانت العقدة تحتوي على طفلين، نبحث عن أقل قيمة في العقدة اليمنى (أو أكبر قيمة في العقدة اليسرى)
            min_larger_node = self._min_value_node(node.right)
            node.value = min_larger_node.value  # استبدال القيمة بالقيمة الأصغر
            node.right = self._delete(node.right, min_larger_node.value)  # حذف العقدة التي تحتوي على القيمة الأصغر
        return node

    # البحث عن العقدة التي تحتوي على أصغر قيمة
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# اختبار الكود:

# 1. إنشاء شجرة البحث الثنائية
bst = BinarySearchTree()

# 2. إضافة قيم إلى الشجرة
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# 3. عرض الشجرة باستخدام In-order Traversal
print("In-order Traversal:")
bst.in_order_traversal(bst.root)  # النتيجة يجب أن تكون 20 30 40 50 60 70 80
print("\n")

# 4. البحث عن قيم في الشجرة
print("Search for 40 in BST:", bst.search(40))  # النتيجة يجب أن تكون True
print("Search for 90 in BST:", bst.search(90))  # النتيجة يجب أن تكون False
print("\n")

# 5. عرض الشجرة باستخدام Pre-order Traversal
print("Pre-order Traversal:")
bst.pre_order_tr
