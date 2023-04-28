def write(object):
    pathFile = "Notes.csv"
    with open(pathFile, 'a') as file:
        file.writelines('{};{};{};{}\n'.format(object.getId(), object.getHeading(), object.getBody(), object.getTime()))

def reader():
    pathFile = "Notes.csv"
    data = ""
    with open(pathFile, 'r') as file:
        data = file.read()
    return data

