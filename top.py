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
    
    file.write(f"{index}.  {columns[5].find('span').text}, {columns[6].find('span').text}\n")

    # print(f"{columns[3].find('a', {'class': 'site_title'}).text} ({columns[3].find('a', {'class': 'cat_name_list'}).text}") ამ კონსტრუქციით ვცდილობდი საიტის სახელზე წვდომას

    if index > 20:
        break 
file.close()  

print("მონაცემები წარმატებით ჩაიწერა ფაილში!")