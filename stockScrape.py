import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('https://www.quiverquant.com/congresstrading/')
soup = BeautifulSoup(res.text, 'html.parser')

rows = soup.select('body > main > div:nth-child(7) > div.table-inner > table > tbody')
print(rows)
with open('politician_trading_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Name', 'Number of Trades', 'Amount Traded'])

    for row in rows:
        cells = row.find_all('td')
        data = [cell.get_text(strip=True) for cell in cells]
        
        #datasets are grouped in threes, so use simple for loop process it that way
        for i in range(0, len(data), 3):
            #complete record of a politician's trading data
            record = data[i:i + 3]
            #write into CSV file
            writer.writerow(record)




