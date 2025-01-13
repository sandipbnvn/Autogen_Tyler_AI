# filename: top_indian_companies.py
import requests
from bs4 import BeautifulSoup

url = 'https://www.moneycontrol.com/stocks/marketinfo/marketcap/biggest-companies-in-india.html'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

companies = []
table = soup.find('table', {'class': 'tblbig'})  # Assuming the table of interest

# Find and parse each row in the table
for row in table.find_all('tr')[1:11]:  # Skip the header and take the first 10 companies
    cols = row.find_all('td')
    if len(cols) >= 3:  # Check that there are enough columns for name and revenue
        name = cols[1].text.strip()
        revenue = cols[2].text.strip()  # Adjusted index for revenue
        companies.append((name, revenue))

for idx, (name, revenue) in enumerate(companies):
    print(f"{idx + 1}. {name} - Revenue: {revenue}")