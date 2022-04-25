import pickle

class Rod:

    def __init__(self,name):
        self.name=name
        self.surname=None
        self.middle_name=None
        self.date_of_birth=None
        self.papa = None
        self.mama = None
        self.spouse = None
        self.child = None
        self.sex=None



    def __str__(self):
        return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex}")


    def main_prov(self):
        if (self.papa is None) and (self.mama is None) and (self.spouse is None):
            return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:-,Мама:-,Супруг:-")

        elif (self.papa is None) and (self.mama is None):
            return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:-,Мама:-,Супруг:{self.spouse.name}")

        elif (self.mama is None):
            return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:{self.papa.name},Мама:-,Супруг:{self.spouse.name}")

        elif (self.spouse is None):
            return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:{self.papa.name},Мама:{self.mama.name},Супруг:-")

        elif (self.papa is None):
            return (f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:-,Мама:{self.mama.name},Супруг:{self.spouse.name}")

        else:
            return ((f"Имя:{self.name},Фамилия:{self.surname},Отчество:{self.middle_name},Дата рождения:{self.date_of_birth},Пол:{self.sex},Отец:{self.papa.name},Мама:{self.mama.name},Супруг:{self.spouse.name}"))







