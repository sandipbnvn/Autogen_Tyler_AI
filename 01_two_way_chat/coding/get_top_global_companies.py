# filename: get_top_global_companies.py
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the appropriate table
table = soup.find('table', {'class': 'wikitable'})

# Collect the top 10 global companies
top_companies = []
for row in table.find_all('tr')[1:11]:  # Skip the header
    cols = row.find_all('td')
    company_name = cols[1].text.strip()
    revenue = cols[2].text.strip()
    top_companies.append((company_name, revenue))

# Print the result
for idx, (name, revenue) in enumerate(top_companies, start=1):
    print(f"{idx}: {name} - Revenue: {revenue}")