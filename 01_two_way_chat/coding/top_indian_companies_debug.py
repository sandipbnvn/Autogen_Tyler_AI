# filename: top_indian_companies_debug.py
import requests
from bs4 import BeautifulSoup

url = 'https://www.moneycontrol.com/stocks/marketinfo/marketcap/biggest-companies-in-india.html'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Print the soup content to inspect its structure with encoding handling
print(soup.encode('utf-8').decode('utf-8'))