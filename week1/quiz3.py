# 학생정보와 국영수 총합과 평균을 알려주는 프로그램을 만들어보자

# 학생 이름을 입력받고 name 변수에 담으세요
name = input("이름: ")
# 국어 성적을 입력받고 korean 변수에 담으세요
korean = int(input("국어: "))
# 영어 성적을 입력받고 english 변수에 담으세요
english = int(input("영어: "))
# 수학 성적을 입력받고 math 변수에 담으세요
math = int(input("수학: "))
# 점수 총합을 계산하여 total 변수에 담으세요
total = korean + english + math
# 평균을 계산하여 avg 변수에 담으세요
avg = total / 3
# 학생의 이름과 총합, 평균을 출력하세요
print(name, "\n총점:", total, "\n평균:", avg)