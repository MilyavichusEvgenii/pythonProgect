from core.model.inputUser import Input
import datetime


def explorer():
    y = int(Input.input("Введите год в формате: YYYY\n"))
    m = int(Input.input("Введите месяц в формате: MM\n"))
    d = int(Input.input("Введите день в формате: DD\n"))
    dateUser = datetime.date(year=y, month=m, day=d)
    dateUser = str(dateUser)
    print(dateUser)
    pathfile = "Notes.csv"
    build = ""
    with open(pathfile, 'r') as file:
        data = file.readlines()
    for i in data:
        if dateUser in i:
            build = build + i

    return build
