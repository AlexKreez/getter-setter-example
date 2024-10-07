class School:
    def __init__(self, name, level, NumberOfStudents):
        self.name = name
        self.level = level
        self.NumberOfStudents = NumberOfStudents


    @property
    def getName(self):
        return self._name

    @getName.setter
    def getName(self, name):
        self._name = name

    @property
    def getLevel(self):
        return self._level

    @getLevel.setter
    def getLevel(self, level):
        self._level = level

    @property
    def getNumb(self):
        return self._NumberOfStudents

    @getNumb.setter
    def getNumb(self, NumberOfStudents):
        self._NumberOfStudents = NumberOfStudents

    def __repr__(self):
        return  f"Имя школы:{self.name}, Номер школы: {self.level}, Количество учеников:{self.NumberOfStudents}"



class PrimarySchool(School):
    def __init__(self, name, level, NumberOfStudents, PickUpPolicy):
        super().__init__(name, level, NumberOfStudents)
        self.PickUpPolicy = PickUpPolicy

    @property
    def getPUP(self):
        return self._PickUpPolicy

    @getPUP.setter
    def getPUP(self, PickUpPolicy):
        self._PickUpPolicy = PickUpPolicy

    def __repr__(self):
        return f"{ super().__repr__()}, PickUpPolicy:{self.PickUpPolicy}"

school2 = PrimarySchool('№1', 377, 100, '4pm')
print(school2)

