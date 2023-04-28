from core.model.note import NoteUser
from core.model.inputUser import Input
import datetime


def change(a: int):
    numberLines = 0
    text = str(a) + ";"
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    for number, i in enumerate(data):
        if text in data:
            numberLines = number
    objData = data[numberLines]
    objData = list(filter(None, objData.split(";")))

    sign = Input.input("Введите один из параметров 'h' или 'b': h - редактировать заголовок\n, "
                       "b - редактировать текст заметки")
    t = datetime.datetime.now()
    if sign.lower() == "h":
        heading = Input.input("Введите новый заголовок")
        dataObject = NoteUser(int(objData[0]), heading, objData[2], t)
        data[numberLines] = '{};{};{};{}\n'.format(dataObject.getId(), dataObject.getHeading(), dataObject.getBody(),
                                                   dataObject.getTime())

    if sign.lower() == "b":
        body = Input.input("Введите новую заметку")
        dataObject = NoteUser(int(objData[0]), objData[1], body, t)
        data[numberLines] = '{};{};{};{}\n'.format(dataObject.getId(), dataObject.getHeading(), dataObject.getBody(),
                                                   dataObject.getTime())

    with open(pathfile, 'w') as file:
        file.writelines(data)