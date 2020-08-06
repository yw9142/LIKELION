#1번 문제
Object1 = float(input("첫번째 물건 무게 : "))
Object2 = float(input("두번째 물건 무게 : "))

Max_weight = 500
Current_Weight = Max_weight - (Object1 + Object2) #추가로 적재할 수 있는 무게

print("현재 엘리베이터의 허용 무게는 ",Current_Weight,"kg 입니다.")


# 2번 문제

count = int(input("입력 : "))

print(("■ " *count + "\n")*count)
# for i in range(1,count+1):
#     print("■ "*count) 


# #3번 문제
address = "용인시 처인구 모현읍"

print("시" , address[0:3])
print("구", address[4:7])
print("읍", address[9:11])

#4번 문제
life = "life is too short you need Tython"
# T = life.find("T")
# print(str[0:T] , "P" , str[T+1:-1])
replace = life.replace("T","P",1)
print(replace)

#5번 문제
print(replace.upper())


