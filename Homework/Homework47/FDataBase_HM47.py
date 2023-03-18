import sqlite3
import time
import math


class FDataBase_HM47:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из Базы Данных")
        return []

    def add_post(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в Базу Данных" + str(e))
            return False
        return True

    def get_courses(self, courses_id):
        try:
            self.__cur.execute(f"SELECT title, price, text FROM courses WHERE id = {courses_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))

        return False, False, False

    def get_courses_announce(self):
        try:
            self.__cur.execute(f"SELECT id, title, price, text FROM courses")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД" + str(e))

        return []

