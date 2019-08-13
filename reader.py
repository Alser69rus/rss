import requests
from xml.dom.minidom import parseString
import pickle

proxy = {'https': 'https://Evdokimow:evd@pkbgate:8080', 'http': 'http://Evdokimow:evd@pkbgate:8080'}
urls = {
    'Алексеева Яна': 'http://flibusta.is/a/25256/rss/',
    'Артьемьев роман': 'http://flibusta.is/a/51654/rss/',
    'Белаш Людмила': 'http://flibusta.is/a/25830/rss/',
    'Бирюк': 'http://flibusta.is/a/119452/rss/',
    'Буревой': 'http://flibusta.is/a/37715/rss/',
    'Буджолд': 'http://flibusta.is/a/17587/rss/',
    'Вебер Дэвид': 'http://flibusta.is/a/18973/rss/',
    'Горькавый Николай': 'http://flibusta.is/a/32311/rss/',
    'Громыко': 'http://flibusta.is/a/30331/rss/',
    'Далин Макс': 'http://flibusta.is/a/53216/rss/',
    'Дивов Олег': 'http://flibusta.is/a/2526/rss/',
    'Довыдовский Кирилл': 'http://flibusta.is/a/147590/rss/',
    'Еськов Кирилл': 'http://flibusta.is/a/3150/rss/',
    'Жарковский': 'http://flibusta.is/a/27509/rss/',
    'Завацкая Яна': 'http://flibusta.is/a/13622/rss/',
    'Иванова Вероника': 'http://flibusta.is/a/5110/rss/',
    'Каменистый': 'http://flibusta.is/a/17904/rss/',
    'Ким Сергей': 'http://flibusta.is/a/70463/rss/',
    'Князев Милослав': 'http://flibusta.is/a/71790/rss/',
    'Корнев Павел': 'http://flibusta.is/a/29121/rss/',
    'Костин Константин': 'http://flibusta.is/a/79687/rss/',
    'Кош Алекс': 'http://flibusta.is/a/6300/rss/',
    'Лаарен': 'http://flibusta.is/a/152742/rss/',
    'Леки Энн': 'http://flibusta.is/a/148062/rss/',
    'Лисина Александра': 'http://flibusta.is/a/89485/rss/',
    'Лукьненко Сергей': 'http://flibusta.is/a/1801/rss/',
    'Мартыненко Всеволод': 'http://flibusta.is/a/7925/rss/',
    'Михайлов Дем': 'http://flibusta.is/a/75588/rss/',
    'Метельский Николай': 'http://flibusta.is/a/109170/rss/',
    'Мусаниф Сергей': 'http://flibusta.is/a/28816/rss/',
    'Мясоедов Владимир': 'http://flibusta.is/a/57434/rss/',
    'Ночкин Виктор': 'http://flibusta.is/a/24229/rss/',
    'Панкеева Оксана': 'http://flibusta.is/a/19750/rss/',
    'Пехов Алексей': 'http://flibusta.is/a/9438/rss/',
    'Плотников Сергей': 'http://flibusta.is/a/123080/rss/',
    'Попова Надежда': 'http://flibusta.is/a/77203/rss/',
    'Радов Алексей': 'http://flibusta.is/a/60207/rss/',
    'Ротфус Патрик': 'http://flibusta.is/a/17357/rss/',
    'Рудазов Александр': 'http://flibusta.is/a/86365/rss/',
    'Садов Сергей': 'http://flibusta.is/a/10677/rss/',
    'Сыромятникова': 'http://flibusta.is/a/37110/rss/',
    'Федотова Юлия': 'http://flibusta.is/a/73243/rss/',
    'Чешко Федор': 'http://flibusta.is/a/20782/rss/',
    'Чичин Сергей': 'http://flibusta.is/a/20758/rss/',
    'Шевченко Ирина': 'http://flibusta.is/a/47198/rss/',
    'Шумил Павел': 'http://flibusta.is/a/7369/rss/',
    'Юдковски Элиезер': 'http://flibusta.is/a/29650/rss/'}
res = {}
newdic = {}
dic = {}
with open('last.txt', 'rb') as f:
    dic = dict(pickle.load(f))
count = 0
for url in urls.values():
    try:
        res = requests.get(url, proxies=proxy)
        res.encoding = 'utf-8'
        xml = parseString(res.text)
        items = xml.getElementsByTagName('item')
        for item in items:
            guid = item.getElementsByTagName('guid')[0].childNodes[0].nodeValue
            title = item.getElementsByTagName('title')[0].childNodes
            if len(title) > 0:
                title = title[0].nodeValue
            else:
                title = ''
            pub_date = item.getElementsByTagName('pubDate')[0].childNodes
            if len(pub_date) > 0:
                pub_date = pub_date[0].nodeValue
            else:
                pub_date = ''
            desc = item.getElementsByTagName('description')[0].childNodes
            if len(desc) > 0:
                desc = desc[0].nodeValue
            else:
                desc = ''
            # text = '<p>{}</p><p>{}</p>{}'.format(title, pub_date, desc)
            text = '<p>{}</p><p>{}</p>'.format(title, pub_date, desc)
            newdic[guid] = text
            count += 1 / (len(urls) * len(items))
            if dic.get(guid) == newdic.get(guid):
                print('{:.1%}'.format(count))
                pass
            else:
                f = open('text.txt', 'a', encoding='utf-8')
                print('', '{:.1%}{} {}'.format(count, guid, title))
                print('{:.1%} \t {} \t {}'.format(count, guid, title), file=f)
                f.close()
    except Exception as e:
        print(e)

with open('last.txt', 'wb') as f:
    pickle.dump(newdic, f)
    # pickle.dump({}, f)

# input()
