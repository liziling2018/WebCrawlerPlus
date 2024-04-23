import requests
from bs4 import BeautifulSoup
import csv
from config import URL, DATA, MAX_PAGES, OUTPUT_FILE

def extract_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    extracted_data = {}

    for key, value in DATA.items():
        selector = value['selector']
        attribute = value['attribute']
        elements = soup.select(selector)
        if elements:
            extracted_data[key] = [element.get(attribute) for element in elements]
        else:
            extracted_data[key] = []

    return extracted_data

def crawl():
    pages_crawled = 0
    extracted_data = []

    while pages_crawled < MAX_PAGES:
        response = requests.get(f'{URL}/page/{pages_crawled + 1}')
        if response.status_code == 200:
            data = extract_data(response.content)
            extracted_data.extend(list(zip(*data.values())))
            pages_crawled += 1
        else:
            break

    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(DATA.keys())
        writer.writerows(extracted_data)

    print(f'Crawling completed. Extracted data saved to {OUTPUT_FILE}.')

if __name__ == '__main__':
    crawl()
