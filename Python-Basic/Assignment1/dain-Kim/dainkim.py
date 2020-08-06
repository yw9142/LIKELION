# 1번 문제: 자료형(숫자형) 실습
Max_weight = 500
Object1 = float(input('첫번째 물건 무게: '))
Object2 = float(input('두번째 물건 무게: '))

Current_Weight = Max_weight - Object1 - Object2

print ("현재 엘리베이터의 허용 무게는", Current_Weight, "kg 입니다.")


# 2번 문제: 문자열 실습
n = int(input())

for i in range(n):
    print("■ " * n)
    

# 3번 문제: 문자열 실습(2)
address = "용인시 처인구 모현읍"

print("시:", address[0:3])
print("구:", address[4:7])
print("읍:", address[8:])


# 4번 문제: 문자열 실습(3) - 슬라이싱
str = "life is too short you need Tython"

str2 = str[:27] + "P" + str[28:]
print(str2)

str3 = str.replace("T", "P")
print(str3)


# 5번 문제: 문자열 실습(4) - 내장함수
str = "life is too short you need Python"
print(str.upper())