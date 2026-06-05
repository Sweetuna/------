x = int(input("x값을 입력하세요:"))
y = int(input("y값을 입력하세요:"))

if x>0 and y>0:
    print("1사분면입니다.")

elif x>0 and y<0:
    print("4사분면입니다.")

elif x<0 and y>0:
    print("2사분면입니다.")

elif x<0 and y<0:
    print("3사분면입니다.")

elif x==0 and y==0:
    print("원점입니다.")

elif x==0:
    print("y축 위의 점입니다.")

elif y==0:
    print("x축 위의 점입니다.")

