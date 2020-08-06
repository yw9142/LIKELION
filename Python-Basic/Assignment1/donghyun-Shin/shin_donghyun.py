#1번
Max_weight = 500
Object1 = float(input("첫번째 물건 무게 입력ㄱㄱ: "))
Object2 = float(input("두번째 물건 무게 입력ㄱㄱ: "))
Current_Weight = Max_weight - Object1 - Object2
print("첫번째 물건 무게: " ,Object1, "두번쨰 물건 무게: ", Object2, "현재 엘리베이터의 허용무게는 :", Current_Weight,"입니다.")

#2번
a = int(input("몇개?: "))
for i in range (a):
    for j in range (a):
        print('ㅁ', end='')
    print()

#3번
addr = "용인시 처인구 모현읍"
print("시",addr[0:3])
print("구",addr[4:7])
print("읍",addr[8:11])

#4번
li = "life is too short you need tython"
print(li[0:27],"P",li[28:33], sep="")
print(li.replace("t","P"))

#5번
print(li.upper())
