import requests
from bs4 import BeautifulSoup


def fetch_nbc_news_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []

        for headline in soup.find_all('h2', class_='storyline__headline'):
            headlines.append(headline.get_text().strip())

        return set(headlines)

    except requests.RequestException as e:
        print(f"error {url}: {e}")
        return []
    
    
def get_last_nbc_news():
    url = 'https://www.nbcnews.com/'
    return fetch_nbc_news_headlines(url)
