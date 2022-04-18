korean = int(input("국어점수: "))
english = int(input("영어점수: "))

if korean >= 70:
    if english >= 90:
        print("국어 70점 이상, 영어 90점 이상") 
    else:
	    print("국어만 70점 이상")
else:
    if english >= 90:
        print("영어만 90점 이상")
    else:
        print("둘 다 기준 점수 미만")