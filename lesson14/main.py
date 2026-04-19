import requests
import csv
from bs4 import BeautifulSoup


def get_parsed_data(html_content: bytes) -> list:
    soup = BeautifulSoup(html_content, "html.parser")
    books_list = []
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="instock availability").text.strip()
        books_list.append([title, price, rating, availability])
    return books_list


def parser(url: str) -> None:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            books_list = get_parsed_data(response.content)
            with open('books.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Книга', 'Ціна', 'Рейтинг', 'Наявність'])
                writer.writerows(books_list)
        elif response.status_code in [404, 500]:
            print(f"Помилка {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    parser("http://books.toscrape.com/")
