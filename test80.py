
def binary_search(arr, target):
    low = 0
    hight = len(arr) -1
    
    while low <= hight:
        mid  = (low + hight) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            hight = mid - 1
        return None
    return -1  # ��ذا لم يتم العثور على العنصر

# مثال لا��تخدام الخوارزمية
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target)

if result != -1:
    print("عنصر مطلوب موجود في المصفوفة")
else:
    print("عنصر مطلوب غير موجود في المصفوفة")
    


            