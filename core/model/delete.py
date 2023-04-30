from core.model import operations


def delNote(a: int):
    text = str(a) + ";"
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    if len(data) == 0:
        print("Операция не может быть выполнена. Отстутствуют записи.\n")
        return
    if len(data) > 0:
        answer = False
        for i in data:
            if text in i:
                answer = True
        if not answer:
            print("Операция преравана. Отсутствует значение.\n")
            return
    listS = list(filter(None, data))
    listS = [list(filter(None, i.split(";"))) for i in listS]
    with open(pathfile, 'w') as file:
        for line in range(len(listS)):
            if a != listS[line][0]:
                file.write('{};{};{};{}'.format(listS[line][0], listS[line][1], listS[line][2],
                                                  listS[line][3]))
    print("Запись удалена.")
