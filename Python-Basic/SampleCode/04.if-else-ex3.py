#if(조건) :

# 예제 - 3

# 5000 이상 : 아웃백 / 3000 이상 : 학식 
# 1000 이상 : 컵라면 / ㅠㅠ : 공깃밥
 
money = int(input("$ 돈 얼마 있어?\n>> "))

if(money >= 5000):
    print("$ 아웃백 가자")
elif(money >= 3000):
    print("$ 학식 먹자")
elif(money >= 1000):
    print("$ 컵라면 먹자")
else:
    print("$ 공깃밥 가즈아")


# if(money >= 5000):
#     print("아웃백 가자")
# else:
#     if(money >= 3000):
#         print("학식 먹자")
#     else:
#         if(money >= 1000):
#             print("컵라면 먹자")
#         else:
#             print("공깃밥 가즈아ㅏㅏㅏ")
# else if = elif