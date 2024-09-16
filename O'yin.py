import random

rondomNumber = random.randint(1, 40)
count = 0
print("1 dan 40 gacha son kiriting ")
while True:
    count += 1
    son = int(input("Sonni kiriting: "))
    if son == rondomNumber:
        print(f"siz {count} ta urinish bilan to'g'ri topdingiz. ")
        break
    elif son > rondomNumber:
        print(f"qidirilayotgan son {son} dan kichik. ")
    elif son < rondomNumber:
        print(f"qidirilayotgan son {son} dan katta. ")
    else:
        print("son xato kiritildi. ")
