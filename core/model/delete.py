from core.model import operations


def delNote(a: int):
    text = str(a) + ";"
    pathfile = "Notes.csv"
    with open(pathfile, 'r') as file:
        data = file.readlines()
    with open(pathfile, 'w') as file:
        for line in data:
            if text not in line.strip("\n"):
                file.write(line)

