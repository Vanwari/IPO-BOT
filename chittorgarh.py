import requests
from bs4 import BeautifulSoup
URL='https://www.chittorgarh.com/ipo/ipo_dashboard.asp'
def get_mainboard_ipos():
    html=requests.get(URL,headers={'User-Agent':'Mozilla/5.0'},timeout=30).text
    soup=BeautifulSoup(html,'html.parser'); results=[]
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            cells=[c.get_text(' ',strip=True) for c in row.find_all(['th','td'])]
            if cells: results.append(cells)
    return results
