import requests
from bs4 import BeautifulSoup


def main():
    url = input("Enter URL: ")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    print(f"\nPage title: {soup.title.text}\n")

    quotes = soup.find_all("span", class_="text")

    print(f"Found {len(quotes)} quotes:\n")

    for index, quote in enumerate(quotes, start=1):
        print(f"{index}. {quote.text}")
        print("-" * 60)


if __name__ == "__main__":
    main()