#1
max_weight = 500
object1=float(input('첫번째 물건 무게: '))
object2=float(input('두번째 물건 무게: '))
current_weight = max_weight-(object2+object1)
print('첫번째 물건 무게:',object1,'두번째 물건 무게:',object2,'현재 엘레베이터의 허용무게는 ', current_weight,'kg 입니다')
#2
n = int(input())
for i in range(n):
    print('■ '*n, end='\n')
#3
address = '용인시 처인구 모현읍'
print('시: '+address[0:4])
print('구: '+address[4:7])
print('읍: '+address[8:])
#4
wrong = 'Life is too short you need Tython'
correct1 = wrong[:27]+'P'+wrong[28:]

correct2 = wrong.replace('T','P')

print(correct1)
print(correct2)
#5
sentence = 'Life is too short you need Python'
upper = sentence.upper()

print(upper)