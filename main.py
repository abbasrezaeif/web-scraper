import requests
from bs4 import BeautifulSoup


def main():
    url = input("Enter URL: ")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    print(f"\nPage title: {title}\n")

    first_quote = soup.find("span", class_="text")

    print("First Quote:")
    print(first_quote.text)


if __name__ == "__main__":
    main()