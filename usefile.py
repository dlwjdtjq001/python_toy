def writeFile(dir, push_item):
    f = open(dir, "w", encoding="utf8")
    f.write(str(push_item))
    f.close()


def updateFile(dir, push_item): ## 파일 편집
    f = open(dir, "a", encoding="utf8")
    f.write("\n" + str(push_item))
    f.close()


def listReadfile(dir): ## 줄단위로 끊어서 배열로 리턴
    f = open(dir, "r", encoding="utf8")
    read = f.read()
    split = read.split("\n")
    return split

def deleteFilefood(string):  ## 원하는 음식 파일에서 삭제하고 해당 라인 몇번째인지 리턴
    with open("foodsample.txt", 'r', encoding="utf8") as infile:
        data = infile.readlines()
    with open("foodsample.txt", 'w', encoding="utf8") as outfile:
        count_line = 1

        for i in data:
            if not i.startswith(string):
                outfile.write(i)

        for i in data:
            if not i.startswith(string):
                count_line = count_line + 1

            else:
                break

    return count_line

def deleteFileline(count_line): ##원하는 라인 삭제
    with open("sample.txt", "r") as infile:
        lines = infile.readlines()

    with open("sample.txt", "w") as outfile:
        for pos, line in enumerate(lines):
            if pos != count_line - 1:
                outfile.write(line)
