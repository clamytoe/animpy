from re import sub
from os import system, name
from bs4 import BeautifulSoup
import requests
import textwrap


def clear_screen():
    """
    Clears the screen
    :return: None
    """
    _ = system('cls' if name == 'nt' else 'clear')


def _soup(url):
    """
    Generic BeautifulSoup page scraping starter code
    :param url: String, the url of the page to scrape
    :return: BeautifulSoup object
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


def scrape_hits(soup):
    """
    Scrapes the soup object for the search term results that were found.
    :param soup: BeautifulSoup object
    :return: Tuple, The title, url, and description of each is captured and returned.
    """
    # extract the sections that we are interested in
    hits_soup = soup.find_all('a', {'class': 'hoverinfo_trigger fw-b fl-l'})
    desc_soup = soup.find_all('div', {'class': 'pt4'})
    # extract the information that we need
    titles = [hit.string for hit in hits_soup]
    links = [hit['href'] for hit in hits_soup]
    desc = [blurb.text for blurb in desc_soup]
    # combine it all
    captured = list(zip(titles, links, desc))
    return captured


def scrape_details(url):
    """
    Scrapes the details about the show from the provided url
    :param url: String, the url of the page to scrape
    :return: None
    """
    sections = ['English:', 'Synonyms:', 'Rating:']
    soup = _soup(url)
    summary = soup.find('span', {'itemprop': 'description'}).text
    info_section = soup.find('div', {'class': 'js-scrollfix-bottom'})
    all_divs = info_section.find_all('div')
    divs = [div.text.strip() for div in all_divs]

    clear_screen()
    # iterate over all of the div tags and only return the sections that we are interested in
    for div in divs:
        for section in sections:
            if div.startswith(section):
                print(div.strip())

    print('\nSUMMARY: \n')
    wrapped = textwrap.dedent(summary)
    print(textwrap.fill(wrapped, initial_indent='    ', subsequent_indent='  ', width=110))
    scrape_reviews(f'{url}/reviews')


def scrape_reviews(url):
    soup = _soup(url)
    reviews_all = soup.find_all('div', {'class': 'borderDark'})
    print('\nREVIEWS:')
    for i, post in enumerate(reviews_all):
        review_div = post.find('div', {'class': 'spaceit textReadability word-break pt8 mt8'})
        # totally inefficient way to clean this up, too lazy to use re atm...
        review = review_div.text.split('\n\n\n\n\n', 1)[1]
        review = review.rsplit('\n\n', 2)[0]
        review = review.replace('\n\n', ' ')
        review = review.replace('\n        ', ' ')
        review = review.replace('            ', ' ')
        review = review.replace('    ', '')
        review_sections = review.rsplit('\n')
        for section in review_sections:
            print(textwrap.fill(section, initial_indent='    ', subsequent_indent='  ', width=110))
        choice = input('\nWould like like to read another review? [(y),n] ')
        if choice.startswith('n'):
            break
        else:
            clear_screen()


def search(term):
    """
    Searches for the show entered by the user
    :param term: String, the title of the show
    :return: List, containing the first 10 hits
    """
    search_term = sub(' ', '+', term)
    url = f'https://myanimelist.net/anime.php?q={search_term}'
    soup = _soup(url)
    hits = scrape_hits(soup)
    return hits[:10]


def search_divs(term, divs):
    """
    Searches the provided div tags for the term that we are interested in
    :param term: String, the search term
    :param divs: List, div tags that were scraped
    :return: List of divs or None
    """
    for div in divs:
        if div.startswith(term):
            return div.split('\n')[1]
    return None
