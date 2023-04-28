import datetime


class NoteUser:
    def __init__(self, id: int, heading: str, body: str, time: datetime):
        self.__id = id
        self.__heading = heading
        self.__body = body
        self.__time = time

    def getId(self):
        return self.__id

    def getHeading(self):
        return self.__heading

    def getBody(self):
        return self.__body

    def getTime(self):
        return self.__time

    def setId(self, id: int):
        self.__id = id

    def setHeading(self, heading: str):
        self.__heading = heading

    def setBody(self, body: str):
        self.__body = body

    def setTime(self, time: datetime):
        self.__time = time


