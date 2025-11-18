import requests
from bs4 import BeautifulSoup
import re
from transformers import pipeline

class search():

    def __init__(self, url:str):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers = headers, timeout=10)
        if response.status_code > 300:
            self.content = None
            print("error")
            print(response.status_code)
        else:
            self.stuff = response.text

    def data_extraction(self, content):
        full_date_pattern = r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4})\b'
        soup = BeautifulSoup(content, 'html.parser')
        main_area = soup.find('div', id = 'bodyContent') #fill with tag and class in html search up
        paragraphs = main_area.find_all('p')
        for para in paragraphs:
            text = para.get_text(" ",strip=True)
            full_dates = re.findall(full_date_pattern, text)
            print(full_dates)

    def names_extraction(self,content):
        ner = pipeline("token-classification",model = "dslim/bert-base-NER", aggregation_strategy="simple")
        soup = BeautifulSoup(content,'html.parser' )
        text = soup.get_text(separator=" ", strip = True)
        entities = ner(text)
        person_names = [ent["word"] for ent in entities if ent["entity_group"] == "PER"]
        print(person_names)
        

    def start(self):
        #self.data_extraction(self.stuff)
        self.names_extraction(self.stuff)

