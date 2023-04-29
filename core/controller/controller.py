from core.model.inputUser import Input
from core.model import add
from core.model import operations
from core.model import delete
from core.model import changeNote
from core.model import explorer
from core.view import out



def start():
    end = True
    while end == True:
        numb = Input.input("Введите команду:\n1 - добавить заметку\n2 - редактировать заметку\n3 - удалить заметку\n"
                           "4 - сделать выборку заметок по дате\n5 - вывести полный список заметок\n"
                           "6 - закончить работу программы.\n")
        if numb == "1":
            add.add()
        if numb == "2":
            r = Input.input("Укажите номер изменяемой заметки по id:\n")
            changeNote.change(r)
        if numb == "3":
            d = Input.input("Укажите номер удаляемой заметки по id:\n")
            delete.delNote(d)
        if numb == "4":
            data = explorer.explorer()
            out.out(data)
        if numb == "5":
            data = operations.reader()
            out.out(data)
        if numb == "6":
            end = False
        if numb != "1" and numb != "2" and numb != "3" and numb != "4" and numb != "5" and numb != "6":
            print("Вы ввели неверное значение\n")




