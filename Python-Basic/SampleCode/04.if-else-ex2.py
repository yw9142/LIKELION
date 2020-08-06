# if(조건):

# 예제 - 2-1

solution = input("12 + 3 = ")

if(solution == "15"):
    print("정답입니다!")
else:
    print("틀렸어요.")


# 예제 - 2-2

tangsuyuk = input("$ 너 부먹이야?\n")

if(tangsuyuk == "응! 나 부먹이야!"):
    print("----상대방이 대화방을 나갔습니다.----")
elif(tangsuyuk == "아니 나는 찍먹!"):
    print("♥"*3)
else:
    print("나는 찍먹이야")