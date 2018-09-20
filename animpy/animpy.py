import textwrap
from os import environ, name, system
from re import sub

import requests
from bs4 import BeautifulSoup

WIDTH = 70
LINES = 21

try:
    from os import get_terminal_size
    term_col, term_lin = get_terminal_size()
    WIDTH = term_col - 2 if term_col < 119 else 118
    LINES = term_lin
except OSError:
    pass


def display_reviews(reviews):
    """
    Cleans up the reviews
    :param reviews: String, contains the review section portion
    :return: List, with the review sections
    """
    # totally inefficient way to clean this up, too lazy to use re atm...
    review = reviews.split('\n\n\n\n\n', 1)[1]
    review = review.rsplit('\n\n', 2)[0]
    review = review.replace('\n\n', ' ')
    review = review.replace('\n        ', ' ')
    review = review.replace('            ', ' ')
    review = review.replace('    ', '')
    review_sections = review.rsplit('\n')
    for section in review_sections:
        wrapped = textwrap.fill(
            section, initial_indent='    ',
            subsequent_indent='  ',
            width=WIDTH
        )
        print(wrapped)


def clear_screen():
    """
    Clears the screen
    :return: None
    """
    _ = system('cls' if name == 'nt' else 'clear')


def cleanup_reviews(reviews_all):
    """
    Displays the reviews for the show
    :param reviews_all: BeautifulSoup object, contains the reviews
    :return: None
    """
    for i, post in enumerate(reviews_all, 1):
        total = len(reviews_all)
        clear_screen()
        print(f'[ REVIEW: #{i} of {total} ]')
        review_div = post.find(
            'div',
            {'class': 'spaceit textReadability word-break pt8 mt8'}
        )
        display_reviews(review_div.text)
        if i != total:
            choice = input('\nWould like like to read another review? ([y],n) ')
            if choice.startswith('n'):
                clear_screen()
                exit_message()
        else:
            exit_message()
    else:
        print('Sorry, was not able to retrieve any reviews at this time...')


def display_review_choice(url):
    """
    Asks the user if they want to retrieve the reviews section
    :param url: String, url of the main page
    :return: None
    """
    choice = input('\nWould you like to read the reviews? ([y], n)')
    if choice.startswith('n'):
        clear_screen()
        print('Thank you for using AnimPy!')
        exit(0)
    else:
        scrape_reviews(f'{url}/reviews')


def display_summary(divs, summary):
    """
    Displays the summary for the show
    :param divs: List, the div blocks for some of the sections
    :param summary: BeautifulSoup object, with the summary
    :return: None
    """
    sections = ['English:', 'Synonyms:', 'Rating:']
    clear_screen()
    # iterate over all of the div tags and only return the sections that we are
    # interested in
    for div in divs:
        for section in sections:
            if div.startswith(section):
                print(div.replace('\n ', '').strip())

    print('\nSUMMARY: \n')
    # wrapped = textwrap.dedent(summary)
    for line in summary.split('\n'):
        line = line.replace('  ', ' ')
        wrapped = textwrap.fill(
            line, initial_indent='    ',
            subsequent_indent='  ',
            width=WIDTH
        )
        print(wrapped)


def exit_message():
    """
    Displays an exit message
    :return: None
    """
    print('\nThank you for using AnimPy!')
    exit(0)


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
    :return: Tuple, The title, url, and description of each is captured and
             returned.
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
    try:
        soup = _soup(url)
        summary = soup.find('span', {'itemprop': 'description'}).text
        info_section = soup.find('div', {'class': 'js-scrollfix-bottom'})
        all_divs = info_section.find_all('div')
        divs = [div.text.strip() for div in all_divs]
        display_summary(divs, summary)
        display_review_choice(url)
    except AttributeError:
        print("You're connection timed out, please try again.")
        exit_message()


def scrape_reviews(url):
    """
    Scrapes the reviews page
    :param url: String, url of the reviews page
    :return: None
    """
    clear_screen()
    print(f'Retrieving: {url}')
    soup = _soup(url)
    reviews_all = soup.find_all('div', {'class': 'borderDark'})
    cleanup_reviews(reviews_all)


def search(term, count):
    """
    Searches for the show entered by the user
    :param term: String, the title of the show
    :param count: Integer, number or search results to return
    :return: List, containing the first 10 hits
    """
    search_term = sub(' ', '+', term)
    url = f'https://myanimelist.net/anime.php?q={search_term}'
    soup = _soup(url)
    hits = scrape_hits(soup)
    return hits if count > len(hits) else hits[:count]


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
