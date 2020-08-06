# 1번 문제

Max_weight = 500  # kg
Object1 = float(input('첫번째 물건 무게: '))  # kg, :2.f
Object2 = float(input('두번째 물건 무게: '))  # kg, :2.f
Current_Weight = float(Max_weight) - Object1 - Object2

print(f'현재 엘리베이터의 허용 무게는 {Current_Weight:.2f} kg 입니다.')

#  2번 문제

line = int(input())

if line == 5:
  print('''
  ■■■■■
  ■■■■■
  ■■■■■
  ■■■■■
  ■■■■■
  ''')
elif line == 3:
  print('''
  ■■■
  ■■■
  ■■■
  ''')

# 3번 문제

address = "용인시 처인구 모현읍"
spl_address = address.split(" ")
print(f'''
시 : {spl_address[0]}
구 : {spl_address[1]}
읍 : {spl_address[2]}
''')

# 4번 문제 - 1

st = "life is too short you need Tython"
spl_st = st.split('T')
new_st = spl_st[0] + 'P' + spl_st[1]
print(new_st)

# 4번 문제 - 2

st = "life is too short you need Tython"
rep_st =  st.replace("T","P")
print(rep_st)

# 5번 문제
st = "life is too short you need Python"
print(st.upper())
