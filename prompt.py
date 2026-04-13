button = 0

def coffee_machine(button): 
    print()
    print("#1. 뜨거운 물을 준비한다.");
    print("#2. 종이컵을 준비한다.");

    if button == 1:
        print("#3. 보통커피를 탄다.")
    elif button == 2:
        print("#3. 설탕커피를 탄다.")
    elif button == 3: 
        print("#3. 블랙커피를 탄다.")
    else: 
        print("#아무거나 탄다.\n")

    print("#4. 물을 붓는다.");
    print("#5. 스푼으로 젓는다.");
    print()

coffee = int(input("어떤 커피를 드릴까요? (1: 보통 2: 설탕 3: 블랙)"))
coffee_machine(coffee)
print("커피 드리겠습니다. 손님.")