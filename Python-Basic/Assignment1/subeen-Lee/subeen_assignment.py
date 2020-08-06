# 1번 문제: 자료형(숫자형) 실습
Max_weight = 500
Object1 = float(input("첫 번째 물건의 무게: "))
Object2 = float(input("두 번째 물건의 무게: "))
Current_Weight = float(Max_weight - Object1 - Object2)
print("첫번째 물건 무게:", Object1,"두번째 물건 무게:",Object2,"현재 엘리베이터의 허용 무게는 ",Current_Weight,"kg 입니다.")


# 2번 문제: 문자열 실습
a = int(input())
for i in range (a):
    print("■ "*a)

# 3번 문제: 문자열 실습
address = "용인시 처인구 모현읍"
new_address = address.split(" ")
print("시 :",new_address[0])
print("구 :", new_address[1])
print("읍 :", new_address[2])

# 4번 문제: 문자열 실습 -슬라이싱
#version1
sentence = "life is too short you need Tython"
new_s = sentence.split(" ")
new_s[6] = "Python"
print(new_s[6])
print(new_s)
#version2 = replace
sentence = "life is too short you need Tython"
print(sentence.replace("Tython", "Python"))

# 5번 문제: 문자열 실습 - 내장함수
str = "life is too short you need Python"
print(str.upper())





