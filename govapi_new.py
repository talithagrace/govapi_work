import requests, bs4, re
from django.shortcuts import render
from time import sleep
import datetime


def consultation_search():
    #consultations = []
    url_2 = 'https://www.gov.uk/search/policy-papers-and-consultations'
    params_2 = {'keywords': 'immigration', 'content_store_document_type': 'open_consultations', 'content_store_document_type': 'closed_consultations'}
    base_url = "https://www.gov.uk"

    #download the webpage using base url and params above
    r_2 = requests.get(url_2, params_2)

    #check status of the page
    r_2.raise_for_status()

    #createinstance of the BeautifulSoup class
    search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')

    #search for any links which are consultations
    for link in search_results_2.find_all('a', href=re.compile("/government/consultations")):
        consultations = base_url + link.get('href')
        print(consultations)


def count():
    #consultations = []
    url_2 = 'https://www.gov.uk/search/policy-papers-and-consultations'
    params_2 = {'keywords': 'immigration', 'content_store_document_type': 'open_consultations', 'content_store_document_type': 'closed_consultations'}
    base_url = "https://www.gov.uk"

    #download the webpage using base url and params above
    r_2 = requests.get(url_2, params_2)

    #check status of the page
    r_2.raise_for_status()

    #createinstance of the BeautifulSoup class
    search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')
    no_cons_text = search_results_2.find('h2', {"class": "result-region-header__counter"}).text
    #no_cons = int(no_cons_text[:2])
    no_cons = no_cons_text.strip()
    no_cons_int = int(no_cons[:2])
    print(no_cons_int)

#consultation_search()
count()
