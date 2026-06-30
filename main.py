import csv
import requests
from bs4 import BeautifulSoup


def main():
    url = input("Enter URL: ")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Quote", "Author"])

        for block in quote_blocks:

            quote = block.find("span", class_="text").text
            author = block.find("small", class_="author").text

            writer.writerow([quote, author])

    print("quotes.csv created successfully.")


if __name__ == "__main__":
    main()