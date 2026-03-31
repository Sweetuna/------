A = int(input("1. 입력한 수식을 계산하기 / 2. 두 수 사이의 합계를 계산하기 :"))

if A == 1 :
    numA = input("수식을 입력하세요 : ")
    answerA = eval(numA)
    print("{}결과는 {}입니다.".format(numA, answerA))

elif A == 2 :
    numB1 = int(input("첫 번째 수를 입력하세요 : "))
    numB2 = int(input("두 번째 수를 입력하세요 : "))
    answer = 0
    for answerB in range(numB1, numB2+1) : 
        answer = answer + answerB
    print("{}+...+{} 결과는 {}입니다.".format(numB1, numB2, answer))

else : 
    print("1 또는 2만 입력하세요.")