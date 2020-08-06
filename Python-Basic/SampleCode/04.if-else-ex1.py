# 제어문 - 분기문
# if(조건):

# 예제 - 1

## 점수를 입력받아서 85점 이상 PASS, 미만 FAIL을 출력해보자

score = int(input("점수를 입력해 주세요 : "))

if(score >= 85):
    print("PASS")
else:
    print("FAIL")