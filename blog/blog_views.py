import requests, bs4, re
from django.shortcuts import render
from time import sleep
from blog.models import Opencons

def searchlist(request):
    search_query = request.GET.get('search_box', None)
    #create lists
    legislation_1 = []
    legislation_2 = []
    consultations = []
    news = []
    url = 'http://www.gov.uk/government/publications'
    params = {'publication_filter_option': 'open-consultations'}
    base_url = 'https://www.gov.uk'

    r = requests.get(url, params)
    #r.raise_for_status()

    search_results = bs4.BeautifulSoup(r.content, 'html.parser')
    #find the number of pages the search results are displayed across
    #40 is the number of results per page
    pages = int(search_results.find('span', {"class": "count"}).text)//40
    if int(search_results.find('span', {"class": "count"}).text)%40 > 0:
        no_pages = pages + 2

    #iterate through each page and scrape
    for page in range(1, no_pages):
        params_a = {'publication_filter_option': 'open-consultations', 'page': page}
        r_a = requests.get(url, params_a)
        #sleep so that multiple requests are not made simultaneously
        sleep(0.2)
        search_results_a = bs4.BeautifulSoup(r_a.content, 'html.parser')

        for link in search_results_a.find_all('a', href=re.compile("/government/consultations")):
            hyper_link = (base_url + link.get('href'))
            title_text = link.text
            open_con = Opencons.objects.get_or_create(hyperlink=hyper_link, title=title_text)
            open_cons = Opencons.objects.all()

    if search_query:
        url_1 = 'http://www.legislation.gov.uk/id'
        params_1 = {'title': search_query}
        base_url_1 = 'http://www.legislation.gov.uk'

        url_2 = 'https://www.gov.uk/government/publications'
        params_2 = {'keywords': search_query, 'publication_filter_option': 'consultations'}
        base_url_2 = 'https://www.gov.uk'

        url_3 = 'http://www.gov.uk/government/announcements'
        params_3 = {'keywords': search_query, 'from_date': '01%2F01%2F2016'}
        base_url_3 = 'http://www.gov.uk'


        r_1 = requests.get(url_1, params_1)

        #r_1.raise_for_status()

        search_results_1 = bs4.BeautifulSoup(r_1.content, 'html.parser')

        for link in search_results_1.find_all('a', href=re.compile("/id/ukpga")):
            #append each link in the loop to the list created above
            legislation_1.append(base_url_1 + link.get('href'))

        for link in search_results_1.find_all('a', href=re.compile("/id/uksi")):
            #append each link in the loop to the list created above
            legislation_2.append(base_url_1 + link.get('href'))

        r_2 = requests.get(url_2, params_2)

        #r_2.raise_for_status()

        search_results_2 = bs4.BeautifulSoup(r_2.content, 'html.parser')

        pages_2 = int(search_results_2.find('span', {"class": "count"}).text)//40
        if int(search_results_2.find('span', {"class": "count"}).text)%40 > 0:
            no_pages_2 = pages_2 + 2

        for page in range(1, no_pages_2):
            params_c = {'keywords': search_query, 'publication_filter_option': 'consultations'}
            r_c = requests.get(url_2, params_c)
            sleep(0.2)

            search_results_c = bs4.BeautifulSoup(r_c.content, 'html.parser')

            for link in search_results_c.find_all('a', href=re.compile("/government/consultations")):
                consultations.append(base_url_2 + link.get('href'))

        r_3 = requests.get(url_3, params_2)

        #r_3.raise_for_status()

        search_results_3 = bs4.BeautifulSoup(r_3.content, 'html.parser')

        for link in search_results_3.find_all('a', href=re.compile("/government/news")):
            news.append(base_url_3 + link.get('href'))

    context = {
        'legislation_1': legislation_1,
        'legislation_2': legislation_2,
        'consultations': consultations,
        'news': news,
        'open_cons': open_cons
        }
    return render(request, 'blog/search_list.html', context)

# Create your views here.
