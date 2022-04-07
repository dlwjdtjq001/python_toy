import datetime
import os
import usefile ## 파일처리 함수
import useprintrecipe as up ## printrecripeT, printrecripeF 안에 들어가는 함수


def printrecipeT(title, r_txt, fs_txt):
    recipea = up.ingredients(r_txt)
    foodsample = up.refrigerator(fs_txt)
    요리가능성possible = up.cookability(foodsample, recipea)
    if 요리가능성possible == True:
        recipepr = up.recipe(title, r_txt)
        print("\n사용가능한 재료가 모두 있습니다")
        print("메뉴재료 -", recipea)
        print(recipepr)


def printrecipeF(title, r_txt, fs_txt):
    recipea = up.ingredients(r_txt)
    foodsample = up.refrigerator(fs_txt)
    요리가능성possible = up.cookability(foodsample, recipea)
    if 요리가능성possible == True:
        print("")
    else:
        print(title,"을 만들기위한",요리가능성possible)

##------------------------------------------------------------------------------


def timeRemaing(): ## 유통기한 입력받기
    slife_year = int(input("유통기한 연도"))
    slife_month = int(input("유통기한 월"))
    slife_day = int(input("유통기한 일"))

    input_time = datetime.datetime(slife_year, slife_month, slife_day)
    return input_time ## type = daterime.datetime


################################# main #########################################################

while True:
    menu = int(input("메뉴 화면입니다.(1.음식 추가 2.남은 유통기한 확인 3.음식 삭제 4. 현재 냉장고에 있는 음식은? 5. 레시피 추천 6.프로그램 종료)"))

    if menu == 1: ## 음식추가
        shelf_life = timeRemaing()
        usefile.updateFile("sample.txt", shelf_life)  ## 파일에 유통기한 넣기

        food = input("등록할 음식은 무엇인가요?")
        usefile.updateFile("foodsample.txt", food) ## 파일에 음식 넣기

    ##---------------------------------------------------------------------------------------------------

    elif menu == 2: ## 남은 유통기한 확인
        arr = usefile.listReadfile("sample.txt")  ## 파일에서 유통기한 리스트로 받기 type datetime.datetime
        food_list = usefile.listReadfile("foodsample.txt")  ## 음식 목록 리스트로
        remain_arr = []

        for i in arr:  ## 유통기한 - 현재시간 하여 남은 기간 list 생성(remain_arr)
            current_time = datetime.datetime.today()
            remain_day = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S') - current_time
            remain_arr.append(remain_day.days)

        dictionary = dict(zip(food_list, remain_arr))  ## 음식 리스트와 남은기간 리스트로 딕셔너리 생성

        fmt = "| {0:<7} | {1:>4}일 남았습니다." ## 형식에 맞게 출력
        print("| 음식이름 | 남은 기간")
        for key, balue in dictionary.items():
            print(fmt.format(key, balue))

    ##---------------------------------------------------------------------------------------------------

    elif menu == 3: ## 음식목록 삭제
        want_delete = input("어떤걸 삭제 하시겠습니까?")
        count_line = usefile.deleteFilefood(want_delete) ## 음식 파일에서 원하는 음식 줄 삭제 ,몇번쨰 줄인지 리턴
        usefile.deleteFileline(count_line)

        arr = usefile.listReadfile("sample.txt")  ## 파일에서 유통기한 리스트로 받기 type datetime.datetime
        food_list = usefile.listReadfile("foodsample.txt")  ## 음식 목록 리스트로
        remain_arr = []

        for i in arr:  ## 유통기한 - 현재시간 하여 남은 기간 list 생성(remain_arr)
            current_time = datetime.datetime.today()
            remain_day = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S') - current_time
            remain_arr.append(remain_day.days)

        dictionary = dict(zip(food_list, remain_arr))  ## 음식 리스트와 남은기간 리스트로 딕셔너리 생성

        fmt = "| {0:<7} | {1:>4}|"  ## 형식에 맞게 출력
        print("| 음식이름 | 남은 기간|")
        for key, balue in dictionary.items():
            print(fmt.format(key, balue))

    elif menu==4: ##냉장고에 있는 음식을 출력하기]

        f = open("foodsample.txt", 'r', encoding='utf8')
        read=f.read()
        split=read.split('\n')
        print(split)

    elif menu ==5: ##recipe와 foodsample을 비교하여 겹치는 음식이 많이 있는 레시피를 추천
       print("냉장고 안에 있는 음식을 바탕으로 적합한 레시피 추천을 해드리겠습니다!")
       flist = usefile.listReadfile("foodsample.txt")  ## 줄단위로 끊어서 배열로 리턴
       foodsample_txt = ','.join(flist)

       def printrcpouter(): ## 클로저 활용 (외부함수 리스트(arr,titlelist를 사용하는 내부함수를 외부로 전달함으로써 outer 함수의 컨텍스트가 종료되어도 arr,titlelist를 사용할 수 있음.)
           arr = ['recipe0.txt', 'recipe1.txt', 'recipe2.txt', 'recipe3.txt', 'recipe4.txt', 'recipe5.txt',
                  'recipe6.txt',
                  'recipe7.txt', 'recipe8.txt', 'recipe9.txt', 'recipe10.txt', 'recipe11.txt', 'recipe12.txt',
                  'recipe13.txt',
                  'recipe14.txt', 'recipe15.txt', 'recipe16.txt', 'recipe17.txt', 'recipe18.txt', 'recipe19.txt']
           titlelist = ["김치찌개", "고등어조림", "스팸간장덮밥", "새우볶음우동", "짜장밥", "멘보샤", "크림파스타", "감바스", "차돌박이된장찌개",
                        "차돌박이숙주볶음", "스팸부대찌개", "강된장찌개와부추무침", "떡볶이", "간장닭조림", "순두부찌개", "명란계란말이", "꽃게찜",
                        "소고기뭇국", "들깨칼국수", "프렌치토스트"]
           recipe_arr = []
           for i in arr:
               recipe_arr.append(open(i, 'r', encoding='utf8').read())
           r_dict = dict(zip(recipe_arr, titlelist))
           def printrcpinner(func):## 외부함수의 지역변수를 참조하고 콜백함수를 인자로 전달받는 내부함수
               for key, value in r_dict.items():
                   func(value, key, foodsample_txt)
           return printrcpinner ##외부로 내부함수를 전달함으로써 outer컨텍스트가 종료되어도 outer지역변수가 사라지지 않음.

       closer = printrcpouter()
       while True:
         a = int(input("(1.지금 있는 재료로 가능한 레시피 2.어떤 재료가 더 필요할까요? 3.메인메뉴로!"))
         if a==1: ## 가능한 레시피 출력
            closer(printrecipeT) ## 재료 다 있을시 레시피 출력
         elif a==2: ## 해당 레시피 완성 하기 위해 더필요한 재료 출력
            closer(printrecipeF) ## 재료 부족할시 모자란 재료 출력
         elif a==3: ## 메인메뉴로
             break
         else: ## 에러방지
            continue

    else:
            os._exit(1)








