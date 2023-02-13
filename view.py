def decorator_method(ar):
    def accepts_method(fn):
        def arguments_method(*args, **kwargs):
            print(ar.center(50, "="))
            f = fn(*args, **kwargs)
            print("=" * 50)
            return f

        return arguments_method

    return accepts_method


class UserInterface:
    @decorator_method(" Ввод пользовательских данных ")
    def wait_user_answer(self):
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\n3 - просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")

        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @decorator_method(" Создание статьи ")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        return dict_article

    @decorator_method(" Список статей: ")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")
