import requests
from bs4 import BeautifulSoup

def fetch_topic_resource(topic):
    query = f"gfg {topic}"
    search_url = f"https://www.google.com/search?q={query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    first_result = soup.find('div', class_='tF2Cxc')
    
    if first_result:
        link = first_result.find('a')['href']
        return f"Resource link:\n{link}"
    return "Unable to fetch resource link."