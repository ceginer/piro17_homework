from ast import While


num = 0

def StrtoInt(s):
  try:
    int(s)
    return True
  except:
    return False

def TellNum():
  while True:
    global a
    a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

    if StrtoInt(a):
      a = int(a)
      if a != 1 and a!= 2 and a!=3:
        print('1,2,3 중 하나를 입력하세요')
        continue
      else:
        break
        
    else:
      print('정수를 입력하세요')
      continue

winner = 0
try:
  while (True):
    TellNum()
    num += a

    for i in range(num-a+1,num+1):
      print('playerA :', i)
      if i == 31:
        winner=1
        raise

    TellNum()
    num += a

    for i in range(num-a+1,num+1):
      print('playerB :', i)
      if i == 31:
        winner=2
        raise
except:
  if winner==1:
    print('playerA win!')
  else:
    print('playerB win!')
