# 함수란!

def plusOne(x):
    return x + 1

mayBeSix = plusOne(5)
print(mayBeSix)

print('##############################################')

def plus(x,y):
    return x+y

x = plus(10, 20)
print(x)


# 전역변수, 지역변수 이해하기

x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

# 20
# 10

print('##############################################')

x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

# 20
# 20

print('##############################################')


a = 2

def test() :
    global b 
    b = 34
    c = 50
    print("inside test", a)
    print("inside test", b)
    print("inside test", c)

test()
print("after test", a)
print("after test", b)
print("after test", c)


# 반복문에서 사용된 지역변수


