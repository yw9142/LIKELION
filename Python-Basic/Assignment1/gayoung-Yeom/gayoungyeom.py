# 1
Max_weight = 500
Object1 = float(input("첫 번째 물건 무게: "))
Object2 = float(input("두 번째 물건 무게: "))
Current_Weight = Object1 + Object2
print("현재 엘리베이터의 허용 무게는 ", Max_weight - Current_Weight, "kg 입니다.")

# 2
num = int(input("입력: "))
for i in range(num):
    print("■ "*num)

# 3
addr = "용인시 처인구 모현읍"
addr = addr.split(" ")
print("시: ", addr[0])
print("구: ", addr[1])
print("읍: ", addr[2])

# 4
str1 = "life is too short you need Tython"
str2 = str1[:26] + ' P' + str1[28:]
str3 = str1.replace("T", "P")
print(str2)
print(str3)

# 5
str4 = str2.upper()
print(str4)
