import requests
def main():
    response = requests.get("http://www.google.com")
    print("STATUS CODE:", response.status_code)
    print("HEADERS:", response.headers)
    print("CONTENT:", response.text)

if __name__ == '__main__':
    main()
