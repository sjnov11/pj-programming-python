# if - elif - else 구문을 사용해봅시다

word_test_score = int(input("단어점수를 입력하세요. "))

if word_test_score == 100:
    print("와우! 축하합니다! 만점을 받으셨어요!")
elif word_test_score >= 70:
    print("단어 테스트에 통과하셨습니다.")
else:
    print("단어 테스트에 통과하지 못했습니다.")