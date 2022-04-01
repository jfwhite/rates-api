import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('rates.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS rates')
cursor.execute('CREATE TABLE rates (date text, libor real, sofr real)')

response = requests.get('https://www.pensford.com/resources/forward-curve')
soup = BeautifulSoup(response.text, 'html.parser')
for row in soup.table.tbody.find_all('tr'):
    date, libor, _, sofr = [tag.string for tag in row.find_all('td')]
    month, day, year = date.split('/')
    month = month if len(month) == 2 else "0"+month
    date = f"{year}-{month}-{day}"
    libor = float(libor.replace("%", "")) / 100
    sofr = float(sofr.replace("%","")) / 100
    cursor.execute(f"INSERT INTO rates VALUES ('{date}','{libor}','{sofr}')")

connection.commit()
connection.close()

