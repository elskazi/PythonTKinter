from bs4 import BeautifulSoup
import urllib.request # не работает
import requests

class Parser:
    raw_html = ""
    html = ""
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        #req = urllib.request.urlopen(self.url) # не работает
        #self.raw_html=req.read()
        url = self.url
        self.raw_html = requests.get(url)
        self.html = BeautifulSoup(self.raw_html.text, "html.parser") # .text - обязантельно

    def parsing(self):
        news = self.html.find_all("article", class_="post mb-2")
        for item in news:
            desc = item.find("div", class_="btn").get_text()
            # print(desc)
            title = item.find("div", class_="text-color-dark").get_text(strip=True)
            # print(title)
            href = item.a.get('href')
            # print(href)
            self.results.append({
                'desc': desc,
                'title': title,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nВремя: {item["desc"]}\nНазвание: {item["title"]}\n'
                        f'Ссылка: {item["href"]}\n****************\n\n ')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()




