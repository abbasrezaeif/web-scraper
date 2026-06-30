import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    quote_blocks = soup.find_all("div", class_="quote")

    for block in quote_blocks:
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text

        tags = block.find_all("a", class_="tag")
        tag_list = []

        for tag in tags:
            tag_list.append(tag.text)

        quotes_data.append([
            quote,
            author,
            ", ".join(tag_list)
        ])

    next_button = soup.find("li", class_="next")

    if next_button:
        next_url = next_button.find("a")["href"]
        next_url = urljoin(url, next_url)
    else:
        next_url = None

    return quotes_data, next_url


def save_to_csv(quotes_data):
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Quote", "Author", "Tags"])

        for row in quotes_data:
            writer.writerow(row)


def main():
    url = input("Enter URL: ")

    all_quotes = []

    while url:
        print(f"Scraping: {url}")

        quotes_data, next_url = scrape_page(url)

        all_quotes.extend(quotes_data)

        url = next_url

    save_to_csv(all_quotes)

    print(f"\nDone. {len(all_quotes)} quotes saved to quotes.csv")


if __name__ == "__main__":
    main()