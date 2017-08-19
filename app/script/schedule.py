from  urllib.request import *
from bs4 import BeautifulSoup
import ssl
import re

from constant.constant_map import SCHEDULE_LINK_MAP

ssl._create_default_https_context = ssl._create_unverified_context

def flatten(l):
    return [item for sublist in l for item in sublist]

def parse_onclick_to_link(onclick_string):
    if not onclick_string: return

    return re.match('location.href=\'(.*)\'', onclick_string).group(1)

def get_book_link(td):
    button = td.find('button')
    if not button: return

    return button.get('onclick')

def parse_single_tr(tr):
    tds = tr.find_all('td')
    return {
        'date': tds[0].string,
        'event': tds[1].string,
        'gym': tds[2].string,
        'book_link': parse_onclick_to_link(get_book_link(tds[3]))
    }

def single_event(event_link):
    with urlopen(event_link) as f:
        bs = BeautifulSoup(f, "html.parser")

    trs = [i for i in bs.find_all('tr')]
    trs = filter(lambda tr: len(tr.find_all('td')) == 4, trs)
    trs = map(parse_single_tr, trs)

    trs = list(trs)
    return trs


def main():
    return flatten(list(map(lambda item: single_event(item[1]), SCHEDULE_LINK_MAP.items())))
