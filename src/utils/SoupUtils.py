"""BeautifulSoupの共通処理"""
import requests
from bs4 import BeautifulSoup as bs


# URLからHTMLを取得
def get_soup(url: str):
    res = requests.get(url)
    soup = bs(res.content, "html.parser")
    return soup


# タイトルを取得
def get_title(soup: bs):
    return soup.title.text


# HTMLを整形して全表示
def print_all_html(soup: bs):
    print(soup.prettify())
