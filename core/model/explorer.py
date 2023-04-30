from core.model.inputUser import Input
import datetime


def explorer():
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    if len(data) == 0:
        print("Операция прерава. Отсутствуют записи.\n")
        return
    y = int(Input.input("Введите год в формате: YYYY\n"))
    m = int(Input.input("Введите месяц в формате: MM\n"))
    d = int(Input.input("Введите день в формате: DD\n"))
    dateUser = datetime.date(year=y, month=m, day=d)
    dateUser = str(dateUser)
    print(dateUser)
    build = ""
    for i in data:
        if dateUser in i:
            build = build + i
    return build


def explorerId():
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    if len(data) == 0:
        print("Операция прерава. Отсутствуют записи.\n")
        return
    id = int(Input.input("Введите id для поиска.\n"))
    listS = list(filter(None, data))
    listS = [list(filter(None, i.split(";"))) for i in listS]
    line = 0
    for i in range(len(listS)):
        if id == int(listS[i][0]):
            line = i
    build = '{};{};{};{}\n'.format(listS[line][0], listS[line][1], listS[line][2],
                                   listS[line][3])

    return build
