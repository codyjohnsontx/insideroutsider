import requests
from bs4 import BeautifulSoup
import csv

def save_to_csv(rows, filename):
    ####overwrite with 'w' everytime I call the function###
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Stock Name', 'Transaction Type', 'Amount', 'Politician', 'Transaction Date', 'Filing Date'])

        for row in rows:
            cells = row.find_all('td')

            stock = cells[0].text.strip()
            transaction_type = cells[1].find_all('span')[0].text.strip() 
            amount = cells[1].find_all('span')[1].text.strip()  
            politician = cells[2].text.strip()
            transaction_date = cells[3].text.strip()
            filing_date = cells[4].text.strip()

            writer.writerow([stock, transaction_type, amount, politician, transaction_date, filing_date])

#Semiconductor requests###
#AMD###
amdRes = requests.get('https://www.quiverquant.com/congresstrading/stock/amd?')
amdSoup = BeautifulSoup(amdRes.text, 'html.parser')
amdRows = amdSoup.select('tbody > tr')
save_to_csv(amdRows, 'amd_trades_data.csv')
##

#Nvidia###
nviRes = requests.get('https://www.quiverquant.com/congresstrading/stock/NVDA?')
nviSoup = BeautifulSoup(nviRes.text, 'html.parser')
nviRows = nviSoup.select('tbody > tr')
save_to_csv(nviRows, 'nvidia_trades_data.csv')
##

#Texas Instruments###
txRes = requests.get('https://www.quiverquant.com/congresstrading/stock/TXN?')
txSoup = BeautifulSoup(txRes.text, 'html.parser')
txRows = txSoup.select('tbody > tr')
save_to_csv(txRows, 'texas_instruments_trades_data.csv')
##