import requests
import lxml
import re
from bs4 import BeautifulSoup

book_list = []


def page_loop(url, book_object_locator, book_price_locator):
    res = requests.get ( url )
    soup = BeautifulSoup ( res.text, 'html.parser' )
    max_page = int ( soup.select_one ( 'li.current' ).string.replace ( 'Page 1 of ', '' ) )
    for i in range ( 1, max_page + 1 ):
        get_book_object ( url, i, book_object_locator, book_price_locator )
    return book_list


def get_book_object(url, page_count, book_object_locator, book_price_locator):
    # print(f'{url}+/catalogue/page-{page_count}.html')
    url_page = url + "/catalogue/page-" + str ( page_count ) + ".html"
    # print(url_page)
    res = requests.get ( url_page )
    soup = BeautifulSoup ( res.text, 'html.parser' )
    # print(soup.select(book_object_locator))
    # print(len(soup.select(book_object_locator)))
    for i in soup.select ( book_object_locator ):
        book_name = get_book_name ( i )
        book_price = get_book_price ( i, book_price_locator )
        book_rating = get_book_rating ( i )
        dict = {'name': book_name, 'price': book_price, 'rating': book_rating}
        book_list.append ( dict )
    return book_list


def get_book_name(i):
    return (i.find ( 'h3' ).find ( 'a' )['title'])
    # return i.select_one(book_name_locator).string


def get_book_rating(i):
    if (i.find ( 'p' ).attrs['class'][1]) == 'One':
        return 1
    if (i.find ( 'p' ).attrs['class'][1]) == 'Two':
        return 2
    if (i.find ( 'p' ).attrs['class'][1]) == 'Three':
        return 3
    if (i.find ( 'p' ).attrs['class'][1]) == 'Four':
        return 4
    if (i.find ( 'p' ).attrs['class'][1]) == 'Five':
        return 5


def get_book_price(i, book_price_locator):
    # print(re.search('£([0-9]+\.[0-9]+)', i.select_one(book_price_locator).string).groups()[0])
    # return i.select_one(book_price_locator).string
    return float ( re.search ( '£([0-9]+\.[0-9]+)', i.select_one ( book_price_locator ).string ).groups ()[0] )
