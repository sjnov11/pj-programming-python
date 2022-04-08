# 점수를 입력받고 점수에 따라 등급을 출력하는 프로그램을 만들어봅시다
# A: 90점 이상
# B: 80점 이상
# C: 70점 이상
# D: 60점 이상
# F: 그 외

# score 변수에 점수를 입력 받아봅시다.
score = int(input("점수를 입력하세요. "))
# if-elif-else 구문을 통해 등급을 출력해봅시다.
if score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
elif score >= 60:
    print("D등급입니다.")
else:
    print("F등급입니다.")