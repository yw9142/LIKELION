# 제어문(2) - 반복문

# for문

# for 반복제어변수 in 반복대상 :
# 	반복실행 할 내용


for score in [96,98,100,87]:
	print(score)

number = 0

# 1부터 10까지의 수 더하기!
sum1 = 0

for number in [1,2,3,4,5,6,7,8,9,10]:
    sum1 += number
    # sum = sum + number
    print("1부터 10까지 더하기 : ", sum1)

# range 이용해서 1부터 10까지의 수 더하기!
sum2 = 0

for number in range(1, 11):
    sum2 += number
    # sum = sum + number
    print("(range) 1부터 10까지 더하기 : ", sum2)

# range 인자 1개
sum3 = 0
for number in range(5):
    sum3 += number
    # sum = sum + number
    print("(인자 1개) 0부터 5까지 더하기 : ", sum3)


# range 같은 코드!
sum4 = 0
for number in range(0, 5):
    sum4 += number
    # sum = sum + number
    print("(인자 2개) 0부터 5까지 더하기 : ", sum4)