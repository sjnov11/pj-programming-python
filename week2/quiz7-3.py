# 윤년인지 아닌지 판별하는 프로그램

# 윤년: 2월 29일이 있는 날
# 1. 년도가 400로 나누어 떨어지면 윤년이다.
# 2. 년도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않으면 윤년이다.

# 연도를 입력받습니다.
year = int(input("연도를 입력하세요. "))

# 윤년인지 아닌지 판별합니다
if year % 400 == 0:
    print(year, "는 윤년입니다.")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "는 윤년입니다.")
else:
    print(year, "는 윤년이 아닙니다.")

## 9 2 3