# الهدف: طباعة الأعداد الأولية بين 10 و 30

for num in range(10, 31):  # نكرر الأرقام من 10 إلى 30
    is_prime = True   # نفترض أن العدد أولي
    for i in range(2,num):  # نتحقق من قابلية القسمة على أي رقم من 2 إلى num-1
        if num % i ==0:  # إذا كان باقي القسمة 0
            is_prime =False  # العدد ليس أوليًا
            break  # نخرج من الحلقة الداخلية
    if is_prime:  # إذا بقي is_prime = True، فالعدد أولي
        print(f"{num} is a prime number")
