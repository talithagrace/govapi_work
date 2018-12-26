import requests, bs4, re#, html5lib, lxml
import pandas as pd
from time import sleep

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
        legislation = base_url + link.get('href')
        print(legislation)

def print_page_no():
    url_2 = 'https://www.gov.uk/government/publications'
    params_2 = {'keywords': 'immigration', 'publication_filter_option': 'consultations'}
    base_url = "https://www.gov.uk"

    #download the webpage using base url and params above
    r_2 = requests.get(url_2, params_2)

    #check status of the page
    r_2.raise_for_status()

    #createinstance of the BeautifulSoup class
    search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')
    #40 is the number of results per page
    #find the count class to find the total number or results and divide by 40 to get the number of pages with no remainder
    pages = int(search_results_2.find('span', {"class": "count"}).text)//40
    #if there is a remainder, add 1 to the number of pages, add another 1 so that the range includes total number of pages
    if int(search_results_2.find('span', {"class": "count"}).text)%40 > 0:
        no_pages = pages + 2
    for page in range(1, no_pages):
        print(page)
        
    #print(no_pages)
    for page in range(1, no_pages):
        params_3 = {'keywords': 'immigration', 'publication_filter_option': 'consultations', 'page': page}
        r_3 = requests.get(url_2, params_3)
        #add sleep so that the function doesn't call two different pages at once
        sleep(0.2)
        r_3.raise_for_status()
        search_results_3 = bs4.BeautifulSoup(r_3.content, 'html.parser')
        
        for link in search_results_3.find_all('a', href=re.compile("/government/consultations")):
            consultations = base_url + link.get('href')
            con_text = link.text
            print(con_text)
            #print(consultations)
            
        
    
    

def consultation_search():
    #consultations = []
    url_2 = 'https://www.gov.uk/government/publications'
    params_2 = {'keywords': 'immigration', 'publication_filter_option': 'consultations'}
    params_2a = {'keywords': 'immigration', 'publication_filter_option': 'consultations', 'page': '2'} 
    base_url = "https://www.gov.uk"

    #download the webpage using base url and params above
    r_2 = requests.get(url_2, params_2)

    #check status of the page
    r_2.raise_for_status()

    #createinstance of the BeautifulSoup class
    search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')
    #page = search_results_2.find('span', {"class": "count"}).content
    #params_2b = 

    #print(type(search_results_2))
    #print(search_results_2.prettify(search_results_2.content))

    #print(r_2.url)

    #search for any links which are consultations
    for link in search_results_2.find_all('a', href=re.compile("/government/consultations")):
        consultations = base_url + link.get('href')
        print(consultations)

    #results_table = pd.DataFrame({
    #            "consultations": consultations,
    #            },
    #            index=[0])
    #results_table

    r_3 = requests.get(url_2, params_2a)
    r_3.raise_for_status()
    search_results_3 = bs4.BeautifulSoup(r_3.content, 'html.parser')

    for link in search_results_3.find_all('a', href=re.compile("/government/consultations")):
        consultations = base_url + link.get('href')
        print(consultations)

    

#https://stackoverflow.com/questions/26018591/display-all-search-results-when-web-scraping-with-python
#to iterate over pages

#legislation_search()
#consultation_search()
print_page_no()
