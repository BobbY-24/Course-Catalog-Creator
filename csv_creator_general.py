import json
from bs4 import BeautifulSoup
import re
import requests
import csv
def csv_creator(source, csv_name):
    soup = requests.get(source).text
    soup = BeautifulSoup(soup, 'html.parser')
 
    res = soup.find_all('strong')

    final = []
    res2 = soup.find_all(class_ = 'courseblockdesc')
    print('Info collected')


    i=0
    for combo in res:
        name = re.search(r'([A-Z]{2,4}.+?)\.', combo.text).group()[:-1]
        name = name.split()[0]+'_'+name.split()[1]
        
        credit = combo.text[-15]
        if not credit.isnumeric():
            credit = 1
        des = re.search(r'\s([A-Z].+?\.)\s', combo.text).group()[1:-2]
    
        des2 = res2[i].text[1:-2]
        final.append(list([name,credit,des,des2]))
        i+=1

    print('Data stored')
    

    with open('output.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['class_code', 'credit_hours', 'official_name', 'description'])
        writer.writerows(final)
        print('File created')
        import os

    old_file_name = "output.csv"
    new_file_name = f"{csv_name}.csv"

    try:
        os.rename(old_file_name, new_file_name)
        print(f"File '{old_file_name}' successfully renamed to '{new_file_name}'.")
    except FileNotFoundError:
        print(f"Error: The file '{old_file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


