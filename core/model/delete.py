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
    with open(pathfile, 'w') as file:
        for line in data:
            if text not in line.strip("\n"):
                file.write(line)
    print("Запись удалена.")
