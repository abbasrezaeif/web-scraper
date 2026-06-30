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

        writer.writerow([
            "Quote",
            "Author",
            "Tags"
        ])

        for block in quote_blocks:

            quote = block.find("span", class_="text").text
            author = block.find("small", class_="author").text

            tags = block.find_all("a", class_="tag")

            tag_list = []

            for tag in tags:
                tag_list.append(tag.text)

            writer.writerow([
                quote,
                author,
                ", ".join(tag_list)
            ])

    print("quotes.csv created successfully.")


if __name__ == "__main__":
    main()