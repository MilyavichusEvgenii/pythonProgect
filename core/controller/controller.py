from core.model.inputUser import Input
from core.model import add
from core.model import operations
from core.model import delete
from core.model import changeNote



def start():
    numb = Input.input("Введите команду: 1 - добавить заметку\n2 - редактировать заметку\n3 - удалить заметку\n"
                       "4 - вывести полный список заметок\n5 - закончить работу программы.\n")
    if numb == "1":
        add.add()
        data = operations.reader()
        print(data)
    if numb == "2":
        r = Input.input("Укажите номер изменяемой заметки по id:\n")
        changeNote.change(r)
        data = operations.reader()
        print(data)
    if numb == "3":
        d = Input.input("Укажите номер удаляемой заметки по id:\n")
        delete.delNote(d)
        data = operations.reader()
        print(data)
    if numb == "4":
        data = operations.reader()
        print(data)
    if numb == "4":
        return


