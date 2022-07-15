def StrtoInt(s):
  try:
    int(s)
    return True
  except:
    return False

def brGame():
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

from random import randint

num = 0
winner = 0
# membernum 0 = player, 1 = omputer 승리
membernum=2
member = {1:'computer', 0:'player'}

try:
  while (True):
    membernum += 1
    membernum %= 2

    if membernum == 0:
      brGame()
    if membernum == 1:
      a=randint(1,3)
    
    num += a

    for i in range(num-a+1,num+1):
      print(f'{member[membernum]}', i)
      if i == 31:
        raise

except:
  if membernum==0:
    print('computer win!')
  elif membernum==1:
    print('player win!')
