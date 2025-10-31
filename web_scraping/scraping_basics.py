
#### Пример содержимого файлов:

##### `scraping_basics.py`
```python
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.text.strip())

if __name__ == "__main__":
    scrape_website("https://example.com")