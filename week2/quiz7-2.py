# 쇼핑몰 결제 금액을 계산해봅시다

# 총 구매 금액을 입력받아 total_price 변수에 담으세요
total_price = int(input("총 구매 금액을 입력해주세요. "))
# 할인된 금액을 담을 변수 sale_price 를 선언하고, 총 구매금액을 담으세요
# 가격 할인은 이 변수에다 수행합니다.
sale_price = total_price

# 10% 할인 쿠폰 사용여부를 Y 또는 N 으로 입력받아 
# coupon_use 변수에 담으세요
coupon_use = input("10% 할인 쿠폰 사용여부(Y/N): ")


# coupon_use 가 Y 또는 N 이 아닌 경우, 
# 잘못된 입력입니다 라고 출력후 프로그램을 종료하세요
# 파이썬 프로그램을 종료하는 방법은 exit(0) 입니다
if not(coupon_use == "Y" or coupon_use == "N"):
    print("잘못된 입력입니다")
    exit(0)

# coupon_use 가 Y 인 경우, 금액의 10%를 할인해주세요.
# sale_price 에 0.9 를 곱하면 10% 를 할인한 것과 같습니다.
if coupon_use == "Y":
    sale_price *= 0.9
    # sale_price = sale_price * 0.9

# 마일리지 사용 금액을 입력받아 mileage 변수에 담으세요.
# 이 때, 메시지로 사용가능한 마일리지가 5000원 남아있다고 안내해주세요.
mileage = int(input("마일리지 사용금액(잔액 5000원): "))

# 5000원 초과하는 마일리지 금액을 입력 받았을 때, 금액초과를 출력하고 종료해주세요.
if mileage > 5000:
    print("금액 초과")
    exit(0)

# sale_price 를 초과하는 마일리지 금액을 입력 받았을 때, 
# sale_price 로 마일리지 금액을 변경해주세요.
if mileage > sale_price:
    mileage = sale_price

# sale_price 에서 마일리지 사용액을 빼주세요
sale_price -= mileage

# 배송비 shipping 변수를 선언하고 3500 을 담습니다. 
# 단, sale_price 가 3만원 이상일 경우 배송비는 무료입니다.
shipping = 3500
if sale_price >= 30000:
    shipping = 0

# 배송비를 sale_price 에 추가합니다.
sale_price += shipping

# 총 구매금액, 쿠폰 사용여부(Y/N), 마일리지 사용금액, 
# 배송비, 할인된 금액을 순서대로 출력합니다. 
print("총 구매금액:", total_price)
print("쿠폰 사용여부(Y/N):", coupon_use)
print("마일리지 사용금액:", mileage)
print("배송비:", shipping)
print("할인 금액:", sale_price)



