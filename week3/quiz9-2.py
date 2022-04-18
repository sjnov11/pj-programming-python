# 구구단을 출력하는 프로그램을 작성해봅시다. (2단~9단)

for num1 in range(2, 10):
    for num2 in range(1, 10):
        print(num1, "*", num2, "=", num1 * num2)