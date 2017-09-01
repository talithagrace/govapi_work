import requests, bs4, re, html5lib, lxml
"""
# http://www.legislation.gov.uk/id?title={title}&type={type}&year={year}&number={number}
# http://www.legislation.gov.uk/id?title=immigration
# https://www.gov.uk/government/publications?publication_filter_option=consultations
# https://www.gov.uk/government/publications?keywords=immigration&publication_filter_option=consultations
# https://www.gov.uk/government/publications.atom?publication_filter_option=consultations&keywords=immigration
# the above '.atom' link is rss feed from the publications page

this prints links from the search results from the above websites
"""

def legislation_search():
    url_1 = 'http://www.legislation.gov.uk/id'
    params_1 = {'title': 'immigration'}
    base_url = "http://www.legislation.gov.uk"

    r_1 = requests.get(url_1, params_1)
    r_1.raise_for_status()
    search_results_1 = bs4.BeautifulSoup(r_1.content, 'html.parser')

    print(type(search_results_1))

    for link in search_results_1.find_all('a', href=re.compile("/id/ukpga")):
        print(base_url + link.get('href'))
        

def consultation_search():
    url_2 = 'https://www.gov.uk/government/publications'
    params_2 = {'keywords': 'immigraion', 'publication_filter_option': 'consultations'}

    r_2 = requests.get(url_2, params_2)
    r_2.raise_for_status()
    search_results_2 = bs4.BeautifulSoup(r_2.text, 'html.parser')

    print(type(search_results_2))
    #print(search_results_2.prettify(search_results_2.content))
    print(r_2.url)

    for link in search_results_2.find_all('a'):#, href=re.compile("/government/consultations/")):
        print(link.get('href'))

legislation_search()

consultation_search()
