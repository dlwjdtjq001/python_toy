import re


def ingredients(txt):  ## 텍스트 넣으면 재료만 리스트형식으로 빼주는 함수
    pattern = r"\([^.(?!\n)]+\)"
    txt = re.findall(pattern, txt)
    txt = str(txt[0])
    txt = txt.replace(" ", "")
    txt = txt.replace("(", "")
    txt = txt.replace(")", "")
    txt = txt.split(",")
    return txt

def recipe(menuName, txt):
    pattern = r"\([^.(?!\n)]+\)"
    txt = re.sub(pattern, "", txt)
    str = """\
       -------------------------------------------
       ['{0}' 레시피]
       {1}
       -------------------------------------------
              """.format(menuName, txt)
    return str

    ##냉장고 텍스트를 받아서 리스트로 반환하는 함수


def refrigerator(txt):
    txt = str(txt)
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = txt.split(",")
    return txt

    ##요리가 가능한지 foodsample와 recipe를 통해 요리가능인지 판단해주는 함수


def cookability(foodsample, recipec):  ##recipe0에 대하여 요리가능인지 판단
    foodsample = set(foodsample)
    recipec = set(recipec)
    부족한재료less = recipec.difference(foodsample)
    부족한재료less = list(부족한재료less)
    if len(부족한재료less) == 0:
        return True
    else:
        str = """재료가 부족합니다
           부족한 재료 {0}
           """.format(list(부족한재료less))
        return str