# 논리연산자 or 를 사용해봅시다

score = int(input("점수를 입력하세요. "))

if score < 10 or score >= 90:
    print("점수가 10점 미만 또는 90점 이상입니다.")
else:
    print("점수가 10점 이상, 90점 미만입니다.")