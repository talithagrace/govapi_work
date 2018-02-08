import requests, bs4, re#, html5lib, lxml

"""
http://www.legislation.gov.uk/id?title={title}&type={type}&year={year}&number={number}
http://www.legislation.gov.uk/id?title=immigration
https://www.gov.uk/government/publications?publication_filter_option=consultations
https://www.gov.uk/government/publications?keywords=immigration&publication_filter_option=consultations
https://www.gov.uk/government/publications.atom?publication_filter_option=consultations&keywords=immigration
the above '.atom' link is rss feed from the publications page
this prints links from the search results from the above websites
"""



def legislation_search():
    url_1 = 'http://www.legislation.gov.uk/id'
    params_1 = {'title': 'immigration'}
    base_url = "http://www.legislation.gov.uk"

    #download the webpage using base url and params above
    r_1 = requests.get(url_1, params_1)

    #check status of the page
    r_1.raise_for_status()

    #create instance of the beautifulsoup class
    search_results_1 = bs4.BeautifulSoup(r_1.content, 'html.parser')

    #print(type(search_results_1))

    #search for any links which contain "/id/ukpga" and print
    for link in search_results_1.find_all('a', href=re.compile("/id/ukpga")):
        print(base_url + link.get('href'))

    #search for any links which contain "/id/uksi"
    for link in search_results_1.find_all('a', href=re.compile("/id/uksi")):
        print(base_url + link.get('href'))

def consultation_search():
    url_2 = 'https://www.gov.uk/government/publications'
    params_2 = {'keywords': 'immigration', 'publication_filter_option': 'consultations'}
    base_url = "https://www.gov.uk"

    #download the webpage using base url and params above
    r_2 = requests.get(url_2, params_2)

    #check status of the page
    r_2.raise_for_status()

    #createinstance of the BeautifulSoup class
    search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')

    #print(type(search_results_2))
    #print(search_results_2.prettify(search_results_2.content))

    #print(r_2.url)

    #search for any links which are consultations
    for link in search_results_2.find_all('a', href=re.compile("/government/consultations")):
        print(base_url + link.get('href'))

legislation_search()
consultation_search()
