#함수 이름은 변경 가능합니다.

##############  menu 1
from pickle import APPEND


# def Menu1()#매개변수가 필요한지 판단 후 코딩할 것) :
    #사전에 학생 정보 저장하는 코딩 




##############  menu 2
# def Menu2#매개변수가 필요한지 판단 후 코딩할 것) :
    #학점 부여 하는 코딩

##############  menu 3
# def Menu3#매개변수가 필요한지 판단 후 코딩할 것) :
    #출력 코딩

##############  menu 4
# def Menu4#매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
student_dict={}
student_sublist =[]

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

      def StrtoInt(s):
        try:
          int(s)
          return True
        except:
          return False

      while True:
        try:
          student_sublist.clear()
          insert_name, insert_mid, insert_fin = input('Enter name mid-score final-score').split()
          student_sublist.extend([insert_name, insert_mid, insert_fin])

          if not(StrtoInt(insert_mid)) or not(StrtoInt(insert_fin)):
            print('양의 정수값을 입력하세요')
            continue

          elif int(insert_mid) < 0 or int(insert_fin) < 0:
            print('양의 정수값을 입력하세요')
            continue

          if insert_name in student_dict:
            print('이미 존재하는 학생입니다.')
            continue
          
          else:
            student_dict[student_sublist[0]]  = [insert_mid, insert_fin]
            break
      
        except ValueError:
          print('Num of data is not 3!')

      # print(student_dict)




    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
      def avg(x):
        global grade
        if x >= 90:
          grade = 'A'
        elif 80 <= x < 90:
          grade = 'B'
        elif 70 <= x < 80:
          grade = 'C'
        else:
          grade = 'D'

      student_list = list(student_dict.keys())
      grade ='A'

      if len(student_dict) == 0:
        print('학생들의 데이터가 없어요!')

      else:
        for i in range(len(student_dict)):
          student_scorepart = student_dict[student_list[i]]
          average = (int(student_scorepart[0]) + int(student_scorepart[1])) / 2
          avg(average)
          student_scorepart.append(grade)
          # print(student_scorepart)
          # print(student_dict)

    # elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    # elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    # elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료

    # else :
        #"Wrong number. Choose again." 출력