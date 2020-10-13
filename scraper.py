# Developed by Jinmo Rhee
# all rights reserved by Jinmo Rhee
# leeuack@jinmorhee.net, www.jinmorhee.net

'''CumInCAD Crawler by Keywords'''
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import time
# ----------------------------------------------------------------------------------------------------------------------

folder = "raw_data/"

#please change the search words
search_words = ["deep learning", "deep-learning", "deep-learning-based",
                "deep neural network", "deep neural networks",
                "artificial neurpip freeze > requirements.txtal network", "artificial neural networks",
                "neural network", "neural networks",
                "gan", "generative adversarial network", "generative adversarial networks",
                "vgg", "cnn",
                "imagenet", "image-net", "image net",
                "unet", "u-net", "u net"]


def searchWord(w):
    '''check the word w is in the publication information'''
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def searchContainment(words, conents):
    '''check whether the contents have words or not'''
    for word in words:
        if searchWord(word)(conents) != None:
            print(word)
            return True
    return False

def getPapers(main_soup):
    '''find all papers link and return the list of papers'''
    form = main_soup.find('form', attrs={'name': 'main'})
    papers = form.find_all('a')[::2]
    return papers

def getPaperInfo(paper):
    '''extract information of the input paper, input is id of a paper'''
    data = []
    paper_site = str(paper).replace("<", "*").replace(">", "*").split("*")[1][8:-1] # generate paper url

    #scraping
    paper_request = requests.get(paper_site)
    main_soup = BeautifulSoup(paper_request.text, 'html.parser')
    paper_table_1 = main_soup.find_all('tr', attrs={'class': 'DATA'})
    score = 0

    for row in paper_table_1:
        cols = row.find_all('td')
        item = [ele.text.strip() for ele in cols]
        filter = searchContainment(search_words, item[0].lower())  # check a paper is relevant
        score += filter  # score is how many words in contents are related to the keywords
        data.append(item)
    if score > 0:
        df = pd.DataFrame(data)
        filename = folder + paper_site.split("/")[-1] + ".csv"  # make a new folder named as paper id
        df.to_csv(filename, sep=",", encoding='utf-8-sig')   # save as csv file

def countPapers(folder):
    '''count the number of currently scraped paper'''
    return len(os.listdir(folder))

def main(total=15260):
    '''wrapper function of scraper'''
    page_number = 0
    count = 0
    while page_number <= total:
        # access the main site, e.g. CumInCAD
        main_site = "http://papers.cumincad.org/cgi-bin/works/Search?&first={}".format(page_number)
        # the first page of archive
        print(page_number)
        main_request = requests.get(main_site)
        main_soup = BeautifulSoup(main_request.text, 'html.parser')
        # get the papers in the page
        papers = getPapers(main_soup)
        # extract paper info
        for paper in papers:
            start = time.time()
            getPaperInfo(paper)
            count += 1
            end = time.time()
            print("{}/15176        {} papers,      {} sec".format(count, countPapers(folder), end - start))
        page_number += 20


if __name__ == "__main__":
    main()