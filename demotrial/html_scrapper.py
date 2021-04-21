from bs4 import BeautifulSoup
import requests


web_content = requests.get('https://codingbat.com/java',verify=False)

soup = BeautifulSoup(web_content.content,'lxml')
q_cat_content = soup.find_all( 'div', attrs={'class' : 'summ'} )
#q_cat_name = 'div.a.span.string'
#q_cat_url = 'div.a[href]'
#q_subcat_name =  div class=indent -> div.table.tbody.tr.td.a
#q_subcat_url = 'div.table.tbody.tr.td.a['href']'
q_subcat_a = []
q_cat = {i.a.span.string:i.a['href'] for i in q_cat_content}
for i in q_cat.values():
    web_cat_content = requests.get('https://codingbat.com'+i)
    print(web_cat_content.url)
    soup_subcat = BeautifulSoup(web_cat_content.content,'lxml')
    div = soup_subcat.find('div',attrs={'class':'indent'})
    for d in div.table.find_all('a'):
        q_subcat_a.append(d['href'])

print(q_subcat_a)

for i in q_subcat_a:
    q_content = requests.get('https://codingbat.com'+i)
    soup = BeautifulSoup(q_content.content,'lxml')
    q = soup.find('div',attrs={'class':'minh'})
    print('question - ' + q.text)
    #print('example - ' + q.find_next_sibling())
    #print('example - ' + q.next_siblings)