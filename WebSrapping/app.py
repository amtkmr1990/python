from utils.css_locator import page_loop

url_page = 'http://books.toscrape.com'
books_page_locator = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
book_object_locator = 'li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
book_name_locator = 'h3 a'
book_rating_locator = ''
book_price_locator = 'p.price_color'

print ( page_loop ( url_page, book_object_locator, book_price_locator ) )


# books_rating_five = [i['name'] for i in book_list if i['rating'] == 5]
