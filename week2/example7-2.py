# 논리연산자 or 를 사용해봅시다

korean = int(input("국어 점수를 입력하세요. "))
english = int(input("영어 점수를 입력하세요. "))

# korean 이 10 점 미만이거나 english 가 10 점 미만인 경우
# 이 학생은 보충수업 대상자 입니다.
if korean < 10 or english < 10:
    print("보충수업 대상자입니다.")

print("국어:", korean)
print("영어:", english)