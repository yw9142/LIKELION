import random


print("☆★☆★ 로또 번호 자동 생성기 ★☆★☆")
print("-"*30)
print("게임 수를 입력하세요!")

num = int(input("게임 수 : "))

print("-"*30)

for i in range(0, num):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("-" * 30)
print("☆★☆★ 로또 번호 생성 완료 ★☆★☆")
print("-" * 30)
