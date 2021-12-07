from bs4 import BeautifulSoup
import urllib.request
import requests
# так не запускается urllib.request
#url = urllib.request.urlopen('https://mignews.com')
# page = url.read()  #
# soup = BeautifulSoup(page, "html.parser")


url = 'https://mignews.com/'
page = requests.get(url)
#print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")  # .text - обязантельно
print(soup)
news = soup.find_all("article", class_="post mb-2" ) # класс с подчеркиванием
#print(news)
results = []
for item in news:
    desc = item.find("div", class_="btn").get_text()
    #print(desc)
    title = item.find("div", class_="text-color-dark").get_text(strip=True)
    #print(title)
    href = item.a.get('href')
    #print(href)
    results.append({
        'desc': desc,
        'title':title,
        'href':href,
    })

print(results)

f = open("news.txt", 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nВремя: {item["desc"]}\nНазвание: {item["title"]}\n'
            f'Ссылка: {item["href"]}\n****************\n\n ')
    i += 1
f.close()

