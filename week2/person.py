# class person

class person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age