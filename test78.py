
def find_big_number(numbers):
   
    big = numbers[0]
    for i in numbers:
        if i > big:
            big = i
    return big

numbers = [12, 45, 67, 23, 89, 34]
result = find_big_number(numbers)
print("الرقم الأكبر في القائمة:", result)



def find_small_number(numbers):
    small = numbers[0]
    for i in numbers:
        if i < small:
            small = i
    return small
numbers = [12, 45, 67, 23, 89, 34]
result = find_small_number(numbers)
print("الرقم الأكبر في القائمة:", result)
