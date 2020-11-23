import requests
from bs4 import BeautifulSoup

headers = {
    "Referer": "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

titles = []
for page in range(1, 3):
    url = f'https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176/page-{page}.ajax?limit=1000'
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser").find_all("li", {"class": "elpo-item"})
    titles.extend(i.find("h2").getText().strip('\n') for i in soup)


def sort_by_date(titles):
    with open('Meilleurs films français.txt', 'w') as ftw:
        final_list = [x.replace('(', '').replace(')', '').split('\n') for x in titles]
        final_list.sort(key=lambda a:a[1])
        ftw.writelines(str(final_list).split(','))
    print(str(final_list).strip())


sort_by_date(set(titles))