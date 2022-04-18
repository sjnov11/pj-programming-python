# continue 문을 사용하여 반복문을 스킵시켜 봅시다

num = 0
while num < 5:
    if num == 2:
        num += 1
        continue
    print(num)
    num += 1