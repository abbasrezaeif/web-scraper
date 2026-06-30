import requests
from bs4 import BeautifulSoup


def main():
    url = input("Enter URL: ")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"\nPage title: {soup.title.text}\n")

    quote_blocks = soup.find_all("div", class_="quote")

    print(f"Found {len(quote_blocks)} quotes:\n")

    for index, block in enumerate(quote_blocks, start=1):
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text

        print(f"{index}. {quote}")
        print(f"Author: {author}")
        print("-" * 60)


if __name__ == "__main__":
    main()