def search_number(number, target):
    low = 0
    high = len(number) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if number[mid] == target:
            return f"تم العثور على العنصر في الموقع {mid}"
        
        elif number[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return "العنصر غير موجود"

# تجربة البرنامج
my_list = [10, 20, 30, 40, 50]
target = 30

print(search_number(my_list, target))
# Output
# تم العثور على العنصر في الموقع 2