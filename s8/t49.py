"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной

"""
# если поставить r перед стройкой, то будет сырая строка
file_path = r'folder\new_text.txt'
file_path = r'new_text.txt'
f = open(file_path, 'w')
f.write('Hello, world!')
f.close()

# with сам закрывает файл
file_path = r'python_lectures\s8\new_text.txt'
with open(file_path, 'w') as f1:
    f1.write("Hello, my friend!")

# справочник
# меню программы
def menu():
    print('Нажми что требуется по кнопке: \n ')
    print('1. Все контакты\n')
    print('2. Найти контакт\n')
    print('3. Добавить контакт\n')
    print('0. Выход\n')

def main():
    print("Телефонный справочник!!!\n")
    file_path = r'python_lectures\s8\phonebook.txt'
    menu()
    key_input = int(input('Введите цифру: '))
    while(key_input != 0):
        if key_input == 1:
            read_phonebook(file_path)
        elif key_input == 2:
            find_by_substring(file_path, input('Введи контакт: '))
        elif key_input == 3:
            add_contact(file_path)
        print("Хотите узнать что-то еще?")
        menu()
        key_input = int(input("Введите цифру: "))
    print('До свидания!')

# вывод справочника
def read_phonebook(file):
    with open(file, 'r', encoding="utf-8") as pb:
        for line in pb:
            print(line)
    print()

# найти контакт по введенным данным
def find_by_substring(file, substring):
    with open(file, 'r', encoding="utf-8") as pb:
        is_found = False
        for line in pb:
            if substring.lower() in line.lower():
                print(line)
                is_found = True
        if not is_found:
            print("Контакт не найден")         
    print()

# создать список из справочника
def create_list_phonebook(file):
    phonebook = {}
    with open(file, 'r', encoding="utf-8") as pb:
        for line in pb:
            lst = line.split()
            key_dic = lst[0]
            data_dic = [lst[i] for i in range(1, len(lst))]
            phonebook[key_dic] = data_dic
    return phonebook
            

# добавление контакта
def add_contact(file):
    pb = create_list_phonebook(file)
    contact = []
    sirname = contact.append(input("Введи Фамилию контакта: "))
    name = contact.append(input("Введи Имя контакта: "))
    secondname = contact.append(input("Введи Отчество контакта: "))
    number = contact.append(input("Введи Номер контакта: "))
    id = len(pb) + 1
    pb[id] = contact
    with open(file, 'w', encoding="utf-8") as f:
        for (k,v) in pb.items():
            data = " ".join(v)
            f.write(f'{k} ' + data + '\n')
        

main()
# file_path = r'python_lectures\s8\phonebook.txt'
# print(create_list(file_path))
# add_contact(file_path)