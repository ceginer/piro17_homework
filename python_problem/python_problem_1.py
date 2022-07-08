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




num = 0
winner = 0
membernum=2
member = {1:'A', 0:'B'}

try:
  while (True):
    brGame()
    num += a
    membernum += 1

    for i in range(num-a+1,num+1):
      membernum %= 2
      print(f'player {member[membernum]} :', i)
      if i == 31:
        raise
      
except:
  if membernum==1:
    print('player A win!')
  elif membernum==2:
    print('player B win!')
