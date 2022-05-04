# 논리연산자 and 를 사용해봅시다

korean = int(input("국어 점수를 입력하세요. "))
english = int(input("영어 점수를 입력하세요. "))

# korean 이 70 점 이상이고 english 가 90 점 이상인 경우
# 이 학생은 학업 우수자 입니다.
if korean >= 70 and english >= 90:
    print("축하합니다. 학업 우수자입니다.")

print("국어:", korean)
print("영어:", english)