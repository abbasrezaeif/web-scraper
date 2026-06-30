import requests
from bs4 import BeautifulSoup


def main():
    url = input("Enter URL: ")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    print(f"Page title: {title}")


if __name__ == "__main__":
    main()