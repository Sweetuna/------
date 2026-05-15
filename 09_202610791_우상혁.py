print("학점 총합과 평균을 계산해드립니다.")

math = int(input("수학 점수를 입력하세요:"))
eng = int(input("영어 점수를 입력하세요:"))
korean = int(input("국어 점수를 입력하세요:"))
science = int(input("과학 점수를 입력하세요:"))

print(f"학점 총 합은 {math+eng+korean+science}입니다.")
print(f"학점 평균은 {(math+eng+korean+science)/4}입니다.")