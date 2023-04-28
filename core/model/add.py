from core.model.note import NoteUser
from core.model import operations
from core.model.inputUser import Input
from core.model import operations
import datetime


def add():
    heading = Input.input("Введите заголовок заметки")
    body = Input.input("Введите текст заметки")
    t = datetime.datetime.now()
    data = operations.reader()

    if len(data) == 0:
        a = NoteUser(1, heading, body, t)
        operations.write(a)
    if len(data) > 0:
        listS = data.split("\n")
        listS = list(filter(None, listS))
        listS = [list(filter(None, i.split(";"))) for i in listS]
        numb = int(listS[len(listS) - 1][0]) + 1
        a = NoteUser(numb, heading, body, t)
        operations.write(a)










