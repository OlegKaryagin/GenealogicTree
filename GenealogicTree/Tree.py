import  pickle
import os
from Genealogiya import Rod



def main():



        if input('Введите Вход')=='Вход':
            exit = 1
            while exit != 0:
                print('Чтобы узнать команды введите "Список команд"')
                command=input()
                if command=='Добавить начального человека':
                    people=Rod(input('Введите Имя '))
                    people.middle_name=input('Введите Отчество ')
                    people.surname=input('Введите Фамилию ')
                    people.date_of_birth=input('Введите Дату рождения ')
                    people.sex=input('Введите пол ')
                elif command=='Добавить отца':
                    people.papa=Rod(input('Введите Имя '))
                    people.papa.child=people
                    people.papa.middle_name = input('Введите Отчество ')
                    people.papa.surname = input('Введите Фамилию ')
                    people.papa.date_of_birth = input('Введите Дату рождения ')
                    people.sex = input('Введите пол ')
                    if (people.mama is not None) and (people.papa.spouse is None):
                        people.papa.spouse=people.mama
                        people.mama.spouse=people.papa
                elif command=='Добавить мать':
                    people.mama = Rod(input('Введите Имя '))
                    people.mama.child = people
                    people.mama.middle_name = input('Введите Отчество ')
                    people.mama.surname = input('Введите Фамилию ')
                    people.mama.date_of_birth = input('Введите Дату рождения ')
                    people.sex = input('Введите пол ')
                    if (people.papa is not None) and (people.mama.spouse is None):
                        people.papa.spouse=people.mama
                        people.mama.spouse=people.papa
                elif command == 'Проверка позиции в дереве':
                    print(people.main_prov())
                elif command == 'Добавить ребенка':
                    people.child=Rod(input('Введите имя '))
                    people.child.papa=people
                    people.child.middle_name = input('Введите Отчество ')
                    people.child.surname=input('Введите Фамилию ')
                    people.child.date_of_birth = input('Введите Дату рождения ')
                    people.sex = input('Введите пол ')
                    if people.spouse is not None:
                        people.child.mama=people.spouse
                elif command=='Шаг на отца':
                    people=people.papa
                elif command=='Шаг на мать':
                    people=people.mama
                elif command=='Шаг на жену':
                    people=people.spouse
                elif command=='Шаг на ребенка':
                    people=people.child
                elif command=='Добавить жену':
                    people.spouse=Rod(input('Введите Имя '))
                    people.spouse.surname=input('Введите Фамилию ')
                    people.spouse.middle_name=input('Введите Отчество ')
                    people.spouse.date_of_birth=input('Введите дату рождения ')
                    people.sex = input('Введите пол ')
                    people.spouse.spouse=people
                    if people.child is not None:
                        people.child.mama=people.spouse
                elif command == 'Выход':
                    exit = 0
                elif command == 'Сохранение':
                    the_save_name=input('Введите имя файла для сохранения " ')
                    output1=open(the_save_name,'wb')
                    pickle.dump(people,output1,2)
                    output1.close()
                elif command == 'Загрузка':
                    directory=os.getcwd()
                    file_list=os.listdir(directory)
                    print('Список файлов:',file_list)
                    the_save_name = input('Введите имя файла для загрузки ')
                    input1=open(the_save_name,'rb')
                    people = pickle.load(input1)
                    input1.close()
                elif command == 'Поиск':
                    while people.child:
                        people = people.child
                    family = []
                    prov = set()
                    family.append(people)
                    prov.add(people)
                    end = 1
                    while end != 0:
                        if (people.papa not in prov) and (people.papa is not None):
                            people=people.papa
                            family.append(people)
                            prov.add(people)
                        elif (people.mama not in prov) and (people.mama is not None):
                            people = people.mama
                            family.append(people)
                            prov.add(people)
                        elif (people.papa is None) or (people.mama is None):
                            people = people.child
                        elif (people.spouse) and (people.spouse not in prov) and (people.child is None):
                            people = people.spouse
                            family.append(people)
                            prov.add(people)
                        elif (people.papa in prov) and (people.mama in prov):
                            if people.child:
                                people = people.child
                            else: end = 0
                    print('Введите "По фамилии", если хотите искать человека по фамилии. Введите "По полу", если хотите искать человека по полу.')
                    command=input('')
                    if command == 'По фамилии':
                        second_name=input('Введите фамилию ')
                        wm='а'
                        for j in range(len(family)):
                            if family[j].surname==second_name:
                                people = family[j]
                                print(people.main_prov())
                        for j in range(len(family)):
                            if family[j].surname==(second_name+wm):
                                people = family[j]
                                print(people.main_prov())
                    if command == 'По полу':
                        find_sex = input('Введите пол ')
                        for j in range(len(family)):
                            if family[j].sex==find_sex:
                                people = family[j]
                                print(people.main_prov())
                elif command == 'Изменить':
                    print('Введите "Имя", для изменения фамилии')
                    print('Введите "Фамилия", для изменения фамилии')
                    print('Введите "Отчество", для изменения фамилии')
                    print('Введите "Дата рождения", для изменения фамилии')
                    print('Введите "Пол", для изменения фамилии')
                    command=input()
                    if command == 'Имя':
                        people.name=input('Введите имя ')
                    if command == 'Фамилия':
                        people.surname=input('Введите фамилию ')
                    if command == 'Отчество':
                        people.middle_name=input('Введите отчество ')
                    if command == 'Дата рождения':
                        people.date_of_birth=input('Введите дату рождения ')
                    if command == 'Пол':
                        people.sex=input('Введите пол ')
                elif command == 'Вывод ':
                    while people.child:
                        people = people.child
                    family = []
                    prov = set()
                    family.append(people)
                    prov.add(people)
                    end=1
                    while end!=0:
                        if (people.papa not in prov) and (people.papa is not None):
                            people=people.papa
                            family.append(people)
                            prov.add(people)
                        elif (people.mama not in prov) and (people.mama is not None):
                            people = people.mama
                            family.append(people)
                            prov.add(people)
                        elif (people.papa is None) or (people.mama is None):
                            people = people.child
                        elif (people.spouse) and (people.spouse not in prov) and (people.child is None):
                            people = people.spouse
                            family.append(people)
                            prov.add(people)
                        elif (people.papa in prov) and (people.mama in prov):
                            if people.child :
                                people = people.child
                            else:end=0
                    while family:
                        people = family.pop()
                        print(people.main_prov())
                elif command == 'Список команд':
                    print(''' 
                    Добавить начального человека
                    Добавить отца
                    Добавить мать
                    Добавить жену
                    Добавить ребенка
                    Сохранение
                    Загрузка
                    Поиск
                    Вывод
                    Проверка позиции в дереве
                    Шаг на отца
                    Шаг на мать
                    Шаг на жену
                    Шаг на ребенка
                    Изменить
                    Выход''')





main()