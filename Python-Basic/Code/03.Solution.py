Max_weight = 500
Object1 = float(input("첫번째 물건 무게: "))
Object2 = float(input("두번째 물건 무게: "))
weight = Max_weight - (Object1 + Object2)

print("현재 엘리베이터의 허용 무게는 ", weight, "kg 입니다.")