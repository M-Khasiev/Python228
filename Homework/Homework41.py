from bs4 import BeautifulSoup
import requests
import csv
import re


def pars(url):
    soup = BeautifulSoup(url, "lxml")
    name = soup.find_all("article", class_='card d-flex')
    for tag in name:
        try:
            name_cinema = tag.find("h2", class_='card__title').find("a").text
            year_issue = tag.find("ul", class_="card__list").find("li").find("a").text
            duration = tag.find("ul", class_="card__list").find_all("li")[1].text
            duration = re.sub(r"[А-я]+:\s+", "", duration)
            country = tag.find("ul", class_="card__list").find_all("li")[3].find('a').text
            genre = tag.find("ul", class_="card__list").find_all("li")[4].find_all('a')
            director = tag.find("ul", class_="card__list").find_all("li")[9].text
            director = re.sub(r'[А-я]+:', "", director)
            link = tag.find("h2", class_='card__title').find("a").get("href")
            print(f"{name_cinema} - {year_issue} - {duration} - {country} - {genre[1].text} - {director} - {link}")
            with open("cinema.csv", 'a') as f:
                writer = csv.writer(f, delimiter=";", lineterminator='\r')
                writer.writerow([name_cinema.strip(), duration.strip(), year_issue.strip(), country.strip(),
                                 genre[1].text.strip(), director.strip(), link])
        except AttributeError:
            continue


def website():
    for i in range(1, 6):
        html = requests.get(f'https://redheadsound.ru/page/{i}/').text
        pars(html)


if __name__ == "__main__":
    with open("cinema.csv", 'w') as f:
        writer = csv.writer(f, delimiter=";", lineterminator='\r')
        writer.writerow(['Название фильма', 'Продолжительность', 'Год выпуска', 'Страна', 'Жанр', 'Режиссёр', 'Ссылка'])
    website()
