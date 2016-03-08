import jieba
import requests
from bs4 import BeautifulSoup

def exteat_text(url):
    """Ectract html content"""
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'


    return text

def