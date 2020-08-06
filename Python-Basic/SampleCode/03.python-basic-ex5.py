# 딕셔너리 (내장함수)
pairs = {'지코' : '아무노래', '오반' : '어떻게 지내', '크러쉬' : '가끔'}
print(pairs)

# 하나의 key-value 쌍을 추가하는 방법
# 딕셔너리형 변수 [키] = value
pairs['Maroon 5'] = 'Memories'
# 4번째 key-value 쌍을 추가했어요!
print(pairs)

# 특정 key-value 삭제하는 방법 : del 함수
del pairs['지코']
print(pairs)

# key로 value 얻기 : 변수.get(키)
v = pairs.get('오반')
print(v)