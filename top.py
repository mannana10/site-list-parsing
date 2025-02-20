import requests
from bs4 import BeautifulSoup


URL = "https://top.ge/"

req = requests.get(URL)

soup = BeautifulSoup(req.content, "html.parser")

table = soup.find("tbody")

rows = table.find_all("tr")

file = open("საიტები.txt", "w", encoding = "utf-8")

for index, row in enumerate(rows, 1):
    columns = row.find_all("td")

    site_data = columns[2].find_all("a")

    file.write(f"{index}. {site_data[0].text} - {site_data[1].text.strip()} - {columns[5].find('span').text} - {columns[6].find('span').text}\n")

    if index > 20:
        break

file.close() 
 
print("მონაცემები წარმატებით ჩაიწერა ფაილში!")