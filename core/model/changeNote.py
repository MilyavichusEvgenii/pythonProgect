from core.model.note import NoteUser
from core.model.inputUser import Input
import datetime


def change(a: int):
    numberLines = 0
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    if len(data) == 0:
        print("Операция не может быть выполнена. Отстутствуют записи.\n")
        return
    listS = list(filter(None, data))
    listS = [list(filter(None, i.split(";"))) for i in listS]
    for i in range(len(listS)):
        if a == listS[i][0]:
            numberLines = i
    if numberLines == 0:
        print("Операция прервана. Такой записи нет.\n")
        return
    objData = data[numberLines]
    objData = list(filter(None, objData.split(";")))

    sign = Input.input("Введите один из параметров 'h' или 'b': h - редактировать заголовок,\n"
                       "b - редактировать текст заметки.\n")
    t = datetime.datetime.now()
    if sign.lower() == "h":
        heading = Input.input("Введите новый заголовок:\n")
        dataObject = NoteUser(int(objData[0]), heading, objData[2], t)
        data[numberLines] = '{};{};{};{}\n'.format(dataObject.getId(), dataObject.getHeading(), dataObject.getBody(),
                                                   dataObject.getTime())

    if sign.lower() == "b":
        body = Input.input("Введите новую заметку:\n")
        dataObject = NoteUser(int(objData[0]), objData[1], body, t)
        data[numberLines] = '{};{};{};{}\n'.format(dataObject.getId(), dataObject.getHeading(), dataObject.getBody(),
                                                   dataObject.getTime())

    with open(pathfile, 'w') as file:
        file.writelines(data)
    print("Запись редактирована.\n")
