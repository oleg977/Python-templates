import requests

def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for post in data[:5]:
            print(post['title'])
    else:
        print("Ошибка при получении данных.")

if __name__ == "__main__":
    fetch_data_from_api()