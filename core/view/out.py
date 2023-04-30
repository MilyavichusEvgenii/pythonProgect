from core.model.inputUser import Input


def out(text: str):
    listText = list(filter(None, text.split("\n")))
    listText = [list(filter(None, i.split(";"))) for i in listText]
    value = len(listText)
    params = value // 5
    page = 1
    app = 0
    c = 5
    end = True
    if value % 5 > 0:
        params = params + 1
    while end == True:
        if len(listText) <= 5:
            print("ID TITLE TEXT  TIME {} из {}".format(page, params))
            for i in range(0, len(listText)):
                print("{}  {}  {}  {}".format(listText[i][0], listText[i][1], listText[i][2], listText[i][3]))
                stap = Input.input("Нажмите 'e' чтоб выйти.\n")
                if stap == 'e':
                    end = False
        if len(listText) > 5:
            print("ID TITLE TEXT  TIME {} из {}".format(page, params))
            for i in range(0 + app, c):
                print("{}  {}  {}  {}".format(listText[i][0], listText[i][1], listText[i][2], listText[i][3]))
            stap = Input.input("Перевернуть страницу вперед '+'\nперевернуть назад страницу '-':\n"
                            "выйти из списка 'e'\n")
            if stap == "+":
                if page == params - 1:
                    page = page + 1
                    app = len(listText) - 5
                    c = len(listText)
                elif page < params - 1:
                    page = page + 1
                    app = app + 5
                    c = c + 5
            if stap == "-":
                if page == 1:
                    app = 0
                    c = 5
                elif page == params:
                    page = page - 1
                    app = app - 5
                    c = c - 1
                elif page < params:
                    page = page - 1
                    app = app - 5
                    c = c - 5
            if stap == 'e':
                end = False



