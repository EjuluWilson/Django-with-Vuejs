import requests
def main():
    response = requests.get("http://api.exchangeratesapi.io/latest")
    print("STATUS CODE:", response.status_code)
    print("content-type", response.headers["Content-Type"])
 

if __name__ == '__main__':
    main()
