# 1번 문제 : 자료형(숫자형) 실습
Max_weight = 500
Object1 = float(input("첫 번째 물건의 무게를 입력해주세요 : "))
Object2 = float(input("두 번째 물건의 무게를 입력해주세요 : "))
Current_Weight = Max_weight - (Object1 + Object2)
print("첫번째 물건 무게: %.2f 두번째 물건 무게: %.2f 현재 엘리베이터의 허용 무게는 %.2f 입니다." % (Object1, Object2, Current_Weight))

# 2번 문제 : 문자열 실습
num = int(input ("입력 : "))

for i in range(num):
    result = ''
    for j in range(num):
        result += "■ "
    print(result)

# 3번 문제 : 문자열 실습(2)
address = "용인시 처인구 모현읍"
address2 = address.split(" ")
print("시 :", address2[0])
print("구 :", address2[1])
print("읍 :", address2[2])

# 4번 문제 : 문자열 실습(3) - 슬라이싱
str1 = "life is too short you need Tython"
print(str1[:27] + "P" + str1[28:])
#replace 사용
print(str1.replace("T", "P", 1))

# 5번 문제 : 문자열 실습(4) - 내장함수
str2 = "life is too short you need Python"
print(str2.upper())