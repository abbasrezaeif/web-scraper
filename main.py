import requests


def main():
    url = input("Enter URL: ")

    response = requests.get(url)

    print(response.status_code)


if __name__ == "__main__":
    main()