import requests, bs4, re
from django.shortcuts import render
#from blog.models import Legislation

def searchlist(request):
    #legislation = []
    url_1 = 'http://www.legislation.gov.uk/id'
    params_1 = {'title': 'immigration'}
    base_url = 'http://www.legislation.gov.uk'

    r_1 = requests.get(url_1, params_1)

    r_1.raise_for_status()

    search_results_1 = bs4.BeautifulSoup(r_1.content, 'html.parser')

    for link in search_results_1.find_all('a', href=re.compile("/id/ukpga")):
        legislation_1 = base_url + link.get('href')

    for link in search_results_1.find_all('a', href=re.compile("/id/uksi")):
        legislation_2 = base_url + link.get('href')

    context = {
        'legislation_1': legislation_1,
        'legislation_2': legislation_2
    }
    return render(request, 'blog/search_list.html', context)
# Create your views here.
