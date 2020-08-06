# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


Max_weight = 500

Object1 = float(input(f"첫 번째 물건 무게를 입력 해주세요 : "))
Object2 = float(input(f"두 번째 물건 무게를 입력 해주세요 : "))

Current_Weight = Object1 + Object2

print(f"첫 번째 물건 무게 : {Object1}kg 두 번째 물건 무게 : {Object2}kg 현재 엘리베이터의 허용 무게는 {Max_weight - Current_Weight}kg입니다.")
