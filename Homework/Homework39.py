import json


class Country:
    dict_data_country = dict()

    @staticmethod
    def adding_data(country, town, file_name):
        Country.dict_data_country[country.strip()] = town.strip()
        with open(file_name, "w", encoding='utf-8') as f:
            json.dump(Country.dict_data_country, f, ensure_ascii=False, indent=4)
        print("Данные сохранены в файл")

    @staticmethod
    def delete_data(country, file_name):
        try:
            del Country.dict_data_country[country]
            print(f"Ключ с именем '{country}' удален")
            with open(file_name, "w", encoding='utf-8') as f:
                json.dump(Country.dict_data_country, f, ensure_ascii=False, indent=4)
        except KeyError:
            print("Данные нельзя удалить, так как они не существуют")

    @staticmethod
    def search_data(country):
        try:
            print(Country.dict_data_country[country])
        except KeyError:
            print("Таких данных не существует")

    @staticmethod
    def editing_data(country, town, file_name):
        keys = Country.dict_data_country.keys()
        if country in keys:
            Country.dict_data_country[country] = town.strip()
            with open(file_name, "w", encoding='utf-8') as f:
                json.dump(Country.dict_data_country, f, ensure_ascii=False, indent=4)
            print("Данные отредактированы")
        else:
            print("Данные которые вы хотите отредактировать не существуют")

    @staticmethod
    def view_data():
        if Country.dict_data_country:
            print(Country.dict_data_country)
        else:
            print("Данные отсутствуют")

    @staticmethod
    def value_examination(data):
        for i in data:
            if i.isdigit():
                return True
        return False


print("*" * 30)
while True:
    file_name_js = input("Введите название вашего нового файла в формате JSON: ")
    if file_name_js.endswith(".json") and len(file_name_js) > 5:
        break
    else:
        print("Файл должен быть с именем и в формате JSON")
        continue
print("*" * 30)

while True:
    print()
    print("Выбор действия:\n1 -добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n"
          "5 - просмотр данных\nЛюбые другие целые числа приведут к завершению работы!")
    num = input("Ввод: ")
    try:
        num = int(num)
    except ValueError:
        print("Вводите только целые числа!")
        continue
    if num == 1:
        name_country = input("Введите название страны (с заглавной буквы): ")
        name_town = input("Введите название столицы страны (с заглавной буквы): ")
        if Country.value_examination(name_country) or Country.value_examination(name_town):
            print("Данные должны быть корректные")
            continue
        elif not name_country or not name_town:
            print("Данные должны быть корректные")
            continue
        Country.adding_data(name_country, name_town, file_name_js)
        print("*" * 30)
    elif num == 2:
        name_delete = input("Введите название страны которую желаете удалить: ")
        Country.delete_data(name_delete, file_name_js)
        print("*" * 30)
    elif num == 3:
        name_search = input("Введите название страны которую желаете найти в ваших данных: ")
        Country.search_data(name_search)
        print("*" * 30)
    elif num == 4:
        name_editing_country = input("Введите название страны которую желаете отредактировать: ")
        name_editing_town = input("Введите новое название города: ")
        Country.editing_data(name_editing_country, name_editing_town, file_name_js)
        print("*" * 30)
    elif num == 5:
        Country.view_data()
        print("*" * 30)
    else:
        print("Программа завершена")
        print("Файл с вашими данными готов.")
        break
